def get_text():
    with open("page.html", "r", encoding="utf-8") as f:
        return f.read()

def build_frequency_dict(text):
    frequencies = {}
    words = text.split()

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies

def main():
    words_file = "words.txt"

    words_to_count = []
    with open(words_file, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            if word:
                words_to_count.append(word)

    text = get_text()
    frequency_dict = build_frequency_dict(text)

    result = {}
    for word in words_to_count:
        result[word] = frequency_dict.get(word, 0)

    print(result)

if __name__ == "__main__":
    main()
