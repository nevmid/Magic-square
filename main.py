from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import *
from PyQt5.QtCore import QObject
import sys, random


class Magic_Square(QMainWindow):
    def __init__(self):
        super(Magic_Square, self).__init__()
        self.size = 0
        self.range = 0
        self.x = 0
        self.y = 0
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
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
        self.inter_menu(MainWindow)

    def inter_menu(self, MainWindow):
        MainWindow.setWindowTitle("Магичесий квадрат")
        self.play_button.setText("Играть")
        self.rules_button.setText("Как играть")
        self.exit_button.setText("Выход")
        self.label.setText("Магический квадрат")
        self.exit_button.clicked.connect(lambda: QApplication.quit())
        self.rules_button.clicked.connect(self.show_rules)
        self.play_button.clicked.connect(lambda: self.Mode(MainWindow))



    def show_rules(self):
        msg = QMessageBox()
        msg.setWindowTitle('Как играть')
        msg.setIcon(QMessageBox.Question)
        msg.setWindowIcon(QtGui.QIcon('pr2.png'))
        msg.setStyleSheet('')
        msg.setText('Магический квадрат - это n * n квадратная сетка, заполненная'
                    ' различными целыми положительными числами в диапазоне 1, 2 , . . . , n *n'
                    ' таким образом, что каждая ячейка содержит целое число, а сумма целых'
                    ' чисел в каждой строке, столбце и диагонали равна.\nНеобходимо заполнить каждую ячейку так,'
                    ' чтобы суммы в каждой строке, столбце и диагонали были равными.')
        msg.exec_()

    def Mode(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4.addWidget(self.frame_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.mode_btn(MainWindow)

    def mode_btn(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Магический квадрат"))
        self.pushButton.setText(_translate("MainWindow", "Меню"))
        self.pushButton_3.setText(_translate("MainWindow", "Магический"))
        self.pushButton_4.setText(_translate("MainWindow", "Полумагический"))
        self.pushButton.clicked.connect(self.__init__)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet('''
                             QPushButton{
                             font: 14pt Arial;
                             background-color: lightgrey;
                             border-radius: 10px;
                             border: 2px solid black;
                             }

                             QPushButton:hover {
                             background-color:white;
                             }

                             QPushButton:pressed{
                             background-color: grey;
                             }
                                                     ''')
    MainWindow = QMainWindow()
    MainWindow.resize(1080, 720)
    ui = Magic_Square()
    MainWindow.show()
    sys.exit(app.exec_())