import json
import subprocess

subprocess.run("clear")

#Constants
Headers = ["word", "translation"]
Hello_message = "Hello! It's your dictionary"
Help_message = "Press 'F' to get help"
Header_format = "{:<30} {:<30}"
Enc_inp_message = f"\nEnccorect input. Press 'f' to get help.\n"
Help_message = """
add <word> <translation>
get <word>
r <word> (remove)
'q' - quit programm
't' - get table"""
Centered_help_message = "\n".join(line.center(80) for line in Help_message.splitlines())


print("\n", Hello_message.center(80))
print(Centered_help_message.center(80))

def encorrect_input():
    print(Enc_inp_message)

def rm_funct(word):
    with open("dict.txt", 'r') as file_dict:
        main_dict = json.load(file_dict)
        if main_dict.pop(word, 'bobr') == 'bobr':
            print(f"Value '{word}' does't exist")
        else:
            with open("dict.txt", "w") as file_dict:
                json.dump(main_dict, file_dict)
            

def get_table(Headers, Header_format):
    row_format = "{:<30} {:<30}"
    
    print()
    print(Header_format.format(*Headers))
    print('-' * 60)
    with open("dict.txt", "r") as file_dict:
        main_dict = json.load(file_dict)
        for word, translation in main_dict.items():
            print(row_format.format(word, translation))
        print()

def add_funct(word, translation):
    with open("dict.txt", "r") as file_dict:
        main_dict = json.load(file_dict)
        main_dict[word] = translation
    with open("dict.txt", "w") as file_dict:
        json.dump(main_dict, file_dict)


def get_funct(word):
    with open("dict.txt", "r") as file_dict:
        main_dict = json.load(file_dict)
        print(f"\n{word} | {main_dict.get(word)}\n") 
    
def get_help():
    print(Help_message.center(80))

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
    elif enter[0] == 'r':
        rm_funct(enter[1])
    else:
        encorrect_input()



