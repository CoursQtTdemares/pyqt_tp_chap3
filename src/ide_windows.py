from PyQt6.QtWidgets import QHBoxLayout, QLabel, QListWidget, QMainWindow, QTextEdit, QVBoxLayout, QWidget


class FileExplorerWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        # Créer le layout vertical
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Ajouter le titre "Explorateur"
        title_label = QLabel("Explorateur")
        layout.addWidget(title_label)

        # Créer la liste des fichiers
        self.file_list = QListWidget()

        # Ajouter des fichiers factices pour la validation
        fake_files = [
            "src/",
            "tests/",
            "main.py",
            "requirements.txt",
            "README.md",
            "config.json",
            "assets/",
            ".gitignore",
            "docs/",
            "setup.py",
        ]

        self.file_list.addItems(fake_files)

        layout.addWidget(self.file_list)


class CentralEditorWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        # Créer le layout vertical principal
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Créer l'éditeur de texte principal
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Éditeur de code - Zone d'édition principale")
        self.editor.setStyleSheet("""
            QTextEdit {
                background-color: #2b2b2b;
                color: #ffffff;
                font-family: 'Courier New', monospace;
                font-size: 12px;
                border: 1px solid #555;
                padding: 5px;
            }
        """)

        # Créer la console
        self.console = QTextEdit()
        self.console.setPlaceholderText("Console - Sortie des commandes et logs")
        self.console.setReadOnly(True)
        self.console.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #00ff00;
                font-family: 'Courier New', monospace;
                font-size: 10px;
                border: 1px solid #555;
                padding: 5px;
            }
        """)

        # Ajouter du contenu d'exemple à la console
        self.console.append(">>> Console initialisée")
        self.console.append(">>> Prêt pour les commandes...")

        # Ajouter les widgets avec les proportions 75%-25%
        layout.addWidget(self.editor, 3)  # 75% (3/4)
        layout.addWidget(self.console, 1)  # 25% (1/4)


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
        left_sidebar = FileExplorerWidget()
        left_sidebar.setFixedWidth(200)

        # Zone centrale - proportion 3
        central_area = CentralEditorWidget()

        # Zone droite (panneau droit) - proportion 1
        right_panel = QLabel("Panneau Droit")
        right_panel.setStyleSheet("background-color: lightgreen; border: 1px solid black; padding: 10px;")
        right_panel.setFixedWidth(150)

        # Ajouter les widgets avec les proportions 1:3:1 avec stretch_factor
        main_layout.addWidget(left_sidebar, 1)
        main_layout.addWidget(central_area, 3)
        main_layout.addWidget(right_panel, 1)
