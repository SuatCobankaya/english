from PyQt5.QtWidgets import *
from ui_flashcardtekrar import Ui_MainWindow
from veritabani import database
from PyQt5.QtCore import Qt,QEvent

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
        self.flashcardtekrar_pencere.pushButton_kelime.clicked.connect(self.cevir)
        self.flashcardtekrar_pencere.pushButton_sonraki.clicked.connect(self.sonraki)
        self.flashcardtekrar_pencere.pushButton_onceki.clicked.connect(self.onceki)
        self.flashcardtekrar_pencere.pushButton_biliyom.clicked.connect(self.kolay)
        self.flashcardtekrar_pencere.pushButton_orta.clicked.connect(self.orta)
        self.flashcardtekrar_pencere.pushButton_bilmiyom.clicked.connect(self.zor)
        self.setCentralWidget(self.flashcardtekrar_pencere.centralwidget) 
        self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeyi_sigdir(self.kelimeler[0][0]))
        self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
        self.index = 0
        self.sayac = 0
        self.kelime = None
        self.flashcardtekrar_pencere.progressBar.setRange(0, len(self.kelimeler)-1)
        self.flashcardtekrar_pencere.progressBar.setValue(self.sayac)
        cw = self.flashcardtekrar_pencere.centralwidget
        cw.installEventFilter(self)
        cw.setFocusPolicy(Qt.StrongFocus)
        cw.setFocus()

    def eventFilter(self, obj, event):
        from PyQt5.QtCore import QEvent
        if obj is self.flashcardtekrar_pencere.centralwidget and event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Right:
                self.kolay()
                return True
            elif key == Qt.Key_Down:
                self.orta()
                return True
            elif key == Qt.Key_Left:
                self.zor()
                return True
            elif key == Qt.Key_Space:
                self.cevir()
                return True
            elif key == Qt.Key_Escape:
                self.geri()
                return True
            elif key == Qt.Key_A:
                self.onceki()
                return True
        
        
        return super().eventFilter(obj, event)
        
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
            self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeyi_sigdir(self.kelimeler[self.sayac][0]))
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
            self.index = 0
    def sonraki(self,):
        if self.sayac == self.boyut-1:
            if self.kelime is not None:
                self.db.algo(self.zorluk,self.kelime)
                QMessageBox.information(self, "Başarılı", " Kelimeleri Başarıyla Tamamladınız! ")
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
                self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeyi_sigdir(self.kelimeler[self.sayac][0]))
                self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
                self.index = 0
            else:
                QMessageBox.warning(self, "Hata", "bir zorluk degeri girin!")

    def cevir(self,):
        current_index = self.index

        if current_index == 0:
            self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeyi_sigdir(self.kelimeler[self.sayac][1]))
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightgreen; color: black;")
            self.index = 1
        else:
            self.flashcardtekrar_pencere.pushButton_kelime.setText(self.kelimeyi_sigdir(self.kelimeler[self.sayac][0]))  
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")
            self.index = 0
        cw = self.flashcardtekrar_pencere.centralwidget
        cw.setFocus()

    def kolay(self,):
        self.kelime = self.kelimeler[self.sayac][0]
        self.zorluk = 1
        self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("background-color: lightgreen; color: black;")
        self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("")
        self.sonraki()
    def orta(self,):
        self.kelime = self.kelimeler[self.sayac][0]
        self.zorluk = 2
        self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("background-color: lightgreen; color: black;")
        self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("")
        self.sonraki()
    def zor(self,):
        self.kelime = self.kelimeler[self.sayac][0]
        self.zorluk = 3
        self.flashcardtekrar_pencere.pushButton_biliyom.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_orta.setStyleSheet("")
        self.flashcardtekrar_pencere.pushButton_bilmiyom.setStyleSheet("background-color: lightgreen; color: black;")
        self.sonraki()
    def kelimeyi_sigdir(self, kelime, max_satir_uzunlugu=20):
        kelimeler = kelime.split()
        satirlar = []
        satir = ""
        for k in kelimeler:
            if len(satir) + len(k) + 1 <= max_satir_uzunlugu:
                satir += (" " if satir else "") + k
            else:
                satirlar.append(satir)
                satir = k
        if satir:
            satirlar.append(satir)
        return '\n'.join(satirlar)