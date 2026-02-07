from scoop import futures
import math
import numpy as np
import operator

def func(value):
    result = math.sqrt(value)
    print("The value %s and the elaboration is %s" % (value, result))
    return result

if __name__ == "__main__":
    data = np.array([10,3,6,1,4,8,25,9])
    # Single reduce
    total = sum(futures.map(func, data))
    print("This is the reduction result:", total)

    # Using mapReduce
    total2 = futures.mapReduce(func, operator.add, data)
    print("This is the reduction result (mapReduce):", total2)

    # Chained mapping then reduction (mean of int(sqrt(x)))
    import numpy as np
    mean_val = np.mean(list(futures.map(int, futures.map(func, data))))
    print("Mean of int(sqrt(x)):", mean_val)
