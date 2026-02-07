
import numpy as np, pyopencl as cl, pyopencl.array
from pyopencl.elementwise import ElementwiseKernel
import os
os.environ.setdefault('PYOPENCL_CTX', '0')

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

a_host = np.array([0.1, 1.4, 2.3, 1.7], dtype=np.float32)
b_host = np.array([0.2, 0.3, 1.0, 0.5], dtype=np.float32)

a_dev = cl.array.to_device(queue, a_host)
b_dev = cl.array.to_device(queue, b_host)
res_dev = cl.array.empty_like(a_dev)

add = ElementwiseKernel(ctx,
    "float *a_dev, float *b_dev, float *res_dev",
    "res_dev[i] = a_dev[i] + b_dev[i]",
    "add")

add(a_dev, b_dev, res_dev)

print("Vector A:", a_host)
print("Vector B:", b_host)
print("Vector Result:", res_dev.get())
