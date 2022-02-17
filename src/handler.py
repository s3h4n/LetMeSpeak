from PyQt5 import QtCore, QtGui, QtWidgets
from . import constants
from ..packages import TextToSpeech


class Handler(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(
            QtGui.QPixmap(
                "/home/sehan/Python-Projects/LetMeTalk/resources/LetMeTalk-removebg-preview.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(self.icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.volume = QtWidgets.QSlider(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(10, 60, 200, 17))
        self.volume.setMinimum(10)
        self.volume.setMaximum(200)
        self.volume.setSingleStep(1)
        self.volume.setProperty("value", 100)
        self.volume.setSliderPosition(100)
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setObjectName("volume")

        self.speed = QtWidgets.QSlider(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(10, 130, 200, 17))
        self.speed.setMinimum(10)
        self.speed.setMaximum(200)
        self.speed.setProperty("value", 100)
        self.speed.setSliderPosition(100)
        self.speed.setOrientation(QtCore.Qt.Horizontal)
        self.speed.setObjectName("speed")

        self.input_area = QtWidgets.QTextEdit(self.centralwidget)
        self.input_area.setGeometry(QtCore.QRect(230, 60, 560, 410))
        self.input_area.setObjectName("input_area")

        self.language_select = QtWidgets.QComboBox(self.centralwidget)
        self.language_select.setGeometry(QtCore.QRect(340, 480, 230, 50))
        self.language_select.setObjectName("language_select")

        self.key_list = constants.LANGUAGES.keys()

        for language in constants.LANGUAGES:
            self.language_select.addItem(constants.LANGUAGES[language])

        self.language_select.setCurrentText("English")

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(580, 480, 100, 50))
        self.save_btn.setObjectName("save_btn")

        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(690, 480, 100, 50))
        self.play_btn.setObjectName("play_btn")
        self.play_btn.clicked.connect(self.play_btn_action)

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(230, 480, 100, 50))
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.clicked.connect(self.reset_btn_action)

        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(10, 20, 90, 26))
        self.volume_label.setObjectName("volume_label")

        self.speed_label = QtWidgets.QLabel(self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(10, 90, 80, 26))
        self.speed_label.setObjectName("speed_label")

        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(230, 20, 180, 26))
        self.input_label.setObjectName("input_label")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 40, 380, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.speed_value = QtWidgets.QLabel(self.centralwidget)
        self.speed_value.setGeometry(QtCore.QRect(130, 90, 80, 26))
        self.speed_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.speed_value.setObjectName("speed_value")

        self.volume_value = QtWidgets.QLabel(self.centralwidget)
        self.volume_value.setGeometry(QtCore.QRect(130, 20, 80, 26))
        self.volume_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.volume_value.setObjectName("volume_value")

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
        self.actionAbout.triggered.connect(self.about_dialog)

        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.speed.sliderMoved["int"].connect(self.speed_value.setNum)
        self.volume.sliderMoved["int"].connect(self.volume_value.setNum)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LetMeSpeak"))
        self.volume_label.setText(_translate("MainWindow", "Volume"))
        self.speed_label.setText(_translate("MainWindow", "Speed"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.input_label.setText(_translate("MainWindow", "Paste your text here"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.speed_value.setText(_translate("MainWindow", "100"))
        self.volume_value.setText(_translate("MainWindow", "100"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def about_dialog(self):
        about_dialog = QtWidgets.QMessageBox()
        about_dialog.setWindowTitle("About")

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(
            QtGui.QPixmap("LetMeTalk/resources/LetMeTalk-removebg-preview.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        about_dialog.setIconPixmap(self.icon.pixmap(QtCore.QSize(180, 180)))

        about_dialog.setText(
            "\n<h3 style='font-family:ubuntu,sans-serif;'>LetMeSpeak</h3>"
        )
        about_dialog.setInformativeText(constants.ABOUT)

        about_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        about_dialog.setDefaultButton(QtWidgets.QMessageBox.Ok)

        about_dialog.exec_()

    def play_btn_action(self):
        for key in self.key_list:
            if constants.LANGUAGES[key] == self.language_select.currentText():
                language = key
                break

        self.tts = TextToSpeech(
            text=self.input_area.toPlainText(),
            language=language,
            speed=self.speed.value(),
            volume=self.volume.value(),
        )

        self.tts.say()

    def reset_btn_action(self):
        self.language_select.setCurrentText("English")
        self.input_area.clear()
        self.speed.setValue(100)
        self.volume.setValue(100)

        self.speed_value.setText("MainWindow", "100")
        self.volume_value.setText("MainWindow", "100")
