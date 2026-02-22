# Перший код написаний Козловським Олександром Васильовичем
# Доповнено функціями сортування завданням Маніловим Володимиром Миколайовичем

# Словник з інформацією про студентів
students = {
    1: {
        "група": "КНдн-41",
        "ПІБ": "Арцаблюк Роман Володимирович",
        "курс": 2,
        "предмети": {"Математика": 12, "Програмування": 11, "Англійська": 10}
    },
    2: {
        "група": "КНдн-41",
        "ПІБ": "Воробйов Михайло Олегович",
        "курс": 2,
        "предмети": {"Математика": 11, "Програмування": 12, "Англійська": 10}
    }
}


# Функція для виводу даних
def show_students():
    print("Список студентів:")
    for key in students:
        print("Номер:", key)
        print("Група:", students[key]["група"])
        print("ПІБ:", students[key]["ПІБ"])
        print("Курс:", students[key]["курс"])
        print("Предмети та оцінки:", students[key]["предмети"])
        print("-" * 40)


# Функція для додавання нового студента
def add_student():
    number = len(students) + 1
    pib = input("Введіть ПІБ студента: ")
    group = input("Введіть групу: ")
    course = int(input("Введіть курс: "))
    subjects = {"Математика": 12, "Програмування": 11, "Англійська": 10}
    students[number] = {"група": group, "ПІБ": pib, "курс": course, "предмети": subjects}
    print("Студента додано!")


# Функція для обчислення середнього балу студента
def calculate_average_grade(student):
    grades = student["предмети"].values()
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


# Функція сортування студентів за ПІБ
def sort_by_name():
    sorted_items = sorted(students.items(), key=lambda x: x[1]["ПІБ"])
    sorted_dict = {item[0]: item[1] for item in sorted_items}
    return sorted_dict


# Функція сортування студентів за середнім балом (за спаданням)
def sort_by_average_grade():
    sorted_items = sorted(students.items(),
                          key=lambda x: calculate_average_grade(x[1]),
                          reverse=True)
    sorted_dict = {item[0]: item[1] for item in sorted_items}
    return sorted_dict


# Функція для виводу відсортованого списку
def show_sorted_students(sorted_students):
    print("\nВідсортований список студентів:")
    for key, student in sorted_students.items():
        print(f"Номер: {key}")
        print(f"ПІБ: {student['ПІБ']}")
        print(f"Середній бал: {calculate_average_grade(student):.2f}")
        print(f"Предмети та оцінки: {student['предмети']}")
        print("-" * 40)


# Оновлене головне меню
def main_menu():
    print("\n" + "=" * 50)
    print("ОБЕРІТЬ ДІЮ:")
    print("=" * 50)
    print("1 - Показати всіх студентів")
    print("2 - Додати нового студента")
    print("3 - Відсортувати студентів за ПІБ")
    print("4 - Відсортувати студентів за середнім балом")
    print("5 - Вийти з програми")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_students()
        main_menu()
    elif choice == "2":
        add_student()
        show_students()
        main_menu()
    elif choice == "3":
        sorted_students = sort_by_name()
        show_sorted_students(sorted_students)
        main_menu()
    elif choice == "4":
        sorted_students = sort_by_average_grade()
        show_sorted_students(sorted_students)
        main_menu()
    elif choice == "5":
        print("Дякую за використання програми!")
        return
    else:
        print("Невірний вибір! Спробуйте ще раз.")
        main_menu()


# Запуск програми
if __name__ == "__main__":
    print("Програма управління студентами")
    print("Доповнено функціями сортування")
    main_menu()
