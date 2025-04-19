from PyQt5.QtWidgets import *
from ui_yenidosya import Ui_MainWindow
from veritabani import database
from PyQt5 import QtCore, QtGui, QtWidgets

class yenidosyapencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.yenidosya_pencere = Ui_MainWindow()
        self.yenidosya_pencere.setupUi(self)
        self.db = database()
        self.yenidosya_pencere.pushButton_geri.clicked.connect(self.geri)
        self.yenidosya_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.yenidosya_pencere.pushButton_yeni.clicked.connect(self.yenikelime)
        self.yenidosya_pencere.pushButton_kaydet.clicked.connect(self.kaydet)
        self.setCentralWidget(self.yenidosya_pencere.centralwidget) 

    def geri(self):
        from dosya import dosyapencere
        self.close()
        self.giris = dosyapencere()
        self.giris.show()

    def anasayfa(self):
        from anasayfa import anapencere
        self.close()
        self.giris = anapencere()
        self.giris.show()
    def yenikelime(self):
        self.yenidosya_pencere.yenikelime()
    def kaydet(self):
        dosyaadi = self.yenidosya_pencere.lineEdit_dosya.text().strip()
        if dosyaadi:
         self.db.dosyaekle(dosyaadi)
         id = self.db.dosyaidgetir(dosyaadi)
         for row in range(1, self.yenidosya_pencere.gridLayout.rowCount()):
            kelime_widget = self.yenidosya_pencere.gridLayout.itemAtPosition(row, 0)
            anlami_widget = self.yenidosya_pencere.gridLayout.itemAtPosition(row, 1)
            ornek_widget = self.yenidosya_pencere.gridLayout.itemAtPosition(row, 2)
            if kelime_widget is not None and anlami_widget is not None:
                kelime = kelime_widget.widget().text().strip()
                anlami = anlami_widget.widget().text().strip()
                if kelime and anlami:
                    ornek = ornek_widget.widget().text().strip() if ornek_widget else ""
                    self.db.kelimeekle(kelime, anlami, id, ornek)

            else:
                QMessageBox.warning(self, "Hata", "eksik bilgi!")
         QMessageBox.warning(self, "basarili", "yeni dosya olusturuldu.")
         self.geri()
                
        else:
            QMessageBox.warning(self, "Hata", "Dosya adi bos olamaz!")
