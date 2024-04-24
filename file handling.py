#es program ch aapan roll number di file bnoni aa. user ton 10 names di input leni aa, fer 6th roll number delete krna hai fer 8th roll number da naam change krna hai
file1=open('rollno.txt','w')
for i in range(0,10):
    inp=input("enter name:")
    file1.writelines(str(i+1)+' '+inp+'\n')
file1.close()
file2=open('rollno.txt','r+')
line=file2.readlines()
file3=open('rollno.txt','w')
line[7]='8 Rohit \n'
del line[5]

file3.writelines(line)
file2.close()
file3.close()
