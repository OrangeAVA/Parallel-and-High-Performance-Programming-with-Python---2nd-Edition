# Chapter 4 — Asynchronous Programming (AsyncIO) — Code Pack

This folder contains runnable Python scripts for each example from Chapter 4.
File naming: `ch04_XX_*.py`. Many scripts are self-contained. Some (like aiohttp) require extra packages or internet access.

Suggested order:
1. ch04_01_asyncio_hello.py
2. ch04_03_coroutine_await.py
3. ch04_04_create_task.py
4. ch04_05_tasks_concurrent.py vs ch04_06_coroutines_sequential.py
5. ch04_07_task_names.py / ch04_08_gather_returns.py
6. ch04_09_future_basic.py
7. ch04_10_event_loop_explicit.py
8. ch04_11_async_generator.py / ch04_12_as_completed.py
9. ch04_13_queue_producer_consumer.py
10. ch04_15_run_in_executor_factorial.py / ch04_16_run_in_executor_heavy.py
11. ch04_17_error_handling_local.py / ch04_18_gather_return_exceptions.py / ch04_19_retry_timeout_logging.py
12. Patterns: ch04_20..24

> Note: `ch04_14_aiohttp_many_requests.py` requires `aiohttp` and network access.
