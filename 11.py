from random import randint
a = int(input("введи положительное число:"))
spisok =[randint(0,a) for i in range(a)]
for spisok in spisok:
    print(spisok, end=";")
print("\b", end="")
print(" ")
