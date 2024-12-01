import numpy as np
import matplotlib.pyplot as plt
import math


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


def High_ODE_Euler(F, U0 ,x0 , n , h):
    T = []
    U = U0
    soln = []
    T.append(x0)
    soln.append(U)
    for i in range(1, n+1):
        U_temp = np.zeros(len(U0))
        for j in range(len(U0)):
            U_temp[j] = U[j] + h * F[j](T[-1], U)
        U = U_temp
        soln.append(U)
        T.append(T[-1] + h)
    
    array_of_y = []
    for i in range(len(soln)):
        array_of_y.append(soln[i][0])
    array_of_y = np.array(array_of_y)

    print(len(T), len(array_of_y))
    print(T)
    print(array_of_y)
    
    return T, array_of_y

def High_ODE_Euler2(F,U0,a,b,n):
    h = (b-a)/n
    t = a
    return High_ODE_Euler(F,U0,t,n,h)


def linear_shooting( p_x , q_x , r_x, a, b, alpha, beta, n):

    f1 = lambda t,U : U[1]
    f2 = lambda t,U : p_x(t)*U[1] +q_x(t)*U[0] + r_x(t)

    F1 = [f1,f2]

    U0 = [alpha,0]

    T1, Y1 = High_ODE_Euler2(F1, U0, a, b, n)
    # T1, Y1 = High_ODE_RK4(F1, U0, a, b, n)

    f1 = lambda t,U : U[1]
    f2 = lambda t,U : p_x(t)*U[1] +q_x(t)*U[0]

    F2 = [f1,f2]

    U0 = [0,1]

    T2, Y2 = High_ODE_Euler2(F2, U0, a, b, n)
    # T2, Y2 = High_ODE_RK4(F2, U0, a, b, n)

    assert(len(T1) == len(T2))
    assert(len(Y1) == len(Y2))

    Y = np.zeros(len(Y1))

    for i in range(len(Y1)):
        Y[i] = Y1[i] + (beta - Y1[-1]) * Y2[i] / Y2[-1]

    return T1, Y


def p_x(x):
    return -2/x

def q_x(x):
    return 2/x**2   

def r_x(x):
    return np.sin(np.log(x))/x**2

def exact(t):
    c1 = 1.13921
    c2 = -0.03921
    return c1 * t + c2 * t**(-2) - 3/10 * np.sin(np.log(t)) - 1/10 * np.cos(np.log(t))


a = 1
b = 2
alpha = 1
beta = 2
n = 10

T, Y = linear_shooting(p_x, q_x, r_x, a, b, alpha, beta, n)

exact_sol = np.zeros(len(T))
for i in range(len(T)):
    exact_sol[i] = exact(T[i])

plt.plot(T, Y, label = "Approximation")
plt.plot(T, exact_sol, label = "Exact")
plt.legend()
plt.show()

# clea
