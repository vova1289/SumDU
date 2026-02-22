import json
import os

# Початкові дані про автомобілі
cars = [
    {"model": "Toyota Camry", "price": 25000, "age": 3},
    {"model": "Honda Accord", "price": 22000, "age": 5},
    {"model": "Ford Focus", "price": 18000, "age": 8},
    {"model": "BMW X5", "price": 45000, "age": 10},
    {"model": "Audi A4", "price": 32000, "age": 7},
    {"model": "Mercedes C-Class", "price": 38000, "age": 4},
    {"model": "Volkswagen Golf", "price": 20000, "age": 9},
    {"model": "Hyundai Elantra", "price": 19000, "age": 2},
    {"model": "Kia Sportage", "price": 23000, "age": 6},
    {"model": "Nissan Altima", "price": 21000, "age": 11}
]


# Функція для збереження даних у файл JSON
def save_to_file(data, filename="cars.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"✓ Дані збережено у файл {filename}")


# Функція для завантаження даних з файлу JSON
def load_from_file(filename="cars.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створено новий з початковими даними.")
        save_to_file(cars, filename)
        return cars
    except json.JSONDecodeError:
        print(f"Помилка читання файлу {filename}. Використовуються початкові дані.")
        return cars


# Функція для виведення вмісту JSON файлу
def display_data(data):
    print("\n" + "=" * 80)
    print("ВМІСТ ФАЙЛУ JSON (автомобілі):")
    print("=" * 80)
    print(f"{'№':<3} {'Модель':<25} {'Вартість ($)':<15} {'Вік (років)':<12}")
    print("-" * 60)

    for i, car in enumerate(data, 1):
        print(f"{i:<3} {car['model']:<25} {car['price']:<15} {car['age']:<12}")
    print("-" * 60)
    print(f"Всього автомобілів: {len(data)}")
    print("=" * 80)


# Функція для додавання нового запису
def add_car(data):
    print("\n" + "=" * 80)
    print("ДОДАВАННЯ НОВОГО АВТОМОБІЛЯ")
    print("=" * 80)

    model = input("Введіть модель автомобіля: ").strip()

    while True:
        try:
            price = float(input("Введіть вартість автомобіля ($): "))
            if price <= 0:
                print("Вартість повинна бути більше 0!")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть числове значення!")

    while True:
        try:
            age = int(input("Введіть вік автомобіля (років): "))
            if age < 0:
                print("Вік не може бути від'ємним!")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число!")

    new_car = {
        "model": model,
        "price": price,
        "age": age
    }

    data.append(new_car)
    save_to_file(data)
    print(f"✓ Автомобіль '{model}' успішно додано!")
    return data


# Функція для видалення запису
def delete_car(data):
    display_data(data)

    while True:
        try:
            car_num = int(input("\nВведіть номер автомобіля для видалення (або 0 для скасування): "))
            if car_num == 0:
                print("Видалення скасовано.")
                return data

            if 1 <= car_num <= len(data):
                deleted_car = data.pop(car_num - 1)
                save_to_file(data)
                print(f"✓ Автомобіль '{deleted_car['model']}' успішно видалено!")
                return data
            else:
                print(f"Будь ласка, введіть номер від 1 до {len(data)}")
        except ValueError:
            print("Будь ласка, введіть ціле число!")


# Функція для пошуку даних
def search_data(data):
    print("\n" + "=" * 80)
    print("ПОШУК АВТОМОБІЛІВ")
    print("=" * 80)
    print("Критерії пошуку:")
    print("1 - За моделлю")
    print("2 - За віком (старіше зазначеного)")
    print("3 - За ціною (дешевше зазначеної)")
    print("4 - За ціною (дорожче зазначеної)")

    while True:
        try:
            choice = int(input("\nВиберіть критерій пошуку (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Будь ласка, виберіть число від 1 до 4")
        except ValueError:
            print("Будь ласка, введіть ціле число!")

    results = []

    if choice == 1:  # Пошук за моделлю
        search_term = input("Введіть назву моделі або частину назви: ").strip().lower()
        results = [car for car in data if search_term in car['model'].lower()]

    elif choice == 2:  # Пошук за віком (старіше)
        try:
            min_age = int(input("Введіть мінімальний вік автомобіля (років): "))
            results = [car for car in data if car['age'] >= min_age]
        except ValueError:
            print("Невірний формат віку!")
            return

    elif choice == 3:  # Пошук за ціною (дешевше)
        try:
            max_price = float(input("Введіть максимальну вартість ($): "))
            results = [car for car in data if car['price'] <= max_price]
        except ValueError:
            print("Невірний формат ціни!")
            return

    elif choice == 4:  # Пошук за ціною (дорожче)
        try:
            min_price = float(input("Введіть мінімальну вартість ($): "))
            results = [car for car in data if car['price'] >= min_price]
        except ValueError:
            print("Невірний формат ціни!")
            return

    # Виведення результатів пошуку
    if results:
        print(f"\nЗнайдено {len(results)} автомобілів:")
        print(f"{'№':<3} {'Модель':<25} {'Вартість ($)':<15} {'Вік (років)':<12}")
        print("-" * 60)

        for i, car in enumerate(results, 1):
            print(f"{i:<3} {car['model']:<25} {car['price']:<15} {car['age']:<12}")
    else:
        print("\nАвтомобілів за вказаними критеріями не знайдено.")


# Функція для розрахунку середньої вартості автомобілів старше 6 років
def calculate_average_price(data):
    print("\n" + "=" * 80)
    print("РОЗРАХУНОК СЕРЕДНЬОЇ ВАРТОСТІ АВТОМОБІЛІВ СТАРШЕ 6 РОКІВ")
    print("=" * 80)

    # Фільтруємо автомобілі старше 6 років
    old_cars = [car for car in data if car['age'] > 6]

    if not old_cars:
        print("Автомобілів старше 6 років не знайдено.")
        return

    # Розраховуємо середню вартість
    total_price = sum(car['price'] for car in old_cars)
    average_price = total_price / len(old_cars)

    print(f"Знайдено автомобілів старше 6 років: {len(old_cars)}")
    print("\nСписок автомобілів старше 6 років:")
    print(f"{'№':<3} {'Модель':<25} {'Вартість ($)':<15} {'Вік (років)':<12}")
    print("-" * 60)

    for i, car in enumerate(old_cars, 1):
        print(f"{i:<3} {car['model']:<25} {car['price']:<15} {car['age']:<12}")

    print("-" * 60)
    print(f"Сумарна вартість: ${total_price:.2f}")
    print(f"Середня вартість: ${average_price:.2f}")

    # Зберігаємо результати у окремий JSON файл
    result_data = {
        "calculation_date": "2024",
        "condition": "автомобілі старше 6 років",
        "total_cars": len(old_cars),
        "total_price": total_price,
        "average_price": average_price,
        "cars": old_cars
    }

    save_to_file(result_data, "average_price_result.json")
    print(f"\n✓ Результати розрахунку збережено у файл 'average_price_result.json'")


# Головна функція з меню
def main():
    print("=" * 80)
    print("ПРОГРАМА ДЛЯ РОБОТИ З ДАНИМИ ПРО АВТОМОБІЛІ У ФОРМАТІ JSON")
    print("=" * 80)

    # Завантажуємо дані з файлу або створюємо нові
    data = load_from_file()

    while True:
        print("\n" + "=" * 80)
        print("ГОЛОВНЕ МЕНЮ")
        print("=" * 80)
        print("1 - Вивести всі дані на екран")
        print("2 - Додати новий автомобіль")
        print("3 - Видалити автомобіль")
        print("4 - Пошук автомобілів")
        print("5 - Розрахувати середню вартість автомобілів старше 6 років")
        print("6 - Вихід")
        print("=" * 80)

        try:
            choice = int(input("Виберіть опцію (1-6): "))
        except ValueError:
            print("Будь ласка, введіть число від 1 до 6!")
            continue

        if choice == 1:
            display_data(data)

        elif choice == 2:
            data = add_car(data)

        elif choice == 3:
            data = delete_car(data)

        elif choice == 4:
            search_data(data)

        elif choice == 5:
            calculate_average_price(data)

        elif choice == 6:
            print("\n" + "=" * 80)
            print("Дякую за використання програми! До побачення!")
            print("=" * 80)
            break

        else:
            print("Будь ласка, виберіть число від 1 до 6!")


# Запуск програми
if __name__ == "__main__":
    main()
