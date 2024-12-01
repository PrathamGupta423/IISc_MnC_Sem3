"""Use Taylor’s series method of order 2 to approximate the solution for each
of the following initial value problems and compare the results to the actual
values
"""

import numpy as np
import math 

def f1_dev(x,y):
    return y/x - (y/x)**2

def f1_dev2(x,y):
    return (-y/x**2 + 2*y/x**3) + (1/x -2*y/x**2)*f1_dev(x,y)

def f2_dev(x,y):
    return (y**2 + y)/x

def f2_dev2(x,y):
    return -(y**2 + y)/x**2 + f2_dev(x,y)*(2*y + 1)/x

def f3_dev(x,y):
    return -x*y + 4*x/y

def f3_dev2(x,y):
    return -y - x*f3_dev(x,y) + 4/y - (4*x/(y**2))*f3_dev(x,y)

def f1_actual(x):
    return x/(1+math.log(x))

def f2_actual(x):
    return 2*x/(1- 2* x)

def f3_actual(x):
    return (4-2*(math.e)**(-x**2))**(1/2)


def taylor_2(x0,y0,h,n,func,func2):
    x = x0
    y = y0
    for i in range(n):
        y = y + h*func(x,y) + (h**2/2)*func2(x,y)
        x = x + h
        print("x: ", x, "y: ", y)
        print("local error: ", abs(y - f1_actual(x)))    
    return y


def main():
    print("Problem 1")
    print("f1")
    taylor_2(1,1,0.1,2,f1_dev,f1_dev2)

    print("f2")
    taylor_2(1,-2,0.5,4,f2_dev,f2_dev2)

    print("f3")
    taylor_2(0,1,0.25,4,f3_dev,f3_dev2)



if __name__ == "__main__":
    main()
