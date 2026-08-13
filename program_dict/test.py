import json

data = dict(word='слово')

with open("dict.txt", "w") as file:
    json.dump(data, file)

with open("dict.txt", "r") as file:
    dictionary = json.load(file)
    dictionary["dog"] =  "sobaka"
    print(dictionary)
