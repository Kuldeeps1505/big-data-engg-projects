# AI Event Lake: CSV/JSONL to Parquet

## Project Objective

Build a local data pipeline that generates synthetic AI agent telemetry, converts raw JSONL into CSV and Parquet, validates data correctness, and compares storage and query performance.

## Technologies Used

- Python
- Pandas
- PyArrow
- Apache Parquet
- DuckDB
- JSONL and CSV

## Pipeline Workflow

1. Generate 100,000 synthetic AI events.
2. Read JSONL using Pandas.
3. Convert the dataset into CSV and Snappy-compressed Parquet.
4. Validate row counts, identifiers, values, and data types.
5. Query Parquet data using DuckDB SQL.
6. Benchmark CSV and Parquet file sizes and query times.
7. Create partitioned Parquet files and test filtered queries.

## How to Run

```bash
python generate_events.py
python convert_events.py
python validate_events.py
python query_events.py
python benchmark_events.py
python partition_events.py
```

## Results

See `results.md` for measured file sizes, query times, validation outcomes, and partitioning observations.

## Results and Analysis

The CSV and Parquet benchmarking experiment was performed on a dataset containing 100,000 synthetic AI telemetry events.

The CSV file occupied 9,106,087 bytes, while the Parquet file occupied 1,016,498 bytes. Therefore, Parquet reduced storage requirements by approximately 88.8%. This improvement is due to Parquet's column-oriented storage, binary data representation, and compression.

The median query execution time for CSV was 0.167562 seconds, compared with 0.009498 seconds for Parquet. In this experiment, Parquet queries were approximately 17.6 times faster. DuckDB can process columnar Parquet data efficiently because it can read the required columns without parsing the entire dataset as text. The measured performance applies to this dataset, query, and execution environment; results may vary with different workloads.

The query results obtained from CSV and Parquet matched, confirming that the conversion preserved the results of the tested analytical queries.

The partitioning experiment accounted for all 100,000 events and produced four Parquet files. Since the synthetic data contains one event date and four agent names, partitioning by `event_date` and `agent_name` creates separate agent-level partitions within the date directory. The reported aggregation contained 25,000 events and an average latency of 2,542.51732 milliseconds for the selected partition.

This experiment demonstrates important data engineering concepts, including data format conversion, schema and data validation, analytical querying, query benchmarking, columnar storage, compression, and partitioning. These techniques are commonly used when building scalable data lakes for telemetry and event analytics.

## Conclusion

This project demonstrates basic data ingestion, file-format conversion, data validation, analytical querying, benchmarking, and partitioned data-lake storage using Python.
