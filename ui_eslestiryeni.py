from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setText("")
        self.pushButton_geri.setMaximumSize(QtCore.QSize(40, 40))  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_geri.setIcon(icon)
        self.pushButton_geri.setDefault(True)
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout.addWidget(self.pushButton_geri)
        
        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setText("")
        self.pushButton_anasayfa.setMaximumSize(QtCore.QSize(40, 40))  
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_anasayfa.setIcon(icon1)
        self.pushButton_anasayfa.setDefault(True)
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout.addWidget(self.pushButton_anasayfa)
        
        self.horizontalLayout.addStretch(1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        button_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setSizePolicy(button_size_policy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(100, 80))  
        self.pushButton_1.setDefault(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setSizePolicy(button_size_policy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setSizePolicy(button_size_policy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setSizePolicy(button_size_policy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 3, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setSizePolicy(button_size_policy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setSizePolicy(button_size_policy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setSizePolicy(button_size_policy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setSizePolicy(button_size_policy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setSizePolicy(button_size_policy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setSizePolicy(button_size_policy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setSizePolicy(button_size_policy)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setSizePolicy(button_size_policy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 3, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setSizePolicy(button_size_policy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setSizePolicy(button_size_policy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_14.setDefault(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 3, 1, 1, 1)

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setSizePolicy(button_size_policy)
        self.pushButton_15.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_15.setDefault(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 3, 2, 1, 1)

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setSizePolicy(button_size_policy)
        self.pushButton_16.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 3, 1, 1)
        
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))  
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar, 3)  
        
        self.pushButton_sonraki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sonraki.setMinimumSize(QtCore.QSize(100, 30))  
        self.pushButton_sonraki.setDefault(True)
        self.pushButton_sonraki.setObjectName("pushButton_sonraki")
        self.horizontalLayout_2.addWidget(self.pushButton_sonraki, 1)  
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
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
        self.label.setText(_translate("MainWindow", "Kelimeleri anlamlarıyla eşleştir."))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_1.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_sonraki.setText(_translate("MainWindow", "Sonraki"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())