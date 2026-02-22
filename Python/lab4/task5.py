def first_occurrences():
    # Введення слова з клавіатури
    word = input("Enter a word: ").strip()

    if not word:
        print("Error: Empty input!")
        return None

    # Виведення початкового слова
    print(f"Original word: '{word}'")

    # Створення множини з літер слова
    letters_set = set(word)
    print(f"Set of letters: {letters_set}")

    # Оскільки множина не зберігає порядок, потрібно працювати зі списком
    # Знаходимо перші входження літер, зберігаючи порядок
    first_occurrences_list = []
    seen_letters = set()

    for letter in word:
        if letter not in seen_letters:
            first_occurrences_list.append(letter)
            seen_letters.add(letter)

    # Перетворюємо результат назад у множину для виведення (якщо потрібно)
    result_set = set(first_occurrences_list)

    # Виведення результатів
    print(f"First occurrences (in order): {first_occurrences_list}")
    print(f"Result as set: {result_set}")

    return first_occurrences_list


# Виклик функції
first_occurrences()
