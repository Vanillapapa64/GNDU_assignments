a=int(input())
product=1
while a>0:
    digit=a%10
    a=a//10
    product=product*digit
print(product) 