import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip= "Enter to-do", key="To-do")
add_button = sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
completed_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

stacked=sg.Column([[edit_button],
                   [completed_button]])


window =sg.Window("My To-do App",
                  layout=[[label],
                          [input_box, add_button],
                          [list_box,stacked],
                          [exit_button]],
                  font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos= values['To-do'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todos = values['To-do'] + "\n"

            todos = functions.get_todos()
            index =todos.index(todo_to_edit)
            todos[index] = new_todos
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case 'Complete':
            completed_todos = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(completed_todos)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["To-do"].update(value='')

        case "Exit":
            break

        case "todos":
            window["To-do"].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()