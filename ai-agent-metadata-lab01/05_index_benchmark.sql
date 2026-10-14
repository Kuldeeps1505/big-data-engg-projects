
INSERT INTO agent_runs (
    run_id, tenant_id, agent_name, model_name,
    status, started_at, latency_ms, token_count, cost_usd
)
SELECT
    'bench-' || g,
    'tenant-' || (g % 100),
    CASE
        WHEN g % 5 = 0 THEN 'research-agent'
        ELSE 'support-agent'
    END,
    CASE
        WHEN g % 2 = 0 THEN 'model-a'
        ELSE 'model-b'
    END,
    CASE
        WHEN g % 10 = 0 THEN 'failed'
        ELSE 'success'
    END,
    NOW() - (g % 30) * INTERVAL '1 day',
    100 + (g % 3000),
    500 + (g % 5000),
    ((g % 1000) + 1)::NUMERIC / 100000
FROM generate_series(1, 100000) AS g;




// indexing performance measure
EXPLAIN (ANALYZE, BUFFERS)
SELECT run_id, agent_name, latency_ms
FROM agent_runs
WHERE agent_name = 'research-agent';


CREATE INDEX idx_agent_runs_agent_name
ON agent_runs(agent_name);


EXPLAIN (ANALYZE, BUFFERS)
SELECT run_id, agent_name, latency_ms
FROM agent_runs
WHERE agent_name = 'research-agent';