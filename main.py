import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont

from ui.styles import get_dark_theme_stylesheet
from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    font = QFont("Microsoft YaHei", 10)
    app.setFont(font)
    app.setStyleSheet(get_dark_theme_stylesheet())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
