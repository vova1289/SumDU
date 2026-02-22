# Робота з файлами. Студент: Манілов В.М.

def open_file(file_name, mode):
    """Функція для відкриття файлу з обробкою виключень"""
    try:
        file = open(file_name, mode, encoding="utf-8")
    except FileNotFoundError:
        print(f"Помилка: Файл {file_name} не знайдено!")
        return None
    except PermissionError:
        print(f"Помилка: Немає доступу до файлу {file_name}!")
        return None
    except Exception as e:
        print(f"Помилка відкриття файлу {file_name}: {e}")
        return None
    else:
        print(f"Файл {file_name} успішно відкрито у режимі '{mode}'")
        return file


# Назва файлу, з яким працюватимуть усі студенти
file_name = "students_questions.txt"

# 1. Спочатку читаємо існуючий вміст файлу
print("=" * 50)
print("ЧИТАННЯ ІСНУЮЧОГО ВМІСТУ ФАЙЛУ:")
print("=" * 50)

file_read = open_file(file_name, "r")
if file_read:
    try:
        content = file_read.read()
        print(content)
        print("-" * 50)
    except Exception as e:
        print("Помилка читання файлу:", e)
    finally:
        file_read.close()

# 2. Дописуємо свою відповідь та нове питання
print("\n" + "=" * 50)
print("ДОДАВАННЯ ВІДПОВІДІ ТА НОВОГО ПИТАННЯ:")
print("=" * 50)

file_append = open_file(file_name, "a")  # Відкриваємо для доповнення
if file_append:
    try:
        # Додаємо роздільник
        file_append.write("\n" + "=" * 50 + "\n")

        # Додаємо своє прізвище
        file_append.write("Прізвище: Манілов\n")

        # Додаємо відповідь на питання першого студента
        file_append.write("Відповідь: У Python є кілька способів прочитати вміст текстового файлу:\n")
        file_append.write("1. read() - читає весь файл як один рядок\n")
        file_append.write("2. readline() - читає файл по одному рядку\n")
        file_append.write("3. readlines() - читає всі рядки у список\n")
        file_append.write("4. Ітерація по файлу - найефективніший спосіб для великих файлів\n\n")

        file_append.write("Приклад виведення вмісту файлу на екран:\n")
        file_append.write("```python\n")
        file_append.write("with open('file.txt', 'r', encoding='utf-8') as file:\n")
        file_append.write("    content = file.read()\n")
        file_append.write("    print(content)\n")
        file_append.write("```\n\n")

        file_append.write("Або з використанням циклу:\n")
        file_append.write("```python\n")
        file_append.write("with open('file.txt', 'r', encoding='utf-8') as file:\n")
        file_append.write("    for line in file:\n")
        file_append.write("        print(line.strip())  # strip() видаляє зайві пробіли та переведення рядка\n")
        file_append.write("```\n\n")

        # Додаємо нове питання для третього студента
        file_append.write("Нове питання для третього студента:\n")
        file_append.write("Що таке контекстний менеджер (context manager) у Python?\n")
        file_append.write("Як працює конструкція 'with open() as file' при роботі з файлами?\n")
        file_append.write("Наведіть приклад створення власного контекстного менеджера.\n")

        print("Дані успішно дописано у файл!")

    except Exception as e:
        print("Помилка запису у файл:", e)
    finally:
        file_append.close()

# 3. Виводимо оновлений вміст файлу
print("\n" + "=" * 50)
print("ОНОВЛЕНИЙ ВМІСТ ФАЙЛУ:")
print("=" * 50)

file_final = open_file(file_name, "r")
if file_final:
    try:
        final_content = file_final.read()
        print(final_content)
    except Exception as e:
        print("Помилка читання файлу:", e)
    finally:
        file_final.close()

print("\n" + "=" * 50)
print("СТРУКТУРА ФАЙЛУ:")
print("=" * 50)
print("1. Прізвище першого студента та його питання")
print("2. Роздільник (==========)")
print("3. Прізвище другого студента")
print("4. Розгорнута відповідь на попереднє питання з прикладами коду")
print("5. Нове питання для третього студента")

print("\n" + "=" * 50)
print("ПОСИЛАННЯ НА ФАЙЛ:")
print("=" * 50)
print("Файл доступний за шляхом:", file_name)
print("Або за абсолютним шляхом (може відрізнятися):")
import os

print(os.path.abspath(file_name))
