
import os
import pandas as pd
import duckdb

df = pd.read_json("agent_events.jsonl", lines=True)

output_dir = "partitioned-events"

df.to_parquet(
    output_dir,
    engine="pyarrow",
    partition_cols=["event_date", "agent_name"],
    compression="snappy",
    index=False
)

# Count generated Parquet files.
parquet_files = []

for root, _, files in os.walk(output_dir):
    for filename in files:
        if filename.endswith(".parquet"):
            parquet_files.append(os.path.join(root, filename))

print("Partitioned rows:", len(df))
print("Parquet files:", len(parquet_files))
print("Partition directories:")
for path in sorted(os.listdir(output_dir)):
    print(" ", path)

# Query one agent on the specified date.
query = """
    SELECT COUNT(*) AS event_count,
           AVG(latency_ms) AS avg_latency_ms
    FROM read_parquet(
        'partitioned-events/**/*.parquet',
        hive_partitioning = true
    )
    WHERE event_date = '2026-10-09'
      AND agent_name = 'agent-0'
"""

result = duckdb.sql(query).df()
print(result)
