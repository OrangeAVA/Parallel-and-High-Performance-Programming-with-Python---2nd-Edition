import threading
import time

def function(i):
    print(f"start Thread {i}")
    time.sleep(2)
    print(f"end Thread {i}")

n_threads = 5
threads = []

for i in range(n_threads):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
