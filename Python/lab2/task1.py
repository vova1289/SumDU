import math


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


def sum_even_numbers():
    print("\nСума парних чисел від x до y")
    print("=============================")

    try:
        x = int(input("Введіть початкове число x: "))
        y = int(input("Введіть кінцеве число y: "))

        if x > y:
            print("Помилка: x повинно бути менше або дорівнювати y")
            return None

        total = 0
        even_numbers = []

        for number in range(x, y + 1):
            if number % 2 == 0:
                total += number
                even_numbers.append(number)

        print(f"Результат:")
        print(f"Діапазон: від {x} до {y}")
        print(f"Парні числа: {even_numbers}")
        print(f"Сума парних чисел: {total}")

        return total

    except ValueError:
        print("Помилка: будь ласка, введіть коректні цілі числа")
        return None


def main():
    print("Програма з двома функціями користувача")
    print("======================================")

    while True:
        print("\nОберіть функцію:")
        print("1 - Обчислити z = (1 - z*sin²x) / (1 + sin²x)")
        print("2 - Знайти суму парних чисел у діапазоні")
        print("3 - Вийти з програми")

        choice = input("Ваш вибір (1, 2 або 3): ")

        if choice == "1":
            calculate_z()
        elif choice == "2":
            sum_even_numbers()
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

