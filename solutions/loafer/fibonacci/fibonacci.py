def fib(n):
    return int(((1+(5**.5))**n-(1-(5**.5))**n)/(2**n*(5**.5))*1)

# this is just a short and optimized form of the function below

'''
def fib(n):
    square_root_5 = 5 ** .5
    Phi = (square_root_5 + 1) / 2
    phi = Phi - 1
    fib_n = \
        ( (Phi ** n) - (-phi ** n) ) /\
        ( (Phi     ) - (-phi     ) )
    fib_n = int( fib_n * 1 )
    return fib_n
'''
