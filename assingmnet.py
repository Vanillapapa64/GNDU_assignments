list1=[10,20,30,40]
list2=[50,60,70,80]
list3=list1+list2
print(list3)
#or there is another way but is lil bit complex
for i in range(0,len(list2)):
    list1.append(list2[i])
print(list1)
