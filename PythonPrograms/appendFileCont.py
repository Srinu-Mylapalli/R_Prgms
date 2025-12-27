# to append the content
fp=open("abc.txt","w")
lis=fp.read()
lis.append("and AI ")
fp.write(lis)
print(fp.read())
fp.close()
