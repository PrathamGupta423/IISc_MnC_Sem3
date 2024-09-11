"""Evaluate the following integral by using one point Gauss quadrature and
compute the true error"""

import math

def f(x):
    return (x**2)*(math.sin(x))

def star(a,b,x):
    return ((b-a)/2)*x + (a+b)/2

def OnePointGaussQuadrature(a, b, f: callable):
    ans = ((b-a)/2)*(2*f(star(a,b,0)))
    return ans

def main():
    a = 0
    b = math.pi / 4
    print("One Point Gauss Quadrature: ", OnePointGaussQuadrature(a, b, f))


if __name__ == "__main__":
    main()