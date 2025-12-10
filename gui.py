import functions
import FreeSimpleGUI as sg
import time


sg.theme('Black')

clock=sg.Text('',key='clock')
label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip= "Enter to-do", key="To-do")
add_button = sg.Button("Add",size=10)
list_box=sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
completed_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

stacked=sg.Column([[edit_button],
                   [completed_button]])


window =sg.Window("My To-do App",
                  layout=[[clock],
                          [label],
                          [input_box, add_button],
                          [list_box,stacked],
                          [exit_button]],
                  font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b-%d-%y : %H:%M:%S"))
    '''print(event)
    print(values)'''
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos= values['To-do'].rstrip("\n")  + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todos = values['To-do'] + "\n"

                todos = functions.get_todos()
                index =todos.index(todo_to_edit)
                todos[index] = new_todos.rstrip("\n") + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Select something to edit first")

        case 'Complete':
            try:
                completed_todos = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(completed_todos)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["To-do"].update(value='')
            except IndexError:
                sg.popup("Select something to complete first")

        case "Exit":
            break

        case "todos":
            try:
                window["To-do"].update(value=values['todos'][0])
            except IndexError:
                pass

        case sg.WIN_CLOSED:
            break

window.close()