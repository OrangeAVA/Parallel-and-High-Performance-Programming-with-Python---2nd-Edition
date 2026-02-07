import threading, time

shared_data = 0

def funcA():
    global shared_data
    for i in range(10_000):
        v = shared_data
        time.sleep(0)
        shared_data = v + 10
        if i % 2000 == 0:
            print(f"A i={i:5d} -> {shared_data}")

def funcB():
    global shared_data
    for i in range(10_000):
        v = shared_data
        time.sleep(0)
        shared_data = v - 10
        if i % 2000 == 0:
            print(f"B i={i:5d} -> {shared_data}")

t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)
t1.start(); t2.start()
t1.join(); t2.join()

print("Final (unsynchronized):", shared_data)
