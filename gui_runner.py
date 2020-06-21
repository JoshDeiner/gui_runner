import PySimpleGUI as sg
import sys


class GuiWrapper:
    def __init__(self):
        self.action: str = ""
        self._table: str = "table"
        self._csv_file: str = ""

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

    def validate_prop_vals(self):
        if not (
            len(self._get_csv_file()) 
            or self.validate_csv(self._get_csv_file())
            ):
            self.raise_error("file")
        elif not len(self.get_action()):
            self.raise_error("action")
        elif not len(self._get_table()):
            self.raise_error("table")
        else:
            print("start program")

    def raise_error(self, *args):
        sg.Popup("Please run again", f"failed because of {args}")
        raise SystemExit(
            f"Please re input information, the failed attributes are: {args}"
        )

    def completion_popup(self):
        # will remove from this file eventually
        import PySimpleGUI as sg

        sg.Popup("completed program", "finished")
        raise SystemExit("Done")

    def validate_csv(self, file):
        return file.split(".")[-1] == "csv"

    def logic_loop(self):
        switch_statment = {
            "Display": self.set_final_values,
            "Insert": self.update_action,
            "Update": self.update_action,
            "Delete": self.update_action,
        }
        window = self.initalize_runner()

        while True:
            event, values = window.read()
            apply_switch = switch_statment.get(event, "404")
            apply_switch(window, values, event)
            print(self.action)
            print(self._get_csv_file().split(".")[-1])

            print(self._get_table())

    def initalize_runner(self):
        sg.theme("BluePurple")
        layout = [
            [sg.Text("CSV File", size=(8, 1)), sg.InputText(), sg.FileBrowse()],
            [sg.Button("Insert"), sg.Button("Update"), sg.Button("Delete")],
            [
                sg.Text("Replace your table below if necessary:"),
                sg.Text(size=(15, 1), key="-OUTPUT-"),
            ],
            [sg.Input("Table", key="-IN-")],
            [sg.Button("Display"), sg.Button("Exit")],
        ]
        # window
        return sg.Window("Parser", layout)


if __name__ == "__main__":
    gui = GuiWrapper()
    gui.logic_loop()
