def add_expense():
  date = input("Введите дату выполнения задачи (YYYY-MM-DD): ")
  category = input("Введите тему задачи: ")
  description = input("Введите описание задачи: ")
  with open("diary.txt", "a", encoding='utf-8') as file:
    file.write(f"{date},{category},{description}\n")
  print("Задача добавлена.")
def view_expenses():
  print("Дата\t\tТема\tОписание")
  with open("diary.txt", "r", encoding='utf-8') as file:
    for line in file:
      date, category, description = line.strip().split(",")
      print(f"{date}\t{category}\t\t{description}")
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
