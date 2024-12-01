"""Use the linear finite difference algorithm with N = 9 to approximate the so-
lution to problem 1 and compare the results obtained in the linear shooting
method.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

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

# def linear_finite_diffrence(p_x, q_x, r_x, a, b, alpha, beta, N):
#     h = (b - a) / N + 1
#     x = np.linspace(a, b, N+2)
#     print(x)
#     A = np.zeros((N, N))
#     B = np.zeros(N)

#     # A[0][0] = 2 + h**2 * q_x(x[1])
#     # A[0][1] = -1 + h/2 * p_x(x[1])
#     # for i in range(1, N-1):
#     #     print(i)
#     #     A[i][i-1] = -1 - h/2 * p_x(x[i+1])
#     #     A[i][i] = 2 + h**2 * q_x(x[i+1])
#     #     A[i][i+1] = -1 + h/2 * p_x(x[i+1])
#     # A[N-1][N-2] = -1 - h/2 * p_x(x[N])
#     # A[N-1][N-1] = 2 + h**2 * q_x(x[N])

#     for i in range(N):
#         A[i][i] = -(2 + h**2 * q_x(x[i+1]))
#         if i != 0:
#             A[i][i-1] = 1 + h/2 * p_x(x[i+1])
#         if i != N-1:
#             A[i][i+1] = 1 - h/2 * p_x(x[i+1])



#     B[0] = h**2 * r_x(x[1]) - (1 + h/2 * p_x(x[1])) * alpha
#     for i in range(1, N-1):
#         B[i] = h**2 * r_x(x[i+1])
#     B[N-1] = h**2 * r_x(x[N]) - (1 - h/2 * p_x(x[N+1])) * beta

#     Y = np.linalg.solve(A, B)
#     print(Y)

#     ret_y = [alpha] + list(Y) + [beta]
    
#     return x, np.array(ret_y)\

def f(x):
    return (-2/x, 2/x**2, math.sin(math.log(x))/x**2)

def linear_difference(p_x,q_x,r_x,a,b,y_a,y_b,n):
    h = (b-a)/(n+1)
    x = np.linspace(a,b,n+2)

    A = np.zeros((n,n))
    b = np.zeros(n)

    b[0] += -h**2*r_x(x[1]) + (1+h*(p_x(x[1]))/2)*y_a
    b[n-1] += -h**2*r_x(x[n]) + (1-h*(p_x(x[n]))/2)*y_b
    for i in range(1,n-1):
        b[i] += -h**2*r_x(x[i+1])
    
    for i in range(n):
        A[i,i] += (2 + (h**2)*(q_x(x[i+1])))
        if i < n-1:
            A[i,i+1] += -1 + h*(p_x(x[i+1]))/2
            A[i+1,i] += -1 - h*(p_x(x[i+2]))/2
    
    y = np.linalg.solve(A,b)

    y_ret = [y_a] + list(y) + [y_b]
    return x, np.array(y_ret)




a = 1
b = 2
alpha = 1
beta = 2
n = 9

T , Y = linear_difference(p_x,q_x,r_x,a,b,alpha,beta,n)

plt.plot(T, Y, label = "Approximation")
plt.plot(T, exact(T), label = "Exact")
plt.legend()
plt.show()

plt.plot(T, Y - exact(T))
plt.show()
