def display_all_cars(cars):
    """Функція для виведення всіх значень словника"""
    print("\n" + "=" * 50)
    print("ВСІ АВТОМОБІЛІ:")
    print("=" * 50)
    for model, (price, age) in cars.items():
        print(f"{model}: ${price:,.2f}, {age} років")
    print("=" * 50)


def add_car(cars, model, price, age):
    """Функція для додавання нового запису до словника"""
    cars[model] = (price, age)
    print(f"\nАвтомобіль {model} додано успішно!")
    return cars


def delete_car(cars, model):
    """Функція для видалення запису зі словника"""
    if model in cars:
        del cars[model]
        print(f"\nАвтомобіль {model} видалено успішно!")
    else:
        print(f"\nАвтомобіль {model} не знайдено!")
    return cars


def display_sorted_cars(cars):
    """Функція для виведення вмісту словника за відсортованими ключами"""
    print("\n" + "=" * 50)
    print("АВТОМОБІЛІ (відсортовані за назвою):")
    print("=" * 50)

    # Сортуємо ключі словника
    sorted_models = sorted(cars.keys())

    for model in sorted_models:
        price, age = cars[model]
        print(f"{model}: ${price:,.2f}, {age} років")
    print("=" * 50)


def calculate_average_price_for_old_cars(cars, min_age=6):
    """Функція для обчислення середньої вартості автомобілів старших за вказаний вік"""
    total_price = 0
    count = 0

    print(f"\nАвтомобілі старші {min_age} років:")
    print("-" * 40)

    for model, (price, age) in cars.items():
        if age > min_age:
            print(f"{model}: ${price:,.2f}, {age} років")
            total_price += price
            count += 1

    print("-" * 40)

    if count > 0:
        average_price = total_price / count
        print(f"\nЗнайдено {count} автомобілів старших {min_age} років")
        print(f"Сумарна вартість: ${total_price:,.2f}")
        print(f"Середня вартість: ${average_price:,.2f}")
        return average_price
    else:
        print(f"\nНе знайдено автомобілів старших {min_age} років")
        return 0


def main():
    """Головна функція програми"""

    # Початкові дані
    cars = {
        "Toyota Camry": (25000, 3),
        "Honda Civic": (22000, 2),
        "Ford Focus": (18000, 8),
        "BMW X5": (55000, 5),
        "Mercedes C-Class": (45000, 7),
        "Audi A4": (35000, 10),
        "Volkswagen Golf": (20000, 9),
        "Tesla Model 3": (42000, 1),
        "Hyundai Tucson": (28000, 4),
        "Nissan Qashqai": (23000, 6)
    }

    # Демонстрація роботи всіх функцій
    display_all_cars(cars)

    display_sorted_cars(cars)

    calculate_average_price_for_old_cars(cars, 6)

    # Приклад додавання нового автомобіля
    add_car(cars, "Mazda CX-5", 32000, 8)

    # Приклад видалення автомобіля
    delete_car(cars, "Tesla Model 3")

    # Показуємо оновлений список
    display_all_cars(cars)

    # Перераховуємо середню вартість після змін
    calculate_average_price_for_old_cars(cars, 6)


# Запускаємо програму
if __name__ == "__main__":
    main()
