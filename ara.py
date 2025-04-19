from PyQt5.QtWidgets import *
from ui_ara import Ui_MainWindow
from veritabani import database
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class arapencere(QMainWindow):  

    def __init__(self):
        super().__init__()
        self.ara_pencere = Ui_MainWindow()
        self.ara_pencere.setupUi(self)
        self.ara_pencere.pushButton_geri.clicked.connect(self.geri)
        self.ara_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.ara_pencere.pushButton_ara.clicked.connect(self.arama)
        self.setCentralWidget(self.ara_pencere.centralwidget) 
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
