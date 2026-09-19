# Evaluation-First RAG Sample

This is a dependency-free demonstration of clause-aware retrieval and
evaluation over synthetic technical rulebooks. It exists to make the proposed
measurement method inspectable; no client documents are included.

## Run

```bash
python rag_eval.py
python rag_eval.py --question "How quickly must a P1 alarm be acknowledged?"
```

## Design choices

- Chunks follow numbered clauses instead of fixed token windows, so a citation
  points to a stable rule rather than an arbitrary text slice.
- Tables remain attached to the clause that defines them.
- The retriever uses a readable BM25 baseline that can be replaced by a dense
  or hybrid adapter without changing the evaluation interface.
- Answers are extractive in this sample. Each accepted answer must carry the
  source clause; low-score or ambiguous retrieval abstains.
- The evaluation separates retrieval recall, citation accuracy, abstention
  accuracy, and false-answer rate.

## What this demonstrates

The useful part is not that a lexical baseline is sufficient for every corpus.
It is that retrieval and generation can be measured separately against a
ground-truth question set, and that a clear negative result is a valid outcome.

## Current synthetic evaluation

Measured with 15 answerable questions and 5 deliberately out-of-corpus
questions:

| Metric | Result |
|---|---:|
| Retrieval recall@3 | 1.000 |
| Citation accuracy | 1.000 |
| Abstention accuracy | 1.000 |
| False-answer rate | 0.000 |
| Overall decision accuracy | 1.000 |

These numbers apply only to this synthetic benchmark. The real value lies in
the measurement design: on a client corpus, the same report can identify table
loss, retrieval misses, unsupported answers, and failures to abstain instead
of returning one opaque score.
