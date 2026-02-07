
import numpy as np, time, math
from numba import cuda, float32

TILE = 32

@cuda.jit
def matmul_shared(A, B, C, N):
    sA = cuda.shared.array((TILE, TILE), dtype=float32)
    sB = cuda.shared.array((TILE, TILE), dtype=float32)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bx = cuda.blockIdx.x
    by = cuda.blockIdx.y

    row = by * TILE + ty
    col = bx * TILE + tx

    tmp = 0.0
    for m in range((N + TILE - 1)//TILE):
        if row < N and m*TILE + tx < N:
            sA[ty, tx] = A[row, m*TILE + tx]
        else:
            sA[ty, tx] = 0.0
        if col < N and m*TILE + ty < N:
            sB[ty, tx] = B[m*TILE + ty, col]
        else:
            sB[ty, tx] = 0.0
        cuda.syncthreads()

        for k in range(TILE):
            tmp += sA[ty, k] * sB[k, tx]
        cuda.syncthreads()

    if row < N and col < N:
        C[row, col] = tmp

@cuda.jit
def matmul_global(A, B, C, N):
    row, col = cuda.grid(2)
    if row < N and col < N:
        tmp = 0.0
        for k in range(N):
            tmp += A[row, k] * B[k, col]
        C[row, col] = tmp

def bench(N=2048):
    A = np.random.rand(N, N).astype(np.float32)
    B = np.random.rand(N, N).astype(np.float32)
    C1 = np.zeros((N, N), dtype=np.float32)
    C2 = np.zeros((N, N), dtype=np.float32)

    A_d, B_d = cuda.to_device(A), cuda.to_device(B)
    C1_d, C2_d = cuda.to_device(C1), cuda.to_device(C2)

    blocks = ((N + TILE - 1)//TILE, (N + TILE - 1)//TILE)
    threads = (TILE, TILE)

    t0 = time.time()
    matmul_shared[blocks, threads](A_d, B_d, C1_d, N)
    cuda.synchronize()
    t1 = time.time()
    t_shared = t1 - t0

    t0 = time.time()
    matmul_global[blocks, threads](A_d, B_d, C2_d, N)
    cuda.synchronize()
    t1 = time.time()
    t_global = t1 - t0

    print(f"N={N} -> shared={t_shared:.2f}s, global={t_global:.2f}s")

if __name__ == "__main__":
    bench(1024)
    bench(2048)
