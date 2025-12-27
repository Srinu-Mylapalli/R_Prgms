# to count the frequency of words appearing in a string using dictionary

def wordCount(str):
    counts=dict()
    words= str.split()
    for word in words:
        if word in counts:
            counts[word]=counts[word]+1
        else:
            counts[word]=1

    return counts

string=input("Enter string : ")
print(wordCount(string))
