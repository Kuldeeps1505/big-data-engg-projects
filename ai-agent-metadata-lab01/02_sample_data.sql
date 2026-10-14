
INSERT INTO agent_runs
(run_id, tenant_id, agent_name, model_name, status,
 started_at, latency_ms, token_count, cost_usd)
VALUES
('run-001', 'tenant-a', 'support-agent', 'model-a',
 'success', NOW(), 850, 1200, 0.012),
('run-002', 'tenant-a', 'support-agent', 'model-a',
 'failed', NOW(), 2200, 900, 0.009),
('run-003', 'tenant-b', 'research-agent', 'model-b',
 'success', NOW(), 1400, 1800, 0.021);

INSERT INTO tool_calls
(tool_call_id, run_id, tool_name, status, latency_ms)
VALUES
('tool-001', 'run-001', 'search-tool', 'success', 300),
('tool-002', 'run-002', 'search-tool', 'failed', 800),
('tool-003', 'run-002', 'database-tool', 'success', 450),
('tool-004', 'run-003', 'search-tool', 'success', 600);
