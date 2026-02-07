from joblib import Memory
import time, os

memory = Memory(location=os.path.join(os.path.dirname(__file__), "..", "cache_dir"), verbose=0)

@memory.cache
def expensive_function(x: int) -> int:
    time.sleep(0.3)
    return x * x

def main():
    t0 = time.time()
    print("First call:", expensive_function(10))
    t1 = time.time()
    print(f"First call time: {t1 - t0:.3f}s")

    t0 = time.time()
    print("Second call:", expensive_function(10))
    t1 = time.time()
    print(f"Second call time (cached): {t1 - t0:.3f}s")

if __name__ == "__main__":
    main()
