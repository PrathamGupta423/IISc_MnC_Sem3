"""Redo problem 1 by the two step Adams Moulton implicit method. Com-
pare the results with Adam-Bashforth explicit method. """

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

def Adams_Moulton_2(t0, y0, h, N,f):
    t = np.zeros(N+1)
    y = np.zeros(N+1)
    t[0] = t0
    y[0] = y0
    t[1] = t0 + h
    y[1] = y0 + h * f(t0, y0)
    for i in range(1, N):
        t[i+1] = t[i] + h
        g = lambda w: y[i] + h/12 * (5*f(t[i+1], w) + 8*f(t[i], y[i])-f(t[i-1], y[i-1]))
        y[i+1] = fixed_point(y[i], 10**-5, g)
    return t, y

def main():
    t0 = 0
    y0 = 0.5
    h = 0.25
    N = 10
    t, y = Adams_Moulton_2(t0, y0, h, N,f)
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

    plt.plot(t, y, 'o-', label='Adams-Moulton2')
    plt.plot(t, exa, label='Exact')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()