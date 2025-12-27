def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


n=int(input("enter n value: "))
res=fact(n)


print("Factorial of given no. by recursion is : ",res)
