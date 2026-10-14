
import duckdb

result = duckdb.sql("""
    SELECT
        agent_name,
        status,
        COUNT(*) AS event_count,
        ROUND(AVG(latency_ms), 2) AS avg_latency_ms,
        SUM(token_count) AS total_tokens
    FROM read_parquet('agent_events.parquet')
    GROUP BY agent_name, status
    ORDER BY agent_name, status
""").df()

print(result.to_string(index=False))
