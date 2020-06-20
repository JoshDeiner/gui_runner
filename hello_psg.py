import PySimpleGUI as sg

layout = [[sg.Text("Hello From PySimpleGUI")], [sg.Button("OK")]]

# create window
window = sg.Window("Demo", layout)

# create event loop
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
