str = "welcome to python lab and it is easy to learn"
words=str.split()
dict = {}

for word in words:
    if (word[0] not in dict.keys()):
        dict[word[0]]=[]
        dict[word[0]].append(word)

    else:
        if (word not in dict[word[0]]):
            dict[word[0]].append(word)






print(dict)
