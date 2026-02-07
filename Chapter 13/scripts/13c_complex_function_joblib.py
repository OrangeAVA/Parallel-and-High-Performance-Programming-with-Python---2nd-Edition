from joblib import Parallel, delayed
import numpy as np
import time, math

def complex_function(x: float) -> float:
    # Non-vectorizable-ish workload (Python math + condition)
    acc = 0.0
    for i in range(1, 500):  # keep moderate for demo
        acc += math.sin(x * i) ** 2 + math.cos(x / (i + 1)) ** 3
    return acc ** 0.5 if x > 0.5 else acc ** 0.33

def main():
    arr = np.random.rand(100_000)  # adjust up if you want a heavier run

    t0 = time.time()
    res_par = Parallel(n_jobs=-1)(delayed(complex_function)(x) for x in arr)
    t1 = time.time()
    print("Parallel time:", round(t1 - t0, 2), "s")

    t0 = time.time()
    res_seq = [complex_function(x) for x in arr]
    t1 = time.time()
    print("Sequential time:", round(t1 - t0, 2), "s")

    # Sanity check
    assert len(res_par) == len(res_seq)
    print("Results match length:", len(res_par))

if __name__ == "__main__":
    main()
