from typing import override

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QResizeEvent
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class HeaderWidget(QWidget):
    """Widget header avec logo, navigation et profil"""

    def __init__(self) -> None:
        super().__init__()
        self.current_mode = "desktop"  # Mode responsive actuel
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Configure l'interface utilisateur du header"""
        self.setFixedHeight(70)  # Hauteur fixe pour le header
        self.setStyleSheet("""
            HeaderWidget {
                background-color: #2c3e50;
                border-bottom: 3px solid #34495e;
                min-height: 70px;
                max-height: 70px;
            }
        """)

        # Layout horizontal pour le header
        self.header_layout = QHBoxLayout(self)
        self.header_layout.setContentsMargins(20, 10, 20, 10)

        # Créer les sections (on les stocke comme attributs pour pouvoir les manipuler)
        self.logo_section = self._create_logo_section()
        self.navigation_section = self._create_navigation_section()
        self.hamburger_section = self._create_hamburger_section()
        self.profile_section = self._create_profile_section()

        # Ajouter les sections au layout initial (mode desktop)
        self._setup_desktop_layout()

    def _create_logo_section(self) -> QLabel:
        """Crée la section logo à gauche"""
        logo_label = QLabel()
        pixmap = QPixmap("src/corbeau.png")
        # Redimensionner l'image pour qu'elle s'adapte au header
        scaled_pixmap = pixmap.scaled(
            40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        logo_label.setPixmap(scaled_pixmap)
        logo_label.setStyleSheet("""
            QLabel {
                background: transparent;
                padding: 5px;
            }
        """)
        return logo_label

    def _create_navigation_section(self) -> QWidget:
        """Crée la section navigation au centre"""
        nav_widget = QWidget()
        nav_layout = QHBoxLayout(nav_widget)
        nav_layout.setContentsMargins(0, 0, 0, 0)

        nav_items = ["Accueil", "Articles", "À propos", "Contact"]
        for item in nav_items:
            nav_btn = QPushButton(item)
            nav_btn.setStyleSheet("""
                QPushButton {
                    background-color: #34495e;
                    color: #ffffff;
                    border: 2px solid #5d6d7e;
                    border-radius: 6px;
                    padding: 8px 15px;
                    margin: 2px;
                    font-size: 14px;
                    font-weight: bold;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #4a5f7a;
                    border: 2px solid #7fb3d3;
                    color: #ffffff;
                }
                QPushButton:pressed {
                    background-color: #2c3e50;
                    border: 2px solid #3498db;
                }
            """)
            nav_layout.addWidget(nav_btn)

        return nav_widget

    def _create_hamburger_section(self) -> QPushButton:
        """Crée le bouton hamburger pour le mode responsive"""
        hamburger_btn = QPushButton("☰")
        hamburger_btn.setStyleSheet("""
            QPushButton {
                background-color: #34495e;
                color: #ffffff;
                border: 2px solid #5d6d7e;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 18px;
                font-weight: bold;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: #4a5f7a;
                border: 2px solid #7fb3d3;
            }
            QPushButton:pressed {
                background-color: #2c3e50;
                border: 2px solid #3498db;
            }
        """)

        hamburger_btn.clicked.connect(self._toggle_mobile_menu)
        return hamburger_btn

    def _create_profile_section(self) -> QPushButton:
        """Crée la section profil à droite"""
        profile_btn = QPushButton("👤 Profil")
        profile_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: #ffffff;
                border: 2px solid #c0392b;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #d62c1a;
                border: 2px solid #a93226;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #c0392b;
                border: 2px solid #922b21;
            }
        """)
        return profile_btn

    def _setup_desktop_layout(self) -> None:
        """Configure le layout pour le mode desktop"""
        # Vider le layout
        self._clear_layout()

        # Mode desktop : logo + navigation + profil
        self.header_layout.addWidget(self.logo_section)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.navigation_section)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.profile_section)

    def _setup_tablet_layout(self) -> None:
        """Configure le layout pour le mode tablet/mobile"""
        # Vider le layout
        self._clear_layout()

        # Mode tablet/mobile : logo + hamburger + profil
        self.header_layout.addWidget(self.logo_section)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.hamburger_section)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.profile_section)

    def _clear_layout(self) -> None:
        """Vide le layout header de tous ses widgets"""
        while self.header_layout.count():
            child = self.header_layout.takeAt(0)
            if child is not None:
                widget = child.widget()
                if widget is not None:
                    widget.setParent(None)

    def _toggle_mobile_menu(self) -> None:
        """Bascule l'affichage du menu mobile (pour implémentation future)"""
        print("🍔 [DEBUG] Bouton hamburger cliqué - Menu mobile à implémenter")

    def set_responsive_mode(self, mode: str) -> None:
        """Adapte le header selon le mode responsive"""
        if mode == self.current_mode:
            return  # Pas de changement nécessaire

        if mode == "desktop":
            self._setup_desktop_layout()
            print("   🖥️  Header en mode Desktop: Navigation complète visible")
        else:  # tablet ou mobile
            self._setup_tablet_layout()
            print(f"   📱 Header en mode {mode.title()}: Menu hamburger activé")

        self.current_mode = mode


class SidebarWidget(QWidget):
    """Widget sidebar avec les catégories"""

    def __init__(self) -> None:
        super().__init__()
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Configure l'interface utilisateur de la sidebar"""
        self.setStyleSheet("""
            SidebarWidget {
                background-color: #ffffff;
                border: 1px solid #dee2e6;
                border-radius: 8px;
            }
        """)
        self.setMaximumWidth(250)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)

        # Titre de la sidebar
        title_label = QLabel("Catégories")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
                padding-bottom: 10px;
                border-bottom: 2px solid #3498db;
                margin-bottom: 15px;
            }
        """)
        layout.addWidget(title_label)

        # Liste des catégories
        self.categories_list = QListWidget()
        self.categories_list.setStyleSheet("""
            QListWidget {
                border: none;
                background: transparent;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 8px 5px;
                border-bottom: 1px solid #ecf0f1;
                color: #34495e;
            }
            QListWidget::item:hover {
                background-color: #f1f2f6;
                color: #2c3e50;
            }
            QListWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)

        # Ajouter des catégories
        categories = ["Toutes", "Technologie", "Sciences", "Lifestyle", "Voyage", "Cuisine", "Sport"]
        for category in categories:
            item = QListWidgetItem(f"📁 {category}")
            self.categories_list.addItem(item)

        layout.addWidget(self.categories_list)


class ArticlesWidget(QWidget):
    """Widget zone d'articles principale"""

    def __init__(self) -> None:
        super().__init__()
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Configure l'interface utilisateur de la zone d'articles"""
        self.setStyleSheet("""
            ArticlesWidget {
                background-color: #ffffff;
                border: 1px solid #dee2e6;
                border-radius: 8px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        # Titre de la zone d'articles
        title_label = QLabel("Articles du Blog")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                padding-bottom: 15px;
                border-bottom: 3px solid #e74c3c;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title_label)

        # Zone de texte pour les articles
        self.articles_text = QTextEdit()
        self.articles_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                padding: 15px;
                font-size: 14px;
                line-height: 1.6;
                background-color: #fefefe;
            }
        """)

        # Contenu d'exemple
        self._load_sample_content()
        layout.addWidget(self.articles_text)

    def _load_sample_content(self) -> None:
        """Charge le contenu d'exemple dans la zone d'articles"""
        sample_content = """
<h2 style="color: #2c3e50;">🚀 Bienvenue sur notre Blog Technologique</h2>

<p><strong>Derniers Articles :</strong></p>

<h3 style="color: #3498db;">📱 Les Tendances Tech 2024</h3>
<p>Découvrez les innovations qui façonnent notre avenir : intelligence artificielle, réalité augmentée, et développement durable. Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>

<h3 style="color: #3498db;">🌐 Développement Web Moderne</h3>
<p>Guide complet sur les frameworks JavaScript, Python et les meilleures pratiques de développement. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...</p>

<h3 style="color: #3498db;">🔐 Cybersécurité et Protection des Données</h3>
<p>Comment protéger vos informations personnelles dans le monde numérique d'aujourd'hui. Ut enim ad minim veniam, quis nostrud exercitation ullamco...</p>

<h3 style="color: #3498db;">🎯 Productivité et Outils</h3>
<p>Les meilleurs outils pour optimiser votre workflow de développement et votre productivité quotidienne. Duis aute irure dolor in reprehenderit...</p>

<hr style="margin: 20px 0; border: 1px solid #ecf0f1;">

<p><em>✍️ Cliquez sur une catégorie à gauche pour filtrer les articles par thème.</em></p>
        """
        self.articles_text.setHtml(sample_content)


class MainContentWidget(QWidget):
    """Widget zone de contenu principale avec sidebar et articles"""

    def __init__(self) -> None:
        super().__init__()
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Configure l'interface utilisateur du contenu principal"""
        self.setStyleSheet("""
            MainContentWidget {
                background-color: #f8f9fa;
            }
        """)

        # Layout horizontal pour sidebar (1) + contenu articles (3)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        # Sidebar (proportion 1)
        self.sidebar = SidebarWidget()
        layout.addWidget(self.sidebar, 1)

        # Zone d'articles (proportion 3)
        self.articles = ArticlesWidget()
        layout.addWidget(self.articles, 3)


class BlogResponsive(QMainWindow):
    """Fenêtre principale du blog responsive"""

    def __init__(self) -> None:
        super().__init__()
        # Seuils de largeur pour le responsive design
        self.BREAKPOINT_MOBILE = 500
        self.BREAKPOINT_TABLET = 800
        self.current_layout_mode = "desktop"  # desktop, tablet, mobile
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Configure l'interface utilisateur principale"""
        self.setWindowTitle("Blog Responsive")
        self.setGeometry(100, 100, 800, 600)

        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal vertical
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Créer et ajouter le header en haut
        self.header_widget = HeaderWidget()
        main_layout.addWidget(self.header_widget)

        # Créer la zone de contenu principale du blog
        self.main_content_widget = MainContentWidget()
        main_layout.addWidget(self.main_content_widget)

    @override
    def resizeEvent(self, event: QResizeEvent | None) -> None:
        """Détecte les changements de taille de fenêtre pour le responsive design"""
        if event is None:
            return

        super().resizeEvent(event)

        # Récupérer la nouvelle largeur
        new_width = event.size().width()
        new_height = event.size().height()

        # Déterminer le mode d'affichage selon la largeur
        new_layout_mode = self._get_layout_mode(new_width)

        # Messages de debug pour suivre les changements
        print("🔧 [DEBUG] Redimensionnement détecté:")
        print(f"   📏 Nouvelle taille: {new_width}x{new_height}px")
        print(f"   📱 Mode d'affichage: {new_layout_mode}")

        # Si le mode a changé, adapter l'interface
        if new_layout_mode != self.current_layout_mode:
            print(f"   🔄 Changement de mode: {self.current_layout_mode} → {new_layout_mode}")
            self._adapt_layout_to_mode(new_layout_mode)
            self.current_layout_mode = new_layout_mode

        print(
            f"   ➡️  Seuils Largeur: Mobile<{self.BREAKPOINT_MOBILE}px | Tablet<{self.BREAKPOINT_TABLET}px | Desktop≥{self.BREAKPOINT_TABLET}px"
        )
        print("   " + "=" * 50)

    def _get_layout_mode(self, width: int) -> str:
        """Détermine le mode d'affichage selon la largeur"""
        if width < self.BREAKPOINT_MOBILE:
            return "mobile"
        elif width < self.BREAKPOINT_TABLET:
            return "tablet"
        else:
            return "desktop"

    def _adapt_layout_to_mode(self, mode: str) -> None:
        """Adapte l'interface selon le mode d'affichage"""
        print(f"   🎨 Adaptation de l'interface pour le mode: {mode}")

        # Adapter le header selon le mode
        self.header_widget.set_responsive_mode(mode)

        if mode == "mobile":
            print("      📱 Mode Mobile: Interface compacte")
            # TODO: Adapter la sidebar et le contenu pour mobile

        elif mode == "tablet":
            print("      📱 Mode Tablet: Interface intermédiaire")
            # TODO: Adapter la sidebar et le contenu pour tablet

        else:  # desktop
            print("      🖥️  Mode Desktop: Interface complète")
            # TODO: Assurer que tout est visible en mode desktop
