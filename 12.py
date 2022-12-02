from random import randint
matrix =[]
size = 4
for i in range (size):
    row=[]
    for j in range (size):
        row.append(randint(5, 8))
    matrix.append(row)
for i in range (size):
    for j in range (size):
        print(matrix[i][j], end=" ")
    print()
for i in range (size):
    a = sum((matrix[i]))
    spisok=[a]
    print(spisok,end="")
   