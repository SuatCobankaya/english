from PyQt5.QtWidgets import *
from ui_ara import Ui_MainWindow
from veritabani import database
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt,QEvent

class arapencere(QMainWindow):  

    def __init__(self):
        super().__init__()
        self.ara_pencere = Ui_MainWindow()
        self.ara_pencere.setupUi(self)
        self.ara_pencere.pushButton_geri.clicked.connect(self.geri)
        self.ara_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.ara_pencere.pushButton_ara.clicked.connect(self.arama)
        self.setCentralWidget(self.ara_pencere.centralwidget) 
        cw = self.ara_pencere.centralwidget
        cw.installEventFilter(self)
        cw.setFocusPolicy(Qt.StrongFocus)
        cw.setFocus()

    def eventFilter(self, obj, event):
        from PyQt5.QtCore import QEvent
        if obj is self.ara_pencere.centralwidget and event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Return:
                self.arama()
                return True
            if key == Qt.Key_Escape:
                self.geri()
                return True
        return super().eventFilter(obj, event)
    def geri(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()
    def anasayfa(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()  
    def arama(self,):
        kelime = self.ara_pencere.lineEdit.text()
        db = database()
        anlam = db.ara(kelime)
        self.model = QStandardItemModel()
        self.ara_pencere.listView.setModel(self.model)
        if isinstance(anlam, list):  
         for item in anlam:
            clean_item = str(anlam).strip("[]'\"")
            self.model.appendRow(QStandardItem(str(clean_item)))  
        else:  
            clean_item = str(anlam).strip("[]'\"")
            self.model.appendRow(QStandardItem(str(clean_item)))
