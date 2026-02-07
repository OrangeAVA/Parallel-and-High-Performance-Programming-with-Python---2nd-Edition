
import numpy as np
from numba import cuda

@cuda.jit
def vector_add(a, b, c):
    idx = cuda.grid(1)
    if idx < a.size:
        c[idx] = a[idx] + b[idx]

def main(n=10**7):
    a = np.random.rand(n).astype(np.float32)
    b = np.random.rand(n).astype(np.float32)
    c = np.zeros_like(a)

    a_d = cuda.to_device(a)
    b_d = cuda.to_device(b)
    c_d = cuda.to_device(c)

    tpb = 256
    bpg = (n + tpb - 1) // tpb

    start = cuda.event()
    end = cuda.event()

    start.record()
    vector_add[bpg, tpb](a_d, b_d, c_d)
    end.record()
    end.synchronize()

    ms = cuda.event_elapsed_time(start, end)
    print(f"Kernel execution time: {ms:.3f} ms")

if __name__ == "__main__":
    main()
