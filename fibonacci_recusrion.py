def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_series = fibonacci(n)
print("Fibonacci series:")
print(fib_series)






