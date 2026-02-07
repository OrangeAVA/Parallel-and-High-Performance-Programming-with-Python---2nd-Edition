from joblib import Parallel, delayed
import time

def expensive_operation(n: int) -> int:
    time.sleep(1.0)
    return n ** 3

def run_parallel(num_tasks=6, n_jobs=3):
    t0 = time.time()
    results = Parallel(n_jobs=n_jobs)(delayed(expensive_operation)(i) for i in range(num_tasks))
    dt = time.time() - t0
    print(f"Parallel ({n_jobs} jobs) results: {results}")
    print(f"Parallel time: {dt:.2f}s")

def run_sequential(num_tasks=6):
    t0 = time.time()
    results = [expensive_operation(i) for i in range(num_tasks)]
    dt = time.time() - t0
    print(f"Sequential results: {results}")
    print(f"Sequential time: {dt:.2f}s")

if __name__ == "__main__":
    run_parallel(num_tasks=6, n_jobs=3)
    run_sequential(num_tasks=6)
