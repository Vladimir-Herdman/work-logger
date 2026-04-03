import webview
from webview.menu import Menu, MenuAction


class MainApi:
    """Called by javascript in frontend to execute python."""
    def __init__(self):
        self._window: webview.Window|None = None

    @property
    def window(self) -> webview.Window:
        assert self._window is not None
        return self._window
    @window.setter
    def window(self, win):
        self._window = win

    def menu_file_main(self):
        print("TODO: 'menu_file_main()' functionality")
    def menu_file_exit(self):
        self.window.destroy()

    def nullfunc(self, file:str) -> None:
        print(f"nullfunc called from file:{file.split("/")[-1]}")


def build_menu(api: MainApi):
    return [
        Menu(
            "File",
            [
                MenuAction("Main", api.menu_file_main),
                MenuAction("Exit", api.menu_file_exit),
            ],
        ),
        Menu(
            "Timekeeping",
            [
                MenuAction("Add Run", lambda: api.nullfunc(__file__)),
                MenuAction("Find/Delete Run", lambda: api.nullfunc(__file__)),
            ],
        ),
        Menu(
            "Employee Record",
            [
                MenuAction("Add Employee", lambda: api.nullfunc(__file__)),
                MenuAction("Find/Edit Employee", lambda: api.nullfunc(__file__)),
            ],
        ),
        Menu(
            "Positions",
            [
                Menu("Salaried", [
                    MenuAction("Add Position", lambda: api.nullfunc(__file__)),
                    MenuAction("Find/Edit Pay Rate", lambda: api.nullfunc(__file__)),
                ]),
                Menu("Pay Rates", [
                    MenuAction("Add Pay Rate", lambda: api.nullfunc(__file__)),
                    MenuAction("Find/Edit Pay Rate", lambda: api.nullfunc(__file__)),
                ]),
            ],
        ),
        Menu(
            "Reports",
            [
                MenuAction("Quarterly Reports", lambda: api.nullfunc(__file__)),
                MenuAction("Employee Master List", lambda: api.nullfunc(__file__)),
                MenuAction("Salaried Job Summary", lambda: api.nullfunc(__file__)),
                MenuAction("Pay Rate Summary", lambda: api.nullfunc(__file__)),
                MenuAction("Run Summary", lambda: api.nullfunc(__file__)),
            ],
        ),
    ]


def main():
    api = MainApi()

    win = webview.create_window(
        title="Ada EMS Timekeeping",
        url="./ui/index.html",
        js_api=api,
        resizable=True,
        menu=build_menu(api),
    )

    api.window = win
    webview.start()


if __name__ == "__main__":
    main()
