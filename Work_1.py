import time
def timer(func):
    def wrapper():
        start_time =time.time();
        func()
        print()
        print(f"Затраченное время = {time.time()-start_time} секунд")
    return wrapper
@timer
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(f"Фибоначчи= {fib2}")
if __name__ == '__main__':
    fibonacci()