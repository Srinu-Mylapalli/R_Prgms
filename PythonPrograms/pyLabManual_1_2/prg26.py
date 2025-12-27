def power(x,n):
    if n==0:
        return 1
    if x==0:
        return 0
    return x*power(x,n-1)


x= int(input("enter x value : "))
n=int(input("enter n value : "))
print("power value is : ",power(x,n))
