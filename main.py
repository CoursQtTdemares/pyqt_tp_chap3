import sys

from PyQt6.QtWidgets import QApplication

from src.ide_windows import IDEWindow


def main() -> None:
    """Entry point for tp_qt_chap3."""
    app = QApplication(sys.argv)
    form_window = IDEWindow()
    form_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
