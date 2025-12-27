# Mutable data types are reflected back from a function call
list=["Hi","hello","python"]
def add(x):
    '''to append an element in the list'''
    list.append(x)


print(list)
add("world")

print(list)

print(add.__doc__)
