from PyQt5.QtWidgets import *
from ui_anasayfayeni import Ui_MainWindow
from ara import arapencere
from cumle import cumlepencere
from dosya import dosyapencere
from eslestir import eslestirpencere
from istatislik import istatislikpencere
from flashcardtekrar import flashcardtekrarpencere
from test import testpencere
from yenikelime import yenikelimepencere

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
        self.ana_pencere = Ui_MainWindow()
        self.ana_pencere.setupUi(self)
        self.ana_pencere.pushButton_ara.clicked.connect(self.ara)
        self.ana_pencere.pushButton_cumle.clicked.connect(self.cumle)
        self.ana_pencere.pushButton_dosya.clicked.connect(self.dosya)
        self.ana_pencere.pushButton_eslestirme.clicked.connect(self.eslestir)
        self.ana_pencere.pushButton_istatislik.clicked.connect(self.istatislik)
        self.ana_pencere.pushButton_kart.clicked.connect(self.kart)
        self.ana_pencere.pushButton_kaydet.clicked.connect(self.kaydet)
        self.ana_pencere.pushButton_test.clicked.connect(self.test)
        self.ana_pencere.pushButton_yenikelime.clicked.connect(self.yenikelime)
        self.ana_pencere.actionDark.triggered.connect(self.darkmode)
        self.ana_pencere.actionWhite.triggered.connect(self.whitemode)
        self.setCentralWidget(self.ana_pencere.centralwidget)
        
        # Başlangıçta global temayı uygula
        apply_theme(self)

    def ara(self):
        self.close()
        self.araac = arapencere()
        apply_theme(self.araac)
        self.araac.show()

    def cumle(self):
        self.close()
        self.cumleac = cumlepencere()
        apply_theme(self.cumleac)
        self.cumleac.show()

    def dosya(self):
        self.close()
        self.dosyaac = dosyapencere()
        apply_theme(self.dosyaac)
        self.dosyaac.show()

    def eslestir(self):
        self.close()
        self.eslestirac = eslestirpencere()
        apply_theme(self.eslestirac)
        self.eslestirac.show()

    def istatislik(self):
        self.close()
        self.istatislikac = istatislikpencere()
        apply_theme(self.istatislikac)
        self.istatislikac.show()

    def kart(self):
        self.close()
        self.kartac = flashcardtekrarpencere()
        apply_theme(self.kartac)
        self.kartac.show()

    def test(self):
        self.close()
        self.testac = testpencere()
        apply_theme(self.testac)
        self.testac.show()

    def yenikelime(self):
        self.close()
        self.yenikelimeac = yenikelimepencere()
        apply_theme(self.yenikelimeac)
        self.yenikelimeac.show()

    def kaydet(self):
        pass

    def darkmode(self):
        global current_theme
        current_theme = "dark"
        apply_theme(self)

    def whitemode(self):
        global current_theme
        current_theme = "white"
        apply_theme(self)

if __name__ == "__main__":
    app = QApplication([])
    window = anapencere()
    window.show()
    app.exec_()