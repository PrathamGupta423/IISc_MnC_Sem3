""" Apply the non-linear shooting method with Newton’s method to the boundary value
problem """

import numpy as np
import matplotlib.pyplot as plt
import math

def High_ODE_RK4_full(F, U0, a , b , n):
    len1 = len(U0)
    soln = []
    soln.append(U0)
    T = np.zeros(n+1)
    T[0] = a
    h = (b-a)/n
    for i in range(1, n+1):
        U = np.zeros(len1)
        k1 = np.zeros(len1)
        k2 = np.zeros(len1)
        k3 = np.zeros(len1)
        k4 = np.zeros(len1)

        T[i] = T[i-1] + h
        for j in range(len1):
            k1[j] = h * F[j](T[i-1], soln[-1])
        
        temp = soln[-1] + k1/2
        for j in range(len1):
            k2[j] = h * F[j](T[i-1] + h/2, temp)
        
        temp = soln[-1] + k2/2
        for j in range(len1):
            k3[j] = h * F[j](T[i-1] + h/2, temp)
        
        temp = soln[-1] + k3
        for j in range(len1):
            k4[j] = h * F[j](T[i], temp)
        
        for j in range(len1):
            U[j] = soln[-1][j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6
        
        soln.append(U)

    # array_of_y = []
    # for i in range(len(soln)):
    #     array_of_y.append(soln[i][0])
    # array_of_y = np.array(array_of_y)

    # print(len(T), len(array_of_y))
    # print(T)
    # print(array_of_y)
    
    return T, soln

def euler_for_non_linear_shooting(T,Soln, Z , a , b , n):
    len1 = len(Soln[0])
    h = (b-a)/n
    T1 = np.zeros(n+1)
    T1[0] = a
    Z_soln = []
    Z_soln.append((0,1))
    for i in range(1, n+1):
        T1[i] = T[i]
        z = (Z_soln[i-1][0] + h * Z_soln[i-1][1] , Z_soln[i-1][1] + h * Z(T1[i-1],Soln[i-1],Z_soln[i-1]) )
        Z_soln.append(z)

    # print(len(T1), len(Z_soln))
    # print(T1)

    return T1, Z_soln


def non_linear_shooting_newton(F, Zf, a, b, y1, y2 , N , M = 1000):
    f1 = lambda x,U: U[1]
    f2 = lambda x,U: F(x,U)

    t = []
    t0 = (y2-y1)/(b-a)
    t.append(t0)

    while(M > 0):

        T , Y = High_ODE_RK4_full([f1,f2], [y1,t[-1]], a, b, N)
        # print(T)
        # print(Y)
        # print(len(T), len(Y))
        Tz , Z = euler_for_non_linear_shooting(T , Y , Zf , a, b , N)
        # print(len(Tz), len(Z))
        print("-----------------")
        # print(Tz)
        # print(Z)

        if abs(Y[-1][0] - y2) < 10**-5:
            return T,Y

        t_temp = t[-1] - (Y[-1][0] - y2)/Z[-1][0]
        t.append(t_temp)
        print(t[-1])
        M = M - 1

    print ("Method failed after M iterations")

    return T,Y



def F(x,U):
    return 1/8 * (32 + 2*x**3 - U[0]*U[1] )

def Z(x,U,Z):
    return Z[0]*(-1/8 * U[1])  + Z[1]*(-1/8 * U[0])

def exact(x):
    return x**2 + 16/x

def main():
    
    a = 1
    b = 3
    y_1 = 17
    y_2 = 43/3
    N = 20
    M = 10

    T , Y = non_linear_shooting_newton(F, Z, a, b, y_1, y_2 , N , M)

    y_arr = []
    for i in range(len(T)):
        y_arr.append(Y[i][0])

    plt.plot(T,y_arr)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Solution of the BVP")
    plt.show()

    plt.plot(T,y_arr, label = "Approximation")
    plt.plot(T,exact(T), label = "Exact")
    plt.legend()
    plt.show()

    diff = np.abs(y_arr - exact(T))
    
    plt.plot(T,diff, label = "Error")
    plt.legend()
    plt.show()




if __name__ == "__main__":
    main()

    



