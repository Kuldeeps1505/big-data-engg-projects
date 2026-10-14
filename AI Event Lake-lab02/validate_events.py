
import pandas as pd

source = pd.read_json("agent_events.jsonl", lines=True)
result = pd.read_parquet("agent_events.parquet")

# Check row counts and column names.
assert len(source) == 100_000
assert len(source) == len(result)
assert list(source.columns) == list(result.columns)

# Check key columns and ordering.
for column in ["event_id", "tenant_id", "agent_name",
               "status", "event_date"]:
    assert source[column].equals(result[column]), column

# Check numeric values.
for column in ["latency_ms", "token_count"]:
    assert source[column].equals(result[column]), column
    assert str(result[column].dtype) == "int64"

# Check required values and ranges.
assert source["event_id"].is_unique
assert result["event_id"].is_unique
assert not result.isnull().any().any()
assert result["latency_ms"].ge(0).all()
assert result["token_count"].ge(0).all()

# Compare timestamps as parsed UTC datetime values.
source_times = pd.to_datetime(source["created_at"], utc=True)
result_times = pd.to_datetime(result["created_at"], utc=True)
assert source_times.equals(result_times)

print("Validation passed")
print("Source rows:", len(source))
print("Parquet rows:", len(result))
print("All checked columns match.")
