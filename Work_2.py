def add_expense():
  date = input("Введите дату (YYYY-MM-DD): ")
  category = input("Введите категорию: ")
  amount = float(input("Введите сумму: "))
  with open("expenses.txt", "a", encoding='utf-8') as file:
    file.write(f"{date},{category},{amount}\n")
  print("Расход добавлен.")

def view_expenses():
  """Выводит список расходов из файла."""
  print("Дата\t\tКатегория\tСумма")
  with open("expenses.txt", "r", encoding='utf-8') as file:
    for line in file:
      date, category, amount = line.strip().split(",")
      print(f"{date}\t{category}\t\t{amount}")
while True:
  action = input("Выберите действие (1-добавить/2-посмотреть/3-выход): ")
  if action.lower() == "1":
    add_expense()
  elif action.lower() == "2":
    view_expenses()
  elif action.lower() == "3":
    break
  else:
    print("Неизвестное действие.")
