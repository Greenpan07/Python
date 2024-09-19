def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return(n*(factorial(n-1)))
print("enter the number you want factorial of")
rs=int(input())
print(factorial(rs))