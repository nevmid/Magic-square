from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QPushButton
import modes


def difficulty(self, MainWindow):
    MainWindow.setWindowTitle("Магический квадрат")
    centralwidget = QtWidgets.QWidget(MainWindow)
    gridLayout_diff_main = QtWidgets.QGridLayout(centralwidget)
    frame_2 = QtWidgets.QFrame(centralwidget)
    frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    gridLayout_diff_frame = QtWidgets.QGridLayout(frame_2)
    gridLayout_diff_btn = QtWidgets.QGridLayout()
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
                                    background-image: url(images/newf.png);
                                    background-repeat: no-repeat;
                                    background-position:center;
                                    background-size: cover;
                                    }
                                                            ''')
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
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(2)
            shadow.setColor(QColor(0, 0, 0, 127))
            shadow.setOffset(1, 2)
            btn = QPushButton(buttons[i][j])
            btn.setGraphicsEffect(shadow)
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
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(2, 2)
    menu_btn.setIcon(QIcon('images/menu.ico'))
    menu_btn.setIconSize(QSize(50, 30))
    menu_btn.setGraphicsEffect(shadow)
    menu_btn.setCursor(Qt.PointingHandCursor)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(2, 2)
    esc_b.setIcon(QIcon('images/arrow.ico'))
    esc_b.setIconSize(QSize(50, 30))
    esc_b.setGraphicsEffect(shadow)
    esc_b.setMinimumSize(QtCore.QSize(80, 40))
    esc_b.setCursor(Qt.PointingHandCursor)
    esc_b.clicked.connect(lambda: modes.Mode(self, MainWindow))
    menu_btn.clicked.connect(self.__init__)