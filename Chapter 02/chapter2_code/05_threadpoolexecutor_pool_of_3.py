import concurrent.futures
import time
import random
import threading

def task(i, sleep_s):
    tname = threading.current_thread().name
    print(f"[{time.strftime('%H:%M:%S')}] START task={i:02d} sleep={sleep_s:.1f}s on {tname}")
    time.sleep(sleep_s)
    print(f"[{time.strftime('%H:%M:%S')}] END   task={i:02d} on {tname}")
    return i, sleep_s

durations = [1.5, 0.8, 2.2, 0.5, 1.0, 1.7, 0.6, 2.0, 0.9, 1.3]

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i, d) for i, d in enumerate(durations, start=1)]
    for fut in concurrent.futures.as_completed(futures):
        i, d = fut.result()

print("Program ended")
