#python program to add two matrices
mat1=[]
mat2=[]
mat3=[]
r=int(input("enter row size. "))
c=int(input("enter column size. "))
print(f"enter {r*c} first matrix elements: ")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    mat1.append(a)
print(f"enter {r*c} second matrix elements: ")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    mat2.append(a)

for i in range(r):
    a=[]
    for j in range(c):
        a.append(mat1[i][j]+mat2[i][j])
    mat3.append(a)
print("matrix1: ")
for i in range(r):
    for j in range(c):
        print(mat1[i][j],end=" ")
    print()
print("matrix2: ")
for i in range(r):
    for j in range(c):
        print(mat2[i][j],end=" ")
    print()
print("sum of two matrices: ")
for i in range(r):
    for j in range(c):
        print(mat3[i][j],end=" ")
    print()
