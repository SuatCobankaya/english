from PyQt5.QtWidgets import *
from ui_eslestiryeni import Ui_MainWindow
import random
from PyQt5 import QtCore,QtGui
from veritabani import database
import json
from datetime import date

class eslestirpencere(QMainWindow):  
    def __init__(self,kelimeler):
        super().__init__()
        self.kelimeler = kelimeler
        i=0
        self.ingilizce = []
        while i<16:
            self.ingilizce.append(self.kelimeler[i][0])
            i = i+1
        self.eslestir_pencere = Ui_MainWindow()
        self.eslestir_pencere.setupUi(self)
        self.eslestir_pencere.pushButton_geri.clicked.connect(self.geri)
        self.eslestir_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.eslestir_pencere.pushButton_sonraki.clicked.connect(self.sonraki)
        self.numbers = random.sample(range(1, 17), 16) 
        self.butonlar()
        self.karistir()
        self.setCentralWidget(self.eslestir_pencere.centralwidget)
        self.index = 0
        self.eslestir_pencere.progressBar.setRange(0, 2)
        self.eslestir_pencere.progressBar.setValue(self.index+1)
        self.secim1 = None
        self.sayac = 0
        self.secim2 = None
        self.dogru = []
        self.yanlis = []
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
    def eslestir(self):
        tiklanan_buton = self.sender()
        if self.secim1 is None:
            self.secim1 = tiklanan_buton
            self.secim1.setStyleSheet("background-color: gray")
        elif self.secim2 is None and tiklanan_buton != self.secim1:
            self.secim2 = tiklanan_buton
            self.secim2.setStyleSheet("background-color: gray")
            metin1 = self.secim1.text()
            metin2 = self.secim2.text()

            if self.dogru_eslesme(metin1, metin2):
               self.secim1.setStyleSheet("background-color: lightgreen")
               self.secim2.setStyleSheet("background-color: lightgreen")
               
               self.secim1.setEnabled(False)
               self.secim2.setEnabled(False)

               btn1 = self.secim1
               btn2 = self.secim2
               QtCore.QTimer.singleShot(1000, lambda: self.butonGizle(btn1, btn2))
               self.sayac += 1
               if self.sayac==8:     
                   QtCore.QTimer.singleShot(1001, lambda: self.sonraki())
               if self.sayac==16:
                   QMessageBox.information(self, "Başarılı", "Eşleştirmeleri tamamladınız.")
                   QtCore.QTimer.singleShot(200, lambda: self.anasayfa())
               
            else:
               self.secim1.setStyleSheet("background-color: red")
               self.secim2.setStyleSheet("background-color: red")

               btn1 = self.secim1
               btn2 = self.secim2
               QtCore.QTimer.singleShot(1000, lambda: self.renkleriSifirla(btn1, btn2))

            self.secim1 = None
            self.secim2 = None

    def karistir(self,):
        numbers = self.numbers
        i = 0
        a = 0
        b = 0
        while i < 16 :
           self.buttons[numbers[i]-1].setText(self.kelimeler[a][b])
           if b == 0:
               b=1
               i = i+1
           else:
               b=0
               a = a+1
               i = i+1

    def sonraki(self,):
        self.numbers = random.sample(range(1, 17), 16)
        self.index = self.index+1

        for button in self.buttons:
           button.setVisible(True)
           button.setEnabled(True)
           button.setStyleSheet("")
        if self.index == 1:
           self.eslestir_pencere.progressBar.setValue(self.index+1)
           numbers = self.numbers
           i = 0
           a = 8
           b = 0
           while i < 16 :
              kelime = self.kelimeler[a][b]
              self.buttons[numbers[i]-1].setText(self.kelimeyi_sigdir(kelime))
              if b == 0:
                  b=1
                  i = i+1
              else:
                  b=0
                  a = a+1
                  i = i+1
        else:
            QMessageBox.information(self, "Başarılı", " eslestirmeler bitti. ")
            self.istatistik_kaydet("eslestirme", self.dogru, self.yanlis)
            self.anasayfa()

    def butonlar(self,):
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttons = [
            self.eslestir_pencere.pushButton_1, self.eslestir_pencere.pushButton_2,
            self.eslestir_pencere.pushButton_3, self.eslestir_pencere.pushButton_4,
            self.eslestir_pencere.pushButton_5, self.eslestir_pencere.pushButton_6,
            self.eslestir_pencere.pushButton_7, self.eslestir_pencere.pushButton_8,
            self.eslestir_pencere.pushButton_9, self.eslestir_pencere.pushButton_10,
            self.eslestir_pencere.pushButton_11, self.eslestir_pencere.pushButton_12,
            self.eslestir_pencere.pushButton_13, self.eslestir_pencere.pushButton_14,
            self.eslestir_pencere.pushButton_15, self.eslestir_pencere.pushButton_16
        ]
        for button in self.buttons:
            button.setFont(font)
            button.clicked.connect(self.eslestir)

    def dogru_eslesme(self, metin1, metin2):
       for ing, tr in self.kelimeler:
           if (metin1 == ing and metin2 == tr) or (metin1 == tr and metin2 == ing):
               if ing not in self.dogru:
                   self.dogru.append(ing)
               return True
       if metin1 not in self.ingilizce:
           if metin2 not in self.yanlis:
               self.yanlis.append(metin2)
       else:
           if metin1 not in self.yanlis:
               self.yanlis.append(metin1)
       return False
           
    def renkleriSifirla(self, btn1, btn2):
       btn1.setStyleSheet("")
       btn2.setStyleSheet("")

    def butonGizle(self, btn1, btn2):
       btn1.setStyleSheet("background-color: transparent; color: transparent; border: none;")
       btn2.setStyleSheet("background-color: transparent; color: transparent; border: none;")
       btn1.setEnabled(False)
       btn2.setEnabled(False)

    def istatistik_kaydet(self,tip, dogru_kelimeler, yanlis_kelimeler):
        db = database()
        db.baglantiac()
        db.cursor.execute("""
            INSERT INTO TestSonuclari (tarih, tip, dogru, yanlis)
            VALUES (?, ?, ?, ?)
        """, (
            date.today().isoformat(),        
            tip,                             
            json.dumps(dogru_kelimeler),     
            json.dumps(yanlis_kelimeler)      
        ))
        db.con.commit()
        db.baglantikapat()
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