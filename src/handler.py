from PyQt5 import QtCore, QtWidgets
from ..packages import Speech


class Handler(object):
    def __init__(self) -> None:
        self.s = Speech()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.amp = QtWidgets.QSlider(self.centralwidget)
        self.amp.setGeometry(QtCore.QRect(10, 60, 200, 17))
        self.amp.setSingleStep(1)
        self.amp.setSliderPosition(50)
        self.amp.setOrientation(QtCore.Qt.Horizontal)
        self.amp.setObjectName("amp")

        self.pitch = QtWidgets.QSlider(self.centralwidget)
        self.pitch.setGeometry(QtCore.QRect(10, 140, 200, 17))
        self.pitch.setSliderPosition(50)
        self.pitch.setOrientation(QtCore.Qt.Horizontal)
        self.pitch.setObjectName("pitch")

        self.speed = QtWidgets.QSlider(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(10, 220, 200, 17))
        self.speed.setSliderPosition(50)
        self.speed.setOrientation(QtCore.Qt.Horizontal)
        self.speed.setObjectName("speed")

        self.input_area = QtWidgets.QTextEdit(self.centralwidget)
        self.input_area.setGeometry(QtCore.QRect(230, 60, 560, 470))
        self.input_area.setObjectName("input_area")

        self.amp_label = QtWidgets.QLabel(self.centralwidget)
        self.amp_label.setGeometry(QtCore.QRect(10, 20, 90, 26))
        self.amp_label.setObjectName("amp_label")
        self.pitch_label = QtWidgets.QLabel(self.centralwidget)
        self.pitch_label.setGeometry(QtCore.QRect(10, 100, 80, 26))
        self.pitch_label.setObjectName("pitch_label")
        self.speed_label = QtWidgets.QLabel(self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(10, 180, 80, 26))
        self.speed_label.setObjectName("speed_label")
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(230, 20, 180, 26))
        self.input_label.setObjectName("input_label")

        self.speed_value = QtWidgets.QLabel(self.centralwidget)
        self.speed_value.setGeometry(QtCore.QRect(130, 180, 80, 26))
        self.speed_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.speed_value.setObjectName("speed_value")
        self.pitch_value = QtWidgets.QLabel(self.centralwidget)
        self.pitch_value.setGeometry(QtCore.QRect(130, 100, 80, 26))
        self.pitch_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.pitch_value.setObjectName("pitch_value")
        self.amp_value = QtWidgets.QLabel(self.centralwidget)
        self.amp_value.setGeometry(QtCore.QRect(130, 20, 80, 26))
        self.amp_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.amp_value.setObjectName("amp_value")

        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(10, 420, 210, 50))
        self.play_btn.setObjectName("play_btn")
        self.play_btn.setCheckable(True)
        self.play_btn.setChecked(False)
        self.play_btn.clicked.connect(self.activate)

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(10, 480, 210, 50))
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.clicked.connect(self.reset)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 40, 380, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.speed.sliderMoved["int"].connect(self.speed_value.setNum)
        self.amp.sliderMoved["int"].connect(self.amp_value.setNum)
        self.pitch.sliderMoved["int"].connect(self.pitch_value.setNum)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LetMeSpeak"))
        self.amp_label.setText(_translate("MainWindow", "Ampitude"))
        self.pitch_label.setText(_translate("MainWindow", "Pitch"))
        self.speed_label.setText(_translate("MainWindow", "Speed"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.input_label.setText(_translate("MainWindow", "Paste your text here"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.speed_value.setText(_translate("MainWindow", "50"))
        self.pitch_value.setText(_translate("MainWindow", "50"))
        self.amp_value.setText(_translate("MainWindow", "50"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def activate(self) -> None:
        if self.play_btn.isChecked():
            self.s.say(
                ampitude=self.amp.value(),
                pitch=self.pitch.value(),
                speed=self.speed.value(),
                words=self.input_area.toPlainText(),
            )
            self.play_btn.setText("Stop")
        else:
            self.s.stop()
            self.play_btn.setText("Play")

    def reset(self) -> None:
        self.amp.setValue(50)
        self.pitch.setValue(50)
        self.speed.setValue(50)
        self.input_area.clear()

        self.amp_value.setNum(50)
        self.pitch_value.setNum(50)
        self.speed_value.setNum(50)
