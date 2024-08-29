'''To find Value of functions at given points by using 
polynomial interpolation via Newton's Forward Difference Formula'''

import numpy as np
# import matplotlib.pyplot as plt

def forward_diff(X0:float, h:float ,k:int , func:callable) -> float:
    '''Implements Δ as forward difference operator 
    Δ^k(X0) = Δ(Δ^k-1(X0))= (Δ^k-1(X0+h) - Δ^k-1(X0))
    
    Δ(X0) = (f(X0+h) - f(X0))
    
    '''

    if k == 1:
        return func(X0+h) - func(X0)
    else:
        return (forward_diff(X0+h, h, k-1, func) - forward_diff(X0, h, k-1, func))
    
def binomial(s:int, k:int) -> int:
    '''Calculates the binomial coefficient (n choose k)'''
    ans = 1
    for i in range(1, k+1):
        ans *= (s-i+1)/i
    return ans

def f1(x:float) -> float:
    if(x == 0):
        return 1.101000
    if(x == -0.25):
        return 0.3349375
    if(x == -0.5):
        return -0.02475
    if(x == -0.75):
        return -0.07181250
    else:
        print("Invalid Input")
        print(x)
        return 0
    
def f2(x:float) -> float:
    eplison = 0.0000001
    if(x < 0.1+eplison and x > 0.1-eplison):
        return -0.62049958
    if(x < 0.2+eplison and x > 0.2-eplison):
        return -0.28398668
    if(x < 0.3+eplison and x > 0.3-eplison):
        return 0.00660095
    if(x < 0.4+eplison and x > 0.4-eplison):
        return 0.24842440
    else:
        print("Invalid Input")
        print(x)
        return 0
    

def main():
    # ---------------------------------------------------------
    # Testing Code
    # ---------------------------------------------------------
    # k = 1
    # h = 0.25
    # X0 = -0.75
    # print(forward_diff(X0, h, k, f1))
    # print((f1(-0.5) - f1(-0.75))/0.25)

    # k=4
    # s = 10
    # print(binomial(s, k))

    # ---------------------------------------------------------

    # Problem 1
    print("Problem 1")
    x = -1/3
    h = 0.25
    X0 = -0.75
    s = (x-X0)/h 
    P_Now = f1(X0)
    for i in range(1,4):
        print(f"Calculating for power {i}")
        print(f"Δ^{i}f({X0}) = {forward_diff(X0, h, i, f1)}")
        print(f"binomial({s}, {i}) = {binomial(s, i)}")
        P_Now += forward_diff(X0, h, i, f1)*binomial(s, i)
        print(f"P_{i}({x}) = {P_Now}\n")
        print("------------------------------------------------------------")
    print (f"Final Answer: P_3({x}) = {P_Now}")
    print("============================================================")

    # Problem 2
    print("Problem 2")
    x = 0.25
    h = 0.1
    X0 = 0.1
    s = (x-X0)/h
    P_Now = f2(X0)
    for i in range(1,4):
        print(f"Calculating for power {i}")
        print(f"Δ^{i}f({X0}) = {forward_diff(X0, h, i, f2)}")
        print(f"binomial({s}, {i}) = {binomial(s, i)}")
        P_Now += forward_diff(X0, h, i, f2)*binomial(s, i)
        print(f"P_{i}({x}) = {P_Now}\n")
        print("------------------------------------------------------------")

    print (f"Final Answer: P_3({x}) = {P_Now}")
    print("============================================================")   

if __name__ == "__main__":
    main()

