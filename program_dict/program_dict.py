import json

#Constants
Headers = ["word", "translation"]
Hello_message = "Hello! It's your dictionary"
Help_message = "Press 'F' to get help"
Header_format = "{:<30} {:<30}"


print("\n", Hello_message.center(80))
print(Help_message.center(80))

def get_table(Headers, Header_format):
    row_format = "{:<30} {:<30}"
    
    print()
    print(Header_format.format(*Headers))
    print('-' * 60)
    with open("dict.txt", "r") as file_dict:
        main_dict = json.load(file_dict)
        for word, translation in main_dict.items():
            print(row_format.format(word, translation))


def add_funct(word, translation):
    with open("dict.txt", "r") as file_dict:
        main_dict = json.load(file_dict)
        main_dict[word] = translation
    with open("dict.txt", "w") as file_dict:
        json.dump(main_dict, file_dict)


def get_funct(word):
    with open("dict.txt", "r") as file_dict:
        main_dict = json.load(file_dict)
        print(f"word | {main_dict.get(word)}") 
    
def get_help():
    print("\n", "add <word> <translation>".center(80),
          "get <word>".center(80),
          "'q' - quit programm".center(80),
          "'t' - get table".center(80))

while True:
    enter = input().lower().split()
    if enter[0] == "add":
        add_funct(enter[1], enter[2])
    elif enter[0] == "get":
        get_funct(enter[1])
    elif enter[0] == "f":
        get_help()
    elif enter[0] == "t":
        get_table(Headers, Header_format)
    elif enter[0] == 'q':
        break
    else:
        enncorrect_input()



