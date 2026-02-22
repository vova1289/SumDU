def calculate_x():
    print("Обчислення значення X")
    print("=====================")

    try:
        a = float(input("Введіть значення a: "))
        b = float(input("Введіть значення b: "))

        if a < 1 or a > 100 or b < 1 or b > 100:
            print("Помилка: значення a та b повинні бути в діапазоні від 1 до 100")
            return

        if a < b:
            X = b / a + 1
        elif a == b:
            X = 2.5
        else:
            X = (a ** 3 - 5) / b

        print(f"\nРезультат обчислення:")
        print(f"a = {a}, b = {b}")
        print(f"X = {X:.4f}")

        if a < b:
            print(f"Використано формулу: b/a + 1 = {b}/{a} + 1 = {X:.4f}")
        elif a == b:
            print("Використано формулу: X = 2.5")
        else:
            print(f"Використано формулу: (a³ - 5)/b = ({a}³ - 5)/{b} = {X:.4f}")

    except ValueError:
        print("Помилка: будь ласка, введіть коректні числові значення")
    except ZeroDivisionError:
        print("Помилка: ділення на нуль неможливе")


def calculate_x_with_loop():
    print("Обчислення значення X (з циклом)")
    print("================================")

    while True:
        try:
            print("\n" + "=" * 40)
            a = float(input("Введіть значення a (або 0 для виходу): "))

            if a == 0:
                print("Програма завершена.")
                break

            b = float(input("Введіть значення b: "))

            if a < 1 or a > 100 or b < 1 or b > 100:
                print("Помилка: значення повинні бути в діапазоні від 1 до 100")
                continue

            if a < b:
                X = b / a + 1
            elif a == b:
                X = 2.5
            else:
                X = (a ** 3 - 5) / b

            print(f"\nРезультат: a={a}, b={b}, X={X:.4f}")

        except ValueError:
            print("Помилка: введіть коректні числові значення")
        except ZeroDivisionError:
            print("Помилка: ділення на нуль")


def main():
    print("Виберіть режим роботи:")
    print("1 - Один раз")
    print("2 - З циклом (багаторазово)")

    choice = input("Ваш вибір (1 або 2): ")

    if choice == "1":
        calculate_x()
    elif choice == "2":
        calculate_x_with_loop()
    else:
        print("Невірний вибір. Запуск режиму за замовчуванням.")
        calculate_x()


if __name__ == "__main__":
    main()

