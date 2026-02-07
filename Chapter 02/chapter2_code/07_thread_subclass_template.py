from threading import Thread

class MyThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # custom initialization here

    def run(self):
        # thread logic here
        pass

t = MyThread()
t.start()
t.join()
