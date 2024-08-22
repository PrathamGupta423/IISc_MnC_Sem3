def F(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9 

def F1(x):
    return 920*x**3 + 54*x**2 + 18*x - 221

def Secant(P0,P1,Tol,F, N0 = 1000):
    i = 2
    q0 = F(P0)
    q1 = F(P1)

    while i <= N0:
        P  = P1 - q1*(P1-P0)/(q1-q0)
        if abs(P-P1) <Tol :
            return P , i
        i = i +1
        P0 = P1
        q0 = q1
        P1 = P
        q1 = F(P)

    return f"Method failed after {N0} iterations"

def False_postion(P0,P1,Tol,F, N0 = 1000):
    i = 2
    q0 = F(P0)
    q1 = F(P1)

    while i <= N0:
        P  = P1 - q1*(P1-P0)/(q1-q0)
        if abs(P-P1) <Tol :
            return P , i
        i = i +1
        q = F(P)
        if(q*q1 < 0):
            P0 = P1
            q0 = q1
        P1 = P
        q1 = q

    return f"Method failed after {N0} iterations"


if __name__ == "__main__":

    # a) In region [-1 ,0]
        # Using Secant Method:
    P0 = -1
    P1 = 0
    Tol = 10**-6
    print(f"Root of the equation 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9 in region [-1 ,0] is {Secant(P0,P1,Tol,F)[0]} in {Secant(P0,P1,Tol,F)[1]} iterations")

        # Using False Position Method:
    P0 = -1
    P1 = 0
    Tol = 10**-6
    print(f"Root of the equation 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9 in region [-1 ,0] is {False_postion(P0,P1,Tol,F)[0]} in {False_postion(P0,P1,Tol,F)[1]} iterations")


    # b) In region [0 ,1]
        # Using Secant Method:
    P0 = 0
    P1 = 1
    Tol = 10**-6
    print(f"Root of the equation 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9 in region [0 ,1] is {Secant(P0,P1,Tol,F)[0]} in {Secant(P0,P1,Tol,F)[1]} iterations")

        # Using False Position Method:
    P0 = 0
    P1 = 1
    Tol = 10**-6
    print(f"Root of the equation 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9 in region [0 ,1] is {False_postion(P0,P1,Tol,F)[0]} in {False_postion(P0,P1,Tol,F)[1]} iterations")