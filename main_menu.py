from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGraphicsDropShadowEffect
import modes


def setupUi(MainWindow, self):
    MainWindow.setObjectName("MainWindow")
    MainWindow.setMinimumSize(QtCore.QSize(650, 300))
    centralwidget = QWidget(MainWindow)
    centralwidget.setMinimumSize(QtCore.QSize(300, 300))
    gridLayout = QtWidgets.QGridLayout(centralwidget)
    frame = QtWidgets.QFrame(centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
    frame.setSizePolicy(sizePolicy)
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    gridLayout_buttons = QtWidgets.QGridLayout(frame)
    gridLayout2 = QtWidgets.QGridLayout()
    play_button = QPushButton(frame)
    sizePolicy_btn = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
    sizePolicy_btn.setHorizontalStretch(0)
    sizePolicy_btn.setVerticalStretch(0)
    sizePolicy_btn.setHeightForWidth(play_button.sizePolicy().hasHeightForWidth())
    play_button.setSizePolicy(sizePolicy_btn)
    play_button.setMaximumSize(QtCore.QSize(190, 55))
    gridLayout2.addWidget(play_button, 0, 0, 1, 1)
    rules_button = QPushButton(frame)
    sizePolicy_btn.setHeightForWidth(rules_button.sizePolicy().hasHeightForWidth())
    rules_button.setSizePolicy(sizePolicy_btn)
    rules_button.setMaximumSize(QtCore.QSize(190, 55))
    gridLayout2.addWidget(rules_button, 1, 0, 1, 1)
    exit_button = QPushButton(frame)
    sizePolicy_btn.setHeightForWidth(exit_button.sizePolicy().hasHeightForWidth())
    exit_button.setSizePolicy(sizePolicy_btn)
    exit_button.setMaximumSize(QtCore.QSize(190, 55))
    gridLayout2.addWidget(exit_button, 2, 0, 1, 1)
    gridLayout_buttons.addLayout(gridLayout2, 0, 0, 1, 1)
    gridLayout.addWidget(frame, 1, 0, 1, 1)
    frame_2 = QtWidgets.QFrame(centralwidget)
    frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    gridLayout_label = QtWidgets.QGridLayout(frame_2)
    label = QtWidgets.QLabel(frame_2)
    label.setStyleSheet("color: black;font: 60pt Century Gothic;")
    shadows = QGraphicsDropShadowEffect()
    shadows.setBlurRadius(5)
    shadows.setColor(QColor(0, 0, 0, 127))
    shadows.setOffset(4, 4)
    label.setGraphicsEffect(shadows)
    gridLayout_label.addWidget(label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
    gridLayout.addWidget(frame_2, 0, 0, 1, 1)
    MainWindow.setCentralWidget(centralwidget)
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
    MainWindow.setWindowTitle("Магический квадрат")
    play_button.setText("Играть")
    rules_button.setText("Как играть")
    exit_button.setText("Выход")
    label.setText("Магический квадрат")
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(1, 2)
    exit_button.clicked.connect(lambda: QApplication.quit())
    exit_button.setGraphicsEffect(shadow)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(1, 2)
    rules_button.clicked.connect(self.show_rules)
    rules_button.setGraphicsEffect(shadow)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(2)
    shadow.setColor(QColor(0, 0, 0, 127))
    shadow.setOffset(1, 2)
    play_button.clicked.connect(lambda: modes.Mode(self, MainWindow))
    play_button.setGraphicsEffect(shadow)
