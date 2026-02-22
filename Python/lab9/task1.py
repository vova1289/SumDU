import csv


def main():
    input_file = "API_SP.csv"
    output_file = "ukraine_life_expectancy_results.csv"

    print("=" * 80)
    print("ПРОГРАМА ДЛЯ АНАЛІЗУ ОЧІКУВАНОЇ ТРИВАЛОСТІ ЖИТТЯ В УКРАЇНІ")
    print("=" * 80)

    try:
        # Відкриваємо файл
        with open(input_file, "r", encoding="utf-8") as file:
            # Читаємо всі рядки
            lines = file.readlines()

            # Знаходимо рядок з заголовками (шукаємо рядок, де є "1960")
            header_line = None
            for line in lines:
                if '"1960"' in line and '"1961"' in line:
                    header_line = line
                    break

            if not header_line:
                # Якщо не знайшли, беремо другий рядок
                header_line = lines[1] if len(lines) > 1 else lines[0]

            print(f"\nЗаголовки знайдено: {header_line[:100]}...")

            # Розбираємо заголовки
            reader = csv.reader([header_line])
            headers = next(reader)
            # Видаляємо зайві пробіли та лапки
            headers = [h.strip().strip('"') for h in headers]

            # Знаходимо рядок з даними для України
            ukraine_line = None
            for line in lines:
                if 'Ukraine' in line or '"UKR"' in line:
                    ukraine_line = line
                    break

            if not ukraine_line:
                print("\nПОМИЛКА: Не знайдено дані для України!")
                return

            print(f"\nЗнайдено дані для України!")

            # Розбираємо рядок з даними України
            reader = csv.reader([ukraine_line])
            ukraine_data = next(reader)
            ukraine_data = [d.strip().strip('"') for d in ukraine_data]

            # Створюємо словник: заголовок -> значення
            data_dict = {}
            for i in range(min(len(headers), len(ukraine_data))):
                data_dict[headers[i]] = ukraine_data[i]

            print(f"\nКраїна: {data_dict.get('Country Name', 'Ukraine')}")
            print(f"Показник: {data_dict.get('Indicator Name', 'Life expectancy at birth, total (years)')}")

            # Збираємо дані за 1991-2019 роки
            years_data = []

            for year in range(1991, 2020):
                year_str = str(year)
                if year_str in data_dict:
                    value_str = data_dict[year_str]
                    if value_str and value_str != '':  # перевіряємо, чи не порожнє
                        try:
                            value = float(value_str)
                            years_data.append((year_str, value))
                        except ValueError:
                            print(f"Увага: некоректне значення для {year}: '{value_str}'")
                            continue

            if not years_data:
                print("\nПОМИЛКА: Не знайдено даних за період 1991-2019!")
                print("\nДоступні роки у даних:")
                available_years = []
                for key in data_dict.keys():
                    if key.isdigit() and 1960 <= int(key) <= 2024:
                        available_years.append(int(key))
                available_years.sort()
                print(f"Роки: {available_years}")
                return

            # Знаходимо мінімальне та максимальне значення
            min_year, min_value = min(years_data, key=lambda x: x[1])
            max_year, max_value = max(years_data, key=lambda x: x[1])

            print(f"\nРЕЗУЛЬТАТИ АНАЛІЗУ:")
            print("-" * 50)
            print(f"Період: 1991-2019")
            print(f"Кількість років з даними: {len(years_data)}")
            print(f"Мінімальне значення: {min_value:.3f} років (у {min_year} році)")
            print(f"Максимальне значення: {max_value:.3f} років (у {max_year} році)")

            # Виводимо всі значення
            print(f"\nВсі значення за період 1991-2019:")
            print("-" * 30)
            for year, value in sorted(years_data):
                print(f"{year}: {value:.3f}")

            # Зберігаємо результати у файл
            try:
                with open(output_file, "w", newline="", encoding="utf-8") as out_file:
                    writer = csv.writer(out_file)

                    # Заголовки
                    writer.writerow([
                        "Показник",
                        "Країна",
                        "Період",
                        "Мінімальне значення",
                        "Рік мінімуму",
                        "Максимальне значення",
                        "Рік максимуму"
                    ])

                    # Дані
                    writer.writerow([
                        data_dict.get('Indicator Name', 'Life expectancy at birth, total (years)'),
                        data_dict.get('Country Name', 'Ukraine'),
                        "1991-2019",
                        f"{min_value:.3f}",
                        min_year,
                        f"{max_value:.3f}",
                        max_year
                    ])

                print(f"\n✓ Результати збережено у файл: {output_file}")

                # Виводимо вміст створеного файлу
                print("\n" + "=" * 80)
                print("ВМІСТ СТВОРЕНОГО ФАЙЛУ:")
                print("=" * 80)
                with open(output_file, "r", encoding="utf-8") as result_file:
                    for line in result_file:
                        print(line.strip())

            except Exception as e:
                print(f"\nПОМИЛКА при записі у файл: {e}")

    except FileNotFoundError:
        print(f"\n✗ ПОМИЛКА: Файл {input_file} не знайдено!")
        print("Переконайтеся, що файл знаходиться в тій самій папці.")
    except Exception as e:
        print(f"\n✗ ПОМИЛКА: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
