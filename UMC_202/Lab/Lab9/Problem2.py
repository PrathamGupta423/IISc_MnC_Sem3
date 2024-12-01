"""Use Gauss Jacobi’s
iterative technique to find the approximations x(k) to x with
x0 = (0, 0, 0, 0)T until ||x(k) − x(k−1)||∞ < 10-3"""

import numpy as np
import math
import matplotlib.pyplot as plt

def Gauss_Jacobi(A,B,x0 = [0,0,0,0],tol = 10**-3 , N=100):
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

def gauss_jacobi2(A,b,x0,N):
    n = len(A)
    x = x0
    for k in range(N):
        x = [1/A[i][i]*(b[i] - sum(A[i][j]*x[j] for j in range(n) if j != i)) for i in range(n)]
        print(x)
    return x

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

A = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
B = np.array([6,25,-11,15])

# print(Gauss_Jacobi(A,B,[0,0,0,0],10**-3,10))
# print(gauss_jacobi2(A,B,[0,0,0,0],10))
print(Gauss_Seidel(A,B,[0,0,0,0],10**-3,10))