
import numpy as np, pyopencl as cl, pyopencl.array, pyopencl.reduction as red
import os
os.environ.setdefault('PYOPENCL_CTX', '0')

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

ah = np.array([0.1, 1.4, 2.3, 1.7], dtype=np.float32)
bh = np.array([0.2, 0.3, 1.0, 0.5], dtype=np.float32)

a = cl.array.to_device(queue, ah)
b = cl.array.to_device(queue, bh)

krnl = red.ReductionKernel(ctx, np.float32, neutral="0",
                           reduce_expr="a+b",
                           map_expr="x[i]*y[i]",
                           arguments="__global float *x, __global float *y")

res = krnl(a, b).get()
print("Vector A:", ah)
print("Vector B:", bh)
print("Dot product:", res)
