a=int(input("enter a value: " ))
b=int(input("enter b value: "))
c=int(input("enter c value: "))
if a>b and a>c:
    print("largest number is ",a)
elif b>c and b>a:
    print("largest number is ",b)
elif c>a and c>b:
    print("largest number is ",c)
else:
    print("The three numbers are equal .")
