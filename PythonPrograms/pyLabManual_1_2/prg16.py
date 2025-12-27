#working with dictionaries

dict1 = {'StdNo':532,'StdName':'Naveen','StuAge':21,'StdCity':'Hyderabad'}
print("\n Dictionary is : ",dict1)

print("\n Student Name is : ",dict1['StdName'])

print("\n Student City is : ",dict1['StdCity'])

print("\n All Keys in Dictionary")

for x in dict1:
    print(x)

print("\n All values in Dictionary")

for x in dict1:
    print(dict1[x])


dict1["Phno"] = 3678268367

print("Updated Dictionary",dict1)

dict1['StdName']="Madhu"
print("Updated Dictionary is : ",dict1)

dict1.pop("StuAge")
print("Updated Dictionary is : ",dict1)

print("Length of Dictionary is : ",len(dict1))
dict2 = dict1.copy()
print("New Dictionary is : ",dict2)

dict1.clear()

print("Updated Dictionary is : ",dict1)

