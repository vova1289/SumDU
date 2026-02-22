import matplotlib.pyplot as plt
import numpy as np
import warnings

# Ігноруємо попередження про ділення на нуль та інші числові помилки
warnings.filterwarnings('ignore')

# Створення масиву значень x
x = np.linspace(0.1, 8, 1000)  # Починаємо з 0.1, щоб уникнути ділення на 0

# Обчислення значень функції Y(x) = 5 * sin(10*x) * sin(3*x) / (x^x)
# Обережно обчислюємо x^x, оскільки 0^0 не визначено
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    y = 5 * np.sin(10 * x) * np.sin(3 * x) / (x ** x)

# Побудова графіка
plt.figure(figsize=(12, 8))

# Використовуємо суцільну лінію, синій колір, товщину 2.5
plt.plot(x, y, label='y = 5·sin(10x)·sin(3x) / xˣ',
         color='blue', linewidth=2.5, linestyle='-')

# Налаштування графіка
plt.title('Графік функції y = 5·sin(10x)·sin(3x) / xˣ',
          fontsize=16, fontweight='bold', pad=20)

plt.xlabel('x', fontsize=14, color='darkred', labelpad=10)
plt.ylabel('y', fontsize=14, color='darkred', labelpad=10)

# Додаємо легенду
plt.legend(loc='upper right', fontsize=12, framealpha=0.9)

# Налаштування сітки
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Встановлюємо межі осей
plt.xlim(0, 8)
plt.ylim(min(y) * 1.1, max(y) * 1.1)

# Додаємо горизонтальну лінію y=0 для кращої орієнтації
plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)

# Додаємо вертикальну лінію x=0 для кращої орієнтації
plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)

# Покращуємо відображення підписів на осях
plt.xticks(np.arange(0, 9, 1))
plt.yticks(np.arange(-6, 7, 1))

# Додаємо інформацію про функцію
plt.figtext(0.5, 0.01,
            'Функція: y = 5·sin(10x)·sin(3x) / xˣ | Область визначення: x ∈ [0, 8]',
            ha='center', fontsize=11, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.5))

# Автоматичне налаштування розміщення елементів
plt.tight_layout()

# Відображення графіка
plt.show()

# Додатково: виведення інформації про функцію
print("=" * 60)
print("ІНФОРМАЦІЯ ПРО ФУНКЦІЮ:")
print("=" * 60)
print(f"Функція: y = 5·sin(10x)·sin(3x) / xˣ")
print(f"Область визначення: x ∈ [0, 8]")
print(f"Кількість точок для побудови: {len(x)}")
print(f"Мінімальне значення y: {min(y):.4f}")
print(f"Максимальне значення y: {max(y):.4f}")
print(f"Значення при x=1: {5*np.sin(10)*np.sin(3):.4f}")
print("=" * 60)
