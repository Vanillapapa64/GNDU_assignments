file1 = open('details','r')
lines=file1.readlines()
findvar='student3'
for i in lines:
    
    if findvar in i:
        print(i)
    else:
        pass
file1.close()