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


def Gauss_Jacobi(A,B,x0,tol = 10**-3 , N=100):
    n = len(B)
    X = x0.copy()
    X_new = np.zeros(n)
    i = 0
    while (N):
        for i in range(n):
            X_new[i] = (B[i] - sum([A[i][j]*X[j] for j in range(n) if j != i]))/A[i][i]
        if max([abs(X_new[i] - X[i]) for i in range(n)]) / max([abs(X_new[i]) for i in range(n)]) < tol:
            return X_new
        X = X_new.copy()
        print(X)
        print("-------------------")
        N -= 1
    print("Method failed after N iterations")
    return X_new


def Gauss_Seidel(A,B,x0,tol = 10**-3 , N=100):
    n = len(B)
    X = x0.copy()
    X_new = np.zeros(n)
    i = 0
    while (N):
        for i in range(n):
            X_new[i] = B[i]
            for j in range(i):
                    X_new[i] -= A[i][j]*X_new[j]
            for j in range(i+1,n):
                    X_new[i] -= A[i][j]*X[j]
            X_new[i] /= A[i][i]
        if max([abs(X_new[i] - X[i]) for i in range(n)]) / max([abs(X_new[i]) for i in range(n)]) < tol:
            return X_new
        X = X_new.copy()
        print(X)
        print("-------------------")
        N -= 1
    print("Method failed after N iterations")
    return X_new



def linear_difference_J(p_x,q_x,r_x,a,b,y_a,y_b,n , N = 100):
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
    
    y = Gauss_Jacobi(A,b,[0 for i in range(n)],10**-6,N)

    y_ret = [y_a] + list(y) + [y_b]
    return x, np.array(y_ret)

def linear_difference_S(p_x,q_x,r_x,a,b,y_a,y_b,n , N = 100):
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
    
    y = Gauss_Seidel(A,b,[0 for i in range(n)],10**-6,N)

    y_ret = [y_a] + list(y) + [y_b]
    return x, np.array(y_ret)

a = 1
b = 2
alpha = 1
beta = 2
n = 9
N = 100

T , Yj = linear_difference_J(p_x,q_x,r_x,a,b,alpha,beta,n,N)
T , Ys = linear_difference_S(p_x,q_x,r_x,a,b,alpha,beta,n,N)

plt.plot(T, Yj, label = "Approximation Jacobi")
plt.plot(T, Ys, label = "Approximation Seidel")
plt.plot(T, exact(T), label = "Exact")
plt.legend()
plt.show()

plt.plot(T, Yj - exact(T) , label = "Error Jacobi")
plt.plot(T, Ys - exact(T) , label = "Error Seidel")
plt.show()