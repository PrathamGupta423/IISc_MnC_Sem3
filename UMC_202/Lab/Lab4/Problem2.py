"""Approximate the following integrals using the Trapezoidal rule and Simpson's rule."""

import math

def f1(x):
    return 2/(x-4)

def f2(x):
    return ((math.e)**(3*x))*math.sin(2*x)

def TrapezoidalRule(a, b, f: callable):
    return ((b-a)/2)*(f(a) + f(b))

def SimpsonsRule(a, b, f: callable):
    return ((b-a)/6)*(f(a) + 4*f((a+b)/2) + f(b))


def main():
    # Problem a
    b = 0.5
    a = 0

    print("Trapezoidal Rule: ", TrapezoidalRule(a, b, f1))
    print("Simpson's Rule: ", SimpsonsRule(a, b, f1))

    # Problem b
    b = math.pi/4 
    a = 0

    print("Trapezoidal Rule: ", TrapezoidalRule(a, b, f2))
    print("Simpson's Rule: ", SimpsonsRule(a, b, f2))

if __name__ == "__main__":
    main()

