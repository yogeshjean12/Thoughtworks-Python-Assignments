from functools import reduce
def fibonacci(count):
    fabi = [0, 1]
    for i in range(2, count):
        fabi += (reduce(lambda a, b: a + b, fabi[-2:]),)

    return fabi[:count]

print(fibonacci(10))