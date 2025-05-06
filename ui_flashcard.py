from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setAlignment(QtCore.Qt.AlignLeft)  

        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_geri.setIcon(icon)
        self.pushButton_geri.setDefault(True)
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout_3.addWidget(self.pushButton_geri)

        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_anasayfa.setIcon(icon1)
        self.pushButton_anasayfa.setDefault(True)
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout_3.addWidget(self.pushButton_anasayfa)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_kelime = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.pushButton_kelime.sizePolicy().hasHeightForWidth())
        self.pushButton_kelime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        self.pushButton_kelime.setFont(font)
        self.pushButton_kelime.setDefault(True)
        self.pushButton_kelime.setObjectName("pushButton_kelime")
        self.verticalLayout.addWidget(self.pushButton_kelime)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignCenter)  

        top_button_font = QtGui.QFont()
        top_button_font.setPointSize(20)

        self.pushButton_bilmiyom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bilmiyom.setFont(top_button_font)
        self.pushButton_bilmiyom.setDefault(True)
        self.pushButton_bilmiyom.setObjectName("pushButton_bilmiyom")
        self.horizontalLayout.addWidget(self.pushButton_bilmiyom)

        self.pushButton_orta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_orta.setFont(top_button_font)
        self.pushButton_orta.setDefault(True)
        self.pushButton_orta.setObjectName("pushButton_orta")
        self.horizontalLayout.addWidget(self.pushButton_orta)

        self.pushButton_biliyom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_biliyom.setFont(top_button_font)
        self.pushButton_biliyom.setDefault(True)
        self.pushButton_biliyom.setObjectName("pushButton_biliyom")
        self.horizontalLayout.addWidget(self.pushButton_biliyom)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_onceki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_onceki.setFont(top_button_font)
        self.pushButton_onceki.setDefault(True)
        self.pushButton_onceki.setObjectName("pushButton_onceki")
        self.horizontalLayout_2.addWidget(self.pushButton_onceki)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)

        self.pushButton_sonraki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sonraki.setFont(top_button_font)
        self.pushButton_sonraki.setDefault(True)
        self.pushButton_sonraki.setObjectName("pushButton_sonraki")
        self.horizontalLayout_2.addWidget(self.pushButton_sonraki)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        dark_stylesheet = """
        QWidget {
            background-color: #2e2e2e;
            color: white;
        }
        QPushButton {
            background-color: #555555;
            color: white;
            border: 1px solid #777777;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #777777;
        }
        """
        MainWindow.setStyleSheet(dark_stylesheet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kelime Uygulaması"))
        self.pushButton_kelime.setText(_translate("MainWindow", "kelime"))
        self.pushButton_bilmiyom.setText(_translate("MainWindow", "Bilmiyorum"))
        self.pushButton_orta.setText(_translate("MainWindow", "      Orta      "))
        self.pushButton_biliyom.setText(_translate("MainWindow", "  Biliyorum  "))
        self.pushButton_onceki.setText(_translate("MainWindow", "Önceki"))
        self.pushButton_sonraki.setText(_translate("MainWindow", "Sonraki"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())