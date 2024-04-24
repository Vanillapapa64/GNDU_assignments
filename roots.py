a=input('write a quadratic equation:')
a=a.split('+')
print(a)
var1=int(a[0][:-2])
var2=int(a[1][:-1])
var3=int(a[2])
def findroot(a,b,c):
    d=b**2-(4*a*c)
    if d>0:
        x1=((-b)+(d**0.5))/(2*a)
        x2=((-b)-(d**0.5))/(2*a)
        print(f'roots are {x1} and {x2}')
    elif d<0:
        x=(d**0.5)
        print(f'roots are (-{b}+i{x})/2 and (-{b}-i{x})/2')
    else:
        print('enter valid input')
findroot(var1,var2,var3)