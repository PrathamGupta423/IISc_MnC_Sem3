"""Redo Problem 6 using the Gaussian quadrature formula with n = 1, m = 2
in both dimensions."""

import math

def f2(x,y):
    return math.log(x+2*y, math.e)

def star(a,b,x):
    return (b-a)/2*x + (a+b)/2

def onePointGaussQuadrature(a, b, f: callable):
    ans = (b-a)/2*(2*f(star(a,b,0)))
    return ans

def twoPointGaussQuadrature(a, b, f: callable):
    ans = (b-a)/2 * (f(star(a,b,-(1/(3**(0.5))))) + f(star(a,b,1/(3**(0.5)))))
    return ans

def Gaussian_quad(n, a, b, f: callable):
    if(n == 1):
        return onePointGaussQuadrature(a,b,f)
    elif (n==2):
        return twoPointGaussQuadrature(a,b,f)
    else:
        print("Not Supported")
        return 
    
def MultiVariate(n,a,b,y,f):
    return Gaussian_quad(n,a,b,lambda x: f(x,y))

def multi(n,xa,xb,ya,yb,f:callable):
    return(Gaussian_quad(n,ya,yb,lambda y: MultiVariate(n,xa,xb,y,f)))

def main():
    xa = 1.4
    xb = 2
    ya = 1
    yb = 1.5
    n = 1
    print("Gaussian Quadrature For n = 1: ", multi(n,xa,xb,ya,yb,f2))
    n = 2
    print("Gaussian Quadrature For n = 2: ", multi(n,xa,xb,ya,yb,f2))



if __name__ == "__main__":
    main()