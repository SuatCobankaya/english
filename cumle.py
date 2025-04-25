from PyQt5.QtWidgets import *
from ui_cumle import Ui_MainWindow
import random

class cumlepencere(QMainWindow):  
    def __init__(self,kelimeler):
        super().__init__()
        self.kelimeler = kelimeler
        self.cumle_pencere = Ui_MainWindow()
        self.cumle_pencere.setupUi(self)
        self.cumle_pencere.pushButton_geri.clicked.connect(self.geri)
        self.cumle_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.cumle_pencere.pushButton_kaydet.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.cumle_pencere.centralwidget) 
        kelime2dane = random.sample(self.kelimeler,2)
        self.cumle_pencere.label.setText(kelime2dane[0][0]+" ve "+ kelime2dane[1][0]+" kelimelerini kullanarak örnek cümle oluşturunuz")
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