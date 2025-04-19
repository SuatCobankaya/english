from PyQt5.QtWidgets import *
from ui_test import Ui_MainWindow

class testpencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.test_pencere = Ui_MainWindow()
        self.test_pencere.setupUi(self)
        self.test_pencere.pushButton_geri.clicked.connect(self.geri)
        self.test_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.test_pencere.centralwidget) 
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