# Chapter 5 — Distributed Python (Celery, Dramatiq, SCOOP)

This package contains runnable examples for the chapter on distributed systems.
Some examples need external services (Redis or RabbitMQ). Others run locally.

## Contents

### Celery
- `celery_tasks_basic/tasks.py` — minimal Celery app with `add`, `mul`, `xsum` tasks.
- `celery_tasks_basic/client_basic.py` — calls tasks via `delay()`/`apply_async()`.
- `celery_tasks_flow/client_group_chain_chord.py` — uses `group`, `chain`, `chord`.
- `pi_celery/pi_calculator.py` — Monte Carlo π with Celery `group` + `chord`.
- `pi_celery/pi_client.py` — client that runs the π simulation.
- `celery_queues/celery_app.py` — queue/routing configuration (default/high/low).
- `celery_queues/tasks.py` — `send_email`, `process_data`, `backup_database` tasks.
- `celery_queues/main.py` — enqueues tasks for different queues.

### Dramatiq
- `dramatiq_basic/dramaserver.py` — basic actor (`wait`) and broker setup comments.
- `dramatiq_basic/dramaclient.py` — fire-and-forget sends in a loop.
- `dramatiq_basic/dramaclient_group.py` — runs a `group` of messages.
- `dramatiq_results/dramaserver_results.py` — Redis-backed results example.
- `dramatiq_results/dramaclient_results.py` — collects results with `get_results`.

### SCOOP
- `scoop_basic/scoopy.py` — toy worker print demo.
- `scoop_basic/scoopy2.py` — returns results; control worker count with `-n`.
- `scoop_basic/scoopy_mapreduce.py` — `mapReduce` and chained map+reduce.
- `scoop_pi/scoopy_pi.py` — Monte Carlo π with SCOOP.

## Quick prerequisites

- Python 3.10+ recommended.
- Create and activate a virtual env.

### Celery
- Install:
  ```bash
  pip install "celery>=5.3" redis kombu
  ```
- Start Redis (Docker recommended):
  ```bash
  docker run -d --name redis -p 6379:6379 redis
  ```
- Start a worker (Linux/macOS):
  ```bash
  celery -A tasks worker --loglevel=INFO
  ```
  On **Windows**, use threads pool:
  ```bash
  celery -A tasks worker --pool=threads --loglevel=INFO
  ```

### Dramatiq
- Install (with Redis extras):
  ```bash
  pip install "dramatiq>=1.13" "dramatiq[redis]" redis
  ```
- Start Redis (see above).
- Run server:
  ```bash
  dramatiq dramaserver
  ```

### SCOOP
- Install:
  ```bash
  pip install scoop
  ```
- Run:
  ```bash
  python -m scoop scoopy.py
  ```

> Note: Some output snippets in the book are illustrative; PIDs/timestamps vary.

## Windows notes
- Celery `prefork` is unsupported; pass `--pool=threads` (or `--pool=eventlet` with eventlet installed).
- Docker Desktop is recommended to run Redis/RabbitMQ locally.

## Security
- Example credentials use localhost only; never expose Redis/RabbitMQ without auth/TLS in production.
