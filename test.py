from PyQt5.QtWidgets import *
from ui_test import Ui_MainWindow
from veritabani import database
import random

class testpencere(QMainWindow):  
    def __init__(self,kelimeler):
        super().__init__()
        self.test_pencere = Ui_MainWindow()
        self.test_pencere.setupUi(self)
        self.test_pencere.pushButton_geri.clicked.connect(self.geri)
        self.test_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.test_pencere.pushButton_sonraki.clicked.connect(self.sonrakisoru)
        self.test_pencere.pushButton_onceki.clicked.connect(self.oncekisoru)
        self.test_pencere.pushButton_a.clicked.connect(lambda: self.kontrolet(self.test_pencere.pushButton_a))
        self.test_pencere.pushButton_b.clicked.connect(lambda: self.kontrolet(self.test_pencere.pushButton_b))
        self.test_pencere.pushButton_c.clicked.connect(lambda: self.kontrolet(self.test_pencere.pushButton_c))
        self.test_pencere.pushButton_d.clicked.connect(lambda: self.kontrolet(self.test_pencere.pushButton_d))
        self.setCentralWidget(self.test_pencere.centralwidget)
        self.db = database()
        self.soru_index = 0
        self.kelimeler = kelimeler
        self.soruolustur()
        #proses bar
        self.test_pencere.progressBar.setRange(0, len(self.kelimeler))
        self.test_pencere.progressBar.setValue(self.soru_index)
        self.dogrusayisi = 0
        self.yanlissayisi = 0
    def geri(self):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()


    # def test_bitti(self):
    #     self.test_pencere.label_soru.setText("Test Bitti!")
    #     self.test_pencere.pushButton_a.setEnabled(False)
    #     self.test_pencere.pushButton_b.setEnabled(False)
    #     self.test_pencere.pushButton_c.setEnabled(False)
    #     self.test_pencere.pushButton_d.setEnabled(False)    
    
    def soruolustur(self):
        if self.soru_index >= len(self.kelimeler):
            
            QMessageBox.information(self, 
                        "Başarılı", 
                        f"Doğru sayınız: {self.asildogru}\nYanlış sayınız: {self.yanlissayisi}\nDoğruluk Oranınız % {self.yuzdelik}", 
                        QMessageBox.Ok)
            from anasayfa import anapencere
            self.giris = anapencere()
            self.giris.show()
            self.close()
            return
        
        kelime = self.kelimeler[self.soru_index]
        ingilizce = kelime[0]
        dogruturkce = kelime[1]
        self.dogru_cevap =dogruturkce
        tumturkceler= self.db.rastgele3kelimeal(dogruturkce)
        yanlisturkceler = random.sample(tumturkceler,3)

        siklar = yanlisturkceler + [dogruturkce]
        random.shuffle(siklar)
        self.test_pencere.label_soru.setText(ingilizce)
        self.test_pencere.pushButton_a.setText(siklar[0])
        self.test_pencere.pushButton_b.setText(siklar[1])
        self.test_pencere.pushButton_c.setText(siklar[2])
        self.test_pencere.pushButton_d.setText(siklar[3])
        #güncelle
        
        butonlar = [self.test_pencere.pushButton_a, self.test_pencere.pushButton_b,
            self.test_pencere.pushButton_c, self.test_pencere.pushButton_d]
        for b in butonlar:
            b.setStyleSheet("")
            b.setEnabled(True)

    def kontrolet(self,buton):
        secilen = buton.text()

        butonlar = [self.test_pencere.pushButton_a, self.test_pencere.pushButton_b,
                self.test_pencere.pushButton_c, self.test_pencere.pushButton_d]
        
        for dogru in butonlar:
            if dogru.text() == self.dogru_cevap:
                dogru.setStyleSheet("background-color: green; color: white;")
                self.dogrusayisi += 1
        
        if secilen != self.dogru_cevap:
            buton.setStyleSheet("background-color: red; color: white;")
            self.yanlissayisi += 1
        
        self.asildogru= self.dogrusayisi - self.yanlissayisi

        self.yuzdelik = self.asildogru/16*100
        for b in butonlar:
            b.setEnabled(False)


    def sonrakisoru(self):
        self.soru_index += 1
        self.test_pencere.progressBar.setValue(self.soru_index)
        self.soruolustur()

    def oncekisoru(self):
        if (self.soru_index <= 0):
            pass
        else:
            self.soru_index -= 1
            self.soruolustur()
        
    
    def anasayfa(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()