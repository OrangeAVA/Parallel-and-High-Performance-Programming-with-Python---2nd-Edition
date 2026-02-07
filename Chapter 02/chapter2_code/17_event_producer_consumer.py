from threading import Thread, Event
import time, random

event = Event()
shared = 1
count = 5

class Consumer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
  
    def run(self):
        global shared
        for _ in range(self.count):
            event.wait()
            print("consumer has used this:", shared)
            shared = 0
            event.clear()

class Producer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
 
    def run(self):
        global shared
        for _ in range(self.count):
            shared = self.request()
            print("producer has loaded this:", shared)
            event.set()

t1 = Producer(count)
t2 = Consumer(count)
t1.start(); t2.start()
t1.join(); t2.join()
