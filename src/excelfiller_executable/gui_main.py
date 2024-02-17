import sys

from PySide2.QtWidgets import QApplication

from excelfiller_executable.gui.ui.mainwindow.window import RuleProcessorWindow


def main():
    app = QApplication()
    main_window = RuleProcessorWindow()
    main_window.show()
    exit_code = app.exec_()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
