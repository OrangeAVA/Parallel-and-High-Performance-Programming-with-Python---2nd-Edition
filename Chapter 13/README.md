# Chapter 13 — Joblib (Code Package)

This bundle contains runnable Python scripts and lightweight notebooks that mirror the examples in **Chapter 13 – Joblib**.

## Contents
- **scripts/**: Standalone `.py` files for each section (parallelism, NumPy, caching, persistence, ML, data processing).
- **notebooks/**: Minimal Jupyter notebooks with the same examples (handy for step‑by‑step runs).
- **data/**: Placeholder for your datasets (not required by these examples).
- **cache_dir/**: Folder used by Joblib `Memory` caching demo.
- **requirements.txt / environment.yml**: Quick setup for pip/conda.

> All scripts are safe to run locally. Some include adjustable sizes/loops for heavier benchmarks; defaults are modest to fit a laptop.

---

## Quickstart

```bash
# (Optional) Create and activate a virtual env
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -U pip
pip install -r requirements.txt
```

Run a quick demo (parallel basics):
```bash
python scripts/13a_parallel_basics.py
```

Open notebooks:
```bash
pip install jupyter
jupyter notebook notebooks/
```

---

## Scripts Overview

**Parallelization**
- `13a_parallel_basics.py` — `Parallel` + `delayed` basics, sequential vs parallel timing.
- `13a_parallel_expensive.py` — Simulates an expensive CPU task (sleep + power), compares sequential vs parallel.

**NumPy & Parallel vs Vectorization**
- `13b_numpy_parallel_vs_vectorized.py` — Normalization with Joblib vs pure Python list vs NumPy vectorization.
- `13c_complex_function_joblib.py` — CPU‑bound non‑vectorizable workload; Joblib shines here.

**Persistence**
- `13d_persistence_joblib_vs_pickle.py` — Save/load with Joblib vs Pickle (compressed/uncompressed). Defaults ~80MB array; adjust sizes if you want.

**Caching**
- `13e_cache_memory.py` — `joblib.Memory` persistent caching demo (re-run to see cache hits).

**Machine Learning**
- `13f_ml_save_load.py` — Train RandomForest on Iris, save & load with Joblib.
- `13g_ml_gridsearch_parallel.py` — `GridSearchCV` using all cores (`n_jobs=-1`), save best model.
- `13h_ml_preprocessing_persist.py` — Persist transformed dataset (`StandardScaler`) + reuse best model.

**Data Processing**
- `13i_data_processing_parallel.py` — Parallel row-wise transform on a 1M‑row DataFrame + vectorized alternative + persistence.

---

## Tips & Notes

- **Choosing `n_jobs`**: `-1` uses all cores. For laptops, feel free to use `n_jobs=4`–`8` to keep the system responsive.
- **NumPy Vectorization** usually beats Python‑level parallel loops for arithmetic array ops. Use Joblib when logic is non‑vectorizable or CPU‑bound per element.
- **Caching**: The `@memory.cache` decorator hashes inputs _and function source_. Change function body → cache invalidated.
- **Large arrays in persistence benchmark**: Defaults are moderate (10M floats ≈ 80MB). You can scale up, but check your RAM/disk.
- **Windows users**: Wrap run blocks in `if __name__ == "__main__":` (already done) to avoid multiprocessing spawn issues.

Enjoy!
