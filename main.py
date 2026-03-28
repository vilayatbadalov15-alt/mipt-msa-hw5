import requests

def get_text(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def count_word_frequencies(text, word):
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    words_to_count = []
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                words_to_count.append(word)

    try:
        text = get_text(url)
    except requests.exceptions.RequestException as error:
        print(f"Не удалось загрузить страницу {url}: {error}")
        return

    frequencies = {}
    for word in words_to_count:
        frequencies[word] = count_word_frequencies(text, word)

    print(frequencies)

if __name__ == "__main__":
    main()