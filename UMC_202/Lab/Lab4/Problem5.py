"""Redo Problem 4 by using two point Gauss quadrature formula."""

import math

def f(x):
    return (x**2)*(math.sin(x))

def star(a,b,x):
    return (b-a)/2*x + (a+b)/2

def TwoPointGaussQuadrature(a, b, f: callable):
    ans = ((b-a)/2)*(f(star(a,b,-(3**(-0.5)))) + f(star(a,b,3**(-0.5))))
    return ans

def main():
    a = 0
    b = math.pi/4
    print("Two Point Gauss Quadrature: ", TwoPointGaussQuadrature(a, b, f))

    

if __name__ == "__main__":
    main()
    