from PyQt5.QtWidgets import *
from ui_flashcard import Ui_MainWindow
from veritabani import database


class flashcardpencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.flashcard_pencere = Ui_MainWindow()
        self.flashcard_pencere.setupUi(self)
        self.flashcard_pencere.pushButton_geri.clicked.connect(self.geri)
        self.flashcard_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.flashcard_pencere.pushButton_kelime.clicked.connect(self.kelime)
        self.flashcard_pencere.pushButton_sonraki.clicked.connect(self.sonraki)
        self.flashcard_pencere.pushButton_onceki.clicked.connect(self.onceki)
        self.setCentralWidget(self.flashcard_pencere.centralwidget) 
        self.flashcard_pencere.pushButton_kelime.setText()
        self.flashcard_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")

    def geri(self, ):
        from yenikelime import yenikelimepencere
        self.giris = yenikelimepencere()
        self.giris.show()
        self.close() 
    def anasayfa(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close() 
    def onceki(self,):
        pass
    def sonraki(self,):
        pass
    def kelimesayisi(self,sayi):
        kelimesayisi = sayi
    def dosyaid(self,id):
        dosyaid = id
    def kelime(self, ):
        current_index = self.index

        if current_index == 0:
            self.flashcard_pencere.pushButton_kelime.setText("Arka Yüzü Göster")
            self.flashcard_pencere.pushButton_kelime.setStyleSheet("background-color: orange; color: white;")

            self.index = 1
        else:
            self.flashcard_pencere.pushButton_kelime.setText("Ön Yüzü Göster")  
            self.flashcard_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")

            self.index = 0
