from joblib import Parallel, delayed

def process_number(n: int) -> int:
    # Return square of n
    return n * n

def main():
    results = Parallel(n_jobs=4)(delayed(process_number)(i) for i in range(10))
    print("Squares:", results)

if __name__ == "__main__":
    main()
