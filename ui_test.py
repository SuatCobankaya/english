from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setAlignment(QtCore.Qt.AlignLeft)  

        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_geri.setIcon(icon)
        self.pushButton_geri.setDefault(True)
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout_2.addWidget(self.pushButton_geri)

        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_anasayfa.setIcon(icon1)
        self.pushButton_anasayfa.setDefault(True)
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout_2.addWidget(self.pushButton_anasayfa)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_soru = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_soru.sizePolicy().hasHeightForWidth())
        self.label_soru.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_soru.setFont(font)
        self.label_soru.setAlignment(QtCore.Qt.AlignCenter)
        self.label_soru.setObjectName("label_soru")
        self.verticalLayout.addWidget(self.label_soru)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_b.sizePolicy().hasHeightForWidth())
        self.pushButton_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_b.setFont(font)
        self.pushButton_b.setDefault(True)
        self.pushButton_b.setObjectName("pushButton_b")
        self.gridLayout.addWidget(self.pushButton_b, 0, 1, 1, 1)

        self.pushButton_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.pushButton_a.sizePolicy().hasHeightForWidth())
        self.pushButton_a.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_a.setFont(font)
        self.pushButton_a.setDefault(True)
        self.pushButton_a.setObjectName("pushButton_a")
        self.gridLayout.addWidget(self.pushButton_a, 0, 0, 1, 1)

        self.pushButton_c = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.pushButton_c.sizePolicy().hasHeightForWidth())
        self.pushButton_c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setDefault(True)
        self.pushButton_c.setObjectName("pushButton_c")
        self.gridLayout.addWidget(self.pushButton_c, 1, 0, 1, 1)

        self.pushButton_d = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_d.sizePolicy().hasHeightForWidth())
        self.pushButton_d.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_d.setFont(font)
        self.pushButton_d.setDefault(True)
        self.pushButton_d.setObjectName("pushButton_d")
        self.gridLayout.addWidget(self.pushButton_d, 1, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.label_cevap = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_cevap.setFont(font)
        self.label_cevap.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cevap.setObjectName("label_cevap")
        self.verticalLayout.addWidget(self.label_cevap)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_onceki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_onceki.setDefault(True)
        self.pushButton_onceki.setObjectName("pushButton_onceki")
        self.horizontalLayout.addWidget(self.pushButton_onceki)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)

        self.pushButton_sonraki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sonraki.setDefault(True)
        self.pushButton_sonraki.setObjectName("pushButton_sonraki")
        self.horizontalLayout.addWidget(self.pushButton_sonraki)

        self.verticalLayout.addLayout(self.horizontalLayout)

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
        self.label_soru.setText(_translate("MainWindow", "Soru ?"))
        self.pushButton_b.setText(_translate("MainWindow", "B.)"))
        self.pushButton_a.setText(_translate("MainWindow", "A.)"))
        self.pushButton_c.setText(_translate("MainWindow", "C.)"))
        self.pushButton_d.setText(_translate("MainWindow", "D.)"))
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