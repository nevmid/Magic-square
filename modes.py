import Difficult
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


def Mode(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    centralwidget = QtWidgets.QWidget(MainWindow)
    centralwidget.setObjectName("centralwidget")
    gridLayout_4 = QtWidgets.QGridLayout(centralwidget)
    gridLayout_4.setObjectName("gridLayout_4")
    frame = QtWidgets.QFrame(centralwidget)
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    frame.setObjectName("frame")
    gridLayout = QtWidgets.QGridLayout(frame)
    gridLayout.setObjectName("gridLayout")
    pushButton = QtWidgets.QPushButton(frame)
    pushButton.setObjectName("pushButton")
    pushButton.setMinimumSize(QtCore.QSize(80, 40))
    pushButton.setIconSize(QSize(50, 30))
    pushButton.setCursor(Qt.PointingHandCursor)
    gridLayout.addWidget(pushButton, 0, 0, 1, 1)
    gridLayout_4.addWidget(frame, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    frame_2 = QtWidgets.QFrame(centralwidget)
    frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_2.setObjectName("frame_2")
    gridLayout_3 = QtWidgets.QGridLayout(frame_2)
    gridLayout_3.setObjectName("gridLayout_3")
    gridLayout_2 = QtWidgets.QGridLayout()
    gridLayout_2.setObjectName("gridLayout_2")
    pushButton_3 = QtWidgets.QPushButton(frame_2)
    pushButton_3.setMaximumSize(QtCore.QSize(330, 100))
    pushButton_3.setObjectName("pushButton_3")
    gridLayout_2.addWidget(pushButton_3, 0, 0, 1, 1)
    pushButton_4 = QtWidgets.QPushButton(frame_2)
    pushButton_4.setMaximumSize(QtCore.QSize(330, 100))
    pushButton_4.setObjectName("pushButton_4")
    gridLayout_2.addWidget(pushButton_4, 1, 0, 1, 1)
    gridLayout_3.addLayout(gridLayout_2, 0, 0, 1, 1)
    gridLayout_4.addWidget(frame_2, 1, 0, 1, 1)
    frame_3 = QtWidgets.QFrame(centralwidget)
    frame_3.setMaximumSize(QtCore.QSize(16777215, 200))
    frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_3.setObjectName("frame_3")
    gridLayout_4.addWidget(frame_3, 2, 0, 1, 1)
    MainWindow.setCentralWidget(centralwidget)
    MainWindow.setWindowTitle("Магический квадрат")
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(2, 2)
    pushButton.setIcon(QIcon('C:/Users/Admin/PycharmProjects/pythonProject1/menu.ico'))
    pushButton.setGraphicsEffect(shadow)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(1, 2)
    pushButton_3.setText("Магический")
    pushButton_3.setGraphicsEffect(shadow)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(1, 2)
    pushButton_4.setText("Полумагический")
    pushButton_4.setGraphicsEffect(shadow)
    pushButton_3.clicked.connect(lambda: num_of_butt(self, MainWindow))
    pushButton_4.clicked.connect(lambda: num_of_butt(self, MainWindow))
    pushButton.clicked.connect(self.__init__)
    MainWindow.setStyleSheet('''QPushButton{
                                 font: 20pt Century Gothic;
                                 background-color: transparent;
                                 border: none;
                                 }

                                 QPushButton:hover {
                                 background-color: transparent;
                                 border: none;
                                 font: 22pt;
                                 }

                                 QPushButton:pressed{
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

def num_of_butt(self, MainWindow):
    self.mode = ''
    if (self.sender()).text() == 'Магический':
        self.mode = 'Magic'
        self.x = 2
        self.y = 4
    else:
        self.mode = 'Semi-magic'
        self.x = 3
        self.y = 3
    Difficult.difficulty(self, MainWindow)

