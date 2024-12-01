"""Redo Problem 1 using the Trapezoidal Method."""

import numpy as np
import math

def f1_dev(x,y):
    return y/x - (y/x)**2

def f2_dev(x,y):
    return (y**2 + y)/x

def f3_dev(x,y):
    return -x*y + 4*x/y

def f1_actual(x):
    return x/(1+math.log(x))

def f2_actual(x):
    return 2*x/(1- 2* x)

def f3_actual(x):
    return (4-2*(math.e)**(-x**2))**(1/2)

def fixed_point(p0, tol,func, max_iter=100):
    
        i = 0
        p = p0
        for i in range(max_iter):
            p = func(p)
            # print("Iteration", i, ":", p)
            if abs(p - p0) < tol:
                return p
            p0 = p
    
        print("Max iterations reached.")
        return p

def trapezoidal(x0,y0,h,n,func):
    """
    wi+1 = wi + h/2(f(xi,wi) + f(xi+1,wi+1))
    fixed point iteration is required to solve for wi+1
    """

    x = x0
    y = y0
    for i in range(n):
        ti = x + h
        g = lambda w: y + h/2*(func(x,y) + func(ti,w))
        y = fixed_point(y,10**(-5),g)
        x = ti
        print("x: ", x, "y: ", y)
        print("local error: ", abs(y - f1_actual(x)))
    return y

def main():
    print("Problem 1")
    print("f1")
    trapezoidal(1,1,0.1,2,f1_dev)

    print("f2")
    trapezoidal(1,-2,0.5,4,f2_dev)

    print("f3")
    trapezoidal(0,1,0.25,4,f3_dev)

if __name__ == "__main__":
    main()