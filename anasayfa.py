from PyQt5.QtWidgets import *
from ui_anasayfayeni import Ui_MainWindow
from ara import arapencere
from cumle import cumlepencere
from dosya import dosyapencere
from eslestir import eslestirpencere
from istatislik import istatislikpencere
from flashcard import flashcardpencere
from test import testpencere
from veritabani import database

# Global tema değişkeni
global current_theme
current_theme = "dark"  # Varsayılan tema

def apply_theme(window):
    """Global temayı belirtilen pencereye uygular."""
    global current_theme
    if current_theme == "dark":
        dark_stylesheet = """
        QWidget {
            background-color: #2e2e2e;
            color: white;
        }
        QPushButton {
            background-color: #555555;
            color: white;
            border: 1px solid #777777;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #777777;
        }
        """
        window.setStyleSheet(dark_stylesheet)
    else:
        light_stylesheet = """
        QWidget {
            background-color: #ffffff;
            color: black;
        }
        QPushButton {
            background-color: #d3d3d3;
            color: black;
            border: 1px solid #a9a9a9;
            padding: 5px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #b0b0b0;
        }
        """
        window.setStyleSheet(light_stylesheet)

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
        self.ana_pencere.actionDark.triggered.connect(self.darkmode)
        self.ana_pencere.actionWhite.triggered.connect(self.whitemode)
        self.setCentralWidget(self.ana_pencere.centralwidget)
        self.showMaximized()
        
        # Başlangıçta global temayı uygula
        apply_theme(self)

    def ara(self):
        self.hide()
        self.araac = arapencere()
        apply_theme(self.araac)
        self.araac.show()

    def cumle(self):
        self.hide()
        self.cumleac = cumlepencere(self.kelimeler)
        apply_theme(self.cumleac)
        self.cumleac.show()

    def dosya(self):
        self.hide()
        self.dosyaac = dosyapencere()
        apply_theme(self.dosyaac)
        self.dosyaac.show()

    def eslestir(self):
        self.hide()
        self.eslestirac = eslestirpencere(self.kelimeler)
        apply_theme(self.eslestirac)
        self.eslestirac.show()

    def istatislik(self):
        self.hide()
        self.istatislikac = istatislikpencere()
        apply_theme(self.istatislikac)
        self.istatislikac.show()

    def kart(self):
        self.hide()
        self.kartac = flashcardpencere(self.kelimeler)
        apply_theme(self.kartac)
        self.kartac.show()

    def test(self):
        self.hide()
        self.testac = testpencere(self.kelimeler)
        apply_theme(self.testac)
        self.testac.show()

    def yenile(self):
        self.kelimeler = self.db.randomtüm(16)
        self.db.baglantiac()
        self.db.cursor.execute("DELETE FROM random20")
        for kelime, anlam in self.kelimeler:
                self.db.cursor.execute("INSERT INTO random20 (kelime, anlam) VALUES (?, ?)", (kelime, anlam))
        self.db.con.commit()
        self.db.baglantikapat()

    def darkmode(self):
        global current_theme
        current_theme = "dark"
        apply_theme(self)

    def whitemode(self):
        global current_theme
        current_theme = "white"
        apply_theme(self)
        
    def closeEvent(self, event):
        self.db.baglantiac()
        self.db.cursor.execute("DELETE FROM random20")
        self.db.con.commit()
        self.db.baglantikapat()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = anapencere()
    window.show()
    app.exec_()