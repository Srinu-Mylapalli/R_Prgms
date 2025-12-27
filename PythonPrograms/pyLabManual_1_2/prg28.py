fname=input("Enter file name : ")
fp=open(fname)
lst=list()
words=[]
for line in fp:
    words+=line.split()
words.sort()

print("The unique words in alphabetical order are : ")
for word in words:
    if word in lst:
        continue
    else:
        lst.append(word)
        print(word)

