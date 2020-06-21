import PySimpleGUI as sg
import sys


class GuiWrapper:
    def __init__(self):
        self.action = None
        self._window = None
        self._table = "table"
        self._csv_file = None

    def _get_window(self):
        return self.window

    def _get_table(self):
        return self._table

    def _set_table(self, table):
        self._table = table

    def _get_csv_file(self):
        return self._csv_file

    def _set_csv_file(self, file):
        self._csv_file = file

    def set_action(self, action):
        self.action = action

    def get_action(self):
        return self.action
    
    def set_final_values(self, window, values, *args):
        self._set_table(values["-IN-"])
        self._set_csv_file(values[0])
        window["-OUTPUT-"].update(values["-IN-"])
    
    def update_action(self, window, values, event):
        window["-OUTPUT-"].update(values["-IN-"])
        self.set_action(event)

    def logic_loop(self):
        self._set_window()
        switch_statment = {
            "Display": self.set_final_values,
            "Insert": self.update_action,
            "Update": self.update_action,
        }
        window = self._get_window()

        while True:
            event, values = window.read()
            apply_switch = switch_statment.get(event, "404")
            apply_switch(window, values, event)

    def _set_window(self):
        self.window = self.initalize_runner()

    def initalize_runner(self):
        sg.theme("BluePurple")
        layout = [
            [sg.Text("CSV File", size=(8, 1)), sg.InputText(), sg.FileBrowse()],
            [sg.Button("Insert"), sg.Button("Update")],
            [
                sg.Text("Replace your table below if necessary:"),
                sg.Text(size=(15, 1), key="-OUTPUT-"),
            ],
            [sg.Input("Table", key="-IN-")],
            [sg.Button("Display"), sg.Button("Exit")],
        ]
        # window
        return sg.Window("Introduction", layout)


if __name__ == "__main__":
    gui = GuiWrapper()
    gui._set_window()
    window = gui._get_window()
    gui.logic_loop()