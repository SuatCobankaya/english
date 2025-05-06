from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyledItemDelegate

class AlignDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter 
        super().paint(painter, option, index)

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
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_geri.setFont(font)
        self.pushButton_geri.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_geri.setIcon(icon)
        self.pushButton_geri.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout_2.addWidget(self.pushButton_geri)

        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_anasayfa.setIcon(icon1)
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout_2.addWidget(self.pushButton_anasayfa)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit_kelime")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_ara = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ara.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ara.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ara.setIcon(icon2)
        self.pushButton_ara.setObjectName("pushButton_ara")
        self.horizontalLayout.addWidget(self.pushButton_ara)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView_anlam")

        font = QtGui.QFont()
        font.setPointSize(45)  
        self.listView.setFont(font)

        self.listView.setStyleSheet("""
            QListView {
                font-size: 45pt;  /* Yazı boyutunu büyüt */
            }
            QListView::item {
                padding: 10px;    /* Satır içi boşluk */
                min-height: 50px; /* Minimum satır yüksekliği */
            }
        """)
        self.verticalLayout.addWidget(self.listView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listView.setItemDelegate(AlignDelegate())
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
