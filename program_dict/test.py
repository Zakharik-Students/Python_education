import json
from os import system

system("toggle.fullscreen")

word = input()
translation = input()
data = {word: translation}

with open("dict.txt", "w") as file:
    json.dump(data, file)

with open("dict.txt", "r") as file:
    dictionary = json.load(file)
    dictionary["dog"] =  "sobaka"
    print(dictionary)
