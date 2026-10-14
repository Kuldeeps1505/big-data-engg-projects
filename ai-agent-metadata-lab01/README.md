
# AI Agent Run Metadata Database

## 1. Objective

The objective of this practical lab was to build a relational database using PostgreSQL to store and analyze AI agent execution metadata.

## 2. Database Design

Two tables were created:

- `agent_runs`: stores run identifiers, tenant IDs, agent and model names, execution status, start time, latency, token count, and model cost.
- `tool_calls`: stores tool call identifiers, associated run IDs, tool names, execution status, and tool latency.

Primary keys, foreign keys, NOT NULL constraints, and CHECK constraints were used to maintain data integrity.

## 3. Operational Queries

The following questions were answered using SQL:

1. Count successful and failed runs.
2. Identify runs with latency greater than 1,000 milliseconds.
3. Calculate average latency per agent.
4. Identify tools used during failed runs.
5. Calculate total model cost per tenant.

The sample data produced three agent runs and four tool calls.

## 4. Data Quality Testing

The duplicate run ID was rejected by the primary key. Negative latency was rejected by the CHECK constraint. A tool call referencing a nonexistent run was rejected by the foreign key.

An incorrect tenant filter returned no matching rows for the sample dataset. This test alone does not prove tenant authorization or isolation.

Repeated ingestion was tested using `ON CONFLICT (run_id) DO NOTHING`, which prevented duplicate insertion while preserving the original record.

## 5. Index Benchmark

A synthetic dataset was generated using PostgreSQL's `generate_series()` function.

The query filtering by `agent_name` was analyzed using `EXPLAIN (ANALYZE, BUFFERS)` before and after creating an index.

- Rows tested: [Enter actual row count]
- Before-index execution time: [Enter measured time]
- After-index execution time: [Enter measured time]
- Before-index scan type: [Enter actual scan type]
- After-index scan type: [Enter actual scan type]

Conclusion: [Describe the actual performance change and execution-plan observations.]

## 6. Limitations and Observations

The database enforces basic data integrity but does not define a fixed set of valid statuses or enforce tenant-level authorization.

Additional production considerations include retention policies, event identity, timestamps for tool calls, ingestion deduplication, tenant isolation using PostgreSQL Row-Level Security, and workload-based index selection.

## 7. Conclusion

This practical demonstrated relational database design, SQL aggregation, joins, constraint validation, idempotent ingestion, and query performance analysis using PostgreSQL.
