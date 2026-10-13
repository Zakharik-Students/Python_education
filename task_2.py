from task_1 import word_frequency

try:
    with open('text.txt', 'r') as file:
        text = file.read()
        dict_of_words = word_frequency(text)

    sorted_dict = dict(sorted(dict_of_words.items(), key=lambda item: item[1], reverse=True))

    with open("top_words.txt", 'w') as file:
        count = 0
        for word, number in sorted_dict.items():
            file.write(f"{word} - {number}\n")
            count += 1
            if count == 5:
                break

except FileNotFoundError:
    print("File not was found. Check this...")

    
