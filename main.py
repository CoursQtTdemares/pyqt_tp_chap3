import sys

from PyQt6.QtWidgets import QApplication

from src.calculatrice_windows import CalculatorWindow


def main() -> None:
    """Entry point for tp_qt_chap3."""
    app = QApplication(sys.argv)
    form_window = CalculatorWindow()
    form_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
