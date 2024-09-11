import math
def F(x):
    return math.e**x - x - 1

def F1(x):
    return math.e**x - 1

def F2(x):
    return math.e**x



def NewtonRaphson_with_error_list(P0 , Tol ,Sol, F, F1, N0 = 1000):
    i = 1
    E = []
    k = abs(Sol - P0)
    E.append(k)
    while i <= N0:
        P = P0 - F(P0)/F1(P0)
        E.append(abs(Sol - P))
        if abs(P - P0) < Tol:
            return P , i , E
        i = i + 1
        P0 = P
    return "Method failed after N0 iterations" , E

def Faster_NewtonRaphson_with_error_list(P0 , Tol ,Sol,F,F1, N0 = 1000):
    i = 1
    E = []
    k = abs(Sol - P0)
    E.append(k)
    while i <= N0:
        P = P0 - 2*F(P0)/F1(P0)
        E.append(abs(Sol - P))
        if abs(P - P0) < Tol:
            return P , i , E
        i = i + 1
        P0 = P
    return "Method failed after N0 iterations" , E

if __name__ == "__main__":

    print("Multiplicity Check")
    print(f"f(0) = {F(0)}")
    print(f"f'(0) = {F1(0)}")
    print(f"f''(0) = {F2(0)}")



    print ("-------------------------------------------")


    P0 = 1
    Tol = 10**-6
    Sol = 0

    P , i , E = NewtonRaphson_with_error_list(P0 , Tol ,Sol, F, F1)

    print(f"Root of the equation  math.e**x - x - 1 is {P} in {i} iterations")
    # # print(E)
    # print("Error List:")
    # for j in range(len(E)):
    #     print(f"Error at iteration {j} is {E[j]}")

    for j in range(len(E)-2):
        ROC = math.log(E[j+2]/E[j+1])/math.log(E[j+1]/E[j])
        print(f"Rate of Convergence at iteration {j} is {ROC}")



    print("-------------------------------------------")


    P0 = 1
    Tol = 10**-6
    
    Sol = 0

    P , i , E = Faster_NewtonRaphson_with_error_list(P0 , Tol ,Sol, F, F1)

    print(f"Root of the equation  math.e**x - x - 1 is {P} in {i} iterations")
    # # print(E)
    # print("Error List:")
    # for j in range(len(E)):
    #     print(f"Error at iteration {j} is {E[j]}")

    for j in range(len(E)-2):
        ROC = math.log(E[j+2]/E[j+1])/math.log(E[j+1]/E[j])
        print(f"Rate of Convergence at iteration {j} is {ROC}")


