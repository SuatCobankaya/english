from PyQt5.QtWidgets import *
from ui_flashcardtekrar import Ui_MainWindow

class flashcardtekrarpencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.flashcardtekrar_pencere = Ui_MainWindow()
        self.flashcardtekrar_pencere.setupUi(self)
        self.flashcardtekrar_pencere.pushButton_geri.clicked.connect(self.geri)
        self.flashcardtekrar_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.flashcardtekrar_pencere.pushButton_kelime.clicked.connect(self.kelime)
        self.setCentralWidget(self.flashcardtekrar_pencere.centralwidget) 
        self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")

        self.index = 0
        
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
    def kelimelerial(self,kelime):
        for i in kelime:
           ingilizce = kelime[0]
           turkce = kelime[1]

    def kelime(self, ):
        current_index = self.index

        if current_index == 0:
            self.flashcardtekrar_pencere.pushButton_kelime.setText("Arka Yüzü Göster")
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: orange; color: white;")

            self.index = 1
        else:
            self.flashcardtekrar_pencere.pushButton_kelime.setText("Ön Yüzü Göster")  
            self.flashcardtekrar_pencere.pushButton_kelime.setStyleSheet("background-color: lightblue; color: black;")

            self.index = 0
