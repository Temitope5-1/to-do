import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do")
input = sg.InputText(tooltip= "Enter to-do")
add_button = sg.Button("Add")


window =sg.Window("My To-do App", layout=[[label], [input, add_button]])
window.read()
window.close()