fp=open("ABC.csv","r")
print(fp.tell())
print("1.",fp.read())
print(fp.tell())

print(fp.seek(0))

print(fp.seek(0))
print("2.",fp.readlines())
print(fp.seek(0))
print(fp.tell())
print(fp.seek(0))

print("3.",fp.readlines(2))


print(fp.seek(0))
fp.close()
