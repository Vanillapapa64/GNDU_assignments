file1=open("123.txt","w")
file2=open('123.txt','a+')
marks=''
totalmarks=0
for i in range(1,3):
    name=input(f"enter name of roll number {i}: ")
    father=input("enter father name: ")
    for j in range(0,2):
        mark= int(input("enter subject marks:"))
        marks= marks+' '+str(mark)
        totalmarks=totalmarks+mark
    file2.writelines(f'{i}  {name}  {father}  {marks} {totalmarks} \n')
    marks=''
file1.close()
file2.close()
file3=open('123.txt',"r")
t=file3.read()
print(t)
file3.seek(0)
user=input('enter the name you want to find:')
line=file3.readlines()
for i in range(0,len(line)):
    if user in line[i]:
        print(line[i])
file3.close()
