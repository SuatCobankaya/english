from PyQt5.QtWidgets import *
from ui_anasayfayeni import Ui_MainWindow
from ara import arapencere
from cumle import cumlepencere
from dosya import dosyapencere
from eslestir import eslestirpencere

from flashcard import flashcardpencere
from test import testpencere
from veritabani import database

class anapencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.db = database()

        self.db.baglantiac()
        self.db.cursor.execute("SELECT kelime, anlam FROM random20")
        self.sayi = self.db.cursor.fetchall()
        self.db.baglantikapat()

        if len(self.sayi) == 16:
            self.kelimeler = self.sayi
        else:
            self.kelimeler = self.db.randomtüm(16)
            self.db.baglantiac()
            for kelime, anlam in self.kelimeler:
                self.db.cursor.execute("INSERT INTO random20 (kelime, anlam) VALUES (?, ?)", (kelime, anlam))
            self.db.con.commit()
            self.db.baglantikapat()


        self.ana_pencere = Ui_MainWindow()
        
        self.ana_pencere.setupUi(self)
        self.ana_pencere.pushButton_ara.clicked.connect(self.ara)
        self.ana_pencere.pushButton_cumle.clicked.connect(self.cumle)
        self.ana_pencere.pushButton_dosya.clicked.connect(self.dosya)
        self.ana_pencere.pushButton_eslestirme.clicked.connect(self.eslestir)
        self.ana_pencere.pushButton_istatislik.clicked.connect(self.istatislik)
        self.ana_pencere.pushButton_kart.clicked.connect(self.kart)
        self.ana_pencere.pushButton_kaydet.clicked.connect(self.yenile)
        self.ana_pencere.pushButton_test.clicked.connect(self.test)
        self.ana_pencere.actionWhite.triggered.connect(self.whitemode)
        self.setCentralWidget(self.ana_pencere.centralwidget)
        self.showMaximized()
        

    def ara(self):
        self.hide()
        self.araac = arapencere()
        self.araac.show()

    def cumle(self):
        self.hide()
        self.cumleac = cumlepencere(self.kelimeler)
        self.cumleac.show()

    def dosya(self):
        self.hide()
        self.dosyaac = dosyapencere()
        self.dosyaac.show()

    def eslestir(self):
        self.hide()
        self.eslestirac = eslestirpencere(self.kelimeler)
        self.eslestirac.show()

    def istatislik(self):
        from istatislik import istatislikpencere
        self.hide()
        self.istatislikac = istatislikpencere()
        self.istatislikac.show()

    def kart(self):
        self.hide()
        self.kartac = flashcardpencere(self.kelimeler)
        self.kartac.show()

    def test(self):
        self.hide()
        self.testac = testpencere(self.kelimeler)
        self.testac.show()

    def yenile(self):
        self.kelimeler = self.db.randomtüm(16)
        self.db.baglantiac()
        self.db.cursor.execute("DELETE FROM random20")
        for kelime, anlam in self.kelimeler:
                self.db.cursor.execute("INSERT INTO random20 (kelime, anlam) VALUES (?, ?)", (kelime, anlam))
        self.db.con.commit()
        self.db.baglantikapat()


        
    def closeEvent(self, event):
        self.db.baglantiac()
        self.db.cursor.execute("DELETE FROM random20")
        self.db.con.commit()
        self.db.baglantikapat()
        event.accept()