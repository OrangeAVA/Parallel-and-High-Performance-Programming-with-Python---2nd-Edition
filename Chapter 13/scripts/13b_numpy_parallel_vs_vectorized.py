from joblib import Parallel, delayed
import numpy as np
import time

def normalize(value, mean, std):
    return (value - mean) / std

def main():
    large_array = np.random.rand(1_000_000)

    mean = large_array.mean()
    std = large_array.std()

    t0 = time.time()
    res_joblib = Parallel(n_jobs=-1)(
        delayed(normalize)(v, mean, std) for v in large_array[:100_000]
    )
    t1 = time.time()
    print("Joblib (first 10):", res_joblib[:10])
    print(f"Joblib time: {t1 - t0:.3f}s")

    t0 = time.time()
    res_list = [(v - mean) / std for v in large_array[:100_000]]
    t1 = time.time()
    print("List (first 10):", res_list[:10])
    print(f"List time: {t1 - t0:.3f}s")

    t0 = time.time()
    res_vec = (large_array[:100_000] - mean) / std
    t1 = time.time()
    print("Vectorized (first 10):", res_vec[:10])
    print(f"Vectorized time: {t1 - t0:.6f}s (usually best)")

if __name__ == "__main__":
    main()
