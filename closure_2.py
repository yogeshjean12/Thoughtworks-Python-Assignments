def f(x):
    def g(y):
        return y
    return g

a = 5
b = 1
h = f(b)
print(h(b))