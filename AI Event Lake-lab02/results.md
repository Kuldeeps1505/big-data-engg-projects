# AI Event Lake — Experiment Results

## 1. Environment

- Operating system: [Enter OS]
- Python version: [Enter version]
- Pandas version: [Enter version]
- PyArrow version: [Enter version]
- DuckDB version: [Enter version]
- Dataset size: 100,000 events

## 2. File Size Comparison

| Format | File size (bytes) |
|---|---:|
| JSONL | [Actual measurement] |
| CSV | [Actual measurement] |
| Parquet with Snappy | [Actual measurement] |
Rows: 100000
JSONL bytes: 21806004
CSV bytes: 9106087
Parquet bytes: 1016498
Conversion completed.

Space saved by Parquet compared with CSV: [Actual percentage]%

## 3. Validation Results

- Source row count: [Actual result]
- Parquet row count: [Actual result]
- Event ID uniqueness: [Pass/Fail]
- Column value comparison: [Pass/Fail]
- Numeric type validation: [Pass/Fail]
- Null and range checks: [Pass/Fail]

Validation passed
Source rows: 100000
Parquet rows: 100000
All checked columns match.

## 4. Query Performance

| Format | Median query time (seconds) |
|---|---:|
| CSV | [Actual measurement] |
| Parquet | [Actual measurement] |

- Query results match: [Yes/No]
- Faster format in this experiment: [Observed result]
- Benchmark observations: [Describe variability and caching effects]

gent_name  status  event_count  avg_latency_ms  total_tokens
   agent-0  failed         8243         2545.00    12693939.0
   agent-0 success         8447         2525.23    13138299.0
   agent-0 timeout         8310         2557.63    12918325.0
   agent-1  failed         8280         2514.98    12888941.0
   agent-1 success         8370         2552.14    13083237.0
   agent-1 timeout         8350         2572.34    12984140.0
   agent-2  failed         8329         2537.46    12813130.0
   agent-2 success         8295         2539.40    12856408.0
   agent-2 timeout         8376         2560.17    12850448.0
   agent-3  failed         8310         2536.02    12852227.0
   agent-3 success         8242         2549.76    12762218.0
   agent-3 timeout         8448         2547.76    13039557.0

## 5. Partitioning Results

- Number of partition directories: [Actual result]
- Number of Parquet files: [Actual result]
- Filtered event count: [Actual result]
- Unpartitioned query time: [Actual measurement]
- Partitioned query time: [Actual measurement]


CSV
File bytes: 9106087
Median query seconds: 0.167562
All query times: [0.216522, 0.164143, 0.147844, 0.187916, 0.167562]

Parquet
File bytes: 1016498
Median query seconds: 0.009498
All query times: [0.012269, 0.012359, 0.009498, 0.0081, 0.007801]

CSV and Parquet query results match.

CSV
File bytes: 9106087
Median query seconds: 0.167562
All query times: [0.216522, 0.164143, 0.147844, 0.187916, 0.167562]

Parquet
File bytes: 1016498
Median query seconds: 0.009498
All query times: [0.012269, 0.012359, 0.009498, 0.0081, 0.007801]

CSV and Parquet query results match.
## 6. Observations

Describe the measured file-size differences, query performance, validation results, and whether partitioning helped this workload.

## 7. Conclusion

The experiment demonstrated how raw JSONL telemetry can be transformed into CSV and compressed Parquet, validated, queried with DuckDB, and organized using partitioned storage. Performance conclusions were based on measured results rather than assumptions.
