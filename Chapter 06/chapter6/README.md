# Chapter 6 – GPU Programming with Python

This folder contains ready-to-run examples for **Numba (CUDA)** and **PyOpenCL** from your Chapter 6 draft.

> ⚠️ **Prereqs**
>
> - NVIDIA GPU + CUDA toolkit (for Numba/CUDA examples)
> - Appropriate OpenCL drivers (for PyOpenCL examples)
> - Python 3.10+ recommended
>
> Create and activate a virtual environment, then:
>
> ```bash
> pip install -r requirements.txt
> ```
>
> For Windows with multiple OpenCL platforms, you can set:
>
> ```bash
> set PYOPENCL_CTX=0
> ```
> Or on Unix:
> ```bash
> export PYOPENCL_CTX=0
> ```

## Contents

### Numba (CUDA)
- `numba_add_one_1d.py` – 1D array increment with CUDA grid helpers
- `numba_add_one_2d.py` – 2D matrix increment
- `numba_matmul.py` – dense matmul on GPU
- `numba_matmul_benchmark.py` – size & thread-block sweep, timing
- `numba_coalesced_vs_noncoalesced.py` – memory coalescing comparison
- `numba_shared_vs_global_matmul.py` – tiled shared memory matmul vs global
- `numba_profile_vector_add.py` – CUDA events & Nsight-ready profiling

### PyOpenCL
- `opencl_list_platforms.py` – enumerate platforms/devices
- `opencl_double_vector.py` – simple kernel with buffers
- `opencl_matmul.py` – dense matmul
- `opencl_matmul_timed.py` – timed matmul
- `opencl_elementwise.py` – `ElementwiseKernel` demo
- `opencl_reduction.py` – `ReductionKernel` map-reduce

---

## Quickstart

```bash
# Numba CUDA: increment 1D
python numba_add_one_1d.py

# PyOpenCL: list platforms
python opencl_list_platforms.py

# Nsight Systems (example; adjust path)
# nsys profile python numba_profile_vector_add.py
```
