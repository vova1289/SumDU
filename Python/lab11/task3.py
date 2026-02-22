import nltk
import matplotlib.pyplot as plt
import string
from collections import Counter
import re

# Завантаження необхідних ресурсів NLTK (робимо один раз)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')

# --- 1. Завантаження тексту ---
# Читаємо файл edgeworth-parents.txt
with open('edgeworth-parents.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Видаляємо заголовок та інформацію про Project Gutenberg на початку та в кінці
# Знаходимо початок основного тексту
start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Знаходимо кінець рядка з маркером початку
    start_content = text.find('\n', start_idx) + 1
    text = text[start_content:end_idx].strip()

print("=" * 70)
print("ТЕКСТ УСПІШНО ЗАВАНТАЖЕНО")
print(f"Довжина тексту: {len(text)} символів")
print("=" * 70)
print("\n")

# --- 2. Визначення кількості слів у тексті ---
# Токенізація тексту на слова
words = nltk.word_tokenize(text.lower())  # переводимо в нижній регістр

# Фільтруємо тільки слова (видаляємо числа та окремі символи)
words_only = [word for word in words if word.isalpha()]

word_count = len(words_only)
print("=" * 70)
print(f"КІЛЬКІСТЬ СЛІВ У ТЕКСТІ: {word_count}")
print("=" * 70)
print("\n")

# --- 3. 10 найбільш вживаних слів без очищення ---
# Підрахунок частоти слів
word_freq = Counter(words_only)

# Топ-10 слів
top_10_raw = word_freq.most_common(10)

print("=" * 70)
print("ТОП-10 НАЙБІЛЬШ ВЖИВАНИХ СЛІВ (БЕЗ ОЧИЩЕННЯ):")
print("=" * 70)
for word, count in top_10_raw:
    print(f"{word}: {count}")

print("\n")

# Побудова стовпчастої діаграми для топ-10 слів (без очищення)
plt.figure(figsize=(12, 6))
words_raw, counts_raw = zip(*top_10_raw)
bars_raw = plt.bar(words_raw, counts_raw, color='skyblue', edgecolor='navy', alpha=0.7)

# Додаємо значення на стовпчики
for bar, count in zip(bars_raw, counts_raw):
    plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 5,
             str(count), ha='center', va='bottom', fontsize=10)

plt.xlabel('Слова', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.title('Топ-10 найбільш вживаних слів (без очищення)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('top_10_words_raw.png', dpi=300, bbox_inches='tight')
plt.show()

print("Графік збережено у файл 'top_10_words_raw.png'")
print("\n")

# --- 4. Видалення стоп-слів та пунктуації ---
# Отримуємо список англійських стоп-слів
stop_words = set(nltk.corpus.stopwords.words('english'))

# Додаємо додаткові стоп-слова, які часто зустрічаються в текстах
additional_stops = {'would', 'could', 'said', 'one', 'also', 'may', 'us', 'upon',
                    'though', 'yet', 'however', 'well', 'shall', 'must', 'might',
                    'thee', 'thou', 'thy', 'ye', 'thence', 'then', 'than', 'thus'}
stop_words.update(additional_stops)

# Фільтруємо слова: видаляємо стоп-слова та слова довжиною менше 3 символів
filtered_words = [word for word in words_only
                  if word not in stop_words and len(word) > 2]

# Підрахунок частоти слів після очищення
filtered_freq = Counter(filtered_words)

# Топ-10 слів після очищення
top_10_filtered = filtered_freq.most_common(10)

print("=" * 70)
print("ТОП-10 НАЙБІЛЬШ ВЖИВАНИХ СЛІВ (ПІСЛЯ ВИДАЛЕННЯ СТОП-СЛІВ):")
print("=" * 70)
for word, count in top_10_filtered:
    print(f"{word}: {count}")

print("\n")

# Побудова стовпчастої діаграми для топ-10 слів після очищення
plt.figure(figsize=(12, 6))
words_filtered, counts_filtered = zip(*top_10_filtered)
bars_filtered = plt.bar(words_filtered, counts_filtered, color='lightcoral', edgecolor='darkred', alpha=0.7)

# Додаємо значення на стовпчики
for bar, count in zip(bars_filtered, counts_filtered):
    plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 5,
             str(count), ha='center', va='bottom', fontsize=10)

plt.xlabel('Слова', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.title('Топ-10 найбільш вживаних слів (після видалення стоп-слів)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('top_10_words_filtered.png', dpi=300, bbox_inches='tight')
plt.show()

print("Графік збережено у файл 'top_10_words_filtered.png'")
print("\n")

# --- 5. Додатковий аналіз: порівняння результатів ---
print("=" * 70)
print("ПОРІВНЯННЯ РЕЗУЛЬТАТІВ:")
print("=" * 70)
print(f"{'Слово (без очищення)':<20} {'Частота':<10} | {'Слово (після очищення)':<20} {'Частота':<10}")
print("-" * 55)
for i in range(10):
    raw_word, raw_count = top_10_raw[i] if i < len(top_10_raw) else ("", "")
    filtered_word, filtered_count = top_10_filtered[i] if i < len(top_10_filtered) else ("", "")
    print(f"{raw_word:<20} {raw_count:<10} | {filtered_word:<20} {filtered_count:<10}")

print("\n")
print("=" * 70)
print(f"Кількість слів у тексті (всього): {word_count}")
print(f"Кількість слів після видалення стоп-слів: {len(filtered_words)}")
print(f"Відсоток слів, що залишились: {len(filtered_words)/word_count*100:.1f}%")
print("=" * 70)
