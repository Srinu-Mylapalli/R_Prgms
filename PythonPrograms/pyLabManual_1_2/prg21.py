def factRec(n):
    if n==1:
        return n
    else:
        return n*factRec(n-1)

n=int(input("enter a number: "))

if n<0:
    print("Sorry,factorial does not exist for negative number")
else:
    print("The factorial of ",n,"is",factRec(n,))

