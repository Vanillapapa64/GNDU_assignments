a='hello everyone in this world'
word=''
list=[]
for i in a:
    if i!=" ":
        word+=i
    else:
        if word:
            list.append(word)
            word=''
if word:
    list.append(word)
print(list)
