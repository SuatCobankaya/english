from PyQt5.QtWidgets import *
from ui_eslestiryeni import Ui_MainWindow

class eslestirpencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.eslestir_pencere = Ui_MainWindow()
        self.eslestir_pencere.setupUi(self)
        self.eslestir_pencere.pushButton_geri.clicked.connect(self.geri)
        self.eslestir_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.eslestir_pencere.centralwidget) 
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