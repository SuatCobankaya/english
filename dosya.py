from PyQt5.QtWidgets import *
from ui_dosyayeni import Ui_MainWindow
from veritabani import database
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class dosyapencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.dosya_pencere = Ui_MainWindow()
        self.dosya_pencere.setupUi(self)
        self.db = database()
        self.dosya_pencere.pushButton_geri.clicked.connect(self.geri)
        self.dosya_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.dosya_pencere.pushButton_yeni.clicked.connect(self.yeni)
        self.dosya_pencere.pushButton_sil.clicked.connect(self.sil)
        self.selected_file = None
        self.setCentralWidget(self.dosya_pencere.centralwidget) 
        self.load_files()
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
    def yeni(self, ):
        from yenidosya import yenidosyapencere
        self.giris = yenidosyapencere()
        self.giris.show()
        self.close() 
    def sil(self, ):
        if hasattr(self, 'selected_file') and self.selected_file is not None:
          reply = QMessageBox.question(
             self,
             "Dosya Silme Onayı",
             f"'{self.selected_file}' dosyasını silmek istediğinizden emin misiniz?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
          )
          if reply == QMessageBox.Yes:
             self.db.dosyasil(self.selected_file)
             self.load_files()
             QMessageBox.information(self, "Başarılı", f"'{self.selected_file}' silindi!")
          else:
             QMessageBox.information(self, "İptal Edildi", "Dosya silme işlemi iptal edildi.")
        else:
          QMessageBox.warning(self, "Hata", "Lütfen silmek için bir dosya seçin!")
    def load_files(self):
        filenames = self.db.dosyalarigetir()

        for i in reversed(range(self.dosya_pencere.gridLayout.count())):
            self.dosya_pencere.gridLayout.itemAt(i).widget().setParent(None)

        for i, filename in enumerate(filenames):
            row = i  
            col1 = 0  
            col2 = 1  
            col3 = 3 
            col4 = 2

            label = QLabel(filename)
            label.setStyleSheet("background-color: #44475a; color: white; border-radius: 5px;")
            label.setFixedHeight(40)
            label.mousePressEvent = lambda event, fname=filename: self.select_file(fname)
            label.setAlignment(Qt.AlignCenter)
            font = QFont("Arial", 14) 
            label.setFont(font)
            

            view_button = QPushButton("Görüntüle")
            view_button.setStyleSheet("background-color: #6272a4; color: black; border-radius: 5px; font-size: 14px;")
            view_button.setFixedHeight(40)
            view_button.clicked.connect(lambda checked, fname=filename: self.view_file(fname))

            tekrar_button = QPushButton("Öğrendiklerini Tekrar Et")
            tekrar_button.setStyleSheet("background-color: #e88c2b; color: black; border-radius: 5px; font-size: 14px;")
            tekrar_button.setFixedHeight(40)
            tekrar_button.clicked.connect(lambda checked, fname=filename: self.tekrar_file(fname))

            learn_button = QPushButton("Öğren")
            learn_button.setStyleSheet("background-color: #50fa7b; color: black; border-radius: 5px; font-size: 14px;")
            learn_button.setFixedHeight(40)
            learn_button.clicked.connect(lambda checked, fname=filename: self.learn_file(fname))

            self.dosya_pencere.gridLayout.addWidget(label, row, col1)  
            self.dosya_pencere.gridLayout.addWidget(view_button, row, col2)  
            self.dosya_pencere.gridLayout.addWidget(learn_button, row, col3)
            self.dosya_pencere.gridLayout.addWidget(tekrar_button, row, col4)
    def select_file(self, filename):
     self.selected_file = filename

     for i in range(self.dosya_pencere.gridLayout.count()):
        widget = self.dosya_pencere.gridLayout.itemAt(i).widget()
        
        if isinstance(widget, QLabel):
            if widget.text() == filename:
                widget.setStyleSheet("background-color: #ffb86c; color: black; border-radius: 5px;")
            else:
                widget.setStyleSheet("background-color: #44475a; color: white; border-radius: 5px;")

    def view_file(self,filename):
        id = self.db.dosyaidgetir(filename)
        self.db.baglantiac()
        self.db.cursor.execute("SELECT Meaning FROM WORDS WHERE FileID = ? AND zorluk =?", (id,1))
        biliyom = self.db.cursor.fetchall()
        self.db.cursor.execute("SELECT Meaning FROM WORDS WHERE FileID = ? AND zorluk =?", (id,3))
        bilmiyom = self.db.cursor.fetchall()
        self.db.cursor.execute("SELECT Meaning FROM WORDS WHERE FileID = ? AND zorluk =?", (id,2))
        orta = self.db.cursor.fetchall()
        self.db.baglantikapat()

        biliyom = len(biliyom)
        bilmiyom = len(bilmiyom)
        orta = len(orta)

        from dosyaici import dosyaicipencere
        self.giris = dosyaicipencere()
        self.giris.dosyaismial(filename,biliyom,orta,bilmiyom)
        self.giris.show()
        self.close()

    def learn_file(self,filename):
        sayi, ok = QInputDialog.getText(self, "Kelime Sayısı", "Kelime Sayısı Giriniz:")
        sinir = self.db.tekrarvarmi(filename)
        id = self.db.dosyaidgetir(filename)
        if ok:
         try:
            kelime_sayisi = int(sayi) 
            if sinir>=kelime_sayisi:
               kelimeler = self.db.randomyeni(id,kelime_sayisi)
               from flashcardtekrar import flashcardtekrarpencere
               self.giris = flashcardtekrarpencere(kelimeler)
               self.giris.show()
               self.close()
            else:
              QMessageBox.warning(self, "Hata", "Öğrenebileceğiniz Maksimum Kelime Sayısı: " + str(sinir))  
         except ValueError:
            QMessageBox.warning(self, "Hata", "Geçerli Bir Sayı Giriniz.")


    def tekrar_file(self,filename):
        sayi, ok = QInputDialog.getText(self, "Kelime Sayısı ", "Kelime Sayısı Giriniz:")
        sinir = self.db.kelimevarmi(filename)
        id = self.db.dosyaidgetir(filename)
        if ok:
         try:
            kelime_sayisi = int(sayi) 
            if sinir>=kelime_sayisi:
               kelimeler = self.db.randomtekrar(id,kelime_sayisi)
               from flashcard import flashcardpencere
               self.giris = flashcardpencere(kelimeler)
               self.giris.show()
               self.close()
            else:
               QMessageBox.warning(self, "Hata", "Toplam Öğrendiğiniz Kelime Sayısı: " + str(sinir) )
               
         except ValueError:
            QMessageBox.warning(self, "Hata", "Geçerli Bir Sayı Giriniz.")

            
        
    