def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


# Назви файлів
file1_name = "TF15_1.txt"
file2_name = "TF15_2.txt"

# Частина а) Створення файлу TF15_1
file_1_w = Open(file1_name, "w")
if file_1_w != None:
    file_1_w.write("Анна знайшла слова: радар, шалаш, топот, машина.\n")
    file_1_w.write("Слова 'казак', 'довод' теж симетричні.\n")
    file_1_w.write("Ротор та потоп - паліндроми, а комп'ютер - ні.")
    print("Інформацію записано у файл TF15_1.txt!")
    file_1_w.close()

# Частина б) Читання TF15_1, пошук симетричних слів та запис у TF15_2
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r != None and file_2_w != None:
    content = file_1_r.read()

    # Розділяємо текст на слова (ігноруємо розділові знаки)
    import re

    words = re.findall(r'\b\w+\b', content)

    # Шукаємо симетричні слова
    symmetric_words = []
    for word in words:
        # Перевіряємо, чи слово складається лише з букв та чи воно симетричне
        if word.isalpha() and word.lower() == word.lower()[::-1]:
            symmetric_words.append(word)

    # Записуємо симетричні слова у TF15_2 через пробіл
    file_2_w.write(" ".join(symmetric_words))

    file_1_r.close()
    file_2_w.close()
    print("Симетричні слова записано у файл TF15_2.txt!")

# Частина в) Читання TF15_2 та вивід кожного слова в окремому рядку
print("\nВміст файлу TF15_2.txt (кожне слово в окремому рядку):")
file_2_r = Open(file2_name, "r")

if file_2_r != None:
    content = file_2_r.read()
    words = content.split()

    for i, word in enumerate(words, 1):
        print(f"{i}. {word}")

    file_2_r.close()
