from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


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


class PropertiesPanelWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        # Créer le layout vertical principal
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Section Propriétés
        properties_title = QLabel("Propriétés")
        properties_title.setStyleSheet("""
            QLabel {
                font-weight: bold;
                padding: 5px;
                background-color: #4a4a4a;
                color: white;
                border: 1px solid #666;
            }
        """)

        self.properties_content = QTextEdit()
        self.properties_content.setStyleSheet("""
            QTextEdit {
                background-color: #f5f5f5;
                border: 1px solid #ccc;
                padding: 5px;
                font-size: 11px;
            }
        """)
        self.properties_content.setReadOnly(True)
        self.properties_content.setMaximumHeight(150)

        # Ajouter du contenu d'exemple aux propriétés
        self.properties_content.append("Fichier: main.py")
        self.properties_content.append("Taille: 1.2 KB")
        self.properties_content.append("Modifié: Aujourd'hui 14:30")
        self.properties_content.append("Encodage: UTF-8")
        self.properties_content.append("Type: Python Script")

        # Section Outline
        outline_title = QLabel("Outline")
        outline_title.setStyleSheet("""
            QLabel {
                font-weight: bold;
                padding: 5px;
                background-color: #4a4a4a;
                color: white;
                border: 1px solid #666;
            }
        """)

        self.outline_list = QListWidget()
        self.outline_list.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: 1px solid #ccc;
                padding: 2px;
                font-size: 11px;
            }
        """)

        # Ajouter du contenu d'exemple à l'outline
        outline_items = [
            "📁 Classes",
            "  🔧 MainWindow",
            "  🔧 FileManager",
            "📁 Fonctions",
            "  ⚙️ init_app()",
            "  ⚙️ load_config()",
            "  ⚙️ save_file()",
            "📁 Variables",
            "  📋 app_config",
            "  📋 current_file",
        ]

        self.outline_list.addItems(outline_items)

        # Ajouter les widgets au layout avec proportions
        layout.addWidget(properties_title)
        layout.addWidget(self.properties_content, 1)
        layout.addWidget(outline_title)
        layout.addWidget(self.outline_list, 2)


class IDEWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("IDE - tp chapitre 3")
        self.setGeometry(100, 100, 800, 600)
        self.setup_menu_bar()
        self.setup_toolbar()
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

    def setup_toolbar(self) -> None:
        # Créer la barre d'outils
        toolbar = QToolBar("Outils principaux")
        toolbar.setMovable(False)  # Empêcher le déplacement de la toolbar
        self.addToolBar(toolbar)

        # Bouton Nouveau
        new_button = QPushButton("📄 Nouveau")
        new_button.setToolTip("Créer un nouveau fichier (Ctrl+N)")
        new_button.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                margin: 2px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-color: #999;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        new_button.clicked.connect(self.new_file)
        toolbar.addWidget(new_button)

        # Bouton Ouvrir
        open_button = QPushButton("📂 Ouvrir")
        open_button.setToolTip("Ouvrir un fichier existant (Ctrl+O)")
        open_button.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                margin: 2px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-color: #999;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        open_button.clicked.connect(self.open_file)
        toolbar.addWidget(open_button)

        # Bouton Sauvegarder
        save_button = QPushButton("💾 Sauver")
        save_button.setToolTip("Sauvegarder le fichier actuel (Ctrl+S)")
        save_button.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                margin: 2px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-color: #999;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        save_button.clicked.connect(self.save_file)
        toolbar.addWidget(save_button)

        # Séparateur
        toolbar.addSeparator()

        # Bouton Exécuter
        run_button = QPushButton("▶️ Exécuter")
        run_button.setToolTip("Exécuter le code (F5)")
        run_button.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                margin: 2px;
                background-color: #4CAF50;
                color: white;
                border: 1px solid #45a049;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
                border-color: #3d8b40;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        run_button.clicked.connect(self.run_code)
        toolbar.addWidget(run_button)

    def new_file(self) -> None:
        print("new_file")

    def open_file(self) -> None:
        print("open_file")

    def save_file(self) -> None:
        print("save_file")

    def run_code(self) -> None:
        print("run_code")

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
        right_panel = PropertiesPanelWidget()
        right_panel.setFixedWidth(220)

        # Ajouter les widgets avec les proportions 1:3:1 avec stretch_factor
        main_layout.addWidget(left_sidebar, 1)
        main_layout.addWidget(central_area, 3)
        main_layout.addWidget(right_panel, 1)
