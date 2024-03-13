a= int(input())
x=a
finalnumber=0
a1=a2=a3=a4=a5=a6=a7=a8=a9=a0=0
while x!=0:
    dig=x%10
    x//=10
    if dig==0:
        a0+=1
    elif dig==1:
        a1+=1
    elif dig==2:
        a2+=1
    elif dig==3:
        a3+=1
    elif dig==4:
        a4+=1
    elif dig==5:
        a5+=1
    elif dig==6:
        a6+=1
    elif dig==7:
        a7+=1
    elif dig==8:
        a8+=1
    else:
        a9+=1
    continue
if a0>0:
    print(f"frequency of 0 is {a0}")
if a1>0:
    print(f"frequency of 1 is {a1}")
if a2>0:
    print(f"frequency of 2 is {a2}")
if a3>0:
    print(f"frequency of 3 is {a3}")
if a4>0:
    print(f"frequency of 4 is {a4}")
if a5>0:
    print(f"frequency of 5 is {a5}")
if a6>0:
    print(f"frequency of 6 is {a6}")
if a7>0:
    print(f"frequency of 7 is {a7}")
if a8>0:
    print(f"frequency of 8 is {a8}")
if a9>0:
    print(f"frequency of 9 is {a9}")
else:
    pass

if a1>=1:
    finalnumber=finalnumber*10+1
if a2>=1:
    finalnumber=finalnumber*10+2
if a3>=1:
    finalnumber=finalnumber*10+3
if a4>=1:
    finalnumber=finalnumber*10+4
if a5>=1:
    finalnumber=finalnumber*10+5
if a6>=1:
    finalnumber=finalnumber*10+6
if a7>=1:
    finalnumber=finalnumber*10+7
if a8>=1:
    finalnumber=finalnumber*10+8
if a9>=1:
    finalnumber=finalnumber*10+9
if a0>=1:
    finalnumber=finalnumber*10+0
else:
    pass
print(finalnumber)
    
    
        
    
            

    
