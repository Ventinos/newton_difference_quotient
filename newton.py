import numpy as np
import math

def forward_differencing(f, a, h):
    num = f(a+h)-f(a)
    return num/h

def backward_differencing(f, a, h):
    num = f(a)-f(a-h)
    return num/h

def centered_differencing(f, a, h):
    num = f(a+h)-f(a-h)
    return num/(2*h)

def test_function(x):
    return math.exp(x)

def test():
    values1 = []
    values2 = []
    values3 = []

    errors1 = []
    errors2 = []
    errors3 = []

    algebric = 2.7182818284590452354

    for i in np.logspace(-4, -20, num=16):
        d1= forward_differencing(test_function, 1, i)
        d2= backward_differencing(test_function, 1, i)
        d3= centered_differencing(test_function, 1, i)

        values1.append(d1)
        values2.append(d2)
        values3.append(d3)

        errors1.append(abs(d1-algebric))
        errors2.append(abs(d2-algebric))
        errors3.append(abs(d3-algebric))

    print('forward:')
    for i in values1: print(i)
    print('')
    print('errors forward:')
    for i in errors1: print(i)
    print('')

    print('backward:')
    for i in values2: print(i)
    print('')
    print('errors backward:')
    for i in errors2: print(i)
    print('')

    print('centerd:')
    for i in values3: print(i)
    print('')
    print('errors centered:')
    for i in errors3: print(i)
    print('')
