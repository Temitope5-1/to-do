import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do")
input = sg.InputText(tooltip= "Enter to-do", key="To-do")
add_button = sg.Button("Add")


window =sg.Window("My To-do App",
                  layout=[[label],
                          [input, add_button]],
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
        case sg.WIN_CLOSED:
            break

window.close()