def analyze_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = text.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        most_frequent_word = max(word_counts, key=word_counts.get)
        word_count = len(words)
    print(f"Количество слов в файле: {word_count}")
    print(f"Самое часто встречающееся слово: '{most_frequent_word}' ({word_counts[most_frequent_word]} раз)")
analyze_text_file("text.txt")
