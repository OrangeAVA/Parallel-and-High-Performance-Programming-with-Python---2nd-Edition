from multiprocessing import Process, Queue
import time, random

class Consumer(Process):
  def __init__(self, count, queue):
    Process.__init__(self)
    self.count = count
    self.queue = queue
  
  def run(self):
    for i in range(self.count):
      local = self.queue.get()
      time.sleep(2)
      print("consumer has used this: %s" %local)

class Producer(Process):
  def __init__(self, count, queue):
    Process.__init__(self)
    self.count = count
    self.queue = queue

  def request(self):
    time.sleep(1)
    return random.randint(0,100)
 
  def run(self):
    for i in range(self.count):
      local = self.request()
      self.queue.put(local)
      print("producer has loaded this: %s" %local)

if __name__ == '__main__':
  queue = Queue()
  count = 5
  p1 = Producer(count, queue)
  p2 = Consumer(count, queue)
  p1.start(); p2.start()
  p1.join(); p2.join()