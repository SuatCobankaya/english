from PyQt5.QtWidgets import *
from ui_istatislik import Ui_MainWindow

class istatislikpencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.istatislik_pencere = Ui_MainWindow()
        self.istatislik_pencere.setupUi(self)
        self.istatislik_pencere.pushButton_geri.clicked.connect(self.geri)
        self.istatislik_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.istatislik_pencere.pushButton_biliyom.clicked.connect(self.biliyom)
        self.istatislik_pencere.pushButton_orta.clicked.connect(self.orta)
        self.istatislik_pencere.pushButton_bilmiyom.clicked.connect(self.bilmiyom)
        self.setCentralWidget(self.istatislik_pencere.centralwidget) 
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
    def biliyom(self, ):
        from dosyaici import dosyaicipencere
        self.giris = dosyaicipencere()
        self.giris.show()
        self.close() 
    def orta(self, ):
        from dosyaici import dosyaicipencere
        self.giris = dosyaicipencere()
        self.giris.show()
        self.close()  
    def bilmiyom(self, ):
        from dosyaici import dosyaicipencere
        self.giris = dosyaicipencere()
        self.giris.show()
        self.close()  