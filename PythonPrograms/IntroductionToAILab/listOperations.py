num=[11,22,33,44,55]
prime=[2,3,5,7,11,13]
print(type(num))
print(num,"\n",prime)
print("length: ",len(num))
print("new list= ",num+prime)

if 11 in num:
    print("yes, 11 in num")
print("prime numbers: ")
for i in prime:
    print(i)

print("prime numbers: ",prime[:])
print("prime numbers in reverse order: ",prime[::-1])
