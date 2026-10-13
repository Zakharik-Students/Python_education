def word_frequency(text: str) -> dict:
    counts = {}
    for token in text.split():
        word = token.lower().strip('.,!?')
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    text = input('Text:')
    print(word_frequency(text))

