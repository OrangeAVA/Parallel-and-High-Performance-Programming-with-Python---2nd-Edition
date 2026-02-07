from threading import Thread
from queue import Queue
import time, random

queue = Queue()
count = 5

class Consumer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count
  
    def run(self):
        for _ in range(self.count):
            local = queue.get()
            print("consumer has used this:", local)
            queue.task_done()

class Producer(Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def request(self):
        time.sleep(1)
        return random.randint(0, 100)
 
    def run(self):
        for _ in range(self.count):
            local = self.request()
            queue.put(local)
            print("producer has loaded this:", local)

t1 = Producer(count); t2 = Producer(count)
t3 = Consumer(count); t4 = Consumer(count)
for t in (t1, t2, t3, t4): t.start()
for t in (t1, t2, t3, t4): t.join()
