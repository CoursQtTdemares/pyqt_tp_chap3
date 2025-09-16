import sys

from PyQt6.QtWidgets import QApplication

from src.blog_responsive import BlogResponsive


def main() -> None:
    """Entry point for tp_qt_chap3."""
    app = QApplication(sys.argv)
    form_window = BlogResponsive()
    form_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
