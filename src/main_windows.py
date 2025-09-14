from PyQt6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget


class FormWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Formulaire - tp chapitre 3")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QVBoxLayout()
        central_widget.setLayout(form_layout)

        # == Informations personnelles ==

        info_layout = QVBoxLayout()
        form_layout.addLayout(info_layout)

        # Nom
        name_layout = QHBoxLayout()
        name_label = QLabel("Nom : ")
        name_layout.addWidget(name_label)
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)

        info_layout.addLayout(name_layout)

        # Prénom
        firstname_layout = QHBoxLayout()
        firstname_label = QLabel("Prénom : ")
        firstname_layout.addWidget(firstname_label)
        self.firstname_input = QLineEdit()
        firstname_layout.addWidget(self.firstname_input)

        info_layout.addLayout(firstname_layout)

        # Email
        email_layout = QHBoxLayout()
        email_label = QLabel("Email : ")
        email_layout.addWidget(email_label)
        self.email_input = QLineEdit()
        email_layout.addWidget(self.email_input)

        info_layout.addLayout(email_layout)

        # == Adresse ==
        address_layout = QVBoxLayout()
        form_layout.addLayout(address_layout)

        # Rue
        street_layout = QHBoxLayout()
        street_label = QLabel("Rue : ")
        street_layout.addWidget(street_label)
        self.street_input = QLineEdit()
        street_layout.addWidget(self.street_input)

        address_layout.addLayout(street_layout)

        # Code postal
        postal_code_layout = QHBoxLayout()
        postal_code_label = QLabel("Code postal : ")
        postal_code_layout.addWidget(postal_code_label)
        self.postal_code_input = QLineEdit()
        postal_code_layout.addWidget(self.postal_code_input)

        address_layout.addLayout(postal_code_layout)

        # Ville
        city_layout = QHBoxLayout()
        city_label = QLabel("Ville : ")
        city_layout.addWidget(city_label)
        self.city_input = QLineEdit()
        city_layout.addWidget(self.city_input)

        address_layout.addLayout(city_layout)

        # Pays
        country_layout = QHBoxLayout()
        country_label = QLabel("Pays : ")
        country_layout.addWidget(country_label)
        self.country_input = QComboBox()
        self.country_input.addItems(["France", "Belgique", "Suisse"])
        country_layout.addWidget(self.country_input)

        address_layout.addLayout(country_layout)

        # Button
        self.button = QPushButton("Valider")
        form_layout.addWidget(self.button)
