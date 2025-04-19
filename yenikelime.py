from PyQt5.QtWidgets import *
from ui_yenikelime import Ui_MainWindow

class yenikelimepencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.yenikelime_pencere = Ui_MainWindow()
        self.yenikelime_pencere.setupUi(self)
        self.yenikelime_pencere.pushButton_geri.clicked.connect(self.geri)
        self.yenikelime_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.yenikelime_pencere.pushButton_ogren.clicked.connect(self.ogren)
        self.setCentralWidget(self.yenikelime_pencere.centralwidget) 
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
    def ogren(self, ):
        from flashcard import flashcardpencere
        self.giris = flashcardpencere()
        self.giris.show()
        self.close() 