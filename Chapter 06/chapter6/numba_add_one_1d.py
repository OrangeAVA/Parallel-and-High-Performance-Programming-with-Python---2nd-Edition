
import numpy as np
from numba import cuda

@cuda.jit
def add_one(a):
    pos = cuda.grid(1)
    if pos < a.size:
        a[pos] += 1

def main():
    n = 10
    a_host = np.random.random(n).astype(np.float32)
    print("Vector a:", a_host)

    a_dev = cuda.to_device(a_host)
    threads_per_block = 128
    blocks_per_grid = (a_host.size + threads_per_block - 1) // threads_per_block

    add_one[blocks_per_grid, threads_per_block](a_dev)
    cuda.synchronize()

    out = a_dev.copy_to_host()
    print("New Vector a:", out)

if __name__ == "__main__":
    main()
