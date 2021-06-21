def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the n value: "))
print(f"{str(n)}th Fibonacci number is: {fibonacci(n)}")