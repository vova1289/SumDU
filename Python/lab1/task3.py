n = int(input("Введіть ціле число N (1 < N < 9): "))

if n <= 1 or n >= 9:
    print("Помилка: N повинно бути в діапазоні (1 < N < 9)")
else:
    print("\nВідзеркалений рисунок з числами:")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "".join(str(j) for j in range(i, 0, -1)))

    print("\nВідзеркалений рисунок з зірочками:")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)
