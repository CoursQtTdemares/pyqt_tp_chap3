from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class FormWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Formulaire - tp chapitre 3")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vertical_layout = QVBoxLayout()
        central_widget.setLayout(vertical_layout)
