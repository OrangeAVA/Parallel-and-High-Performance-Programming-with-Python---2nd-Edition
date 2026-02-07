import threading, time

shared_data = 0
lock = threading.Lock()

def funcA():
    global shared_data
    for i in range(10_000):
        with lock:
            shared_data += 10
            if i % 2000 == 0:
                print(f"A i={i:5d} -> {shared_data}")
        time.sleep(0)

def funcB():
    global shared_data
    for i in range(10_000):
        with lock:
            shared_data -= 10
            if i % 2000 == 0:
                print(f"B i={i:5d} -> {shared_data}")
        time.sleep(0)

t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)
t1.start(); t2.start()
t1.join(); t2.join()

print("Final (synchronized):", shared_data)
