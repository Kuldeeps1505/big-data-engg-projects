
import json
import random
from datetime import datetime, timezone

random.seed(42)

statuses = ["success", "failed", "timeout"]

# Use one timestamp for a consistent generation run.
created_at = datetime.now(timezone.utc).isoformat()

with open("agent_events.jsonl", "w", encoding="utf-8") as file:
    for i in range(100_000):
        event = {
            "event_id": f"event-{i}",
            "tenant_id": f"tenant-{i % 10}",
            "agent_name": f"agent-{i % 4}",
            "status": random.choice(statuses),
            "latency_ms": random.randint(100, 5000),
            "token_count": random.randint(100, 3000),
            "event_date": "2026-10-09",
            "created_at": created_at,
        }

        file.write(json.dumps(event) + "\n")

print("Generated 100,000 events.")
