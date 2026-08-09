def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end="")
        c = a + b
        a = b
        b = c

n = int(input("Enter the number of terms: "))
fibonacci(n)