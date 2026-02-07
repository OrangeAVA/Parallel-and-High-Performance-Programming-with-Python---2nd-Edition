# FPGA vs GPU – At a glance

| Feature | GPU | FPGA |
|---|---|---|
| Parallelism | High (SIMD/SIMT) | High, **custom pipelines** |
| Latency | Higher | **Very low** |
| Energy efficiency | Moderate | **High / Very high** |
| Customization | Limited (fixed uArch) | **Full hardware specialization** |
| Flexibility (software) | **High** | Lower (HDL/HLS/toolchains) |
| Cost to develop | Lower | Higher (tooling + effort) |

**When to pick GPUs**
- General purpose parallel compute
- Throughput over latency (DL training, analytics)
- Fast iteration with rich libraries (CUDA/cuBLAS/cuDNN)

**When to pick FPGAs**
- **Latency‑critical** inference / signal processing / HFT
- Edge/embedded with tight power budgets
- Fixed, repetitive kernels that benefit from hardware pipelines
