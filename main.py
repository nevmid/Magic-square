from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import *
from PyQt5.QtCore import QObject
import sys, random
import main_menu, modes

class Magic_Square(QMainWindow):
    def __init__(self):
        super(Magic_Square, self).__init__()
        self.size = 0
        self.range = 0
        self.x = 0
        self.y = 0
        main_menu.setupUi(MainWindow, self)


    def show_rules(self):
        msg = QMessageBox()
        msg.setWindowTitle('Как играть')
        msg.setIcon(QMessageBox.Question)
        msg.setStyleSheet('')
        msg.setText('Магический квадрат - это n * n квадратная сетка, заполненная'
                    ' различными целыми положительными числами в диапазоне 1, 2 , . . . , n *n'
                    ' таким образом, что каждая ячейка содержит целое число, а сумма целых'
                    ' чисел в каждой строке, столбце и диагонали равна.\nНеобходимо заполнить каждую ячейку так,'
                    ' чтобы суммы в каждой строке, столбце и диагонали были равными.')
        msg.exec_()


    def difficulty(self):
        MainWindow.setWindowTitle("Магический квадрат")
        centralwidget = QtWidgets.QWidget(MainWindow)
        gridLayout_diff_main = QtWidgets.QGridLayout(centralwidget)
        frame_2 = QtWidgets.QFrame(centralwidget)
        frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        gridLayout_diff_frame = QtWidgets.QGridLayout(frame_2)
        gridLayout_diff_btn = QtWidgets.QGridLayout()
        buttons = []
        if self.mode == 'Semi-magic':
            buttons = [['3x3 0-20', '3x3 0-50', '3x3 0-100'],
                       ['4x4 0-20', '4x4 0-50', '4x4 0-100'],
                       ['5x5 0-20', '5x5 0-50', '5x5 0-100']]
        elif self.mode == 'Magic':
            buttons = [['3x3', '4x4', '5x5', '6x6'],
                       ['7x7', '8x8', '9x9', '10x10']]
        for i in range(self.x):
            for j in range(self.y):
                btn = QPushButton(buttons[i][j])
                btn.setMaximumSize(QtCore.QSize(200, 50))
                gridLayout_diff_btn.addWidget(btn, i, j, 1, 1)
                btn.clicked.connect(self.size_and_range)
        gridLayout_diff_frame.addLayout(gridLayout_diff_btn, 0, 0, 1, 1)
        gridLayout_diff_main.addWidget(frame_2, 1, 0, 1, 1)
        frame = QtWidgets.QFrame(centralwidget)
        frame.setMaximumSize(QtCore.QSize(200, 65))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        gridLayout_menu = QtWidgets.QGridLayout(frame)
        menu_btn = QPushButton(frame)
        menu_btn.setMinimumSize(QtCore.QSize(80, 40))
        gridLayout_menu.addWidget(menu_btn, 0, 0, 1, 1)
        esc_b = QPushButton(frame)
        esc_b.setMaximumSize(QtCore.QSize(80, 40))
        gridLayout_menu.addWidget(esc_b, 0, 1, 1, 1)
        gridLayout_diff_main.addWidget(frame, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        MainWindow.setCentralWidget(centralwidget)
        menu_btn.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/menu.ico'))
        menu_btn.setIconSize(QSize(50, 30))
        esc_b.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/arrow.ico'))
        esc_b.setIconSize(QSize(50, 30))
        esc_b.setMinimumSize(QtCore.QSize(80, 40))
        esc_b.clicked.connect(lambda: modes.Mode(self, MainWindow))
        menu_btn.clicked.connect(self.__init__)


    def size_and_range(self):
        sender = self.sender()
        if self.mode == 'Semi-magic':
            self.size = int((sender.text())[0])
            self.range = int((sender.text())[6:])
        else:
            self.size = int((sender.text())[0])
            if self.size == 1:
                self.size = 10
        self.create_square()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet('''
                         QPushButton{
                         font: 14pt Arial;
                         background-color: transparent;
                         border: none;
                         }

                         QPushButton:hover {
                         background-color: transparent;
                         border: none;
                         }

                         QPushButton:pressed{
                         background-color: transparent;
                         border: none;
                         }
                                                 ''')
    MainWindow = QMainWindow()
    MainWindow.resize(1080, 720)
    ui = Magic_Square()
    MainWindow.show()
    sys.exit(app.exec_())