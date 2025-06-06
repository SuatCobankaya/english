from PyQt5 import QtCore, QtGui, QtWidgets
import sys

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
        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_geri.setIcon(icon)
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout_2.addWidget(self.pushButton_geri)

        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_anasayfa.setIcon(icon1)
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout_2.addWidget(self.pushButton_anasayfa)

        self.horizontalLayout_2.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Genel Özet")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_deneme = QtWidgets.QLabel(self.groupBox)
        self.label_deneme.setObjectName("label_deneme")
        self.horizontalLayout.addWidget(self.label_deneme)
        self.horizontalLayout.addStretch(1)  
        self.label_dogruluk = QtWidgets.QLabel(self.groupBox)
        self.label_dogruluk.setObjectName("label_dogruluk")
        self.horizontalLayout.addWidget(self.label_dogruluk)
        self.verticalLayout.addWidget(self.groupBox)

        self.tablo = QtWidgets.QTabWidget(self.centralwidget)
        self.tablo.setObjectName("tablo")

        self.test = QtWidgets.QWidget()
        self.test.setObjectName("test")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.test)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_test = QtWidgets.QTableWidget(self.test)
        self.tableWidget_test.setObjectName("tableWidget_test")
        self.tableWidget_test.setColumnCount(4)
        self.tableWidget_test.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.tableWidget_test, 0, 0, 1, 1)
        self.tablo.addTab(self.test, "")

        self.eslestirme = QtWidgets.QWidget()
        self.eslestirme.setObjectName("eslestirme")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.eslestirme)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_eslestirme = QtWidgets.QTableWidget(self.eslestirme)
        self.tableWidget_eslestirme.setObjectName("tableWidget_eslestirme")
        self.tableWidget_eslestirme.setColumnCount(4)
        self.tableWidget_eslestirme.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_eslestirme.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_eslestirme.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_eslestirme.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_eslestirme.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget_eslestirme, 0, 0, 1, 1)
        self.tablo.addTab(self.eslestirme, "")

        self.verticalLayout.addWidget(self.tablo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tablo.setCurrentIndex(0)
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
        QHeaderView::section {
            background-color: #3c3c3c;
            color: white;
            padding: 5px;
            border: 1px solid #555;
            font-weight: bold;
        }
        QTableWidget {
            gridline-color: #444444;
            background-color: #2e2e2e;
            alternate-background-color: #3a3a3a;
            color: white;
            selection-background-color: #44475a;
            selection-color: white;
        }
        QTableWidget::item {
            background-color: #2e2e2e;
            padding: 4px;
        }
        QTableWidget QTableCornerButton::section {
            background-color: #3c3c3c;
            border: 1px solid #555;
        }

        QTabWidget::pane {
            border: 1px solid #555;
            background: #2e2e2e;
        }

        QTabBar::tab {
            background: #3c3c3c;
            color: white;
            padding: 8px;
            border: 1px solid #555;
            border-bottom: none;
            min-width: 100px;
        }

        QTabBar::tab:selected {
            background: #2e2e2e;
            border-bottom: 1px solid #2e2e2e;
            font-weight: bold;
        }

        QTabBar::tab:!selected {
            margin-top: 2px;
        }
        """
        MainWindow.setStyleSheet(dark_stylesheet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kelime Uygulaması"))
        self.groupBox.setTitle(_translate("MainWindow", "Genel Özet"))
        self.label_deneme.setText(_translate("MainWindow", "TextLabel"))
        self.label_dogruluk.setText(_translate("MainWindow", "TextLabel"))
        item = self.tableWidget_test.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.tableWidget_test.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Doğru"))
        item = self.tableWidget_test.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yanlış"))
        item = self.tableWidget_test.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Doğruluk %"))
        self.tablo.setTabText(self.tablo.indexOf(self.test), _translate("MainWindow", "Testler"))
        item = self.tableWidget_eslestirme.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.tableWidget_eslestirme.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Doğru"))
        item = self.tableWidget_eslestirme.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yanlış"))
        item = self.tableWidget_eslestirme.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Doğruluk %"))
        self.tablo.setTabText(self.tablo.indexOf(self.eslestirme), _translate("MainWindow", "Eşleştirme"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())