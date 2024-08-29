'''
Find the degree of polynomial that best fits the data'''

def f(x):
    if(x==-2):
        return 1
    if(x==-1):
        return 4
    if(x==0):
        return 11
    if(x==1):
        return 16
    if(x==2):
        return 13
    if(x==3):
        return -4
    else:
        print("Invalid Input")
        print(x)
        return 0
    
def forward_diff(Xn, h, k, f):
    if(k==0):
        return f(Xn)
    else:
        return forward_diff(Xn+h, h, k-1, f) - forward_diff(Xn, h, k-1, f)
    
def main():
    X0 = -2
    h = 1

    dd = []

    for i in range(6):
        dd.append(forward_diff(X0, h, i, f)/h**i)

    print(dd)

if __name__ == "__main__":
    main()