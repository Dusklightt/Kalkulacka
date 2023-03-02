from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from functools import partial
import mathlib
"""
@file gui.py
@brief GUI for the calculator
"""
class Window(QMainWindow):
  """
  @brief this class creates basic calculator
  @param QMainWindow this class is inheriting from QMainWindow class
  """
  operations2 = ['+','-','*','/',"nrt","%",'^']
  operations1 = ["x!", "sqrt", "sin"]
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  showText = ""
  entry = ""
  x = ""
  y = ""
  operator = ""
  expecty = False
  lastOp = True
  decimal = False
  def __init__(self, parent=None):
    """
    @brief inicialization of the calculator
    @param self represents the instance of the class
    @param parent
    """
    super().__init__(parent)
    self.setWindowTitle("Kalkulačka")
    self.setFixedSize(300, 300)
    self.setStyleSheet("""
        background: #2b2b2b;
        """
        )

    #creating buttons and display layout
    self.generalLayout = QVBoxLayout()
    self._centralWidget = QWidget(self)
    self.setCentralWidget(self._centralWidget)
    self._centralWidget.setLayout(self.generalLayout)

    self.display = QLineEdit()
    self.display.setFixedHeight(40)
    self.display.setAlignment(Qt.AlignRight)
    self.display.setReadOnly(True)
    self.generalLayout.addWidget(self.display)

    #setting buttons and their position
    self.buttons = {}
    self.buttonsLayout = QGridLayout()
    self.buttons = {
         '1': (2, 0),
         '2': (2, 1),
         '3': (2, 2),
         '4': (1, 0),
         '5': (1, 1),
         '6': (1, 2),
         '7': (0, 0),
         '8': (0, 1),
         '9': (0, 2),
         '/': (0, 3),
         'C': (0, 4),
         '*': (1, 3),
         '-': (2, 3),
         '.': (3, 2),
         '+': (3, 3),
         '=': (3, 5),
         '^': (0, 5),
         '%': (1, 5),
         'nrt': (2, 5),
         'sqrt': (2, 4),
         'sin': (1, 4),
         'x!': (3, 4),

         '0': (3, 0, 1, 2)
          }

    self.createButtons()

    #adding buttons layout and using CSS to give them style
    self.generalLayout.addLayout(self.buttonsLayout)
    self._centralWidget.setStyleSheet("""
            QLineEdit {
              background: #ffffff;
              font-size: 20px;
            }
            QPushButton {
              border-radius: 4px;
              border: 1px solid white;
              background: #868686;
            }

            QPushButton:hover {
              background-color: #918f8b;
              border-style: outset;
              border-width: 3px;
              border-color: #666665;
            }
            QPushButton:pressed {
              background: #414140;
              border-style: outset;
              border-width: 2px;
              border-color: #202020;
            }
            """)


  def createButtons(self):
    """
    @brief creating buttons (positioning them and setting action)
    @param self represents the instance of the class
    """
    for btnText, pos in self.buttons.items():
      self.buttons[btnText] = QPushButton(btnText)
      if(len(pos) == 2):
        self.buttons[btnText].setFixedSize(40, 40)
        self.buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
      elif(len(pos) == 4):
        rows = 40*pos[2] + 7*(pos[2]-1)
        cols = 40*pos[3] + 7*(pos[3]-1)
        self.buttons[btnText].setFixedSize(cols, rows)
        self.buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1], pos[2], pos[3])
      if(btnText != 'C'):
        self.buttons[btnText].clicked.connect(partial(self.setButtonsAction, btnText))
      self.buttons[btnText].setShortcut(btnText)

    self.buttons['C'].clicked.connect(self.clearDisplayText)
    for button in ('=', "Enter", "Return"):
      shorcut = QShortcut(button, self.buttons['='])
      shorcut.activated.connect(self.buttons['='].animateClick)
    for button in (".", ","):
      shorcut = QShortcut(button, self.buttons['.'])
      shorcut.activated.connect(self.buttons['.'].animateClick)


  def setButtonsAction(self, event):
    """
    @brief sets action for most of the buttons on calculator
    @param self represents the instance of the class
    @param event string with character that represents button pressed
    """
    # pressed button is an operation
    if (event in self.operations2):
        # pressed operator needs 2 arguments, expect 2nd argument
        # if entry is empty and first operator is -, negative number
        if(self.showText == "" and event == "-"):
            self.showText = self.showText + event
            self.setDisplay(self.showText)
            self.entry = self.showText
        elif(self.showText == "" or self.showText == "-"):
            # if entry is empty, do nothing
            return

        elif (self.operator == ""):
            # operator was unset
            self.operator = event
            self.expecty = True
            if (self.decimal == True):
                self.x = float(self.entry)
                self.decimal = False
            else:
                self.x = int(self.entry)
            self.showText = self.showText + event
            self.entry = ""
            self.setDisplay(self.showText)
        elif (self.entry == ""):
            # operator was set, entry was empty, rewrite operator
            self.operator = event
            self.expecty = True
        else:
            # operator was set, entry was set, calculate and show result, then add operator
            if (self.decimal == True):
                self.y = float(self.entry)
                self.decimal = False
            else:
                self.y = int(self.entry)
            self.showText = self.calculate(self.operator)
            self.entry = self.showText
            if(self.entry.isdigit()):
                self.decimal = False
            else:
                self.decimal = True

            if (self.decimal == True):
                self.x = float(self.entry)
                self.decimal = False
            else:
                self.x = int(self.entry)
            self.entry = ""
            self.operator = event
            self.expecty = True
            self.showText = self.showText + self.operator
            self.setDisplay(self.showText)

    elif (event in self.operations1):
        # if entry is empty, do nothing
        if(self.showText == "" or self.showText == "-"):
            return
        # pressed operator needs 1 argument, calculate and show result
        elif (self.operator == ""):
            # operator was unset
            self.operator = event
            self.expecty = False
            if (self.decimal == True):
                self.x = float(self.entry)
                self.decimal = False
            else:
                self.x = int(self.entry)
            self.showText = self.calculate(self.operator)
            self.setDisplay(self.showText)
            if(self.showText.isdigit()):
                self.decimal = False
            else:
                self.decimal = True
            self.entry = self.showText

        elif (self.entry == ""):
            # operator was set, entry was empty
            self.operator = event
            self.expecty = False
            self.showText = self.calculate(self.operator)
            self.setDisplay(self.showText)
            if(self.showText.isdigit()):
                self.decimal = False
            else:
                self.decimal = True
            self.entry = self.showText
        else:
            # operator was set, entry was set, calculate old and calculate new and show
            if (self.decimal == True):
                self.y = float(self.entry)
                self.decimal = False
            else:
                self.y = int(self.entry)
            self.showText = self.calculate(self.operator)
            self.entry = self.showText
            if(self.entry.isdigit()):
                self.decimal = False
            else:
                self.decimal = True

            self.operator = event
            self.expecty = False
            if (self.decimal == True):
                self.x = float(self.entry)
                self.decimal = False
            else:
                self.x = int(self.entry)
            self.showText = self.calculate(self.operator)
            self.setDisplay(self.showText)
            if(self.showText.isdigit()):
                self.decimal = False
            else:
                self.decimal = True
            self.entry = self.showText

    elif (event == '='):
        # if entry is empty, do nothing
        if(self.showText == "" or self.showText == "-" or self.operator == ""):
            return
        elif (self.decimal == True):
            self.y = float(self.entry)
            self.decimal = False
        else:
            self.y = int(self.entry)
        self.showText = self.calculate(self.operator)
        self.setDisplay(self.showText)
        self.entry = self.showText
        self.operator = ""
        if(self.entry.isdigit()):
            self.decimal = False
        else:
            self.decimal = True

    elif (event in self.numbers):
        # pressed button is a number
        self.entry = self.entry + event
        self.showText = self.showText + event
        self.setDisplay(self.showText)
    elif (event == '.' or event == ','):
        if(self.decimal == False and (self.entry != "" and self.entry != "-")):
            self.decimal = True
            self.entry = self.entry + '.'
            self.showText = self.showText + '.'
            self.setDisplay(self.showText)

  def setDisplay(self, string):
    """
    @param self represents the instance of the class
    @param string string that will be set to display
    """
    self.display.setText(string)

  def clearDisplayText(self, event):
    """
    @brief clear main display on calculator (for 'C' button)
    @param self represents the instance of the class
    @param event string with character that represents button pressed
    """
    self.display.clear()
    self.showText = ""
    self.entry = ""
    self.x = ""
    self.y = ""
    self.operator = ""
    self.expecty = False
    self.lastOp = True
    self.decimal = False

  def calculate(self, event):
    if (self.operator == '+'):
        return str(mathlib.add(self.x, self.y))
    elif (self.operator == '-'):
        return str(mathlib.sub(self.x, self.y))
    elif (self.operator == '*'):
        return str(mathlib.mul(self.x, self.y))
    elif (self.operator == '/'):
        return str(mathlib.div(self.x, self.y))
    elif (self.operator == '^'):
        return str(mathlib.power(self.x, self.y))
    elif (self.operator == 'nrt'):
        return str(mathlib.nrt(self.x, self.y))
    elif (self.operator == '%'):
        return str(mathlib.mod(self.x, self.y))
    elif (self.operator == 'x!'):
        return str(mathlib.fact(self.x))
    elif (self.operator == 'sqrt'):
        return str(mathlib.sqrt(self.x))
    elif (self.operator == 'sin'):
        return str(mathlib.sin(self.x))
