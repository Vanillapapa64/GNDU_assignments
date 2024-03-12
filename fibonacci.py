num=int(input("enter the number"))
b=1
a=0
c=0
while True:
    c=a+b
    a=b
    b=c
    if c>num:
        break
    else:
        print(c)