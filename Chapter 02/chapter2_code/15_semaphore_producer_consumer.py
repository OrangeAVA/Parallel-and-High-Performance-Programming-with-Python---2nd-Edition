import threading
import time
import random

N_ITEMS = 5
slots = threading.Semaphore(1)
items = threading.Semaphore(0)

buffer = {"value": None}
print_lock = threading.Lock()

def producer():
    for i in range(1, N_ITEMS + 1):
        slots.acquire()
        v = random.randint(0, 100)
        time.sleep(random.uniform(0.2, 0.6))
        buffer["value"] = v
        with print_lock:
            print(f"producer -> put {v:3d} (item {i})")
        items.release()

def consumer():
    for i in range(1, N_ITEMS + 1):
        items.acquire()
        v = buffer["value"]
        time.sleep(random.uniform(0.1, 0.5))
        with print_lock:
            print(f"consumer <- got {v:3d} (item {i})")
        buffer["value"] = None
        slots.release()

tp = threading.Thread(target=producer, name="Producer")
tc = threading.Thread(target=consumer, name="Consumer")
tp.start(); tc.start()
tp.join(); tc.join()
print("Done.")
