try:
    num = int(input("Введите число: "))
    print("Все верно. Число:", num)
except ValueError:
    print("Это не число.")
