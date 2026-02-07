from threading import Thread, Condition
import time, random

condition = Condition()
shared = None
count = 5

class Consumer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def run(self):
        global shared
        for _ in range(self.count):
            with condition:
                while shared is None:
                    condition.wait()
                print(f"consumer <- got {shared}")
                shared = None
                condition.notify()

class Producer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        global shared
        for _ in range(self.count):
            time.sleep(1)
            item = random.randint(0, 100)
            with condition:
                while shared is not None:
                    condition.wait()
                shared = item
                print(f"producer -> put {item}")
                condition.notify()

t1 = Producer(count)
t2 = Consumer(count)
t1.start(); t2.start()
t1.join(); t2.join()
