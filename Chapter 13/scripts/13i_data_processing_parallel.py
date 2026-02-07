import numpy as np
import pandas as pd
from joblib import Parallel, delayed, dump, load
import time

def transformation_tuple(row) -> float:
    return row.column1 * 2.0 + row.column2 ** 2

def main():
    n_rows = 1_000_000
    df = pd.DataFrame({
        "column1": np.random.rand(n_rows),
        "column2": np.random.rand(n_rows),
    })

    t0 = time.time()
    results = Parallel(n_jobs=-1, batch_size=10_000)(
        delayed(transformation_tuple)(row) for row in df.itertuples(index=False)
    )
    df["result"] = results
    t1 = time.time()
    print(f"Parallel row-wise time: {t1 - t0:.2f}s")
    print(df.head())

    t0 = time.time()
    df["result_vec"] = df["column1"] * 2.0 + df["column2"] ** 2
    t1 = time.time()
    print(f"Vectorized time: {t1 - t0:.2f}s")

    dump(df, "preprocessed_dataset.joblib")
    print("Saved preprocessed_dataset.joblib")

    df2 = load("preprocessed_dataset.joblib")
    print("Reloaded shape:", df2.shape)

if __name__ == "__main__":
    main()
