def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("файл пустой")
            return content
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError as e:
        print(e)
with open('text.txt', 'w') as file:
    pass
with open('text2.txt', 'w') as file:
    file.write("Всем привет!!!")
print(read_file_content('text.txt'))
print(read_file_content('text2.txt'))