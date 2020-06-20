import PySimpleGUI as sg

layout = [[sg.Text('Please enter table name')],
[sg.InputText('This is my text')],


    [sg.Text('csv file')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Filename')],
          [sg.ReadFormButton('Insert'), sg.ReadFormButton('Update')]
]

button, (number,) = sg.FlexForm('Get filename example').Layout(layout).Read()

button, (number,) = sg.FlexForm('Get other example').Layout(layout).Read()