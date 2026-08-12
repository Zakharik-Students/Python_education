main_dict = dict() #make dict in saved file

print("\n", "Hello! It's your dictionary".center(80))
print("Press 'F' to get help".center(80))

def add_funct(word, translate, main_dict):
    main_dict[word] = translate
    print(main_dict)

def get_funct(word, main_dict):
    print(f"word | {main_dict[word]}")
    
def get_help():
    print("\n", "add <word> <translate>".center(80),
          "get <word>".center(80),
          "'q' - quit programm".center(80))

while True:
    enter = input().lower().split()
    if enter[0] == "add":
        add_funct(enter[1], enter[2], main_dict)
    elif enter[0] == "get":
        get_funct(enter[1], main_dict)
    elif enter[0] == "f":
        get_help()
    elif enter[0] == 'q':
        break
    else:
        enncorrect_input()



