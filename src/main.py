"""Python implementation of the 32bit-based Visual Basic timekeeping
application. Changes made to work on 64bit Windows 11 systems.

Table of Contents:
    MainApi  - Class bridge between the frontend and 'backend' for calling
               Python code.
    MainMenu - Class that modularizes MainApi. Contains menu functions.
    main()   - Function at bottom of file that creates webview window and
               starts program.

All other functions and classes used, while important, I've deemed
easily understandable if seen, either from their naming or use. Take
the above as a table of contents for the 'important' sections that may
need to be easily found.
"""
import webview
from webview.menu import Menu, MenuAction


class MainApi:
    """Main bridge for frontend javascript to execute python."""
    def __init__(self):
        self._window: webview.Window|None = None
        self.menu: MainMenu = MainMenu(self)

    @property
    def window(self) -> webview.Window:
        assert self._window is not None
        return self._window
    @window.setter
    def window(self, win):
        self._window = win

    def nullfunc(self, file:str) -> None:
        print(f"nullfunc called from file:{file.split("/")[-1]}")

class MainMenu:
    def __init__(self, api: MainApi):
        self.api = api

    def file_main(self):
        print("TODO: 'file_main()' functionality")
    def file_exit(self):
        self.api.window.destroy()

    def timekeeping_addRun(self):
        print("TODO: 'timekeeping_addRun()' functionality")
    def timekeeping_findDeleteRun(self):
        print("TODO: 'timekeeping_findDeleteRun()' functionality")

    def employeeRecord_addEmployee(self):
        print("TODO: 'employeeRecord_addEmployee()' functionality")
    def employeeRecord_findEditEmployee(self):
        print("TODO: 'employeeRecord_findEditEmployee()' functionality")

    def positions_salaried_addPosition(self):
        print("TODO: 'positions_salaried_addPosition()' functionality")
    def positions_salaried_findEditPayRate(self):
        print("TODO: 'positions_salaried_findEditPayRate()' functionality")
    def positions_payRates_addPayRate(self):
        print("TODO: 'positions_payRates_addPayRate()' functionality")
    def positions_payRates_findEditPayRate(self):
        print("TODO: 'positions_payRates_findEditPayRate()' functionality")

    def reports_quarterlyReports(self):
        print("TODO: 'reports_quarterlyReports()' functionality")
    def reports_employeeMasterList(self):
        print("TODO: 'reports_employeeMasterList()' functionality")
    def reports_salariedJobSummary(self):
        print("TODO: 'reports_salariedJobSummary()' functionality")
    def reports_payRateSummary(self):
        print("TODO: 'reports_payRateSummary()' functionality")
    def reports_runSummary(self):
        print("TODO: 'reports_runSummary()' functionality")


def build_menu(api: MainApi):
    return [
        Menu(
            "File",
            [
                MenuAction("Main", api.menu.file_main),
                MenuAction("Exit", api.menu.file_exit),
            ],
        ),
        Menu(
            "Timekeeping",
            [
                MenuAction("Add Run", api.menu.timekeeping_addRun),
                MenuAction("Find/Delete Run", api.menu.timekeeping_findDeleteRun),
            ],
        ),
        Menu(
            "Employee Record",
            [
                MenuAction("Add Employee", api.menu.employeeRecord_addEmployee),
                MenuAction("Find/Edit Employee", api.menu.employeeRecord_findEditEmployee),
            ],
        ),
        Menu(
            "Positions",
            [
                Menu("Salaried", [
                    MenuAction("Add Position", api.menu.positions_salaried_addPosition),
                    MenuAction("Find/Edit Pay Rate", api.menu.positions_salaried_findEditPayRate),
                ]),
                Menu("Pay Rates", [
                    MenuAction("Add Pay Rate", api.menu.positions_payRates_addPayRate),
                    MenuAction("Find/Edit Pay Rate", api.menu.positions_payRates_findEditPayRate),
                ]),
            ],
        ),
        Menu(
            "Reports",
            [
                MenuAction("Quarterly Reports", api.menu.reports_quarterlyReports),
                MenuAction("Employee Master List", api.menu.reports_employeeMasterList),
                MenuAction("Salaried Job Summary", api.menu.reports_salariedJobSummary),
                MenuAction("Pay Rate Summary", api.menu.reports_payRateSummary),
                MenuAction("Run Summary", api.menu.reports_runSummary),
            ],
        ),
    ]


def main():
    api = MainApi()

    api.window = webview.create_window(
        title="Ada EMS Timekeeping",
        url="./ui/index.html",
        js_api=api,
        resizable=True,
        menu=build_menu(api),
    )

    webview.start()

if __name__ == "__main__":
    main()
