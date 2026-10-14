//Test 1 — Duplicate run ID

INSERT INTO agent_runs
(run_id, tenant_id, agent_name, model_name,
 status, started_at, latency_ms, token_count, cost_usd)
VALUES
('run-001', 'tenant-a', 'support-agent', 'model-a',
 'success', NOW(), 100, 100, 0.001);


//Expected: blocked by the primary key because run-001 already exists.

//Test 2 — Negative latency

INSERT INTO agent_runs
(run_id, tenant_id, agent_name, model_name,
 status, started_at, latency_ms, token_count, cost_usd)
VALUES
('run-negative', 'tenant-a', 'support-agent',
 'model-a', 'success', NOW(), -100, 100, 0.001);


//Expected: blocked by CHECK (latency_ms >= 0).

//Test 3 — Nonexistent parent run

INSERT INTO tool_calls
(tool_call_id, run_id, tool_name, status, latency_ms)
VALUES
('tool-orphan', 'run-999', 'search-tool',
 'success', 100);


//Expected: blocked by the foreign key because run-999 does not exist.

//Test 4 — Incorrect tenant filter

SELECT *
FROM agent_runs
WHERE tenant_id = 'tenant-c';


//Expected: query succeeds but returns zero rows, because the sample dataset has no tenant-c.
//Important: a wrong tenant filter is not necessarily an authorization failure. The database accepts the query. In a multi-tenant production system, tenant isolation needs authorization controls such as PostgreSQL Row-Level Security (RLS), appropriate roles, and policies.

//Test 5 — Repeat ingestion

INSERT INTO agent_runs
(run_id, tenant_id, agent_name, model_name,
 status, started_at, latency_ms, token_count, cost_usd)
VALUES
('run-004', 'tenant-a', 'support-agent', 'model-a',
 'success', NOW(), 500, 700, 0.005)
ON CONFLICT (run_id) DO NOTHING;