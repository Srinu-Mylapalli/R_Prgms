try:
    a=int(input("enter a value: "))
    b=int(input("enter b value: "))
    c=a/b
    print(c)
    l=[10,20,30]
    print(l[2])
    print(a,b,c,d)

except ZeroDivisionError:
    print("Divided by zero")

except IndexError:
    print("Index out of range")

except NameError:
    print("Undefined object identified")


