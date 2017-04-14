
def fib(n):
    fibList = [0,1]
    while len(fibList) < n + 2:
        fibList.append(fibList[-2] + fibList[-1])
    return fibList[-2]


# another solution with ony one line of code

'''
def fib(n):
    return int(((1 + (5 ** .5)) ** n - (1 - (5 ** .5)) ** n) / (2 ** n * (5 ** .5)))
'''


# optimized version of loafer's function

'''
def fib(n):
    return int((((5 ** .5 + 1) / 2) ** n - (1 - (5 ** .5 + 1) / 2) ** n) / (5 ** .5))
'''







