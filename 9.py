a = int(input("введи положительное число 1:"))
b = int(input("введи положительное число 2:"))
c = int(input("введи положительное число 3:"))
for i in range(a,b,c):
    if i%5==0:
        print(i)