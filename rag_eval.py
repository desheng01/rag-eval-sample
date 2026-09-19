#!/usr/bin/env python3
import argparse
import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TOKEN_RE = re.compile(r"[a-z0-9]+(?:[.%+-][a-z0-9]+)*")
CLAUSE_RE = re.compile(r"^##\s+(RB-\d{2}\.\d)\s+(.+)$", re.MULTILINE)


@dataclass(frozen=True)
class Chunk:
    clause: str
    title: str
    text: str


def tokenize(value):
    return TOKEN_RE.findall(value.lower())


def load_chunks(path=ROOT / "corpus.md"):
    text = path.read_text(encoding="utf-8")
    matches = list(CLAUSE_RE.finditer(text))
    chunks = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : end].strip()
        chunks.append(Chunk(match.group(1), match.group(2), body))
    return chunks


class BM25Index:
    def __init__(self, chunks, k1=1.5, b=0.75):
        self.chunks = chunks
        self.k1 = k1
        self.b = b
        self.documents = [
            tokenize(f"{chunk.clause} {chunk.title} {chunk.text}")
            for chunk in chunks
        ]
        self.lengths = [len(document) for document in self.documents]
        self.average_length = sum(self.lengths) / len(self.lengths)
        self.term_frequencies = [Counter(document) for document in self.documents]
        document_frequency = Counter()
        for document in self.documents:
            document_frequency.update(set(document))
        total = len(self.documents)
        self.idf = {
            term: math.log(1 + (total - frequency + 0.5) / (frequency + 0.5))
            for term, frequency in document_frequency.items()
        }

    def search(self, query, limit=3):
        query_terms = tokenize(query)
        scored = []
        for index, frequencies in enumerate(self.term_frequencies):
            score = 0.0
            for term in query_terms:
                frequency = frequencies.get(term, 0)
                if not frequency:
                    continue
                denominator = frequency + self.k1 * (
                    1 - self.b + self.b * self.lengths[index] / self.average_length
                )
                score += self.idf.get(term, 0.0) * (
                    frequency * (self.k1 + 1) / denominator
                )
            if score:
                scored.append((score, self.chunks[index]))
        scored.sort(key=lambda item: (-item[0], item[1].clause))
        return scored[:limit]


def first_supporting_sentence(chunk, query):
    sentence = re.split(r"(?<=[.!?])\s+", chunk.text.replace("\n", " "))[0]
    return sentence.strip()


def answer(index, question, minimum_score=5.0, minimum_margin=0.5):
    results = index.search(question, limit=3)
    if not results:
        return {"answer": None, "citation": None, "reason": "no_match", "results": []}
    top_score, top_chunk = results[0]
    second_score = results[1][0] if len(results) > 1 else 0.0
    margin = top_score - second_score
    if top_score < minimum_score or (
        second_score > 0 and margin < minimum_margin
    ):
        return {
            "answer": None,
            "citation": None,
            "reason": "low_confidence",
            "results": [
                {"clause": chunk.clause, "score": round(score, 3)}
                for score, chunk in results
            ],
        }
    return {
        "answer": first_supporting_sentence(top_chunk, question),
        "citation": top_chunk.clause,
        "reason": "answered",
        "results": [
            {"clause": chunk.clause, "score": round(score, 3)}
            for score, chunk in results
        ],
    }


def evaluate():
    chunks = load_chunks()
    index = BM25Index(chunks)
    cases = json.loads((ROOT / "evals.json").read_text(encoding="utf-8"))
    records = []
    for case in cases:
        result = answer(index, case["question"])
        retrieved = [item["clause"] for item in result["results"]]
        source = case["source_clause"]
        retrieval_hit = source is None or source in retrieved[:3]
        citation_correct = source is None or result["citation"] == source
        abstained = result["answer"] is None
        decision_correct = abstained if case["should_abstain"] else not abstained
        records.append(
            {
                **case,
                **result,
                "retrieval_hit": retrieval_hit,
                "citation_correct": citation_correct,
                "abstained": abstained,
                "decision_correct": decision_correct,
            }
        )

    answerable = [record for record in records if not record["should_abstain"]]
    unanswerable = [record for record in records if record["should_abstain"]]
    metrics = {
        "cases": len(records),
        "answerable": len(answerable),
        "unanswerable": len(unanswerable),
        "retrieval_recall_at_3": round(
            sum(record["retrieval_hit"] for record in answerable) / len(answerable),
            4,
        ),
        "citation_accuracy": round(
            sum(record["citation_correct"] for record in answerable)
            / len(answerable),
            4,
        ),
        "abstention_accuracy": round(
            sum(record["abstained"] for record in unanswerable) / len(unanswerable),
            4,
        ),
        "false_answer_rate": round(
            sum(not record["abstained"] for record in unanswerable)
            / len(unanswerable),
            4,
        ),
        "overall_decision_accuracy": round(
            sum(record["decision_correct"] for record in records) / len(records),
            4,
        ),
    }
    return metrics, records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.question:
        result = answer(BM25Index(load_chunks()), args.question)
        print(json.dumps(result, indent=2) if args.json else result)
        return

    metrics, records = evaluate()
    print(json.dumps({"metrics": metrics, "records": records}, indent=2))


if __name__ == "__main__":
    main()
