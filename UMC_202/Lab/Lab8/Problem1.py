""" Apply the Linear Shooting technique with N = 10 to the boundary value problem """

import numpy as np
import matplotlib.pyplot as plt
import math


# def High_ODE_RK4(F, U0, n, h, t):
#     len1 = len(U0)
#     soln = []
#     soln.append(U0)
#     T = np.zeros(n+1)
#     T[0] = t
#     for i in range(1, n+1):
#         U = np.zeros(len1)
#         k1 = np.zeros(len1)
#         k2 = np.zeros(len1)
#         k3 = np.zeros(len1)
#         k4 = np.zeros(len1)

#         T[i] = T[i-1] + h
#         for j in range(len1):
#             k1[j] = h * F[j](T[i-1], soln[-1])
        
#         temp = soln[-1] + k1/2
#         for j in range(len1):
#             k2[j] = h * F[j](T[i-1] + h/2, temp)
        
#         temp = soln[-1] + k2/2
#         for j in range(len1):
#             k3[j] = h * F[j](T[i-1] + h/2, temp)
        
#         temp = soln[-1] + k3
#         for j in range(len1):
#             k4[j] = h * F[j](T[i], temp)
        
#         for j in range(len1):
#             U[j] = soln[-1][j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6
        
#         soln.append(U)

#     array_of_y = []
#     for i in range(len(soln)):
#         array_of_y.append(soln[i][0])
#     array_of_y = np.array(array_of_y)
    
#     return T, array_of_y  

def High_ODE_RK4(F, U0, a , b , n):
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

    array_of_y = []
    for i in range(len(soln)):
        array_of_y.append(soln[i][0])
    array_of_y = np.array(array_of_y)

    print(len(T), len(array_of_y))
    print(T)
    print(array_of_y)
    
    return T, array_of_y




def linear_shooting(f_0,f_1,f_2,a,b,y_1,y_2,y_b,h):
    y1 = [y_1]
    y2 = [y_2]
    
    y = y1[0]
    x = a

    for i in range(int((b-a)/h)):
        y = y[0] + h*f_1(x,y)[0], y[1] + h*f_1(x,y)[1]
        x = x + h
        y1.append(y)

    y = y2[0]
    x = a

    for i in range(int((b-a)/h)):
        y = y[0] + h*f_2(x,y)[0], y[1] + h*f_2(x,y)[1]
        x = x + h
        y2.append(y)
    
    y = []
    for i in range(len(y1)):
        y.append(y1[i][0] + (y_b - y1[-1][0])/y2[-1][0]*y2[i][0])

    ans = []
    for i in range(len(y)):
        print((y[i], abs(y[i] - f_0(a + i*h))))
        # ans.append((y[i], abs(y[i] - f_0(a + i*h))))
        ans.append((a+i*h, (y[i] )))
    return ans
        


def f_1(x,y):
    return y[1], (-2)*y[1]/x + 2*y[0]/x**2 + math.sin(math.log(x))/x**2

def f_2(x,y):
    return y[1], (-2)*y[1]/x + 2*y[0]/x**2

def f_0(x):
    return 1.139*x - 0.039/x**2 -3*math.sin(math.log(x))/10 - math.cos(math.log(x))/10







def F1(t, U):
    return U[1]
def F2(t, U):
    return -2/t * U[1] + 2/(t**2) *U[0] + np.sin(np.log(t)) / (t**2)
def F3(t, U):
    return -2/t * U[1] + 2/(t**2) *U[0]

def exact(t):
    c1 = 1.13921
    c2 = -0.03921
    return c1 * t + c2 * t**(-2) - 3/10 * np.sin(np.log(t)) - 1/10 * np.cos(np.log(t))

def main():
    b = 2
    a = 1
    h = 0.1
    n = int((b-a)/h)
    # print(n)

    U0 = np.array([1, 0])
    T, y1 = High_ODE_RK4([F1, F2], U0 , a, b, n)

    print(len(T), len(y1))
    print(T)
    print(y1)


    U0 = np.array([0, 1])
    T, y2 = High_ODE_RK4([F1, F3], U0, a, b, n)

    print(len(T), len(y2))
    print(T)
    print(y2)

    y = np.zeros(n+1)
    for i in range(n+1):
        y[i] = y1[i] + (2-y1[n])/y2[n] * y2[i]

    print(y)

    plt.plot(T, y, label = "Approximation")
    plt.plot(T, exact(T), label = "Exact")
    plt.legend()
    plt.show()

    diff = np.abs(y - exact(T))
    print(diff)

    plt.plot(T, diff, label = "Error")
    plt.legend()
    plt.show()


    aditya = linear_shooting(f_0,f_1,f_2,1,2,(1,0),(0,1),2,0.1)
    print(aditya)
    # plt.plot(T, y, label = "Approximation") 
    plt.plot([i[0] for i in aditya], [i[1] for i in aditya], label = "Linear Shooting")
    plt.plot(T, exact(T), label = "Exact")
    plt.legend()
    plt.show()

    diff2 = np.abs([i[1] for i in aditya] - exact(T))
    print(diff2)

    plt.plot(T, diff2, label = "Error")
    plt.legend()
    plt.show()



main()
