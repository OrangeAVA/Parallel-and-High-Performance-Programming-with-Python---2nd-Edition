import threading
import time

shared = 0
rlock = threading.RLock()

def func(name, t):
    global shared
    for _ in range(3):
        rlock.acquire()
        local = shared
        time.sleep(t)
        for j in range(2):
            rlock.acquire()
            local += 1
            time.sleep(0.2)
            shared = local
            print(f"Thread {name}-{j} wrote: {shared}")
            rlock.release()
        shared = local + 1
        print(f"Thread {name} wrote: {shared}")
        rlock.release()

t1 = threading.Thread(target=func, args=('A', 0.2))
t2 = threading.Thread(target=func, args=('B', 0.1))
t3 = threading.Thread(target=func, args=('C', 0.05))
t1.start(); t2.start(); t3.start()
t1.join(); t2.join(); t3.join()

print("Expected final value:", shared, "(should be 27)")
