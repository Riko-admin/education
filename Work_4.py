class CacheResult:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]
@CacheResult
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Вычисление
print(fibonacci(10))  # Из кэша
print(fibonacci(5))   # Вычисление
print(fibonacci(5))   # Из кэша
