
import numpy as np
from numba import cuda
import math

@cuda.jit
def matmul(A, B, C):
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.0
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp

def main():
    n = 256
    A = np.random.random((n, n)).astype(np.float32)
    B = np.random.random((n, n)).astype(np.float32)
    C = np.zeros((n, n), dtype=np.float32)

    A_d = cuda.to_device(A)
    B_d = cuda.to_device(B)
    C_d = cuda.to_device(C)

    threadsperblock = (16, 16)
    blockspergrid_x = math.ceil(A.shape[0] / threadsperblock[0])
    blockspergrid_y = math.ceil(B.shape[1] / threadsperblock[1])
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    matmul[blockspergrid, threadsperblock](A_d, B_d, C_d)
    cuda.synchronize()
    C = C_d.copy_to_host()
    print("C shape:", C.shape, " sample:", C.ravel()[:5])

if __name__ == "__main__":
    main()
