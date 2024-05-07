list=[5,6,8,7,3,4,6,4,6,2,1,3,1]
#find length of list
length_of_list=0
for i in list:
    length_of_list+=1
print(length_of_list)
#firstly arrange list in order
for i in range(0,length_of_list):
    for j in range(i+1,length_of_list):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
if length_of_list%2==0:
    n=length_of_list
    #we apply median formula for even number
    term=(n/2)+((n/2)+1)
    median=list[term/2]
else:
    #we apply median formula for even number
    n=length_of_list
    term=(n+1)//2
    #remember to use // in the above step
    median=list[term]
print(median)
