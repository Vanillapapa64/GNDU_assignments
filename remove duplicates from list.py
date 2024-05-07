list=[5,6,8,7,3,4,6,4,6,2,1,3,1]
finallist=[]
for i in list:
    if i in finallist:
        pass
    else:
        finallist.append(i)
print(finallist)
