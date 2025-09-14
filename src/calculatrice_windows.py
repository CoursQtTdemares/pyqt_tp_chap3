from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QVBoxLayout, QWidget


class CalculatorWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # == Affichage ==

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setText("0")
        self.result_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result_display.setStyleSheet("font-size: 16px; padding: 10px;")
        main_layout.addWidget(self.result_display)
