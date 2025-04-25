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
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_geri.setIcon(icon)
        self.pushButton_geri.setDefault(True)
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout.addWidget(self.pushButton_geri)

        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_anasayfa.setIcon(icon1)
        self.pushButton_anasayfa.setDefault(True)
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout.addWidget(self.pushButton_anasayfa)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.groupBox = QtWidgets.QGroupBox()
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea.setWidget(self.groupBox)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButton_sil = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sil.sizePolicy().hasHeightForWidth())
        self.pushButton_sil.setSizePolicy(sizePolicy)
        self.pushButton_sil.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_sil.setDefault(True)
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.horizontalLayout_2.addWidget(self.pushButton_sil)

        self.pushButton_yeni = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_yeni.sizePolicy().hasHeightForWidth())
        self.pushButton_yeni.setSizePolicy(sizePolicy)
        self.pushButton_yeni.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_yeni.setDefault(True)
        self.pushButton_yeni.setObjectName("pushButton_yeni")
        self.horizontalLayout_2.addWidget(self.pushButton_yeni)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

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
        self.pushButton_sil.setText(_translate("MainWindow", "Sil"))
        self.pushButton_yeni.setText(_translate("MainWindow", "Yeni"))
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