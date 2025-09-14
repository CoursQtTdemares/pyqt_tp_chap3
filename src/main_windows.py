from dataclasses import dataclass

from PyQt6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


@dataclass
class FormResult:
    name: str
    firstname: str
    email: str
    street: str
    postal_code: str
    city: str
    country: str
    age: int
    newsletter: bool
    comment: str

    def to_message_box_format(self) -> str:
        return f"Nom : {self.name}\nPrénom : {self.firstname}\nEmail : {self.email}\nRue : {self.street}\nCode postal : {self.postal_code}\nVille : {self.city}\nPays : {self.country}\nAge : {self.age}\nNewsletter : {self.newsletter}\nCommentaire : {self.comment}"


class FormWindow(QMainWindow):
    def create_separator(self) -> QFrame:
        separator = QFrame()
        separator.setFrameStyle(QFrame.Shape.HLine | QFrame.Shadow.Sunken)
        return separator

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

        form_layout.addWidget(self.create_separator())

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

        form_layout.addWidget(self.create_separator())

        # == Préférences ==
        preferences_layout = QVBoxLayout()
        form_layout.addLayout(preferences_layout)

        # Age
        age_layout = QHBoxLayout()
        age_label = QLabel("Age : ")
        age_layout.addWidget(age_label)
        self.age_input = QSpinBox()
        self.age_input.setRange(16, 99)
        age_layout.addWidget(self.age_input)

        preferences_layout.addLayout(age_layout)

        # Newsletter
        newsletter_layout = QHBoxLayout()
        newsletter_label = QLabel("Newsletter : ")
        newsletter_layout.addWidget(newsletter_label)
        self.newsletter_input = QCheckBox()
        newsletter_layout.addWidget(self.newsletter_input)

        preferences_layout.addLayout(newsletter_layout)

        # Commentaire
        comment_layout = QVBoxLayout()
        comment_label = QLabel("Commentaire : ")
        comment_layout.addWidget(comment_label)
        self.comment_input = QTextEdit()
        self.comment_input.setFixedHeight(self.comment_input.fontMetrics().lineSpacing() * 3 + 12)
        comment_layout.addWidget(self.comment_input)

        preferences_layout.addLayout(comment_layout)

        form_layout.addWidget(self.create_separator())

        # == Button ==
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        form_layout.addLayout(button_layout)

        self.validate_button = QPushButton("Valider")
        self.validate_button.clicked.connect(self.validate_form)
        button_layout.addWidget(self.validate_button)

        self.cancel_button = QPushButton("Annuler")
        button_layout.addWidget(self.cancel_button)

    def validate_form(self) -> None:
        result = FormResult(
            name=self.name_input.text(),
            firstname=self.firstname_input.text(),
            email=self.email_input.text(),
            street=self.street_input.text(),
            postal_code=self.postal_code_input.text(),
            city=self.city_input.text(),
            country=self.country_input.currentText(),
            age=self.age_input.value(),
            newsletter=self.newsletter_input.isChecked(),
            comment=self.comment_input.toPlainText(),
        )

        # Créer et afficher le QMessageBox
        message_box = QMessageBox()
        message_box.setWindowTitle("Résultat")
        message_box.setText(result.to_message_box_format())
        message_box.exec()
