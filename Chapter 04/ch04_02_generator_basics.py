def generator():
    yield "A"
    yield "B"
    yield "C"

if __name__ == "__main__":
    iterator = generator()
    print("First call:", next(iterator))
    print("Second call:", next(iterator))
    print("Third call:", next(iterator))
