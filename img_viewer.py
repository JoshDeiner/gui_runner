import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    button, (fname,) = sg.FlexForm('My Script').Layout([[sg.T('Document to open').Read()],
                                                           [sg.In(), sg.FileBrowse()],
                                                           [sg.Open(), sg.Cancel()]])
else:
    fname = sys.argv[1]

if not fname:
    sg.Popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
