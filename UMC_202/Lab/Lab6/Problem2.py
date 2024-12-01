"""Redo Problem 1 using the Runge Kutta method of order 2."""

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

def runge_kutta_2(x0,y0,h,n,func):
    x = x0
    y = y0
    for i in range(n):
        k1 = h*func(x,y)
        k2 = h*func(x + h, y + k1)
        y = y + (k1 + k2)/2
        x = x + h
        print("x: ", x, "y: ", y)
        print("local error: ", abs(y - f1_actual(x)))    
    return y


def main():
    print("Problem 1")
    print("f1")
    runge_kutta_2(1,1,0.1,2,f1_dev)

    print("f2")
    runge_kutta_2(1,-2,0.5,4,f2_dev)

    print("f3")
    runge_kutta_2(0,1,0.25,4,f3_dev)

if __name__ == "__main__":
    main()
