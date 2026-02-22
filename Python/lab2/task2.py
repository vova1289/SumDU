import math
import mod


def calculate_z():
    print("Обчислення z = (1 - z*sin²x) / (1 + sin²x)")
    print("===========================================")

    try:
        x = float(input("Введіть значення x: "))

        sin_squared = math.sin(x) ** 2
        z = 1 / (1 + 2 * sin_squared)

        print(f"Результат:")
        print(f"x = {x}")
        print(f"sin²(x) = {sin_squared:.6f}")
        print(f"z = {z:.6f}")

        return z

    except ValueError:
        print("Помилка: будь ласка, введіть коректне числове значення")
        return None
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")
        return None


def demonstrate_module_functions():
    print("\nДемонстрація роботи з модулем mod")
    print("======================================")

    # Демонстрація різних способів використання функцій з модуля
    print("1. Використання функції з вводом даних:")
    mod.sum_even_numbers()

    print("\n2. Використання функції з параметрами:")
    result1 = mod.sum_even_numbers_range(1, 10)
    print(f"Сума парних чисел від 1 до 10: {result1}")

    result2 = mod.sum_even_numbers_range(5, 15)
    print(f"Сума парних чисел від 5 до 15: {result2}")

    print("\n3. Отримання списку парних чисел:")
    even_list = mod.get_even_numbers_list(1, 10)
    print(f"Парні числа від 1 до 10: {even_list}")

    # Демонстрація з користувацьким вводом
    try:
        print("\n4. Обчислення з вашими числами:")
        x = int(input("Введіть початкове число: "))
        y = int(input("Введіть кінцеве число: "))

        total = mod.sum_even_numbers_range(x, y)
        numbers = mod.get_even_numbers_list(x, y)

        if total is not None:
            print(f"Парні числа: {numbers}")
            print(f"Сума: {total}")
        else:
            print("Невірний діапазон")

    except ValueError:
        print("Помилка введення!")


def main():
    print("Основна програма з підключеним модулем")
    print("======================================")

    while True:
        print("\nОберіть функцію:")
        print("1 - Обчислити z = (1 - z*sin²x) / (1 + sin²x)")
        print("2 - Сума парних чисел (інтерактивно)")
        print("3 - Демонстрація модуля mod")
        print("4 - Вийти з програми")

        choice = input("Ваш вибір (1-4): ")

        if choice == "1":
            calculate_z()
        elif choice == "2":
            mod.sum_even_numbers()
        elif choice == "3":
            demonstrate_module_functions()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
