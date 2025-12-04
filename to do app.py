from functions import get_todos,write_todos

while True:
    user_input = input("Type add, show, edit,complete or exit: ")
    user_input = user_input.strip()

    #changed match-case
    if user_input.startswith("add"):
        todo = user_input[4:]

        #file=open('todos.txt','r')
        #todos=file.readlines()
        #file.close()

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
        #file= open('todos.txt','w')
        #file.writelines(todos)
        #file.close()

    elif user_input.startswith("show"):
        todos = get_todos()

        #new_todos=[item.strip("\n") for item in todos]

        for index, items in enumerate(todos):
            row = f"{index + 1}-{items.strip()}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Type your new todo:")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Invalid command: Edit a number instead")

    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])
            number = number - 1

            todos = get_todos()

            todo_to_remove = todos[number]

            todos.pop(number)

            write_todos(todos)

            print(f'Todo {todo_to_remove.strip('\n')} has been removed.')
        except IndexError:
            print("There is no item with that number.")

    elif user_input.startswith("exit"):
        break
    else:
        print("You have entered the wrong input")
print("Bye")
