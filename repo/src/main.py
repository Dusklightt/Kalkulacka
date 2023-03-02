"""
@file main.py
@brief Main file of the calculator
"""

import gui
import importlib
import sys

if __name__ == '__main__':
    app = gui.QApplication(sys.argv)
    window = gui.Window()
    window.show()

    sys.exit(app.exec_())
