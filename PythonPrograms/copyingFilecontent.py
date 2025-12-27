# to copy content from one file to another
a=open("abc.txt","r")
b=open("abc1.txt","w")
l=a.readlines()
for i in l:
    b.write(i)



a.close()
b.close()
