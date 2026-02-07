import threading
import time

def function(i):
    print(f"start Thread {i}")
    time.sleep(2)
    print(f"end Thread {i}")

t1 = threading.Thread(target=function, args=(1,))
t2 = threading.Thread(target=function, args=(2,))
t3 = threading.Thread(target=function, args=(3,))
t4 = threading.Thread(target=function, args=(4,))
t5 = threading.Thread(target=function, args=(5,))

# First phase
t1.start(); t2.start()
t1.join(); t2.join()
print("First set of threads done")
print("The program can execute other code here")

# Second phase
t3.start(); t4.start(); t5.start()
t3.join(); t4.join(); t5.join()
print("Second set of threads done")
print("END Program")
