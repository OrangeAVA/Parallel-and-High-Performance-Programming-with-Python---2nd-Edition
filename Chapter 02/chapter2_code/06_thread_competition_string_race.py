import threading
import time
import random

sequence = ""
COUNT = 10

def addA():
    global sequence
    for _ in range(COUNT):
        time.sleep(random.uniform(0.1, 0.3))
        sequence = f"{sequence}A"
        print("Sequence:", sequence)

def addB():
    global sequence
    for _ in range(COUNT):
        time.sleep(random.uniform(0.1, 0.3))
        sequence = f"{sequence}B"
        print("Sequence:", sequence)

t1 = threading.Thread(target=addA)
t2 = threading.Thread(target=addB)
t1.start(); t2.start()
t1.join(); t2.join()
