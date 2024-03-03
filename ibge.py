import matplotlib.pyplot as plt
import numpy as np
from newton import *

# Defining Global Scope Lists:
DATA = np.genfromtxt('censo_2022.csv', delimiter= ';', skip_header=1, dtype=int);
X = []
Y = []

for row in DATA:
    X.append(row[0])
    Y.append(row[1])
X.append(2033)
Y.append(Y[-1])
# Interpolation function:
def lagrange_interpolation(x, y, x_interpolate):
    n = len(y)
    result = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interpolate - x[j]) / (x[i] - x[j])
        result += term
    return result

# f(x) used in newton:
def f(target):
    return lagrange_interpolation(X,Y,target)

def p_forward(x,i):
    d = forward_differencing(f, i, 10e-8)
    return lagrange_interpolation(X,Y,i)+(x-i)*d

def p_backward(x,i):
    d = backward_differencing(f, i, 10e-8)
    return lagrange_interpolation(X,Y,i)+(x-i)*d

def p_centered(x,i):
    d = centered_differencing(f, i, 10e-8)
    return lagrange_interpolation(X,Y,i)+(x-i)*d

def p_4points(x,i):
    d = points_method(f, i, 10e-8)
    print(d)
    return lagrange_interpolation(X,Y,i)+(x-i)*d

def main():
    estimate_forward = []
    estimate_backward = []
    estimate_centered = []
    estimate_4points = []
    for i in X:
        for x in X:
            if x>i:
                estimate_forward.append((x ,i, p_forward(x,i)))
                estimate_backward.append((x ,i, p_backward(x,i)))
                estimate_centered.append((x ,i, p_centered(x,i)))
                estimate_4points.append((x,i,p_4points(x,i)))

    # Printing the results:
    print('Estimate_forward:')
    for item in estimate_forward:
        print('x = '+str(item[0])+', i = '+str(item[1])+', p(x)='+str(item[2]))
    print('')

    print('Estimate_backward:')
    for item in estimate_backward:
        print('x = '+str(item[0])+', i = '+str(item[1])+', p(x)='+str(item[2]))
    print('')

    print('Estimate_centered:')
    for item in estimate_centered:
       print('x = '+str(item[0])+', i = '+str(item[1])+', p(x)='+str(item[2]))
    print('')

    print('4_Points:')
    for item in estimate_4points:
       print('x = '+str(item[0])+', i = '+str(item[1])+', p(x)='+str(item[2]))
    print('')

    # Preparing to plot:
    y_estimate1991 = [Y[0]]
    y_estimate2000 = [Y[0],Y[1]]
    y_estimate2010 = [Y[0],Y[1],Y[2]]
    for i in range(0,4):
        y_estimate1991.append(estimate_centered[i][2])
    for i in range(4,7):
        y_estimate2000.append(estimate_centered[i][2])
    for i in range(7,9):
        y_estimate2010.append(estimate_centered[i][2])
    # Plotting:
    # 2 functions in one plot, comparisson:
    plt.plot(X, Y, marker='o', linestyle='-', color='b',label='Realidade')
    plt.plot(X, y_estimate1991, marker='o', linestyle='-', color='r', label='Estimado 1991')
    plt.plot(X, y_estimate2000, marker='o', linestyle='-', color='g', label='Estimado 2000')
    plt.plot(X, y_estimate2010, marker='o', linestyle='-', color='black', label='Estimado 2010')
    plt.legend(loc='best')
    # Combine all the operations and display
    plt.show()
if __name__ == '__main__':
    main()
