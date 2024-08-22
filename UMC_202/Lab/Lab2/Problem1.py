import math

def A(x):
    return x**3 - 2*x**2 -5 # Function to be solved

def A1(x):
    return 3*x**2 - 4*x # Derivative of the function

def B(x):
    return x**2 -2*x*(math.e**(-x)) + math.e**(-2*x) # Function to be solved

def B1(x):
    return 2*x - 2*(math.e**(-x)) + 2*x*(math.e**(-x)) - 2*math.e**(-2*x) # Derivative of the function

def C(x):
    return x**3 - 3*(x**2)*(2**(-x)) +3*x*(4**(-x)) - 8**(-x) # Function to be solved

def C1(x):
    return 3*x**2 - 6*x*(2**(-x)) + 3*(4**(-x)) + 3*(x**2)*(2**(-x))*math.log(2,math.e) - 3*x*(4**(-x))*math.log(4,math.e) + 8**(-x)*math.log(8,math.e) # Derivative of the function

def NewtonRaphson(P0 , Tol , N0 , F, F1):
    i = 1
    while i <= N0:
        P = P0 - F(P0)/F1(P0)
        if abs(P - P0) < Tol:
            return P , i
        i = i + 1
        P0 = P
    return "Method failed after N0 iterations"

if __name__ == "__main__":

    # a) P0 = 1, Tol = 110^-5, N0 = infinite
    P0 = 1
    Tol = 10**-5
    N0 = 1000
    print(f"Root of the equation  x**3 - 2*x**2 -5 is {NewtonRaphson(P0 , Tol , N0 , A, A1)[0]} in {NewtonRaphson(P0 , Tol , N0 , A, A1)[1]} iterations")

    # b) P0 = 0.5, Tol = 10^-5, N0 = infinite

    P0 = 0.5
    Tol = 10**-5
    N0 = 1000
    print (f"Root of the equation x**2 -2*x*(math.e**(-x)) + math.e**(-2*x) is {NewtonRaphson(P0 , Tol , N0 , B, B1)[0]} in {NewtonRaphson(P0 , Tol , N0 , B, B1)[1]} iterations")

    # c) P0 = 0.5, Tol = 10^-5, N0 = infinite

    P0 = 0.5
    Tol = 10**-5
    N0 = 1000

    print(f"Root of the equation x**3 - 3*(x**2)*(2**(-x)) +3*x*(4**(-x)) - 8**(-x) is {NewtonRaphson(P0 , Tol , N0 , C, C1)[0]} in {NewtonRaphson(P0 , Tol , N0 , C, C1)[1]} iterations")
