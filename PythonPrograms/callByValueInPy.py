# int,float are immutable data types in python.and won't be reflected back

def change(x):
    # to increment x value by 1
    x=x+1
    return x
x=10
print(x)

res=change(x)
print(res)

print(x)


print(change.__doc__)
