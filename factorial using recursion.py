user=int(input("write a number to find factorial: "))
def factorial(n):
    if n==0:
        return 1
    else:
        answer=n*factorial(n-1)
        return answer
result=factorial(user)
print(result)
