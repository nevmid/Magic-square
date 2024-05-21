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

    def create_square(self):
        MainWindow.setStyleSheet('''
                                QLineEdit {
                                font: 16pt Arial;
                                border: 5px solid grey;
                                }
                                ''')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        reg_str = ''
        if self.mode == 'Semi-magic':
            if self.range == 20:
                reg_str = '[0-9]|1[0-9]|20'
            elif self.range == 50:
                reg_str = '[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|50'
            elif self.range == 100:
                reg_str = '[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]||5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|100'
        else:
            if self.size == 3:
                reg_str = '[1-9]'
            elif self.size == 4:
                reg_str = '[1-9]|1[0-6]'
            elif self.size == 5:
                reg_str = '[1-9]|1[0-9]|2[0-5]'
            elif self.size == 6:
                reg_str = '[1-9]|1[0-9]|2[0-9]|3[0-6]'
            elif self.size == 7:
                reg_str = '[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]'
            elif self.size == 8:
                reg_str = '[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]||5[0-9]|6[0-4]'
            elif self.size == 9:
                reg_str = '[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]||5[0-9]|6[0-9]|7[0-9]|8[0-1]'
            elif self.size == 10:
                reg_str = '[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]||5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|100'
        regexp = QRegExp(reg_str)
        validator = QRegExpValidator(regexp)
        lineEdits = []
        for i in range(self.size):
            for j in range(self.size):
                self.line_edit = QLineEdit()
                self.line_edit.setMaximumSize(QtCore.QSize(100, 100))
                self.line_edit.setAlignment(Qt.AlignCenter)
                self.line_edit.setValidator(validator)
                self.gridLayout_9.addWidget(self.line_edit, i, j)
                lineEdits.append(self.line_edit)
        if self.mode == 'Semi-magic':
            selected_line = random.sample(lineEdits, self.size)

            for line in selected_line:
                line.setText(str(random.randint(1, self.range//2)))
                line.setEnabled(False)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(310, 65))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.esc_btn = QPushButton(self.frame)
        self.esc_btn.setMaximumSize(QtCore.QSize(80, 40))
        self.esc_btn.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/arrow.ico'))
        self.esc_btn.setIconSize(QSize(50, 30))
        self.gridLayout_5.addWidget(self.esc_btn, 0, 1, 1, 1)
        self.menu_btn_sqr = QPushButton(self.frame)
        self.menu_btn_sqr.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/menu.ico'))
        self.menu_btn_sqr.setIconSize(QSize(50, 30))
        self.gridLayout_5.addWidget(self.menu_btn_sqr, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(500, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.check = QPushButton(self.frame_3)
        self.check.setMinimumSize(QtCore.QSize(30, 30))
        self.check.setMaximumSize(QtCore.QSize(200, 60))
        self.gridLayout.addWidget(self.check, 0, 0, 1, 1)
        if self.mode == 'Semi-magic':
            self.upd_btn = QPushButton(self.frame_3)
            self.upd_btn.setMinimumSize(QtCore.QSize(80, 40))
            self.upd_btn.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/upd.ico'))
            self.upd_btn.setIconSize(QSize(50, 30))
            self.gridLayout.addWidget(self.upd_btn, 0, 1, 1, 1)
            self.upd_btn.clicked.connect(self.create_square)
        self.gridLayout_10.addWidget(self.frame_3, 3, 0, 1, 1, Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.gridlay = QGridLayout(self.frame_4)
        self.lTry = QLabel(self.frame_4)
        self.lTry.setMaximumSize(QSize(200,50))
        self.lTry.setStyleSheet('font: 14pt Arial')
        self.lTry.setHidden(True)
        self.gridlay.addWidget(self.lTry, 0, 0, 1, 1, Qt.AlignHCenter)
        self.try_again = QPushButton(self.frame_4)
        self.try_again.setMaximumSize(QSize(300,50))
        self.try_again.setText('Попробовать снова')
        self.try_again.setHidden(True)
        self.gridlay.addWidget(self.try_again, 1, 0, 1, 1, Qt.AlignHCenter)
        self.gridLayout_10.addWidget(self.frame_4, 2, 0, 1, 1)
        MainWindow.setWindowTitle("Магический квадрат")
        self.check.setText("Проверить")


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