len=0
def length_list(list1):
    global len
    if list1:
        len= len+1
        length_list(list1[1:])
    return len

list1=[1,23,45,6,7]
len=length_list(list1)
print("length of list is : ",len)
