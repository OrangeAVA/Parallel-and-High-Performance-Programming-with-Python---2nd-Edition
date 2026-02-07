
import numpy as np, time, math
from numba import cuda

@cuda.jit
def matmul(A, B, C):
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.0
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp

def bench(n, tpb):
    A = np.random.random((n, n)).astype(np.float32)
    B = np.random.random((n, n)).astype(np.float32)
    C = np.zeros((n, n), dtype=np.float32)
    A_d, B_d, C_d = cuda.to_device(A), cuda.to_device(B), cuda.to_device(C)

    threadsperblock = (tpb, tpb)
    blockspergrid_x = math.ceil(n / tpb)
    blockspergrid_y = math.ceil(n / tpb)
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    start = time.perf_counter()
    matmul[blockspergrid, threadsperblock](A_d, B_d, C_d)
    cuda.synchronize()
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    sizes = [1024, 2048, 3072, 4096]
    tpbs = [16, 32]
    for n in sizes:
        row = []
        for t in tpbs:
            try:
                dt = bench(n, t)
                row.append(f"{dt:.2f}s")
            except cuda.cudadrv.driver.CudaAPIError as e:
                row.append("N/A")
        print(f"n={n} -> tpb={tpbs}: {row}")
