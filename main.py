from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import *
from PyQt5.QtCore import QObject
import sys

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(650, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 300))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_buttons = QtWidgets.QGridLayout(self.frame)
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.play_button = QPushButton(self.frame)
        sizePolicy_btn = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy_btn.setHorizontalStretch(0)
        sizePolicy_btn.setVerticalStretch(0)
        sizePolicy_btn.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy_btn)
        self.play_button.setMaximumSize(QtCore.QSize(300, 80))
        self.gridLayout2.addWidget(self.play_button, 0, 0, 1, 1)
        self.rules_button = QPushButton(self.frame)
        sizePolicy_btn.setHeightForWidth(self.rules_button.sizePolicy().hasHeightForWidth())
        self.rules_button.setSizePolicy(sizePolicy_btn)
        self.rules_button.setMaximumSize(QtCore.QSize(300, 80))
        self.gridLayout2.addWidget(self.rules_button, 1, 0, 1, 1)
        self.exit_button = QPushButton(self.frame)
        sizePolicy_btn.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy_btn)
        self.exit_button.setMaximumSize(QtCore.QSize(300, 80))
        self.gridLayout2.addWidget(self.exit_button, 2, 0, 1, 1)
        self.gridLayout_buttons.addLayout(self.gridLayout2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_label = QtWidgets.QGridLayout(self.frame_2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("color: black;font: 50pt Century Gothic;")
        self.gridLayout_label.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.inter_menu()

    def inter_menu(self):
        MainWindow.setWindowTitle("Магичесий квадрат")
        self.play_button.setText("Играть")
        self.rules_button.setText("Как играть")
        self.exit_button.setText("Выход")
        self.label.setText("Магический квадрат")
        self.exit_button.clicked.connect(lambda: QApplication.quit())
        self.rules_button.clicked.connect(self.show_rules)


    def show_rules(self):
        msg = QMessageBox()
        msg.setWindowTitle('Правила')
        msg.setIcon(QMessageBox.Question)
        msg.setWindowIcon(QtGui.QIcon('pr2.png'))
        msg.setStyleSheet('font: 14pt Arial')
        msg.setText('Магический квадрат - это n * n квадратная сетка, заполненная'
                    ' различными целыми положительными числами в диапазоне 1, 2 , . . . , n *n'
                    ' таким образом, что каждая ячейка содержит целое число, а сумма целых'
                    ' чисел в каждой строке, столбце и диагонали равна.\nНеобходимо заполнить каждую ячейку так,'
                    ' чтобы суммы в каждой строке, столбце и диагонали были равными.')
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.resize(1080, 720)
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
