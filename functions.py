def get_todos(filepath= 'todos.txt'):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos( todos_local, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print("Hello")
    cc=[i.strip('\n') for i in get_todos()]
    print(cc)