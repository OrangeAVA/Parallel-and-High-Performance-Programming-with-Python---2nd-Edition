from threading import Thread
import time

sequence = ""
COUNT = 5
timeA = 1
timeB = 2

class ThreadA(Thread):
    def run(self):
        global sequence
        for _ in range(COUNT):
            time.sleep(timeA)
            sequence += "A"
            print("Sequence:", sequence)

class ThreadB(Thread):
    def run(self):
        global sequence
        for _ in range(COUNT):
            time.sleep(timeB)
            sequence += "B"
            print("Sequence:", sequence)

t1 = ThreadA()
t2 = ThreadB()
t1.start(); t2.start()
t1.join(); t2.join()
