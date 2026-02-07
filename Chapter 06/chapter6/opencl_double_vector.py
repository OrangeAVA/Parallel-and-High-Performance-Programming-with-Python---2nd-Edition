
import numpy as np, pyopencl as cl, os
os.environ.setdefault('PYOPENCL_CTX', '0')

a_host = np.array([0.1, 1.4, 2.3, 1.7], dtype=np.float32)
res_host = np.zeros(4, dtype=np.float32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_dev = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_host)
res_dev = cl.Buffer(ctx, mf.WRITE_ONLY, res_host.nbytes)

prg = cl.Program(ctx, '''
__kernel void doubled(__global const float *a_dev, __global float *res_dev){
    int gid = get_global_id(0);
    res_dev[gid] = a_dev[gid]*2.0f;
}''').build()

prg.doubled(queue, a_host.shape, None, a_dev, res_dev)
cl.enqueue_copy(queue, res_host, res_dev)
print("Vector a:", a_host)
print("Result  :", res_host)
