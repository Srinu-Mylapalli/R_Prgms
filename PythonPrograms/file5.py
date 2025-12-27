#to illustrate readlines()
fp=open("abc.txt","r")
#print(fp.readlines())

print("next")


x=fp.readlines()
for i in x:
    # i.readlines() this code block is same as
    print(i)

fp.close()
print(x)
