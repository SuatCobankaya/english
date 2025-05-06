from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        top_button_font = QtGui.QFont()
        top_button_font.setPointSize(20)  # Artırıldı

        self.pushButton_dosya = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.pushButton_dosya.setSizePolicy(sizePolicy)
        self.pushButton_dosya.setFont(top_button_font)
        self.pushButton_dosya.setDefault(True)
        self.pushButton_dosya.setObjectName("pushButton_dosya")
        self.horizontalLayout.addWidget(self.pushButton_dosya)

        self.pushButton_istatislik = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_istatislik.setSizePolicy(sizePolicy)
        self.pushButton_istatislik.setFont(top_button_font)
        self.pushButton_istatislik.setDefault(True)
        self.pushButton_istatislik.setObjectName("pushButton_istatislik")
        self.horizontalLayout.addWidget(self.pushButton_istatislik)

        self.pushButton_ara = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ara.setSizePolicy(sizePolicy)
        self.pushButton_ara.setFont(top_button_font)
        self.pushButton_ara.setDefault(True)
        self.pushButton_ara.setObjectName("pushButton_ara")
        self.horizontalLayout.addWidget(self.pushButton_ara)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        button_font = QtGui.QFont()
        button_font.setPointSize(30)

        self.pushButton_kart = QtWidgets.QPushButton(self.centralwidget)
        sizePolicyGrid = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.pushButton_kart.setSizePolicy(sizePolicyGrid)
        self.pushButton_kart.setFont(button_font)
        self.pushButton_kart.setDefault(True)
        self.pushButton_kart.setObjectName("pushButton_kart")
        self.gridLayout.addWidget(self.pushButton_kart, 0, 0, 1, 1)

        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setSizePolicy(sizePolicyGrid)
        self.pushButton_test.setFont(button_font)
        self.pushButton_test.setDefault(True)
        self.pushButton_test.setObjectName("pushButton_test")
        self.gridLayout.addWidget(self.pushButton_test, 0, 1, 1, 1)

        self.pushButton_eslestirme = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eslestirme.setSizePolicy(sizePolicyGrid)
        self.pushButton_eslestirme.setFont(button_font)
        self.pushButton_eslestirme.setDefault(True)
        self.pushButton_eslestirme.setObjectName("pushButton_eslestirme")
        self.gridLayout.addWidget(self.pushButton_eslestirme, 1, 0, 1, 1)

        self.pushButton_cumle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cumle.setSizePolicy(sizePolicyGrid)
        self.pushButton_cumle.setFont(button_font)
        self.pushButton_cumle.setDefault(True)
        self.pushButton_cumle.setObjectName("pushButton_cumle")
        self.gridLayout.addWidget(self.pushButton_cumle, 1, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        left_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(left_spacer)

        self.pushButton_kaydet = QtWidgets.QPushButton(self.centralwidget)
        save_button_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.pushButton_kaydet.setSizePolicy(save_button_policy)
        self.pushButton_kaydet.setFont(top_button_font)
        self.pushButton_kaydet.setDefault(True)
        self.pushButton_kaydet.setObjectName("pushButton_kaydet")
        self.horizontalLayout_2.addWidget(self.pushButton_kaydet)

        self.pushButton_yedekle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_yedekle.setSizePolicy(save_button_policy)
        self.pushButton_yedekle.setFont(top_button_font)
        self.pushButton_yedekle.setDefault(True)
        self.pushButton_yedekle.setObjectName("pushButton_yedekle")
        self.horizontalLayout_2.addWidget(self.pushButton_yedekle)
        
        right_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(right_spacer)

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
        self.pushButton_dosya.setText(_translate("MainWindow", "Dosya"))
        self.pushButton_istatislik.setText(_translate("MainWindow", "İstatistik"))
        self.pushButton_ara.setText(_translate("MainWindow", "Arama"))
        self.label.setText(_translate("MainWindow", "Günlük Görevler"))
        self.pushButton_cumle.setText(_translate("MainWindow", "Cümle Oluşturma"))
        self.pushButton_eslestirme.setText(_translate("MainWindow", "Eşleştirme"))
        self.pushButton_kart.setText(_translate("MainWindow", "Kelime Kartları"))
        self.pushButton_test.setText(_translate("MainWindow", "Test"))
        self.pushButton_kaydet.setText(_translate("MainWindow", "  Yeni Kelime  "))
        self.pushButton_yedekle.setText(_translate("MainWindow", "Tekrar Kelime"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
