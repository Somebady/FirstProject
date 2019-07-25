print("Enter the Number")
x=int(input())


def factorial(n):
    if(n==1):
        return 1
    else:
        return(n*factorial(n-1))

print(factorial(x))
