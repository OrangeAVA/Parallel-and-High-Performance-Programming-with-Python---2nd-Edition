import numpy as np
import pickle, gzip, time, os
from joblib import dump, load

def human_mb(bytes_):
    return f"{bytes_ / 1e6:.2f} MB"

def main():
    n = 10_000_000  # ~80MB float64
    arr = np.random.rand(n)

    # Joblib (uncompressed)
    t0 = time.time()
    dump(arr, "large_array_joblib.joblib")
    t1 = time.time()
    t_joblib_save = t1 - t0

    t0 = time.time()
    _ = load("large_array_joblib.joblib")
    t1 = time.time()
    t_joblib_load = t1 - t0

    # Joblib compressed
    t0 = time.time()
    dump(arr, "large_array_compressed.joblib", compress=3)
    t1 = time.time()
    t_joblib_c_save = t1 - t0

    t0 = time.time()
    _ = load("large_array_compressed.joblib")
    t1 = time.time()
    t_joblib_c_load = t1 - t0

    # Pickle (uncompressed)
    t0 = time.time()
    with open("large_array_pickle.pkl", "wb") as f:
        pickle.dump(arr, f, protocol=pickle.HIGHEST_PROTOCOL)
    t1 = time.time()
    t_pickle_save = t1 - t0

    t0 = time.time()
    with open("large_array_pickle.pkl", "rb") as f:
        _ = pickle.load(f)
    t1 = time.time()
    t_pickle_load = t1 - t0

    # Pickle + gzip
    t0 = time.time()
    with gzip.open("large_array_pickle_compressed.pkl.gz", "wb") as f:
        pickle.dump(arr, f, protocol=pickle.HIGHEST_PROTOCOL)
    t1 = time.time()
    t_pickle_c_save = t1 - t0

    t0 = time.time()
    with gzip.open("large_array_pickle_compressed.pkl.gz", "rb") as f:
        _ = pickle.load(f)
    t1 = time.time()
    t_pickle_c_load = t1 - t0

    sizes = {
        "joblib": os.path.getsize("large_array_joblib.joblib"),
        "joblib_compressed": os.path.getsize("large_array_compressed.joblib"),
        "pickle": os.path.getsize("large_array_pickle.pkl"),
        "pickle_gzip": os.path.getsize("large_array_pickle_compressed.pkl.gz"),
    }

    print("=== Save/Load Times ===")
    print(f"Joblib (uncompressed): save={t_joblib_save:.2f}s load={t_joblib_load:.2f}s")
    print(f"Joblib (compressed):   save={t_joblib_c_save:.2f}s load={t_joblib_c_load:.2f}s")
    print(f"Pickle (uncompressed):  save={t_pickle_save:.2f}s load={t_pickle_load:.2f}s")
    print(f"Pickle (gzip):          save={t_pickle_c_save:.2f}s load={t_pickle_c_load:.2f}s")

    print("\n=== File sizes ===")
    for k, v in sizes.items():
        print(f"{k:18s} {human_mb(v)}")

if __name__ == "__main__":
    main()
