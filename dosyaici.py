from PyQt5.QtWidgets import *
from ui_dosyaiciyeni import Ui_MainWindow
from anasayfa import apply_theme  # Tema fonksiyonunu import et
from veritabani import database
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class dosyaicipencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.dosyaici_pencere = Ui_MainWindow()
        self.dosyaici_pencere.setupUi(self)
        self.db = database()
        self.dosyaici_pencere.pushButton_geri.clicked.connect(self.geri)
        self.dosyaici_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.dosyaici_pencere.pushButton_kaydet.clicked.connect(self.kaydet)
        self.dosyaici_pencere.pushButton_yeni.clicked.connect(self.yeni)
        self.dosyaici_pencere.pushButton_goruntule.clicked.connect(self.goruntule)
        self.setCentralWidget(self.dosyaici_pencere.centralwidget) 
        apply_theme(self)
    def dosyaismial(self,isim):
        self.filename = isim
        self.kelimeleriyukle()
    def kelimeleriyukle(self, zorluk = None):
        id = self.db.dosyaidgetir(self.filename)
        kelimeler = self.db.kelimelerigetir(id,zorluk)
        self.dosyaici_pencere.lineEdit_dosya.setText(self.filename)
        for i in reversed(range(self.dosyaici_pencere.gridLayout.count())):
            self.dosyaici_pencere.gridLayout.itemAt(i).widget().setParent(None)

        kelimebaslik = QLabel("kelime")
        kelimebaslik.setStyleSheet("background-color: #44475a; color: white; border-radius: 5px;")
        kelimebaslik.setFixedHeight(40)
        kelimebaslik.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 14) 
        kelimebaslik.setFont(font)

        anlambaslik = QLabel("anlami")
        anlambaslik.setStyleSheet("background-color: #44475a; color: white; border-radius: 5px;")
        anlambaslik.setFixedHeight(40)
        anlambaslik.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 14) 
        anlambaslik.setFont(font)

        cumlebaslik = QLabel("ornek cumle")
        cumlebaslik.setStyleSheet("background-color: #44475a; color: white; border-radius: 5px;")
        cumlebaslik.setFixedHeight(40)
        cumlebaslik.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 14) 
        cumlebaslik.setFont(font)

        self.dosyaici_pencere.gridLayout.addWidget(kelimebaslik, 0, 0)
        self.dosyaici_pencere.gridLayout.addWidget(anlambaslik, 0, 1)
        self.dosyaici_pencere.gridLayout.addWidget(cumlebaslik, 0, 2)

        for i, kelime in enumerate(kelimeler):

            english = kelime[0]
            meaning = kelime[1]
            sentence = kelime[2]
            row = i+1  
            col1 = 0  
            col2 = 1  
            col3 = 2
            
            view1_textedit = QTextEdit()
            view1_textedit.setText(english)
            view1_textedit.setStyleSheet("background-color: #6272a4; color: white; border-radius: 5px; font-size: 14px; padding: 8px;")
            view1_textedit.setFixedHeight(60)
            view1_textedit.setLineWrapMode(QTextEdit.WidgetWidth)

            view2_textedit = QTextEdit()
            view2_textedit.setText(meaning)
            view2_textedit.setStyleSheet("background-color: #6272a4; color: white; border-radius: 5px; font-size: 14px; padding: 8px;")
            view2_textedit.setFixedHeight(60)
            view2_textedit.setLineWrapMode(QTextEdit.WidgetWidth)

            view3_textedit = QTextEdit()
            view3_textedit.setText(sentence)
            view3_textedit.setStyleSheet("background-color: #6272a4; color: white; border-radius: 5px; font-size: 14px; padding: 8px;")
            view3_textedit.setFixedHeight(60)
            view3_textedit.setLineWrapMode(QTextEdit.WidgetWidth)

            self.dosyaici_pencere.gridLayout.addWidget(view1_textedit, row, col1)
            self.dosyaici_pencere.gridLayout.addWidget(view2_textedit, row, col2)
            self.dosyaici_pencere.gridLayout.addWidget(view3_textedit, row, col3)

    def geri(self):
        from dosya import dosyapencere
        self.close()
        self.giris = dosyapencere()
        apply_theme(self.giris)  # Yeni pencereye temayı uygula
        self.giris.show()

    def anasayfa(self):
        from anasayfa import anapencere
        self.close()
        self.giris = anapencere()
        apply_theme(self.giris)  # Yeni pencereye temayı uygula
        self.giris.show()
    def kaydet(self):
        id = self.db.dosyaidgetir(self.filename)
        self.db.kelimesil(id)
        layout = self.dosyaici_pencere.gridLayout
        row_count = layout.rowCount()

        for row in range(1, row_count):
            kelime_widget = layout.itemAtPosition(row, 0)
            anlami_widget = layout.itemAtPosition(row, 1)
            ornek_widget = layout.itemAtPosition(row, 2)

            if kelime_widget and anlami_widget:
               kelime = kelime_widget.widget().toPlainText().strip()
               anlami = anlami_widget.widget().toPlainText().strip()
               ornek = ornek_widget.widget().toPlainText().strip() if ornek_widget else ""

               if kelime and anlami:
                   self.db.kelimeekle(kelime, anlami, id, ornek)
        QMessageBox.information(self, "Başarılı","Dosya Kaydedildi")
        self.geri()
    def yeni(self):
        self.dosyaici_pencere.yenikelime()
    def goruntule(self):
        self.zorluk = []
        if self.dosyaici_pencere.checkBox_hepsi.isChecked():
            self.kelimeleriyukle()
        else:
            if self.dosyaici_pencere.checkBox_biliyom.isChecked():
                self.zorluk.append(1)
            else:
                self.zorluk.append(999)
            if self.dosyaici_pencere.checkBox_orta.isChecked():
                self.zorluk.append(2)
            else:
                self.zorluk.append(999)
            if self.dosyaici_pencere.checkBox_bilmiyom.isChecked():
                self.zorluk.append(3)
            else:
                self.zorluk.append(999)
            self.kelimeleriyukle(self.zorluk)