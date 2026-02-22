n = int(input("n = "))

print(f"Enter {n} array elements:")

arr = [int(input()) for _ in range(n)]

print("Original array: ", arr)

# Створюємо список від'ємних елементів у зворотному порядку
negative_reversed = [num for num in arr if num < 0][::-1]

if negative_reversed:
    print("Negative elements in reverse order: ", negative_reversed)
else:
    print("No negative elements in the array.")
