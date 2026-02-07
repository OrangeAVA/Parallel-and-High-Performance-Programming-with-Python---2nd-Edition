# Chapter 15 – Parallel Programming with FPGAs (Assets)

This bundle accompanies the chapter and gives you **runnable Python examples** for FPGA-style development and simulation,
plus PyOpenCL kernels you can run on **CPU/GPU** (and on FPGA if you have the vendor OpenCL toolchain).

## Contents
- `scripts/myhdl_counter.py` – 4‑bit synchronous counter (simulation with MyHDL).
- `scripts/myhdl_vector_adder.py` – 4×(8‑bit) **parallel vector adder** (simulation with MyHDL).
- `scripts/pyopencl_square.py` – PyOpenCL "square each element" kernel (runs on CPU/GPU; FPGA if supported).
- `scripts/pyopencl_matvec.py` – **Matrix–vector multiplication** with an optimized OpenCL kernel.
- `docs/fpga_vs_gpu.md` – Summary notes and comparison table.
- `requirements.txt` – Core Python deps for local runs (simulation / OpenCL host code).
- `environment.yml` – Optional Conda env.

> 💡 **Tip:** You can run all OpenCL examples on a CPU or GPU even if you don't have an FPGA; that still demonstrates the programming model.
> To use an FPGA you must have the proper OpenCL runtime (Intel FPGA SDK for OpenCL or AMD/Xilinx Vitis) and precompiled kernel binaries
> for your device family (e.g. `.aocx` / `.xclbin`).

---

## Quick start (simulation only)

```bash
# (Recommended) create a fresh venv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install the basics
pip install -r requirements.txt
```

Run the **MyHDL** simulations:

```bash
python scripts/myhdl_counter.py
python scripts/myhdl_vector_adder.py
```

> If you don’t have a physical FPGA, MyHDL lets you develop & test logic **entirely in Python**.

---

## OpenCL examples (CPU/GPU and optionally FPGA)

You need:
- **OpenCL runtime/driver** (GPU: your vendor’s driver; CPU: Intel/POCL; FPGA: *Intel FPGA SDK for OpenCL* or *Xilinx Vitis*).
- `pyopencl` Python package (already in `requirements.txt`).

```bash
# Square each element
python scripts/pyopencl_square.py --list-devices
python scripts/pyopencl_square.py --device 0

# Matrix–vector product
python scripts/pyopencl_matvec.py --device 0
```

### Using an FPGA device
- Ensure your board’s **OpenCL platform** is visible via `pyopencl`.
- **FPGAs require ahead–of–time compilation** of kernels:
  - Intel: build `.aocx` with `aoc`
  - AMD/Xilinx: build `.xclbin` with Vitis
- Modify the scripts to **load the vendor binary** instead of JIT-compiling from source.
  Example (Intel):  
  ```python
  binary = open("kernel.aocx", "rb").read()
  program = cl.Program(ctx, [device], [binary]).build()
  ```

> If you only have CPU/GPU, the current scripts compile from source at runtime (`program = cl.Program(...).build()`).

---

## Notes
- The MyHDL examples illustrate **clocked logic** and **data‑parallel adders**.
- The OpenCL examples mirror data‑parallel kernels that map naturally to FPGA pipelines.
- For production FPGA work, consider **PYNQ** (Zynq), **AMD Vitis** (incl. Vitis AI), or convert MyHDL → VHDL/Verilog for vendor flows.

Enjoy hacking! 🚀
