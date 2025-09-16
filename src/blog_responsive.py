from PyQt6.QtWidgets import QMainWindow


class BlogResponsive(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Blog Responsive")
        self.setGeometry(100, 100, 800, 600)
