""" Redo problem 1 by the three step Adams Bashforth explicit method and
three step Adams Moulton implicit method. Compare the results. """

import numpy as np
import matplotlib.pyplot as plt
import math

def f(t, y):
    return y - t**2 + 1

def exact(t):
    return (t + 1)**2 - 0.5 * math.exp(t)

def fixed_point(p0, tol,func, max_iter=100):
    
        i = 0
        p = p0
        for i in range(max_iter):
            p = func(p)
            # print("Iteration", i, ":", p)
            if abs(p - p0) < tol:
                return p
            p0 = p
    
        print("Max iterations reached.")
        return p


def AdamBashforth3(t0, y0, h, N,f):
    t = np.zeros(N+1)
    y = np.zeros(N+1)
    t[0] = t0
    y[0] = y0
    t[1] = t0 + h
    y[1] = y0 + h * f(t0, y0)
    t[2] = t[1] + h
    y[2] = y[1] + h * f(t[1], y[1])
    for i in range(2, N):
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h * (23/12 * f(t[i], y[i]) - 4/3 * f(t[i-1], y[i-1]) + 5/12 * f(t[i-2], y[i-2]))
    return t, y

def Adams_Moulton_3(t0, y0, h, N,f):
    t = np.zeros(N+1)
    y = np.zeros(N+1)
    t[0] = t0
    y[0] = y0
    t[1] = t0 + h
    y[1] = y0 + h * f(t0, y0)
    t[2] = t[1] + h
    y[2] = y[1] + h * f(t[1], y[1])
    for i in range(2, N):
        t[i+1] = t[i] + h
        g = lambda w: y[i] + h/24 * (9*f(t[i+1], w) + 19*f(t[i], y[i])-5*f(t[i-1], y[i-1])+f(t[i-2], y[i-2]))
        y[i+1] = fixed_point(y[i], 10**-5, g)
    return t, y

def main():
    t0 = 0
    y0 = 0.5
    h = 0.1
    N = 20
    t, y = AdamBashforth3(t0, y0, h, N,f)
    print("t: ", t)
    print("y: ", y)
    print("Exact: ", exact(t[N]))
    print("Error: ", abs(y[N] - exact(t[N])))

    e = np.zeros(N+1)
    for i in range(N+1):
        e[i] = abs(y[i] - exact(t[i]))

    exa = np.zeros(N+1)
    for i in range(N+1):
        exa[i] = exact(t[i])

    plt.plot(t, y, 'o-', label='Adam-Bashforth3')
    plt.plot(t, exa, label='Exact')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    
    t1, y1 = Adams_Moulton_3(t0, y0, h, N,f)
    print("t1: ", t1)
    print("y1: ", y1)
    print("Exact: ", exact(t1[N]))
    print("Error: ", abs(y1[N] - exact(t1[N])))

    e = np.zeros(N+1)
    for i in range(N+1):
        e[i] = abs(y[i] - exact(t[i]))

    exa = np.zeros(N+1)
    for i in range(N+1):
        exa[i] = exact(t[i])

    plt.plot(t1, y1, 'o-', label='Adams-Moulton3')
    plt.plot(t1, exa, label='Exact')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    diff = np.zeros(N+1)
    for i in range(N+1):
        diff[i] = abs(y[i] - y1[i])


    plt.plot(t, y, 'o-', label='Adam-Bashforth3')
    plt.plot(t1, y1, 'o-', label='Adams-Moulton3')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show() 

    plt.plot(t, diff, 'o-', label='Difference')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()  