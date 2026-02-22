import math

print("Таблиця значень квадратних коренів чисел з діапазону [100..1]")
print(f"{'Число':<10} {'Корінь':<15}")
print("-" * 25)

for number in range(100, 0, -1):
    square_root = math.sqrt(number)
    print(f"{number:<10} {square_root:<15.6f}")
