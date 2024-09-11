"""se the Composite Trapezoidal rule and Composite Simpson's rule with
the indicated values of n to approximate the following integrals"""

import math

def f1(x):
    return (x**3)*(math.e**x)

def f2(x):
    return math.tan(x)

def SimpsonsRule(a, b, f: callable):
    return ((b-a)/6)*(f(a) + 4*f((a+b)/2) + f(b))

def CompositeTrapezoidalRule(a, b, n, f: callable):
    h = (b-a)/n
    I = 0
    for i in range(1, n):
        I += f(a + i*h)
    I += (f(a) + f(b))/2
    return h*I

def CompositeSimpsonsRule(a, b, n, f: callable):
    # h = (b-a)/(n)
        # I = 0
    # I += f(a) + f(b)
    # for i in range(1, n):
    #     I += 2*f(a + i*h)
    # for i in range(1, n+1):
    #     u = ((a + (i-1)*h) + (a + i*h))/2
    #     I += 4*f(u)
    # return (h/6)*I
    # I = 0
    # for i in range(1, n+1):
    #     I += SimpsonsRule(a + (i-1)*h, a + i*h, f) 
    # return I

    # xi = []


    h = (b-a)/n
    I = f(a) + f(b)
    for i in range(2, n,2):
        I += 2*f(a + i*h)
    for i in range(1, n ,2):
        u = a + i*h
        I += 4*f(u)
    return (h/3)*I





def main():
    # Problem a
    a = -2
    b = 2
    n = 4

    print("Composite Trapezoidal Rule: ", CompositeTrapezoidalRule(a, b, n, f1))
    print("Composite Simpson's Rule: ", CompositeSimpsonsRule(a, b, n, f1))

    # Problem b
    a = 0
    b = 3*math.pi/8
    n = 8

    print("Composite Trapezoidal Rule: ", CompositeTrapezoidalRule(a, b, n, f2))
    print("Composite Simpson's Rule: ", CompositeSimpsonsRule(a, b, n, f2))

if __name__ == "__main__":
    main()