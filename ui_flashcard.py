# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Geri ve Anasayfa butonlarını sola yasla
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setAlignment(QtCore.Qt.AlignLeft)  # Sola yasla

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

        # Sola yaslamak için esnek boşluk ekle
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # Kelime butonu
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

        # Biliyom, Orta, Bilmiyom butonlarını ortala
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignCenter)  # Ortala

        self.pushButton_bilmiyom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bilmiyom.setDefault(True)
        self.pushButton_bilmiyom.setObjectName("pushButton_bilmiyom")
        self.horizontalLayout.addWidget(self.pushButton_bilmiyom)

        self.pushButton_orta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_orta.setDefault(True)
        self.pushButton_orta.setObjectName("pushButton_orta")
        self.horizontalLayout.addWidget(self.pushButton_orta)

        self.pushButton_biliyom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_biliyom.setDefault(True)
        self.pushButton_biliyom.setObjectName("pushButton_biliyom")
        self.horizontalLayout.addWidget(self.pushButton_biliyom)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Önceki ve Sonraki butonları ile ProgressBar
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_onceki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_onceki.setDefault(True)
        self.pushButton_onceki.setObjectName("pushButton_onceki")
        self.horizontalLayout_2.addWidget(self.pushButton_onceki)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)

        self.pushButton_sonraki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sonraki.setDefault(True)
        self.pushButton_sonraki.setObjectName("pushButton_sonraki")
        self.horizontalLayout_2.addWidget(self.pushButton_sonraki)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        self.menuDarkmode = QtWidgets.QMenu(self.menuAyarlar)
        self.menuDarkmode.setObjectName("menuDarkmode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWhite = QtWidgets.QAction(MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.menuDarkmode.addAction(self.actionWhite)
        self.menuDarkmode.addAction(self.actionDark)
        self.menuAyarlar.addAction(self.menuDarkmode.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_kelime.setText(_translate("MainWindow", "kelime"))
        self.pushButton_bilmiyom.setText(_translate("MainWindow", "bilmiyom"))
        self.pushButton_orta.setText(_translate("MainWindow", "orta"))
        self.pushButton_biliyom.setText(_translate("MainWindow", "biliyom"))
        self.pushButton_onceki.setText(_translate("MainWindow", "Önceki"))
        self.pushButton_sonraki.setText(_translate("MainWindow", "Sonraki"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuDarkmode.setTitle(_translate("MainWindow", "Tema"))
        self.actionWhite.setText(_translate("MainWindow", "White"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())