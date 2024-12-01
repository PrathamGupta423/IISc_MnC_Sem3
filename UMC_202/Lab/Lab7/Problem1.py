""" Use two step Adam-Bashforth explicit method to approximate the solutions
of the following initial value problems. Compute the value of the solution
at the end point of the interval and find the error """

import numpy as np
import matplotlib.pyplot as plt
import math

def f(t, y):
    return y - t**2 + 1

def exact(t):
    return (t + 1)**2 - 0.5 * math.exp(t)

def AdamBashforth2(t0, y0, h, N):
    t = np.zeros(N+1)
    y = np.zeros(N+1)
    t[0] = t0
    y[0] = y0
    t[1] = t0 + h
    y[1] = y0 + h * f(t0, y0)
    for i in range(1, N):
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h * (3/2 * f(t[i], y[i]) - 1/2 * f(t[i-1], y[i-1]))
    return t, y

def main():
    t0 = 0
    y0 = 0.5
    h = 0.01
    N = 1000
    t, y = AdamBashforth2(t0, y0, h, N)
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

    plt.plot(t, y, 'o-', label='Adam-Bashforth2')
    plt.plot(t, exa, label='Exact')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
    