main_dict = dict() #make dict in saved file

print("\n", "Hello! It's your dictionary".center(80))
print("Press 'F' to get help".center(80))

def get_table(main_dict):
    headers = ["word", "translation"]
    header_format = "{:<30} {:<30}"
    row_format = "{:<30} {:<30}"
    
    print()
    print( header_format.format(*headers))
    print('-' * 60)
    for word, translate in main_dict.items():
        print(row_format.format(word, translate))


def add_funct(word, translate, main_dict):
    main_dict[word] = translate
    print(main_dict)

def get_funct(word, main_dict):
    print(f"word | {main_dict[word]}")
    
def get_help():
    print("\n", "add <word> <translate>".center(80),
          "get <word>".center(80),
          "'q' - quit programm".center(80),
          "'t' - get table".center(80))

while True:
    enter = input().lower().split()
    if enter[0] == "add":
        add_funct(enter[1], enter[2], main_dict)
    elif enter[0] == "get":
        get_funct(enter[1], main_dict)
    elif enter[0] == "f":
        get_help()
    elif enter[0] == "t":
        get_table(main_dict)
    elif enter[0] == 'q':
        break
    else:
        enncorrect_input()



