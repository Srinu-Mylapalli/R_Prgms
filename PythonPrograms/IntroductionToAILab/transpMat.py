mat1=[]
trans=[]
r=int(input("enter matrix row size: "))
c=int(input("enter matrix column size: "))
print(f"enter {r*c} elements: ")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
        mat1.append(a)

print("Given matrix: ")

for i in range(r):
    for j in range(c):
        print(mat1[i][j],end=' ')
    print()

print("Transpose of matrix: ")
for i in range(c):
    a=[]
    for j in range(r):
        a.append(mat1[j][i])
        trans.append(a)

for i in range(c):
    for j in range(r):
        print(trans[i][j],end=' ')
    print()
