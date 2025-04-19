from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # **Üst Butonları Sola Yasla**
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setAlignment(QtCore.Qt.AlignLeft)  # Butonları sola yasla

        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setIcon(QtGui.QIcon("geri.png"))
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout_4.addWidget(self.pushButton_geri)

        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setIcon(QtGui.QIcon("main.png"))
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout_4.addWidget(self.pushButton_anasayfa)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        # Dosya Adı ve Filtreleme
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Dosya Adı", self.centralwidget)
        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_dosya = QtWidgets.QLineEdit(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.lineEdit_dosya)

        self.checkBox_hepsi = QtWidgets.QCheckBox("Hepsi", self.centralwidget)
        self.checkBox_biliyom = QtWidgets.QCheckBox("Biliyom", self.centralwidget)
        self.checkBox_orta = QtWidgets.QCheckBox("Orta", self.centralwidget)
        self.checkBox_bilmiyom = QtWidgets.QCheckBox("Bilmiyom", self.centralwidget)

        self.horizontalLayout_2.addWidget(self.checkBox_hepsi)
        self.horizontalLayout_2.addWidget(self.checkBox_biliyom)
        self.horizontalLayout_2.addWidget(self.checkBox_orta)
        self.horizontalLayout_2.addWidget(self.checkBox_bilmiyom)

        self.pushButton_goruntule = QtWidgets.QPushButton("Görüntüle", self.centralwidget)
        self.horizontalLayout_2.addWidget(self.pushButton_goruntule)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # **Scroll Alanı Eklenmiş GroupBox**
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")

        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)

        # **Label ve LineEdit'leri Küçültülmüş Şekilde Ayarla**
        labels = ["Kelime", "Anlamı", "Örnek Cümle"]
        for col, text in enumerate(labels):
            label = QtWidgets.QLabel(text, self.groupBox)
            label.setFixedHeight(20)  # Sabit yükseklik ver
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setStyleSheet("border: 1px solid gray; padding: 2px;")  # Daha düzenli görünüm
            self.gridLayout.addWidget(label, 0, col)

        for row in range(1, 6):  # 5 satırlık örnek girdiler
            for col in range(3):
                lineEdit = QtWidgets.QLineEdit(self.groupBox)
                lineEdit.setFixedHeight(25)  # LineEdit'leri sabitle
                self.gridLayout.addWidget(lineEdit, row, col)

        self.scrollLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        # **Alt Butonları Küçült ve Ortala**
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignCenter)  # Butonları ortala

        self.pushButton_yeni = QtWidgets.QPushButton("Yeni Kelime", self.centralwidget)
        self.pushButton_yeni.setFixedSize(100, 30)  # Butonları küçült

        self.pushButton_kaydet = QtWidgets.QPushButton("Kaydet", self.centralwidget)
        self.pushButton_kaydet.setFixedSize(100, 30)  # Butonları küçült

        self.horizontalLayout.addWidget(self.pushButton_yeni)
        self.horizontalLayout.addWidget(self.pushButton_kaydet)
        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Kelime Uygulaması")
    def yenikelime(self):
     row = self.gridLayout.rowCount()
     for col in range(3):
        kelime = QtWidgets.QTextEdit(self.groupBox)
        kelime.setText("")
        kelime.setStyleSheet("background-color: #6272a4; color: white; border-radius: 5px; font-size: 14px; padding: 8px;")
        kelime.setFixedHeight(60)
        kelime.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.gridLayout.addWidget(kelime, row, col) 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())