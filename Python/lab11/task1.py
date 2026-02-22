# Імпортуємо необхідні бібліотеки
import pandas as pd

# --- 1. Вихідний словник з лабораторної роботи №5 ---
# Доповнимо його новими записами та додамо нову характеристику "Кількість продажів"
cars_data = {
    "Toyota Camry": {"price": 25000, "age": 3, "sales": 120},
    "Honda Civic": {"price": 22000, "age": 2, "sales": 150},
    "Ford Focus": {"price": 18000, "age": 8, "sales": 80},
    "BMW X5": {"price": 55000, "age": 5, "sales": 45},
    "Mercedes C-Class": {"price": 45000, "age": 7, "sales": 60},
    "Audi A4": {"price": 35000, "age": 10, "sales": 55},
    "Volkswagen Golf": {"price": 20000, "age": 9, "sales": 110},
    "Tesla Model 3": {"price": 42000, "age": 1, "sales": 200},
    "Hyundai Tucson": {"price": 28000, "age": 4, "sales": 95},
    "Nissan Qashqai": {"price": 23000, "age": 6, "sales": 70},
    # Нові записи
    "Mazda CX-5": {"price": 32000, "age": 8, "sales": 65},
    "Peugeot 3008": {"price": 27000, "age": 5, "sales": 55}
}

# --- 2. Перетворення словника на DataFrame ---
# Трансформуємо вкладений словник у DataFrame
df = pd.DataFrame.from_dict(cars_data, orient='index')

# Скидаємо індекс, щоб назва моделі стала окремою колонкою
df.reset_index(inplace=True)
df.rename(columns={'index': 'model'}, inplace=True)

# Виводимо вміст DataFrame
print("Вміст датафрейму:")
print(df)
print("\n" + "="*50 + "\n")

# --- 3. Базовий аналіз даних ---

# 3.1 Виведіть перші 3 рядки
print("Перші 3 рядки:")
print(df.head(3))
print("\n" + "="*50 + "\n")

# 3.2 Перевірте типи даних
print("Типи даних:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# 3.3 Визначте кількість рядків і стовпців
print("Кількість рядків і стовпців (shape):")
print(df.shape)
print("\n" + "="*50 + "\n")

# 3.4 Отримайте описову статистику
print("Описова статистика:")
print(df.describe())
print("\n" + "="*50 + "\n")

# --- 4. Додайте новий стовпець (розрахункові значення) ---
# Додамо колонку "total_value" (загальна вартість усіх продажів моделі)
df['total_sales_value'] = df['price'] * df['sales']

print("Датафрейм з новою колонкою 'total_sales_value':")
print(df.head())
print("\n" + "="*50 + "\n")

# --- 5. Фільтрація даних ---
# Виберемо автомобілі з ціною понад 30 000 (умовно, замість гривень використаємо долари)
expensive_cars = df[df['price'] > 30000]
print("Автомобілі з ціною понад 30 000 $:")
print(expensive_cars)
print("\n" + "="*50 + "\n")

# --- 6. Сортування даних ---
# Сортуємо за спаданням ціни
sorted_df = df.sort_values(by='price', ascending=False)
print("Сортування за спаданням ціни:")
print(sorted_df[['model', 'price', 'age', 'sales', 'total_sales_value']])
print("\n" + "="*50 + "\n")

# --- 7. Групування даних та знаходження середнього ---
# Згрупуємо автомобілі за категоріями "вік" (наприклад, до 3 років, 4-7, 8+)
bins = [0, 3, 7, 20]
labels = ['New (0-3 yrs)', 'Medium (4-7 yrs)', 'Old (8+ yrs)']
df['age_category'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)

# Середня ціна за категоріями віку
grouped_mean = df.groupby('age_category')['price'].mean()
print("Середня ціна за категоріями віку:")
print(grouped_mean)
print("\n" + "="*50 + "\n")

# --- 8. Додаткові операції агрегації ---

# 8.1 Максимальна сума продажів у категорії
max_total_sales_by_category = df.groupby('age_category')['total_sales_value'].max()
print("Максимальна загальна сума продажів у кожній категорії віку:")
print(max_total_sales_by_category)
print("\n" + "="*50 + "\n")

# 8.2 Кількість унікальних моделей
unique_models_count = df['model'].nunique()
print(f"Кількість унікальних моделей: {unique_models_count}")
print("\n" + "="*50 + "\n")

# Додатково: унікальні значення цін (кількість унікальних цін)
unique_prices = df['price'].nunique()
print(f"Кількість унікальних цін: {unique_prices}")
