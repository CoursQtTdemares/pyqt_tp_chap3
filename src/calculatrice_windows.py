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
        # Ligne 1: 7, 8, 9
        # Ligne 2: 4, 5, 6
        # Ligne 3: 1, 2, 3
        # Ligne 4: 0 (centré sur 2 colonnes)

        button_layout = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

        # Création des boutons pour les chiffres 1-9
        for row, numbers in enumerate(button_layout):
            for col, number in enumerate(numbers):
                button = QPushButton(str(number))
                button.setMinimumSize(60, 50)
                button.setStyleSheet("font-size: 16px; font-weight: bold;")
                grid_layout.addWidget(button, row, col)

        # Bouton 0 sur la dernière ligne, étendu sur 2 colonnes
        button_0 = QPushButton("0")
        button_0.setMinimumSize(60, 50)
        button_0.setStyleSheet("font-size: 16px; font-weight: bold;")
        # addWidget(widget, row, column, rowSpan, columnSpan)
        grid_layout.addWidget(button_0, 3, 0, 1, 2)
