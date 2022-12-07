def func(a,b,c,d):
    if d =="+":
        print("их сумма:",a+b+c)
    if d =="*":
        print("их произведение:",a*b*c)
    if d =="/":
        print("их частное:",a/b/c)
    if d =="-":
        print("их разность:",a-b-c)

d = input("введи символ:")
a = int(input("введи число:"))
b = int(input("введи число:"))
c = int(input("введи число:"))
func(a, b, c, d)