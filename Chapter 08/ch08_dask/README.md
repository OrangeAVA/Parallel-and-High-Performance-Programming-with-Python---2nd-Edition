# Chapter 8 — Parallel Computing for Data Science (Dask)

This package contains runnable notebooks and sample data that mirror the examples from **Chapter 8**.

## Contents

```
ch08_dask/
├── data/
│   ├── myDataFrame.csv            # tiny CSV used to bootstrap pandas→Dask examples
│   └── prices_sample.csv          # synthetic version of the Kaggle prices.csv (≈50k rows)
├── notebooks/
│   ├── 08a_dask_collections.ipynb
│   ├── 08b_dask_delayed.ipynb
│   ├── 08c_groupby_prices.ipynb
│   ├── 08d_dashboard_profile_and_optimizations.ipynb
│   └── 08e_gpu_dask_cuda.ipynb    # optional (Linux + CUDA only)
├── scripts/
│   └── generate_prices_sample.py
├── requirements.txt
└── environment.yml                # optional conda env
```

## Quick start (conda)

```bash
conda create -n dask-ch08 -y python=3.10
conda activate dask-ch08
# core libs
conda install -y -c conda-forge dask distributed pandas numpy bokeh graphviz python-graphviz
# (optional) for task graph rendering in notebooks
pip install --no-cache-dir "dask[complete]"
```

Or with **pip**:

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install dask distributed pandas numpy bokeh graphviz python-graphviz
```

> **Dashboard**: when a `Client()` is created, open http://localhost:8787/status

## Optional GPU (Linux only)

If you have an NVIDIA GPU + CUDA and want to try **Dask-CUDA / RAPIDS** (optional), see:
- https://docs.rapids.ai/install/
- Packages typically include: `dask-cuda`, `cudf`, `dask-cudf`, `cupy`, `cuml`, `cugraph`.

The notebook `08e_gpu_dask_cuda.ipynb` will skip gracefully if these packages aren't present.

## Notes

- `prices_sample.csv` mimics the schema used in the chapter (`symbol,date,open,high,low,close,volume,adjusted`) and includes an **'Unnamed: 0'** column to demonstrate column dropping / dtype handling.
- Task graph visualization uses Graphviz; if missing, the code will save PNG/SVG files only when possible.
- The notebooks keep data sizes modest so they run comfortably on a laptop. Scale up partitions/sizes as desired.
