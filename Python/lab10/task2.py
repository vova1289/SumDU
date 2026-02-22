import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Роки для аналізу (2000-2020)
x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
     2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# Умовні дані для України (тисяч дітей)
ukraine_data = [
    125.4, 118.7, 112.3, 105.8, 98.2, 92.5, 87.3, 82.1, 78.5, 75.2,
    72.8, 70.5, 68.9, 67.3, 65.8, 64.2, 62.7, 61.3, 59.8, 58.5, 120.1  # Різкий стрибок у 2020 через пандемію
]

# Умовні дані для Польщі (тисяч дітей)
poland_data = [
    45.2, 42.8, 40.3, 38.1, 36.2, 34.5, 32.9, 31.4, 30.1, 28.9,
    27.8, 26.7, 25.9, 25.2, 24.6, 24.1, 23.7, 23.4, 23.1, 22.9, 35.6   # Збільшення у 2020 через пандемію
]

# Конвертація в numpy arrays
years = np.array(x)
ukraine = np.array(ukraine_data)
poland = np.array(poland_data)

print("=" * 70)
print("АНАЛІЗ ДАНИХ: ДІТИ ПОЗА ШКОЛОЮ (ПОЧАТКОВА ОСВІТА)")
print("=" * 70)
print(f"Період: {years[0]} - {years[-1]} роки")
print(f"Країни: Україна та Польща")
print("\nДані для України (тис. осіб):")
for year, value in zip(years, ukraine):
    print(f"{year}: {value:.1f}")
print("\nДані для Польщі (тис. осіб):")
for year, value in zip(years, poland):
    print(f"{year}: {value:.1f}")
print("=" * 70)

# 2.1. Побудова графіків динаміки для двох країн
plt.figure(figsize=(14, 6))

# Графік 1: Лінійні графіки динаміки
plt.subplot(1, 2, 1)
plt.plot(years, ukraine, label='Україна', color='blue', linewidth=2.5, marker='o', markersize=4)
plt.plot(years, poland, label='Польща', color='red', linewidth=2.5, marker='s', markersize=4)

plt.title('Діти поза школою (початкова освіта)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Рік', fontsize=12, color='darkblue')
plt.ylabel('Кількість (тис. осіб)', fontsize=12, color='darkblue')
plt.legend(fontsize=11, loc='upper right')
plt.grid(True, alpha=0.3, linestyle='--')

# Додаємо позначку для 2020 року (пандемія)
plt.annotate('Пандемія COVID-19', xy=(2020, 120), xytext=(2015, 130),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.xticks(years[::2], rotation=45)
plt.tight_layout()

# 2.2. Побудова стовпчастих діаграм
plt.subplot(1, 2, 2)

# Меню для вибору країни
print("\n" + "=" * 70)
print("ВИБІР КРАЇНИ ДЛЯ СТОВПЧАСТОЇ ДІАГРАМИ")
print("=" * 70)
print("Доступні країни: Україна, Польща")
print("=" * 70)

country_choice = "Україна"  # Можна змінити на "Польща"
print(f"Обрана країна: {country_choice}")

if country_choice.lower() in ["україна", "ukraine"]:
    data_to_plot = ukraine
    country_name = 'Україна'
    color = 'blue'
    bar_width = 0.7
elif country_choice.lower() in ["польща", "poland"]:
    data_to_plot = poland
    country_name = 'Польща'
    color = 'red'
    bar_width = 0.7
else:
    print("Країна не знайдена. Буде побудовано для України.")
    data_to_plot = ukraine
    country_name = 'Україна'
    color = 'blue'
    bar_width = 0.7

# Побудова стовпчастої діаграми
bars = plt.bar(years, data_to_plot, color=color, alpha=0.7,
               edgecolor='black', linewidth=1, width=bar_width)

# Додавання значень на стовпці
for bar, value in zip(bars, data_to_plot):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{value:.1f}', ha='center', va='bottom', fontsize=8, rotation=90)

plt.title(f'Діти поза школою: {country_name}', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Рік', fontsize=12, color='darkblue')
plt.ylabel('Кількість (тис. осіб)', fontsize=12, color='darkblue')
plt.grid(True, alpha=0.3, axis='y', linestyle='--')
plt.xticks(years[::2], rotation=45)

# Додаємо горизонтальну лінію для середнього значення
mean_value = np.mean(data_to_plot)
plt.axhline(y=mean_value, color='green', linestyle=':', linewidth=2, alpha=0.7)
plt.text(years[-1] + 0.5, mean_value, f'Середнє: {mean_value:.1f}',
         va='center', ha='left', color='green', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# Додаткова аналітична інформація
print("\n" + "=" * 70)
print("АНАЛІТИЧНА ІНФОРМАЦІЯ")
print("=" * 70)
print(f"Україна:")
print(f"  - Максимум: {np.max(ukraine):.1f} тис. ({years[np.argmax(ukraine)]} р.)")
print(f"  - Мінімум: {np.min(ukraine):.1f} тис. ({years[np.argmin(ukraine)]} р.)")
print(f"  - Середнє: {np.mean(ukraine):.1f} тис.")
print(f"  - Зміна за період: {((ukraine[-1] - ukraine[0]) / ukraine[0] * 100):.1f}%")
print(f"  - Тенденція: {'зниження' if ukraine[-1] < ukraine[0] else 'зростання'}")
print(f"\nПольща:")
print(f"  - Максимум: {np.max(poland):.1f} тис. ({years[np.argmax(poland)]} р.)")
print(f"  - Мінімум: {np.min(poland):.1f} тис. ({years[np.argmin(poland)]} р.)")
print(f"  - Середнє: {np.mean(poland):.1f} тис.")
print(f"  - Зміна за період: {((poland[-1] - poland[0]) / poland[0] * 100):.1f}%")
print(f"  - Тенденція: {'зниження' if poland[-1] < poland[0] else 'зростання'}")
print(f"\nПорівняння:")
print(f"  - Співвідношення (Україна/Польща) у 2020: {ukraine[-1]/poland[-1]:.1f}")
print(f"  - Різниця середніх значень: {np.mean(ukraine) - np.mean(poland):.1f} тис.")
print("=" * 70)
