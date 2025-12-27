from queue import Queue
adj_list={
        "a":["b","d"],
        "b":["a","c"],
        "c":["b"],
        "d":["a","e","f"],
        "e":["d","f","g"],
        "f":["d","e","h"],
        "g":["e","h"],
        "h":["f","b"]
        }
v={}
l={}
p={}
b_o=[]
q=Queue()
for n in adj_list.keys():
    v[n]=False
    l[n]=-1
    p[n]=None
s=input("enter source node: ")
v[s]=True
l[s]=0
q.put(s)
while not q.empty():
    u=q.get()
    b_o.append(u)
    for i in adj_list[u]:
        if not v[i]:
            v[i]=True
            p[i]=u
            l[i]=l[u]+1
            q.put(i)
v=input("enter destination node: ")
path=[]
while v is not None:
    path.append(v)
    v=p[v]
path.reverse()
print(path)
