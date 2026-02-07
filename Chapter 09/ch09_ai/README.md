# Chapter 9 — Parallel Computing for Artificial Intelligence (Python)

This bundle contains runnable notebooks and scripts demonstrating **parallel & distributed AI/ML** with
- Scikit‑learn (+ Dask-ML + joblib)
- PyTorch (CPU & optional CUDA GPU)
- Dask for orchestration on a local machine or a managed cluster (e.g., Saturn Cloud)

> All notebooks are self-contained and generate their own data (or auto-download public datasets like Fashion‑MNIST via `torchvision`).

## Contents
- `notebooks/`
  - `09a_sklearn_linear_regression.ipynb` – basic ML workflow (split, fit, predict, R², plot)
  - `09b_dask_ml_scaling.ipynb` – scale scikit‑learn with **Dask-ML** + `joblib` backend
  - `09c_pytorch_fashion_mnist_cpu.ipynb` – CNN on Fashion‑MNIST (CPU)
  - `09d_pytorch_fashion_mnist_gpu.ipynb` – same CNN using **GPU** if available
  - `09e_pytorch_dask_saturn_template.ipynb` – template to run training via **Dask** locally or on **Saturn Cloud**
  - `09f_visualize_models.ipynb` – visualize networks with **torchviz**, **torchsummary**, **torchinfo** and export TorchScript for Netron
- `scripts/`
  - `09g_pytorch_ddp_minimal.py` – minimal **PyTorch DDP** (multi-process) training skeleton
- `data/`
  - `linear_regression_samples.csv` – tiny CSV used by 09a (also generated in-notebook if missing)
- `environment.yml` + `requirements.txt` – suggested dependencies

## Quickstart (Conda)
```bash
# Create environment (CPU-only baseline)
conda env create -f environment.yml
conda activate ch09-ai

# (Optional) If you have NVIDIA GPU + CUDA:
# conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

# Launch
jupyter lab
```
Then open any notebook under `notebooks/`.

## Notes
- GPU notebooks automatically fall back to CPU if CUDA is not present.
- The Saturn Cloud template notebook gracefully falls back to a **local Dask Client** if `dask-saturn` is not installed.
- The DDP script is a reference you can run with:  
  `torchrun --standalone --nproc_per_node=2 scripts/09g_pytorch_ddp_minimal.py`

Enjoy! ✨
