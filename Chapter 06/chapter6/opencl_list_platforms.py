
import pyopencl as cl

for platform in cl.get_platforms():
    print(f"Platform {platform.name}")
    print(f"  Vendor: {platform.vendor}")
    print(f"  Version: {platform.version}")
    for device in platform.get_devices():
        print(f"     Device {device.name}")
        print(f"       Max Clock Speed: {device.max_clock_frequency} MHz")
        print(f"       Compute Units: {device.max_compute_units}")
        print(f"       Local Memory: {device.local_mem_size/1024.0:.1f} KB")
        print(f"       Global Memory: {device.global_mem_size/1073741824.0:.2f} GB")
