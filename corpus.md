# RB-01 Pressure Systems

## RB-01.1 Scope
This rulebook applies to pressure vessels used in gas and liquid service.

## RB-01.2 Design margin
The nominal design pressure must be at least 1.5 times the maximum operating pressure for gas service and 1.25 times the maximum operating pressure for liquid service.

| Service | Minimum factor |
|---|---|
| Gas | 1.5 |
| Liquid | 1.25 |

## RB-01.3 Test record
A pressure test record must include the test pressure, hold duration, fluid, ambient temperature, and instrument serial number.

# RB-02 Inspection

## RB-02.1 Critical equipment interval
Equipment classified as Critical must receive an internal inspection at least every 180 days.

## RB-02.2 Standard equipment interval
Equipment classified as Standard must receive an internal inspection at least every 365 days.

## RB-02.3 Classification table

| Class | Maximum inspection interval |
|---|---|
| Critical | 180 days |
| Standard | 365 days |
| Limited | 730 days |

# RB-03 Thermal Safety

## RB-03.1 Thermal lockout
A thermal lockout must occur immediately when any validated process sensor exceeds 80 C.

## RB-03.2 Lockout reset
A thermal lockout may be reset only after 10 consecutive validated readings at or below 75 C.

## RB-03.3 Sensor validation
A process sensor reading is validated only when it differs from the redundant sensor by no more than 2 C.

# RB-04 Calibration

## RB-04.1 Calibration tolerance
A calibration passes when the measured error is within plus or minus 0.5 percent of full scale.

## RB-04.2 Drift threshold
An instrument with drift greater than 0.8 percent of full scale must be replaced rather than adjusted.

## RB-04.3 Calibration interval
Flow instruments must be calibrated every 12 months. Pressure instruments must be calibrated every 18 months.

# RB-05 Records Retention

## RB-05.1 Raw telemetry
Raw telemetry must be retained for 90 days.

## RB-05.2 Summary records
Daily summary records must be retained for 7 years.

## RB-05.3 Deletion approval
Permanent deletion of a summary record requires approval from both the data owner and the compliance officer.

# RB-06 Access Control

## RB-06.1 Setpoint changes
A setpoint change greater than 10 percent of the current value requires dual approval by two authorized operators.

## RB-06.2 Emergency access
Emergency access expires automatically after 60 minutes.

## RB-06.3 Shared credentials
Shared operator credentials are prohibited. Every access event must identify one named user.

# RB-07 Alarm Response

## RB-07.1 Priority P1
A P1 alarm must be acknowledged within 5 minutes and escalated after 10 minutes if it remains active.

## RB-07.2 Priority P2
A P2 alarm must be acknowledged within 30 minutes.

## RB-07.3 Priority P3
A P3 alarm must be acknowledged within 8 hours.

# RB-08 Spare Parts

## RB-08.1 Critical spares
At least two serviceable units of every Critical spare must remain in stock.

## RB-08.2 Standard spares
At least one serviceable unit of every Standard spare must remain in stock.

## RB-08.3 Stockout escalation
A Critical spare stockout must be escalated to the maintenance manager within 2 hours.

# RB-09 Emergency Shutdown

## RB-09.1 Trip condition
An automatic emergency shutdown must trip when pressure exceeds 110 percent of the high-pressure trip setpoint or temperature exceeds 95 C.

## RB-09.2 Manual activation
Any operator may activate emergency shutdown without prior approval.

## RB-09.3 Restart
Restart after emergency shutdown requires field verification and written approval from the shift supervisor.

# RB-10 Audit Logs

## RB-10.1 Immutable retention
Audit logs must be immutable for 365 days.

## RB-10.2 Required fields
Each audit event must contain the user identity, timestamp, source address, action, target, and result.

## RB-10.3 Correction method
An incorrect audit entry must be corrected with an appended correction event. Existing entries must never be edited or deleted.

# RB-11 Change Control

## RB-11.1 Production freeze
Production changes are frozen from 20 December through 2 January.

## RB-11.2 Emergency exception
An emergency change during a freeze requires approval from the operations director and a rollback plan.

## RB-11.3 Post-change review
Every emergency change must receive a post-change review within 3 business days.

# RB-12 Reporting

## RB-12.1 Availability metric
Monthly availability is calculated as available minutes divided by total scheduled minutes, multiplied by 100.

## RB-12.2 Compliance threshold
A month is compliant only when availability is at least 99.5 percent and no Critical alarm exceeds its acknowledgement limit.

## RB-12.3 Report deadline
The monthly compliance report must be published by the fifth business day of the following month.
