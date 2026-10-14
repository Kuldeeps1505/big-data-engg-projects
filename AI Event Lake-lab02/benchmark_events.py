
import os
import time
import statistics
import duckdb

con = duckdb.connect(":memory:")

queries = {
    "CSV": """
        SELECT agent_name, status,
               COUNT(*) AS event_count,
               AVG(latency_ms) AS avg_latency_ms,
               SUM(token_count) AS total_tokens
        FROM read_csv_auto('agent_events.csv')
        GROUP BY agent_name, status
        ORDER BY agent_name, status
    """,
    "Parquet": """
        SELECT agent_name, status,
               COUNT(*) AS event_count,
               AVG(latency_ms) AS avg_latency_ms,
               SUM(token_count) AS total_tokens
        FROM read_parquet('agent_events.parquet')
        GROUP BY agent_name, status
        ORDER BY agent_name, status
    """
}

# Warm up and check that both produce the same results.
expected = con.execute(queries["Parquet"]).fetchall()
csv_result = con.execute(queries["CSV"]).fetchall()
assert csv_result == expected, "CSV and Parquet results differ"

# Run repeated measurements.
for name, query in queries.items():
    con.execute(query).fetchall()  # warm-up
    times = []

    for _ in range(5):
        start = time.perf_counter()
        rows = con.execute(query).fetchall()
        times.append(time.perf_counter() - start)

    print(f"\n{name}")
    print("File bytes:", os.path.getsize(
        "agent_events.csv" if name == "CSV"
        else "agent_events.parquet"
    ))
    print("Median query seconds:",
          round(statistics.median(times), 6))
    print("All query times:",
          [round(t, 6) for t in times])

print("\nCSV and Parquet query results match.")
con.close()
