def insert_at_odd_positions(lst, new_element):

    result = []
    for i in range(len(lst)):
        result.append(lst[i])
        if i % 2 == 0 and i != len(lst) - 1:
            result.append(new_element)
    return result

def print_list(lst, message="Список:"):
    """Функція для виведення списку на екран"""
    print(f"{message} {lst}")


def main():
    print("Введіть елементи списку через пробіл:")
    user_input = input()

    # Перетворюємо введений рядок у список (спробуємо як числа, потім як рядки)
    try:
        user_list = [int(x) for x in user_input.split()]
    except ValueError:
        user_list = user_input.split()

    print("\nВведений список:")
    print_list(user_list)

    # Запитуємо елемент для вставки
    new_elem = input("\nВведіть елемент для вставки на непарні позиції: ")

    # Конвертуємо в число, якщо це можливо
    try:
        new_elem = int(new_elem)
    except ValueError:
        pass  # Залишаємо як рядок

    # Виконуємо вставку
    modified_list = insert_at_odd_positions(user_list, new_elem)

    print("\nРезультат:")
    print_list(modified_list, "Список після вставки:")

    # Додатково показуємо, які позиції вважаються непарними
    print("\nПояснення:")
    print(f"Початковий список має {len(user_list)} елементів")
    print(f"Непарні позиції (рахуючи з 1): 1, 3, 5...")
    print(f"Новий елемент '{new_elem}' був вставлений між цими позиціями")


if __name__ == "__main__":
    main()
