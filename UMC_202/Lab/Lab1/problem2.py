# To-do Use fixed point iteration method to determine a solution accurate to 10e-2 for
# f(x) = x^4 - 3x^2 - 3 = 0 in interval [1,2] , with intial guess p0 = 1

def f(x):
    return x**4 - 3*x**2 - 3

def g(x):
    return (3*x**2 + 3)**0.25

def fixed_point(p0, tol, max_iter=100):
    
        i = 0
        p = p0
        for i in range(max_iter):
            p = g(p)
            print("Iteration", i, ":", p)
            if abs(p - p0) < tol:
                return p
            p0 = p
    
        print("Max iterations reached.")
        return p

print("Root :", fixed_point(1, 1e-2))
