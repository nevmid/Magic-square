from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject
import sys, random
import main_menu, modes, Difficult

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
                                font: 16pt Century Gothic;
                                border: 5px solid grey;
                                }
                                QPushButton{
                                 font: 20pt Century Gothic;
                                 background-color: transparent;
                                 border: none;
                                 }
                                 QMainWindow { 
                                 background-image: url(newf.png);
                                 background-repeat: no-repeat;
                                 background-position:center;
                                 background-size: cover;
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
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(2)
                shadow.setColor(QColor(0, 0, 0, 127))
                shadow.setOffset(3, 3)
                self.line_edit.setGraphicsEffect(shadow)
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
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setColor(QColor(0, 0, 0, 127))
        shadow.setOffset(2, 2)
        self.esc_btn.setGraphicsEffect(shadow)
        self.esc_btn.setMaximumSize(QtCore.QSize(80, 40))
        self.esc_btn.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/arrow.ico'))
        self.esc_btn.setIconSize(QSize(50, 30))
        self.esc_btn.setCursor(Qt.PointingHandCursor)
        self.gridLayout_5.addWidget(self.esc_btn, 0, 1, 1, 1)
        self.menu_btn_sqr = QPushButton(self.frame)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setColor(QColor(0, 0, 0, 127))
        shadow.setOffset(2, 2)
        self.menu_btn_sqr.setGraphicsEffect(shadow)
        self.menu_btn_sqr.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/menu.ico'))
        self.menu_btn_sqr.setIconSize(QSize(50, 30))
        self.menu_btn_sqr.setCursor(Qt.PointingHandCursor)
        self.gridLayout_5.addWidget(self.menu_btn_sqr, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(500, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.check = QPushButton(self.frame_3)
        self.check.resize(QtCore.QSize(300, 60))
        self.check.setCursor(Qt.PointingHandCursor)
        self.gridLayout.addWidget(self.check, 0, 0, 1, 1)
        if self.mode == 'Semi-magic':
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(2)
            shadow.setColor(QColor(0, 0, 0, 127))
            shadow.setOffset(2, 2)
            self.upd_btn = QPushButton(self.frame_3)
            self.upd_btn.setGraphicsEffect(shadow)
            self.upd_btn.resize(QtCore.QSize(80, 60))
            self.upd_btn.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/upd.ico'))
            self.upd_btn.setIconSize(QSize(50, 30))
            self.upd_btn.setCursor(Qt.PointingHandCursor)
            self.gridLayout.addWidget(self.upd_btn, 0, 1, 1, 1)
            self.upd_btn.clicked.connect(self.create_square)
        self.gridLayout_10.addWidget(self.frame_3, 3, 0, 1, 1, Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.gridlay = QGridLayout(self.frame_4)
        self.lTry = QLabel(self.frame_4)
        self.lTry.resize(QSize(500,40))
        self.lTry.setStyleSheet('font: 20pt Century Gothic')
        self.lTry.setHidden(True)
        self.gridlay.addWidget(self.lTry, 0, 0, 1, 1, Qt.AlignHCenter)
        self.try_again = QPushButton(self.frame_4)
        self.try_again.resize(QSize(500,40))
        self.try_again.setText('Попробовать снова')
        self.try_again.setHidden(True)
        self.try_again.setCursor(Qt.PointingHandCursor)
        self.try_again.setStyleSheet('font: 16pt Century Gothic; border: none')
        self.gridlay.addWidget(self.try_again, 1, 0, 1, 1, Qt.AlignHCenter)
        self.gridLayout_10.addWidget(self.frame_4, 2, 0, 1, 1)
        MainWindow.setWindowTitle("Магический квадрат")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setColor(QColor(0, 0, 0, 127))
        shadow.setOffset(1, 2)
        self.check.setText("Проверить")
        self.check.setGraphicsEffect(shadow)
        self.check.clicked.connect(self.create_matrix)
        self.menu_btn_sqr.clicked.connect(self.__init__)
        self.esc_btn.clicked.connect(lambda: Difficult.difficulty(self, MainWindow))

    def create_matrix(self):
        try:
            items = [lineEdit.text() for lineEdit in self.frame_2.findChildren(QtWidgets.QLineEdit)]
            matr = []
            flag = False
            j = 0
            for i in range(self.size):
                list = []
                while len(list) != self.size:
                    list.append(int(items[j]))
                    j += 1
                matr.append(list)
            if self.mode == 'Magic':
                for i in range(self.size ** 2):
                    if items.count(items[i]) > 1:
                        flag = True
                        break
            self.result(matr, flag)
        except:
            self.error()

    def error(self):
        error_msg = QMessageBox()
        error_msg.setWindowTitle('Ошибка')
        error_msg.setStyleSheet('font: 14pt Arial')
        error_msg.setIcon(QMessageBox.Warning)
        error_msg.setText('Нужно заполнить все ячейки!')
        error_msg.exec_()

    def SameNum_error(self):
        error_msg = QMessageBox()
        error_msg.setWindowTitle('Ошибка')
        error_msg.setStyleSheet('font: 14pt Arial')
        error_msg.setIcon(QMessageBox.Warning)
        error_msg.setText('Числа во всех ячейках должны отличаться')
        error_msg.exec_()

    def check_matrix(self, matrix):
        first = sum(matrix[0])
        first_diag = 0
        second_diag = 0
        for k in range(1, self.size):
            if sum(matrix[k]) != first:
                return False
        for k in range(self.size):
            if sum([row[k] for row in matrix]) != first:
                return False
        if self.mode == 'Magic':
            for i in range(self.size):
                first_diag += matrix[i][i]
            if first_diag != first:
                return False
            for i in range(self.size):
                second_diag += matrix[i][self.size - i - 1]
            if second_diag != first:
                return False
        return True

    def result(self, matrix, flag):
        if flag:
            self.SameNum_error()
        else:
            if self.check_matrix(matrix):
                self.win()
            else:
                self.lose()

    def win(self):
        lineEdits = MainWindow.findChildren(QtWidgets.QLineEdit)
        for lineedit in lineEdits:
            lineedit.setReadOnly(True)
            lineedit.setStyleSheet('''background-color: lightgreen;
                                       font:16pt Century Gothic;
                                       border: 5px solid grey;
                                            ''')
        self.lTry.setText('Вы выиграли!')
        self.lTry.setHidden(False)

    def lose(self):
        lineEdits = MainWindow.findChildren(QtWidgets.QLineEdit)
        for lineedit in lineEdits:
            lineedit.setReadOnly(True)
            lineedit.setStyleSheet(''' background-color: red;
                                       font:16pt Century Gothic;
                                       border: 5px solid grey;
                                          ''')
        self.lTry.setText('Вы проиграли!')
        self.lTry.setHidden(False)
        self.try_again.setHidden(False)
        self.try_again.clicked.connect(lambda: self.Try_again(lineEdits))

    def Try_again(self, edits):
        for line in edits:
            line.setStyleSheet('''background-color: white;
                                       font:16pt Century Gothic;
                                       border: 5px solid grey;
                                          ''')
            if line.isReadOnly() and (line.isEnabled()):
                line.setText('')
                line.setReadOnly(False)
        self.lTry.setHidden(True)
        self.try_again.setHidden(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.resize(1920, 1080)
    ui = Magic_Square()
    MainWindow.showMaximized()
    sys.exit(app.exec_())