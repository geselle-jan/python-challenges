def fib(n):
    fibList = [0,1]
    while len(fibList) < n + 2:
        fibList.append(fibList[-2] + fibList[-1])
    return fibList[-2]







