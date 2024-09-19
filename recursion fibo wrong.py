n = int(input("Enter the number you want the Fibonacci series of: "))

def fibo(n):
    if n == 0:
        return 0  # Return 0 as a number
    elif n == 1:
        return 1  # Return 1 as a number
    else:
        return fibo(n-1) + fibo(n-2)  # Proper recursion for Fibonacci

# Validation and Outputa
if n == 0:
    print("series is 0")
elif n == 1:
    print("series is 1")
else:
    print("The Fibonacci series is:")
    for i in range(n):
        print(fibo(i), end=" ")
