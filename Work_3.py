def add_two_Input():
    try:
        personNumber = int(input("Введите число: "))
        print(f"Результат сложения: 2 + {personNumber} = {2 + personNumber}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")
add_two_Input()
