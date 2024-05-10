def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib_generator = fib(200)
fibonacci_200th = list(fib_generator)[-1]
print("Фибоначчи(200-ое число)=", fibonacci_200th)