import functools

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget


class CalculatorWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # == Affichage ==

        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setText("0")
        self.result_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result_display.setStyleSheet("font-size: 16px; padding: 10px;")
        self.main_layout.addWidget(self.result_display)

        # == Grille des boutons numériques ==
        self.create_number_buttons()

    def create_number_buttons(self) -> None:
        """Crée la grille des boutons numériques 0-9 dans un layout 4x3"""
        grid_layout = QGridLayout()

        # Widget conteneur pour la grille
        grid_widget = QWidget()
        grid_widget.setLayout(grid_layout)
        self.main_layout.addWidget(grid_widget)

        # Configuration des boutons selon le pavé numérique classique
        # Ligne 0: C, ±, % (fonctions)
        # Ligne 1: 7, 8, 9
        # Ligne 2: 4, 5, 6
        # Ligne 3: 1, 2, 3
        # Ligne 4: 0 (centré sur 2 colonnes)

        button_layout = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

        # Création des boutons pour les chiffres 1-9 (décalés d'une ligne vers le bas)
        for row, numbers in enumerate(button_layout):
            for col, number in enumerate(numbers):
                button = QPushButton(str(number))
                button.setMinimumSize(60, 50)
                button.setStyleSheet("font-size: 16px; font-weight: bold;")
                button.clicked.connect(functools.partial(self.symbol_pressed, symbol=number))
                grid_layout.addWidget(button, row + 1, col)  # +1 pour faire place aux fonctions

        # Bouton 0 sur la dernière ligne, étendu sur 2 colonnes
        button_0 = QPushButton("0")
        button_0.setMinimumSize(60, 50)
        button_0.setStyleSheet("font-size: 16px; font-weight: bold;")
        button_0.clicked.connect(functools.partial(self.symbol_pressed, symbol=0))
        # addWidget(widget, row, column, rowSpan, columnSpan)
        grid_layout.addWidget(button_0, 4, 0, 1, 2)  # Ligne 4 maintenant

        # == Colonne des opérateurs ==
        operators = [
            ("÷", 1),  # Division - ligne 1 (après les fonctions)
            ("x", 2),  # Multiplication - ligne 2
            ("-", 3),  # Soustraction - ligne 3
            ("+", 4),  # Addition - ligne 4
        ]

        # Style pour les boutons d'opérateurs (couleur de fond différente)
        operator_style = """
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                background-color: #FF9500;
                color: white;
                border: 1px solid #CC7700;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFAD33;
            }
            QPushButton:pressed {
                background-color: #CC7700;
            }
        """

        # Création des boutons d'opérateurs dans la colonne 3
        for symbol, row in operators:
            button = QPushButton(symbol)
            button.setMinimumSize(60, 50)
            button.setStyleSheet(operator_style)
            button.clicked.connect(functools.partial(self.symbol_pressed, symbol=symbol))
            grid_layout.addWidget(button, row, 3)  # Colonne 3 (4ème colonne)

        # Bouton "=" dans la colonne 2, ligne 4 (à côté du bouton 0)
        equals_button = QPushButton("=")
        equals_button.setMinimumSize(60, 50)
        equals_button.setStyleSheet(operator_style)
        equals_button.clicked.connect(self.equals_pressed)
        grid_layout.addWidget(equals_button, 4, 2)

        # Liste des fonctions dans l'ordre d'affichage (de gauche à droite)
        functions = [
            ("C", 0),  # Clear - colonne 0
            ("±", 1),  # Plus/Minus - colonne 1
            ("%", 2),  # Pourcentage - colonne 2
        ]

        # Style pour les boutons de fonction (couleur grise claire)
        function_style = """
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                background-color: #A6A6A6;
                color: black;
                border: 1px solid #808080;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #BFBFBF;
            }
            QPushButton:pressed {
                background-color: #808080;
            }
        """

        # Création des boutons de fonction dans la ligne 0
        for symbol, col in functions:
            button = QPushButton(symbol)
            button.setMinimumSize(60, 50)
            button.setStyleSheet(function_style)
            if symbol == "C":
                button.clicked.connect(self.clear_pressed)
            grid_layout.addWidget(button, 0, col)  # Ligne 0, colonnes 0, 1, 2

    def symbol_pressed(self, symbol: int | str) -> None:
        """Gère la saisie des chiffres et met à jour l'affichage"""
        current_text = self.result_display.text()

        if current_text == "0":
            self.result_display.setText(str(symbol))
        else:
            # Sinon, ajouter le chiffre à la fin
            self.result_display.setText(current_text + str(symbol))

    def clear_pressed(self) -> None:
        self.result_display.setText("0")

    def equals_pressed(self) -> None:
        if (display := self.result_display.text()).endswith(("x", "÷", "+", "-")):
            self.result_display.setText(display[:-1])
            return

        formatted_display = self.result_display.text().replace("x", "*").replace("÷", "/")
        result = eval(formatted_display)  # noqa: S307
        self.result_display.setText(str(result))
