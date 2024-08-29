'''To find Value of functions at given points by using 
polynomial interpolation via Newton's Backward Difference Formula'''


import numpy as np

def backward_diff(X0:float, h:float ,k:int , func:callable) -> float:
    '''Implements ∇ as backward difference operator 
    ∇^k(X0) = ∇(∇^k-1(X0))= (∇^k-1(X0) - ∇^k-1(X0-h))
    
    ∇(X0) = (f(X0) - f(X0-h))
    
    '''

    if k == 1:
        return func(X0) - func(X0-h)
    else:
        return (backward_diff(X0, h, k-1, func) - backward_diff(X0-h, h, k-1, func))
    
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
    # Problem 1
    # ---------------------------------------------------------
    print("Problem 1")

    x = -1/3
    h = 0.25
    Xn = 0
    s = (x-Xn)/h 
    print(s)
    P_Now = f1(Xn)
    for i in range(1, 4):
        print(f"Calculating for power {i}")
        print(f"∇^{i}f({Xn}) = {backward_diff(Xn, h, i, f1)}")
        print(f"binomial({s}, {i}) = {binomial(s, i)}")
        P_Now += backward_diff(Xn, h, i, f1)*binomial(-s, i)*((-1)**i)
        print(f"P_{i}({x}) = {P_Now}\n")
        print("------------------------------------------------------------")
    print(f"Final Answer: P_3({x}) = {P_Now}")
    print("============================================================")
    
    # ---------------------------------------------------------
    # Problem 2
    # ---------------------------------------------------------
    print("Problem 2")
    x = 0.25
    h = 0.1
    Xn = 0.4
    s = (x-Xn)/h
    P_Now = f2(Xn)
    print(s)
    for i in range(1, 4):
        print(f"Calculating for power {i}")
        print(f"∇^{i}f({Xn}) = {backward_diff(Xn, h, i, f2)}")
        print(f"binomial({s}, {i}) = {binomial(s, i)}")
        P_Now += backward_diff(Xn, h, i, f2)*binomial(-s, i)*((-1)**i)
        print(f"P_{i}({x}) = {P_Now}\n")
        print("------------------------------------------------------------")

    print(f"Final Answer: P_3({x}) = {P_Now}")



if __name__ == "__main__":
    main()