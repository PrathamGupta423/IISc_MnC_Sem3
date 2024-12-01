'''Transform the second order initial value problem into a system of first order initial value problems, 
and use the Runge Kutta method with h = 0.1 to approximate the solution 

y2 -2y1 +2y = e^(2t)*sin(t)    y1(0) = -0.6, y2(0) = -0.4'''

import numpy as np
import matplotlib.pyplot as plt
import math


def f1(t, U):
    return U[1]

def f2(t, U):
    return 2*U[1] - 2*U[0] + math.exp(2*t)*math.sin(t)

def rk2(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += (k1 + k2) / 2
        x += h
    return y

def HighOrderODE_RK2( F : list[callable] , U0 , n : int , h : float , t : float):

    len1 = len(U0)
    soln = []
    soln.append(U0)
    T = np.zeros(n+1)
    T[0] = t
    for i in range(1, n+1):
        U = np.zeros(len1)
        k1 = np.zeros(len1)
        k2 = np.zeros(len1)

        T[i] = T[i-1] + h
        for j in range(len1):
            k1[j] = h * F[j](T[i-1], soln[-1])
        
        temp = soln[-1] + k1
        for j in range(len1):
            k2[j] = h * F[j](T[i], temp)

        for j in range(len1):
            U[j] = soln[-1][j] + (k1[j] + k2[j]) / 2

        soln.append(U)

    print(T)
    print(soln)

    print ("dfhusdfui")
    print(len(soln))
    print(len(T))
    return T, soln

def HigherOrderODE_RK4(F, U0, n, h, t):
    len1 = len(U0)
    soln = []
    soln.append(U0)
    T = np.zeros(n+1)
    T[0] = t
    for i in range(1, n+1):
        U = np.zeros(len1)
        k1 = np.zeros(len1)
        k2 = np.zeros(len1)
        k3 = np.zeros(len1)
        k4 = np.zeros(len1)

        T[i] = T[i-1] + h
        for j in range(len1):
            k1[j] = h * F[j](T[i-1], soln[-1])
        
        temp = soln[-1] + k1 / 2
        for j in range(len1):
            k2[j] = h * F[j](T[i-1] + h/2, temp)
        
        temp = soln[-1] + k2 / 2
        for j in range(len1):
            k3[j] = h * F[j](T[i-1] + h/2, temp)
        
        temp = soln[-1] + k3
        for j in range(len1):
            k4[j] = h * F[j](T[i], temp)
        
        for j in range(len1):
            U[j] = soln[-1][j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6

        soln.append(U)

    return T, soln



def main():
    
    # u1(t) = y(t)
    # u2(t) = y'(t)
    # u1'(t) = u2(t)
    # u2'(t) = 2u2(t) - 2u1(t) + e^(2t)sin(t)

    U0 = np.array([-0.6, -0.4])
    F = [f1, f2]
    n = 10
    h = 0.1
    t0 = 0

    t, data = HighOrderODE_RK2(F, U0, n, h, t0)
    print(data)

    y = np.zeros(n+1)
    for i in range(n+1):
        y[i] = data[i][0]
    print(y)

    plt.plot(t, y, 'o-', label='Runge-Kutta2')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    t1, data1 = HigherOrderODE_RK4(F, U0, n, h, t0)

    y1 = np.zeros(n+1)
    for i in range(n+1):
        y1[i] = data1[i][0]
    print(y1)

    plt.plot(t1, y1, 'o-', label='Runge-Kutta4')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    plt.plot(t, y, 'o-', label='Runge-Kutta2')
    plt.plot(t1, y1, 'o-', label='Runge-Kutta4')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()






if __name__ == "__main__":
    main()



