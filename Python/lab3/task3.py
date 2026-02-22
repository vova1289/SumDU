z = str(input("Введіть речення: "))

words = z.split()          # розбиваємо речення на слова
words.sort(key=len)        # сортуємо за довжиною слова

print("Слова в порядку неспадання довжин:")
print(words)
