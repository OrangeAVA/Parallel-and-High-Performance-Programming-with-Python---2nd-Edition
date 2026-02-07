import argparse
import numpy as np
import pyopencl as cl

KERNEL = r\"\"\"
__kernel void mat_vec_mult(__global const float* matrix,
                           __global const float* vector,
                           __global float* result,
                           const int N) {
    int row = get_global_id(0);
    float sum = 0.0f;

    #pragma unroll
    for (int col = 0; col < N; ++col) {
        sum += matrix[row * N + col] * vector[col];
    }
    result[row] = sum;
}
\"\"\"

def list_devices():
    for pi, platform in enumerate(cl.get_platforms()):
        print(f\"[Platform {pi}] {platform.name}\")
        for di, dev in enumerate(platform.get_devices()):
            print(f\"  ({di}) {dev.name}  | Type: {cl.device_type.to_string(dev.type)}\")

def main(device_index: int, N: int):
    matrix = np.arange(1, N*N+1, dtype=np.float32).reshape(N, N)
    vector = np.arange(1, N+1, dtype=np.float32)
    expected = matrix @ vector

    all_devs = []
    for platform in cl.get_platforms():
        for dev in platform.get_devices():
            all_devs.append((platform, dev))
    if device_index < 0 or device_index >= len(all_devs):
        raise SystemExit(f\"Invalid --device index {device_index}. Use --list-devices.\")

    platform, device = all_devs[device_index]
    print(f\"Using device: {device.name} (Platform: {platform.name})\")
    ctx = cl.Context([device])
    queue = cl.CommandQueue(ctx)

    m_buf = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=matrix)
    v_buf = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=vector)
    r_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, vector.nbytes)

    program = cl.Program(ctx, KERNEL).build()

    N32 = np.int32(N)
    program.mat_vec_mult(queue, (N,), None, m_buf, v_buf, r_buf, N32)
    queue.finish()

    result = np.empty_like(vector)
    cl.enqueue_copy(queue, result, r_buf).wait()

    print(\"Matrix:\\n\", matrix)
    print(\"Vector:\", vector)
    print(\"Result:\", result)
    print(\"Matches NumPy:\", np.allclose(result, expected))

if __name__ == \"__main__\":
    ap = argparse.ArgumentParser()
    ap.add_argument(\"--list-devices\", action=\"store_true\", help=\"List OpenCL platforms/devices and exit\")
    ap.add_argument(\"--device\", type=int, default=0, help=\"Flat device index across all platforms\")
    ap.add_argument(\"--N\", type=int, default=3, help=\"Size of square matrix/vector\")
    args = ap.parse_args()

    if args.list_devices:
        list_devices()
    else:
        main(args.device, args.N)
