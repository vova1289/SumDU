import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Для коректного відображення українських символів на графіках
plt.rcParams['font.family'] = 'DejaVu Sans'

# --- 1. Завантаження даних ---
# Зчитуємо файл CSV
df = pd.read_csv('comptagevelo2013.csv')

# --- 2. Перевірка основних характеристик ---
print("=" * 70)
print("ПЕРШІ 5 РЯДКІВ ДАНИХ:")
print("=" * 70)
print(df.head())
print("\n")

print("=" * 70)
print("ІНФОРМАЦІЯ ПРО ДАТАФРЕЙМ:")
print("=" * 70)
print(df.info())
print("\n")

print("=" * 70)
print("ОПИСОВА СТАТИСТИКА:")
print("=" * 70)
print(df.describe())
print("\n")

# --- 3. Загальна кількість велосипедистів за рік на всіх велодоріжках ---
# Визначаємо колонки з числовими даними (велодоріжки)
# Перша колонка 'Date' - не числова, тому виключаємо її
bike_columns = df.columns[1:]  # Всі колонки, крім Date

# Сумуємо всі значення по всіх колонках
total_bikers_all = df[bike_columns].sum().sum()
print("=" * 70)
print(f"ЗАГАЛЬНА КІЛЬКІСТЬ ВЕЛОСИПЕДИСТІВ ЗА РІК (ВСІ ДОРІЖКИ): {total_bikers_all:,.0f}")
print("=" * 70)
print("\n")

# --- 4. Загальна кількість велосипедистів за рік на кожній велодоріжці ---
total_per_station = df[bike_columns].sum()
print("=" * 70)
print("ЗАГАЛЬНА КІЛЬКІСТЬ ВЕЛОСИПЕДИСТІВ ЗА РІК НА КОЖНІЙ ВЕЛОДОРІЖЦІ:")
print("=" * 70)

# Сортуємо для кращого відображення (від найбільшої до найменшої)
total_per_station_sorted = total_per_station.sort_values(ascending=False)

for station, count in total_per_station_sorted.items():
    print(f"{station}: {count:,.0f}")

print("\n")

# --- 5. Додатковий аналіз: ТОП-5 найпопулярніших велодоріжок ---
print("=" * 70)
print("ТОП-5 НАЙПОПУЛЯРНІШИХ ВЕЛОДОРІЖОК:")
print("=" * 70)
top_5 = total_per_station_sorted.head(5)
for station, count in top_5.items():
    print(f"{station}: {count:,.0f}")
print("\n")

# --- 6. Додаємо колонку з місяцем для подальшого аналізу ---
# Перетворюємо колонку Date у формат datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['MonthName'] = df['Date'].dt.month_name()

# --- 7. Аналіз за місяцями для обраних трьох велодоріжок ---
# Обираємо три велодоріжки (з топ-5 для різноманітності)
selected_stations = ['Berri1', 'Rachel / Papineau', 'Maisonneuve_1']

print("=" * 70)
print("АНАЛІЗ ПОПУЛЯРНОСТІ ЗА МІСЯЦЯМИ ДЛЯ ОБРАНИХ ВЕЛОДОРІЖОК:")
print("=" * 70)

# Створюємо словник для зберігання результатів
monthly_popularity = {}

for station in selected_stations:
    # Групуємо за місяцями та сумуємо кількість велосипедистів
    monthly_counts = df.groupby('Month')[station].sum()

    # Знаходимо місяць з максимальною кількістю
    max_month = monthly_counts.idxmax()
    max_count = monthly_counts.max()

    # Отримуємо назву місяця
    month_names = {
        1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
        5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
        9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
    }

    print(f"\nВелодоріжка: {station}")
    print(f"Найпопулярніший місяць: {month_names[max_month]} (місяць #{max_month})")
    print(f"Кількість велосипедистів: {max_count:,.0f}")

    # Зберігаємо дані для графіка
    monthly_popularity[station] = monthly_counts

# --- 8. Побудова графіка завантаженості однієї з велодоріжок по місяцях ---
# Обираємо одну велодоріжку для детального графіка (наприклад, Berri1)
station_for_plot = 'Berri1'
monthly_data = monthly_popularity[station_for_plot]

# Створюємо графік
plt.figure(figsize=(12, 6))

# Стовпчикова діаграма
bars = plt.bar(monthly_data.index, monthly_data.values, color='skyblue', edgecolor='navy', alpha=0.7)

# Додаємо значення на стовпчики
for bar, value in zip(bars, monthly_data.values):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 50,
             f'{value:,.0f}', ha='center', va='bottom', rotation=0, fontsize=9)

# Налаштування графіка
month_names_short = ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер', 'Лип', 'Сер', 'Вер', 'Жов', 'Лис', 'Гру']
plt.xlabel('Місяць', fontsize=12)
plt.ylabel('Кількість велосипедистів', fontsize=12)
plt.title(f'Завантаженість велодоріжки "{station_for_plot}" по місяцях за 2013 рік', fontsize=14, fontweight='bold')
plt.xticks(range(1, 13), month_names_short)
plt.grid(axis='y', alpha=0.3)

# Додаємо сітку та підписи
plt.tight_layout()

# Зберігаємо графік у файл
plt.savefig('bike_path_monthly_usage.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "=" * 70)
print("ГРАФІК ПОБУДОВАНО ТА ЗБЕРЕЖЕНО У ФАЙЛ 'bike_path_monthly_usage.png'")
print("=" * 70)

# --- 9. Додатковий аналіз: середньодобова кількість велосипедистів по місяцях ---
print("\n" + "=" * 70)
print("СЕРЕДНЬОДОБОВА КІЛЬКІСТЬ ВЕЛОСИПЕДИСТІВ ПО МІСЯЦЯХ (для обраних доріжок):")
print("=" * 70)

for station in selected_stations:
    # Групуємо за місяцями та обчислюємо середнє
    monthly_avg = df.groupby('Month')[station].mean()

    print(f"\nВелодоріжка: {station}")
    for month, avg in monthly_avg.items():
        print(f"  {month_names[month]}: {avg:.1f} велосипедистів/день")
