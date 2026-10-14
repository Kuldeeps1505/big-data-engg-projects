
SELECT run_id, agent_name, latency_ms
FROM agent_runs
WHERE latency_ms > 1000
ORDER BY latency_ms DESC;



SELECT
    agent_name,
    ROUND(AVG(latency_ms), 2) AS avg_latency_ms
FROM agent_runs
GROUP BY agent_name
ORDER BY agent_name;



SELECT
    agent_name,
    ROUND(AVG(latency_ms), 2) AS avg_latency_ms
FROM agent_runs
GROUP BY agent_name
ORDER BY agent_name;



SELECT
    r.run_id,
    r.status AS run_status,
    t.tool_name,
    t.status AS tool_status
FROM agent_runs r
JOIN tool_calls t ON t.run_id = r.run_id
WHERE r.status = 'failed';



SELECT
    tenant_id,
    SUM(cost_usd) AS total_cost_usd
FROM agent_runs
GROUP BY tenant_id
ORDER BY tenant_id;
