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


def sum_even_numbers_range(x, y):
    """Функція, яка приймає параметри x та y і повертає суму парних чисел"""
    if x > y:
        return None

    total = 0
    for number in range(x, y + 1):
        if number % 2 == 0:
            total += number

    return total


def get_even_numbers_list(x, y):
    """Функція, яка повертає список парних чисел у діапазоні"""
    if x > y:
        return []

    even_numbers = []
    for number in range(x, y + 1):
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers
