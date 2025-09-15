from PyQt6.QtWidgets import QMainWindow


class IDEWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("IDE - tp chapitre 3")
        self.setGeometry(100, 100, 400, 300)
        self.setup_menu_bar()
        self.setup_status_bar()

    def setup_menu_bar(self) -> None:
        if (menu_bar := self.menuBar()) is None:
            return

        if (file_menu := menu_bar.addMenu("File")) is None:
            return

        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addSeparator()
        file_menu.addAction("Exit")

    def setup_status_bar(self) -> None:
        if (status_bar := self.statusBar()) is None:
            return

        status_bar.showMessage("Ready")
