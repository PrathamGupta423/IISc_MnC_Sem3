""" Use Rectangular Rule and midpoint rule to approximate the integral of a function"""

import math
def f(x):
    return math.sqrt(1 + x**2)

def RectangularRule(a, b, f: callable):
     return (b-a)*f(a)

def MidpointRule(a, b, f: callable):
    return (b-a)*f((a+b)/2)

def main():
    a = 1
    b = 5
    print("Rectangular Rule: ", RectangularRule(a, b, f))
    print("Midpoint Rule: ", MidpointRule(a, b, f))

if __name__ == "__main__":
    main()