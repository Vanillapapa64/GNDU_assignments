user=input('type a string  ')
vowels=['a','e','i','o','u']
count=0
for i in user:
    if i in vowels:
        count+=1
print(count)
