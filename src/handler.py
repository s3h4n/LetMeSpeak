from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime
from pathlib import Path
from ..packages import TextToSpeech
from ..packages import FileHelper
from . import constants


class Handler(object):
    def __init__(self) -> None:
        self.key_list = constants.LANGUAGES.keys()
        self.home = Path.home()
        self.mp3_save_path = f"{self.home}/{constants.AUDIO_DIR_PATH}"
        FileHelper.create_dir(self.mp3_save_path)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.MainWindow = MainWindow

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(
            QtGui.QPixmap("LetMeTalk/resources/LetMeTalk-removebg-preview.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(self.icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.language_select = QtWidgets.QComboBox(self.centralwidget)
        self.language_select.setGeometry(QtCore.QRect(10, 40, 220, 40))
        self.language_select.setObjectName("language_select")

        for language in constants.LANGUAGES:
            self.language_select.addItem(constants.LANGUAGES[language])

        self.language_select.setCurrentText("English")

        self.volume = QtWidgets.QSlider(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(10, 150, 220, 17))
        self.volume.setMinimum(10)
        self.volume.setMaximum(200)
        self.volume.setSingleStep(1)
        self.volume.setProperty("value", 100)
        self.volume.setSliderPosition(100)
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setObjectName("volume")

        self.speed = QtWidgets.QSlider(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(10, 220, 220, 17))
        self.speed.setMinimum(10)
        self.speed.setMaximum(200)
        self.speed.setProperty("value", 100)
        self.speed.setSliderPosition(100)
        self.speed.setOrientation(QtCore.Qt.Horizontal)
        self.speed.setObjectName("speed")

        self.input_area = QtWidgets.QTextEdit(self.centralwidget)
        self.input_area.setGeometry(QtCore.QRect(240, 10, 550, 470))
        self.input_area.setObjectName("input_area")

        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(10, 120, 110, 26))
        self.volume_label.setObjectName("volume_label")
        self.speed_label = QtWidgets.QLabel(self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(10, 190, 100, 26))
        self.speed_label.setObjectName("speed_label")
        self.language_label = QtWidgets.QLabel(self.centralwidget)
        self.language_label.setGeometry(QtCore.QRect(10, 10, 110, 26))
        self.language_label.setObjectName("language_label")

        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(690, 490, 100, 40))
        self.play_btn.setObjectName("play_btn")
        self.play_btn.clicked.connect(self.play_btn_action)

        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(580, 490, 100, 40))
        self.stop_btn.setObjectName("stop_btn")

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(10, 290, 220, 40))
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.clicked.connect(self.reset_btn_action)

        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setGeometry(QtCore.QRect(240, 490, 170, 40))
        self.open_btn.setObjectName("open_btn")
        self.open_btn.clicked.connect(self.open_btn_action)

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(420, 490, 150, 40))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.save_btn_action)

        self.speed_value = QtWidgets.QLabel(self.centralwidget)
        self.speed_value.setGeometry(QtCore.QRect(130, 190, 100, 26))
        self.speed_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.speed_value.setObjectName("speed_value")

        self.volume_value = QtWidgets.QLabel(self.centralwidget)
        self.volume_value.setGeometry(QtCore.QRect(130, 120, 100, 26))
        self.volume_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.volume_value.setObjectName("volume_value")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 260, 220, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 100, 220, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 801, 31))
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

        MainWindow.setTabOrder(self.language_select, self.volume)
        MainWindow.setTabOrder(self.volume, self.speed)
        MainWindow.setTabOrder(self.speed, self.play_btn)
        MainWindow.setTabOrder(self.play_btn, self.stop_btn)
        MainWindow.setTabOrder(self.stop_btn, self.save_btn)
        MainWindow.setTabOrder(self.save_btn, self.open_btn)
        MainWindow.setTabOrder(self.open_btn, self.reset_btn)
        MainWindow.setTabOrder(self.reset_btn, self.input_area)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LetMeSpeak"))
        self.volume_label.setText(_translate("MainWindow", "Volume"))
        self.speed_label.setText(_translate("MainWindow", "Speed"))
        self.input_area.setPlaceholderText(
            _translate("MainWindow", "Paste your text here...")
        )
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.speed_value.setText(_translate("MainWindow", "100"))
        self.volume_value.setText(_translate("MainWindow", "100"))
        self.open_btn.setText(_translate("MainWindow", "Open a Text File"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.language_label.setText(_translate("MainWindow", "Language"))
        self.save_btn.setText(_translate("MainWindow", "Save as mp3"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    @staticmethod
    def generate_name() -> str:
        current_date = date.today().strftime("%d-%m-%Y")
        current_time = datetime.now().strftime("%H-%M-%S")
        return f"Audio_{current_date}-{current_time}"

    def setup_audio(self):
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
        self.setup_audio()
        self.tts.say()

    def reset_btn_action(self):
        self.language_select.setCurrentText("English")
        self.input_area.clear()
        self.speed.setValue(100)
        self.volume.setValue(100)

        self.speed_value.setText("100")
        self.volume_value.setText("100")

    def save_btn_action(self):
        self.setup_audio()
        file_name = self.generate_name()
        self.tts.save_to_mp3(f"{self.mp3_save_path}/{file_name}.mp3")

        info_dialog = QtWidgets.QMessageBox()
        info_dialog.setWindowTitle("Info")
        info_dialog.setIcon(QtWidgets.QMessageBox.Information)
        info_dialog.setText(f"Audio saved to {self.mp3_save_path}/{file_name}.mp3")
        info_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        info_dialog.setDefaultButton(QtWidgets.QMessageBox.Ok)
        info_dialog.exec_()

    def open_btn_action(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "Open a Text File", "", "Text Files (*.txt)"
        )

        if file_path[0]:
            with open(file_path[0], "r") as file:
                self.input_area.setText(file.read())
