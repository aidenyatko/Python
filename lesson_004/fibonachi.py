def fib(x1=1, x2=1):
    if x2 == 1:
        print(x1)
        print(x2)
    x3 = x1 + x2
    print(x3)
    if x3 > 1000:
        return
    x1 = x2
    x2 = x3
    fib(x1, x2)


fib()
