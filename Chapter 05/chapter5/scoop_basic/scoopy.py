from scoop import futures

def worker(value):
    print("I am the Worker %s" % value)

if __name__ == "__main__":
    # Synchronize with list() so the program waits for completion
    list(futures.map(worker, range(4)))
