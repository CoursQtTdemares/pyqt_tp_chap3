from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QWidget


class FormWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Formulaire - tp chapitre 3")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QVBoxLayout()
        central_widget.setLayout(form_layout)

        # Nom
        name_layout = QHBoxLayout()
        self.name_label = QLabel("Nom : ")
        name_layout.addWidget(self.name_label)
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)

        form_layout.addLayout(name_layout)

        # Prénom
        firstname_layout = QHBoxLayout()
        self.firstname_label = QLabel("Prénom : ")
        firstname_layout.addWidget(self.firstname_label)
        self.firstname_input = QLineEdit()
        firstname_layout.addWidget(self.firstname_input)

        form_layout.addLayout(firstname_layout)

        # Email
        email_layout = QHBoxLayout()
        self.email_label = QLabel("Email : ")
        email_layout.addWidget(self.email_label)
        self.email_input = QLineEdit()
        email_layout.addWidget(self.email_input)

        form_layout.addLayout(email_layout)
