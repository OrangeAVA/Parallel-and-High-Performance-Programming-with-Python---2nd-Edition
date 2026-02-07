
import numpy as np, time
from numba import cuda

@cuda.jit
def vector_add_coalesced(a, b, c):
    idx = cuda.grid(1)
    if idx < a.size:
        c[idx] = a[idx] + b[idx]

@cuda.jit
def vector_add_non_coalesced(a, b, c):
    idx = cuda.grid(1)
    if idx < a.size:
        c[idx] = a[(idx * 512) % a.size] + b[(idx * 512) % b.size]

def run(n=10**7):
    a = np.random.rand(n).astype(np.float32)
    b = np.random.rand(n).astype(np.float32)
    c = np.zeros_like(a)

    a_d = cuda.to_device(a)
    b_d = cuda.to_device(b)
    c_d = cuda.to_device(c)

    tpb = 256
    bpg = (n + tpb - 1) // tpb

    t0 = time.time()
    vector_add_coalesced[bpg, tpb](a_d, b_d, c_d)
    cuda.synchronize()
    t1 = time.time()
    c = c_d.copy_to_host()

    print("Coalesced first 5:", c[:5], "time:", f"{t1-t0:.3f}s")

    t0 = time.time()
    vector_add_non_coalesced[bpg, tpb](a_d, b_d, c_d)
    cuda.synchronize()
    t1 = time.time()
    c = c_d.copy_to_host()
    print("Non-coalesced first 5:", c[:5], "time:", f"{t1-t0:.3f}s")

if __name__ == "__main__":
    run()
