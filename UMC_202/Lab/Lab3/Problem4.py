'''
To Use Lagrange interpolating polynomial to find the value of the function at given points'''

def f1(x:float) -> float:
    if(x == 0):
        return 1.101000
    if(x == -0.25):
        return 0.3349375
    if(x == -0.5):
        return -0.02475
    if(x == -0.75):
        return -0.07181250
    else:
        print("Invalid Input")
        print(x)
        return 0
    
def f2(x:float) -> float:
    eplison = 0.0000001
    if(x < 0.1+eplison and x > 0.1-eplison):
        return -0.62049958
    if(x < 0.2+eplison and x > 0.2-eplison):
        return -0.28398668
    if(x < 0.3+eplison and x > 0.3-eplison):
        return 0.00660095
    if(x < 0.4+eplison and x > 0.4-eplison):
        return 0.24842440
    else:
        print("Invalid Input")
        print(x)
        return 0
    
def lagrange_interpolating_Polynomial(Inp_List:list, k, x) -> float:

    ans = 1
    for i in range(len(Inp_List)):
        if(i!=k):
            ans *= (x-Inp_List[i])/(Inp_List[k]-Inp_List[i])
        
    
    return ans

def main():
    # Problem 1
    print("Problem 1")
    vals = [-0.75, -0.5, -0.25, 0]
    x = -1/3
    P_Now = 0
    for i in range(len(vals)):
        P_Now += f1(vals[i])*lagrange_interpolating_Polynomial(vals, i, x)
    
    print(f"P({x}) = {P_Now}")

    # Problem 2
    print("Problem 2")
    vals = [0.1, 0.2, 0.3, 0.4]
    x = 0.25
    P_Now = 0
    for i in range(len(vals)):
        P_Now += f2(vals[i])*lagrange_interpolating_Polynomial(vals, i, x)

    print(f"P({x}) = {P_Now}")


if __name__ == "__main__":
    main()