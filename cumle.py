from PyQt5.QtWidgets import *
from ui_cumle import Ui_MainWindow

class cumlepencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.cumle_pencere = Ui_MainWindow()
        self.cumle_pencere.setupUi(self)
        self.cumle_pencere.pushButton_geri.clicked.connect(self.geri)
        self.cumle_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.cumle_pencere.centralwidget) 
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