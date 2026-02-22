def swap_max_min():

    # Введення списку з клавіатури
    A = list(map(int, input('Enter a list of numbers separated by spaces: ').split()))

    # Виведення початкового списку
    print("Original list:", A)

    # Перевірка, чи список не порожній
    if len(A) == 0:
        print("Error: List is empty!")
        return None

    # Знаходимо індекси максимального та мінімального елементів
    max_index = A.index(max(A))
    min_index = A.index(min(A))

    # Виведення знайдених елементів та їх позицій
    print(f"Max element: {A[max_index]} at position {max_index + 1}")
    print(f"Min element: {A[min_index]} at position {min_index + 1}")

    # Обмін місцями максимального та мінімального елементів
    A[max_index], A[min_index] = A[min_index], A[max_index]

    # Виведення результату
    print("List after swapping max and min:", A)

    return A


# Виклик функції
swap_max_min()
