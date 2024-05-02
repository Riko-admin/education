from Gheron_formula import gheron_area
def get_triangle_sides():
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c
def main():
    print("Программа для вычисления площади треугольника по формуле Герона.")
    a, b, c = get_triangle_sides()
    area = gheron_area(a, b, c)
    print(f"Площадь треугольника: {area:.2f} квадратных единиц")
if __name__ == "__main__":
    main()