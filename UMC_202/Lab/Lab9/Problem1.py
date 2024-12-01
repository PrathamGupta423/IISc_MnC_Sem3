"""Use Gaussian elimination with backward substitution with tol-
erance 10−2 to solve the following linear system"""

import numpy as np
import math
import matplotlib.pyplot as plt

def Gaussian_Elimination(A,B):
    n = len(B)

    for i in range(n):
        p = i
        while A[p][i] == 0:
            p += 1
            if p == n:
                return "No unique solution exists"
        if p != i:
            A[i], A[p] = A[p], A[i]
            B[i], B[p] = B[p], B[i]

        for j in range(i+1,n):
            m = A[j][i]/A[i][i]
            A[j] = [A[j][k] - m*A[i][k] for k in range(n)]
            B[j] = B[j] - m*B[i]
            print(A)
            print(B)

    if(A[n-1][n-1] == 0):
        return "No unique solution exists2"
    
    print("-------------------")
    X = [0 for i in range(n)]
    X[n-1] = B[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        X[i] = (B[i] - sum([A[i][j]*X[j] for j in range(i+1,n)]))/A[i][i]

    return X


A = [[4,-1,1],[2,5,2],[1,2,4]]
B = [8,3,11]

print(Gaussian_Elimination(A,B))

A = [[1,1,1],[1,2,3],[1,3,6]]
B = [6,14,24]

print(Gaussian_Elimination(A,B))

A = [[1,1,1],[1,1,3],[1,1,5]]
B = [6,6,24]

print(Gaussian_Elimination(A,B))


