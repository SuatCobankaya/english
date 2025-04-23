from PyQt5.QtWidgets import *
from ui_test import Ui_MainWindow
from veritabani import database
import random
import json
from datetime import date

class testpencere(QMainWindow):  
    def __init__(self, kelimeler):
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
        # Proses bar
        self.test_pencere.progressBar.setRange(0, 15)
        self.test_pencere.progressBar.setValue(self.soru_index)
        self.dogrusayisi = 0
        self.yanlissayisi = 0
        self.dogru = []
        self.yanlis = []

    def geri(self):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()  

    def kelimeyi_parcala(self, metin, max_uzunluk=20):
        # Kelimeyi, belirli bir uzunluğa göre parçalayıp düzgün bir şekilde yerleştir
        if len(metin) > max_uzunluk:
            kelimeler = metin.split()
            satir = ""
            sonuc = ""
            for kelime in kelimeler:
                if len(satir) + len(kelime) < max_uzunluk:
                    satir += kelime + " "
                else:
                    sonuc += satir.strip() + "\n"
                    satir = kelime + " "
            sonuc += satir.strip()
            return sonuc
        return metin

    def soruolustur(self):
        if self.soru_index >= len(self.kelimeler):
            QMessageBox.information(self, 
                        "Başarılı", 
                        f"Doğru sayınız: {self.asildogru}\nYanlış sayınız: {self.yanlissayisi}\nDoğruluk Oranınız % {self.yuzdelik}", 
                        QMessageBox.Ok)
            self.istatistik_kaydet("test", self.dogru, self.yanlis)
            from anasayfa import anapencere
            self.giris = anapencere()
            self.giris.show()
            self.close()
            return
        
        kelime = self.kelimeler[self.soru_index]
        ingilizce = kelime[0]
        dogruturkce = kelime[1]
        self.soru_ingilizce = ingilizce 
        self.dogru_cevap = dogruturkce
        tumturkceler = self.db.rastgele3kelimeal(dogruturkce)
        yanlisturkceler = random.sample(tumturkceler, 3)

        siklar = yanlisturkceler + [dogruturkce]
        random.shuffle(siklar)
        self.test_pencere.label_soru.setText(ingilizce)

        # Buton metinlerini kelimeyi_parcala fonksiyonuyla keserek düzenli bir şekilde yerleştir
        butonlar = [self.test_pencere.pushButton_a, self.test_pencere.pushButton_b,
                    self.test_pencere.pushButton_c, self.test_pencere.pushButton_d]
        
        for i, buton in enumerate(butonlar):
            buton.setText(self.kelimeyi_parcala(siklar[i]))  # Burada metin uzunluğu sınırlanıyor
            buton.setStyleSheet("""
                QPushButton {
                    font-size: 14px;
                    padding: 6px;
                    text-align: center;
                }
            """)
            buton.setMinimumHeight(60)  # Buton yükseklikleri ayarlandı

        # Güncelle
        for b in butonlar:
            b.setStyleSheet("")  # Buton stilini sıfırladık
            b.setEnabled(True)  # Butonları aktif hale getirdik

    def kontrolet(self, buton):
        secilen = buton.text()

        butonlar = [self.test_pencere.pushButton_a, self.test_pencere.pushButton_b,
                self.test_pencere.pushButton_c, self.test_pencere.pushButton_d]
        
        for dogru in butonlar:
            if dogru.text() == self.dogru_cevap:
                dogru.setStyleSheet("background-color: green; color: white;")
                self.dogru.append(self.soru_ingilizce)
                self.dogrusayisi += 1
        
        if secilen != self.dogru_cevap:
            buton.setStyleSheet("background-color: red; color: white;")
            self.yanlis.append(self.soru_ingilizce)
            self.yanlissayisi += 1
        
        self.asildogru = self.dogrusayisi - self.yanlissayisi
        self.yuzdelik = self.asildogru / 16 * 100
        for b in butonlar:
            b.setEnabled(False)

    def sonrakisoru(self):
        self.soru_index += 1
        self.test_pencere.progressBar.setValue(self.soru_index)
        self.soruolustur()

    def oncekisoru(self):
        if self.soru_index <= 0:
            pass
        else:
            self.soru_index -= 1
            self.soruolustur()

    def anasayfa(self):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()

    def istatistik_kaydet(self, tip, dogru_kelimeler, yanlis_kelimeler):
        dogru_kelimeler = [k for k in self.dogru if k not in yanlis_kelimeler]
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