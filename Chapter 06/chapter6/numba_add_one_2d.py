
import numpy as np
from numba import cuda
import math

@cuda.jit
def add_one_2D(A):
    x, y = cuda.grid(2)
    if x < A.shape[0] and y < A.shape[1]:
        A[x, y] += 1

def main():
    n = 4
    A_host = np.random.random((n, n)).astype(np.float32)
    print("Matrix A:\n", A_host)

    A_dev = cuda.to_device(A_host)

    threadsperblock = (16, 16)
    blockspergrid_x = math.ceil(A_host.shape[0] / threadsperblock[0])
    blockspergrid_y = math.ceil(A_host.shape[1] / threadsperblock[1])
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    add_one_2D[blockspergrid, threadsperblock](A_dev)
    cuda.synchronize()

    out = A_dev.copy_to_host()
    print("New Matrix A:\n", out)

if __name__ == "__main__":
    main()
