import argparse
import pyopencl as cl
import numpy as np

KERNEL = r\"\"\"
__kernel void square(__global const float* input, __global float* output) {
    const int i = get_global_id(0);
    output[i] = input[i] * input[i];
}
\"\"\"

def list_devices():
    for pi, platform in enumerate(cl.get_platforms()):
        print(f\"[Platform {pi}] {platform.name}\")
        for di, dev in enumerate(platform.get_devices()):
            print(f\"  ({di}) {dev.name}  | Type: {cl.device_type.to_string(dev.type)}\")

def main(device_index: int):
    # Collect all devices across platforms for a simple flat index
    all_devs = []
    for platform in cl.get_platforms():
        for dev in platform.get_devices():
            all_devs.append((platform, dev))

    if device_index < 0 or device_index >= len(all_devs):
        raise SystemExit(f\"Invalid --device index {device_index}. Use --list-devices to see options.\")

    platform, device = all_devs[device_index]
    print(f\"Using device: {device.name} (Platform: {platform.name})\")

    ctx = cl.Context([device])
    queue = cl.CommandQueue(ctx)

    data = np.arange(1, 11, dtype=np.float32)
    in_buf = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=data)
    out_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, data.nbytes)

    # JIT compile for CPU/GPU; for FPGA load a precompiled binary instead
    program = cl.Program(ctx, KERNEL).build()
    program.square(queue, data.shape, None, in_buf, out_buf)
    queue.finish()

    result = np.empty_like(data)
    cl.enqueue_copy(queue, result, out_buf).wait()
    print(\"Input :\", data)
    print(\"Output:\", result)

if __name__ == \"__main__\":
    ap = argparse.ArgumentParser()
    ap.add_argument(\"--list-devices\", action=\"store_true\", help=\"List OpenCL platforms/devices and exit\")
    ap.add_argument(\"--device\", type=int, default=0, help=\"Flat device index across all platforms\")
    args = ap.parse_args()

    if args.list_devices:
        list_devices()
    else:
        main(args.device)
