from PyQt6.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QWidget


class IDEWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("IDE - tp chapitre 3")
        self.setGeometry(100, 100, 800, 600)
        self.setup_menu_bar()
        self.setup_status_bar()
        self.setup_main_layout()

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

    def setup_main_layout(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Créer les trois zones avec des couleurs temporaires pour la validation
        # Zone gauche (sidebar) - proportion 1
        left_sidebar = QLabel("Sidebar Gauche")
        left_sidebar.setStyleSheet("background-color: lightblue; border: 1px solid black; padding: 10px;")
        left_sidebar.setFixedWidth(150)

        # Zone centrale - proportion 3
        central_area = QLabel("Zone Centrale")
        central_area.setStyleSheet("background-color: lightgray; border: 1px solid black; padding: 10px;")

        # Zone droite (panneau droit) - proportion 1
        right_panel = QLabel("Panneau Droit")
        right_panel.setStyleSheet("background-color: lightgreen; border: 1px solid black; padding: 10px;")
        right_panel.setFixedWidth(150)

        # Ajouter les widgets avec les proportions 1:3:1 avec stretch_factor
        main_layout.addWidget(left_sidebar, 1)
        main_layout.addWidget(central_area, 3)
        main_layout.addWidget(right_panel, 1)
