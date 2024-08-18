# To use bisection method to find the root of a function f(x) = x^3 - 7x^2 + 14x - 6 on the intervals

# [0, 1]
# [1, 3.2]
# [3.2, 4]

# tolerance = 10e-4

def f(x):
    return x**3 - 7*x**2 + 14*x - 6

def bisection(a, b, tol, max_iter=100):

    i = 0
    fa = f(a)
    fb = f(b)
    if f(a) * f(b) > 0:
        print("No root found.")
        return None
    for i in range(max_iter):
        c = a + ((b-a)/2)
        fc = f(c)
        print(f"Iteration {i}: a={a}, b={b}, c={c}, f(c)={fc}")
        if fc== 0 or (b - a)/2 < tol:
            return c
        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Max iterations reached.")
    # return c


# print(1e-4)

print("Root in [0, 1]:", bisection(0, 1, 1e-4))
print("Root in [1, 3.2]:", bisection(1, 3.2, 1e-4))
print("Root in [3.2, 4]:", bisection(3.2, 4, 1e-4))
