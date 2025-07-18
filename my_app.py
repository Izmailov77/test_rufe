from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidgets,
       QHBoxLayout, QVBoxLayout,
       QGrouoBox, QRadioButton,
       QRushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

class MaiWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.Show()

    def initUI(self):
        ''' создаёт графически элементы '''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app = QApplication([])
mw = MaiWin()
app.exec_()