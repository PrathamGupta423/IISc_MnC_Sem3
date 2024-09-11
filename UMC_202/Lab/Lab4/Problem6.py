"""Use Composite Simpson’s rule with n = 4 and m = 2 to approximate"""

import math

def f(x,y):
    return math.log((x+2*y), math.e)

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

    h = (b-a)/n
    I = f(a) + f(b)
    for i in range(2, n,2):
        I += 2*f(a + i*h)
    for i in range(1, n ,2):
        u = a + i*h
        I += 4*f(u)
    return (h/3)*I
    

def CompositeSimpsonsRule_callable(a, b, n,y, f: callable) -> callable:
    return CompositeSimpsonsRule(a,b,n,lambda x: f(x,y))



def multi(xa,xb,ya,yb,n,m,f:callable):
    return CompositeSimpsonsRule(ya,yb,m,lambda y: CompositeSimpsonsRule_callable(xa,xb,n,y,f)) 

def main():
    xa = 1.4
    xb = 2
    ya = 1
    yb = 1.5
    m = 2
    n = 4
    print("Composite Simpson's Rule: ", multi(xa,xb,ya,yb,n,m,f))

if __name__ == "__main__":
    main()