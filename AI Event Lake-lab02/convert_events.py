
import os
import pandas as pd

df = pd.read_json("agent_events.jsonl", lines=True)

df["latency_ms"] = df["latency_ms"].astype("int64")
df["token_count"] = df["token_count"].astype("int64")

df.to_csv("agent_events.csv", index=False)

df.to_parquet(
    "agent_events.parquet",
    engine="pyarrow",
    index=False,
    compression="snappy"
)

print("Rows:", len(df))
print("JSONL bytes:", os.path.getsize("agent_events.jsonl"))
print("CSV bytes:", os.path.getsize("agent_events.csv"))
print("Parquet bytes:", os.path.getsize("agent_events.parquet"))
print("Conversion completed.")
