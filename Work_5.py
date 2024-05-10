class NegativeValueError(ValueError):
    def __init__(self, message="Значение не может быть отрицательным"):
        super().__init__(message)
def calculate_square_root(number):
    if number < 0:
        raise NegativeValueError
    return number * 0.5
def calculate_area(width, height):
    if width < 0 or height < 0:
        raise NegativeValueError("Ширина и высота должны быть положительными значениями")
    return width * height
# Пример 1:
try:
    result = calculate_square_root(-4)
    print(result)
except NegativeValueError as e:
    print(f"Ошибка: {e}")

# Пример 2:
try:
    area = calculate_area(5, -2)
    print(area)
except NegativeValueError as e:
    print(f"Ошибка: {e}")
