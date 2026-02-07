import threading
import time

shared_data = 0
lock = threading.Lock()

def funcA():
    global shared_data
    for i in range(10):
        with lock:
            local = shared_data
            local += 10
            time.sleep(1)
            shared_data = local
            print("Thread A wrote:", shared_data)

def funcB():
    global shared_data
    for i in range(10):
        with lock:
            local = shared_data
            local -= 10
            time.sleep(1)
            shared_data = local
            print("Thread B wrote:", shared_data)

t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)
t1.start(); t2.start()
t1.join(); t2.join()
