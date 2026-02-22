import matplotlib.pyplot as plt
import json
import numpy as np
from collections import defaultdict


# Функція для завантаження даних з JSON файлу
def load_json_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"✓ Дані успішно завантажені з {filename}")
        return data
    except FileNotFoundError:
        print(f"✗ Файл {filename} не знайдено. Використовуються тестові дані.")
        # Повертаємо тестові дані, якщо файл не знайдено
        return [
            {"model": "Toyota Camry", "price": 25000, "age": 3},
            {"model": "Honda Accord", "price": 22000, "age": 5},
            {"model": "Ford Focus", "price": 18000, "age": 8},
            {"model": "BMW X5", "price": 45000, "age": 10},
            {"model": "Audi A4", "price": 32000, "age": 7}
        ]


# Завантаження даних
cars_data = load_json_data('cars.json')

print("\n" + "=" * 70)
print("АНАЛІЗ ДАНИХ ПРО АВТОМОБІЛІ")
print("=" * 70)
print(f"Загальна кількість автомобілів: {len(cars_data)}")

# Створення словника для групування автомобілів за віковими категоріями
age_categories = {
    "До 3 років": 0,
    "3-5 років": 0,
    "6-8 років": 0,
    "9+ років": 0
}

# Групування автомобілів за віком
total_price_by_category = defaultdict(int)
cars_by_category = defaultdict(list)

for car in cars_data:
    age = car['age']

    if age <= 3:
        category = "До 3 років"
    elif age <= 5:
        category = "3-5 років"
    elif age <= 8:
        category = "6-8 років"
    else:
        category = "9+ років"

    age_categories[category] += 1
    total_price_by_category[category] += car['price']
    cars_by_category[category].append(car['model'])

# Підготовка даних для кругової діаграми
categories = list(age_categories.keys())
counts = list(age_categories.values())

# Кольори для кожної категорії
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

# Розрахунок відсотків
total_cars = sum(counts)
percentages = [(count / total_cars) * 100 for count in counts]

# Створення кругової діаграми
plt.figure(figsize=(14, 8))

# Кругова діаграма
plt.subplot(1, 2, 1)
wedges, texts, autotexts = plt.pie(
    counts,
    labels=None,  # Підписи додамо окремо
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=(0.05, 0.05, 0.05, 0.05),  # Виділення секторів
    shadow=True,
    textprops={'fontsize': 11, 'fontweight': 'bold', 'color': 'white'}
)

# Налаштування відображення відсотків
for autotext in autotexts:
    autotext.set_color('black')

# Заголовок
plt.title('Розподіл автомобілів за віковими категоріями',
          fontsize=16, fontweight='bold', pad=20)

# Легенда з детальною інформацієєю
legend_labels = []
for i, category in enumerate(categories):
    avg_price = total_price_by_category[category] / counts[i] if counts[i] > 0 else 0
    legend_labels.append(f'{category}\n({counts[i]} авто, {avg_price:,.0f} грн сер.)')

plt.legend(wedges, legend_labels,
           title="Вікові категорії",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1),
           fontsize=11,
           title_fontsize=12)

# Додаємо інформацію про загальну кількість
plt.figtext(0.5, 0.02,
            f'Загальна кількість автомобілів: {total_cars} | Середній вік: {sum(car["age"] for car in cars_data) / total_cars:.1f} років',
            ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

# Стовпчаста діаграма для порівняння середніх цін
plt.subplot(1, 2, 2)

# Розрахунок середніх цін
avg_prices = []
for category in categories:
    if counts[categories.index(category)] > 0:
        avg_price = total_price_by_category[category] / counts[categories.index(category)]
    else:
        avg_price = 0
    avg_prices.append(avg_price)

# Побудова стовпчастої діаграми
bars = plt.bar(categories, avg_prices, color=colors, alpha=0.8, edgecolor='black')

# Додавання значень на стовпці
for bar, price in zip(bars, avg_prices):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 500,
             f'{price:,.0f} грн', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title('Середня вартість автомобілів за віковими категоріями',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Вікова категорія', fontsize=12)
plt.ylabel('Середня вартість (грн)', fontsize=12)
plt.grid(True, axis='y', alpha=0.3, linestyle='--')

# Загальне налаштування
plt.suptitle('АНАЛІЗ АВТОМОБІЛІВ: ВІК ТА ВАРТІСТЬ',
             fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Відображення графіків
plt.show()

# Виведення детальної інформації в консоль
print("\n" + "=" * 70)
print("ДЕТАЛЬНИЙ АНАЛІЗ ЗА ВІКОВИМИ КАТЕГОРІЯМИ")
print("=" * 70)

for i, category in enumerate(categories):
    print(f"\n{category}:")
    print(f"  Кількість автомобілів: {counts[i]} ({percentages[i]:.1f}%)")
    print(f"  Загальна вартість: {total_price_by_category[category]:,.0f} грн")
    print(f"  Середня вартість: {avg_prices[i]:,.0f} грн")
    print(f"  Моделі: {', '.join(cars_by_category[category])}")

print("\n" + "=" * 70)
print("ЗАГАЛЬНА СТАТИСТИКА:")
print("=" * 70)
print(f"Загальна кількість автомобілів: {total_cars}")
print(f"Загальна вартість всіх автомобілів: {sum(total_price_by_category.values()):,.0f} грн")
print(f"Середня вартість автомобіля: {sum(total_price_by_category.values()) / total_cars:,.0f} грн")
print(f"Середній вік автомобілів: {sum(car["age"] for car in cars_data) / total_cars:.1f} років")

# Розрахунок найпопулярнішої категорії
most_common_category = categories[counts.index(max(counts))]
print(f"Найпоширеніша вікова категорія: {most_common_category} ({max(counts)} авто)")
print("=" * 70)

# Додатковий аналіз: авто старше 6 років
print("\n" + "=" * 70)
print("ДОДАТКОВИЙ АНАЛІЗ: АВТОМОБІЛІ СТАРШЕ 6 РОКІВ")
print("=" * 70)

old_cars = [car for car in cars_data if car['age'] > 6]
old_cars_count = len(old_cars)
old_cars_total_price = sum(car['price'] for car in old_cars)
old_cars_avg_price = old_cars_total_price / old_cars_count if old_cars_count > 0 else 0

print(f"Кількість автомобілів старше 6 років: {old_cars_count}")
print(f"Загальна вартість: {old_cars_total_price:,.0f} грн")
print(f"Середня вартість: {old_cars_avg_price:,.0f} грн")
print("Моделі:", ', '.join(car['model'] for car in old_cars))
print("=" * 70)
