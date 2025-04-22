from PyQt5.QtWidgets import *
from ui_flashcardtekrar import Ui_MainWindow
from veritabani import database

class flashcardtekrarpencere(QMainWindow):  
    def __init__(self,kelimeler):
        super().__init__()
        self.flashcardtekrar_pencere = Ui_MainWindow()
        self.flashcardtekrar_pencere.setupUi(self)
        self.kelimeler = kelimeler
        self.boyut = len(kelimeler)
        self.db = database()
        self.flashcardtekrar_pencere.pushButton_geri.clicked.connect(self.geri)
        self.flashcardtekrar_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.flashcardtekrar_pencere.pushButton_kelime.clicked.connect(self.kelime)
        self.flashcardtekrar_pencere.pushButton_sonraki.clicked.connect(self.sonraki)
        self.flashcardtekrar_pencere.pushButton_onceki.clicked.connect(self.onceki)
        self.flashcardtekrar_pencere.pushButton_biliyom.clicked.connect(self.kolay)
        self.flashcardtekrar_pencere.pushButton_orta.clicked.connect(self.orta)
        self.flashcardtekrar_pencere.pushButton_bilmiyom.clicked.connect(self.zor)
        self.setCentralWidget(self.flashcardtekrar_pencere.centralwidget) 
        self.flashcardtekrar_pencere.pushButton_kelime.setText(kelimeler[0][0])
        self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
        self.index = 0
        self.sayac = 0
        self.kelime = None
        #proses bar
        self.flashcardtekrar_pencere.progressBar.setRange(0, len(self.kelimeler)-1)
        self.flashcardtekrar_pencere.progressBar.setValue(self.sayac)
        
    def geri(self, ):
        from dosya import dosyapencere
        self.giris = dosyapencere()
        self.giris.show()
        self.close() 
    def anasayfa(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close() 
    def onceki(self,):
        if self.sayac == 0:
            QMessageBox.warning(self, "Hata", "en basa geldik")
        else:
            self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("")
            self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("")
            self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("")
            self.sayac = self.sayac - 1
            self.flashcardtekrar_pencere.progressBar.setValue(self.sayac)
            self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeler[self.sayac][0])
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
            self.index = 0
    def sonraki(self,):
        if self.sayac == self.boyut-1:
            if self.kelime is not None:
                self.db.algo(self.zorluk,self.kelime)
                QMessageBox.information(self, "Başarılı", " kelimeler bitti. ")
                from dosya import dosyapencere
                self.giris = dosyapencere()
                self.giris.show()
                self.close() 
            else:
                QMessageBox.warning(self, "Hata", "bir zorluk degeri girin!")
        else:
            if self.kelime is not None:
                self.db.algo(self.zorluk,self.kelime)
                self.kelime = None
                self.zorluk = None
                self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("")
                self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("")
                self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("")
                self.sayac = self.sayac + 1
                self.flashcardtekrar_pencere.progressBar.setValue(self.sayac)
                self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeler[self.sayac][0])
                self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
                self.index = 0
            else:
                QMessageBox.warning(self, "Hata", "bir zorluk degeri girin!")

    def kelime(self,):
        current_index = self.index

        if current_index == 0:
            self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeler[self.sayac][1])
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: orange; color: white;")
            self.index = 1
        else:
            self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeler[self.sayac][0])  
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
            self.index = 0
    def kolay(self,):
        self.kelime = self.kelimeler[self.sayac][0]
        self.zorluk = 1
        self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("background-color: lightgreen; color: black;")
        self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("")
    def orta(self,):
        self.kelime = self.kelimeler[self.sayac][0]
        self.zorluk = 2
        self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("background-color: lightgreen; color: black;")
        self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("")
    def zor(self,):
        self.kelime = self.kelimeler[self.sayac][0]
        self.zorluk = 3
        self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("background-color: lightgreen; color: black;")