from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ui_dosyaiciyeni import Ui_MainWindow
from anasayfa import apply_theme
from veritabani import database
from dosya import dosyapencere
from anasayfa import anapencere

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

    def dosyaismial(self, isim):
        self.filename = isim
        self.kelimeleriyukle()

    def kelimeleriyukle(self, zorluk=None):
        self.setUpdatesEnabled(False) 
        id = self.db.dosyaidgetir(self.filename)
        kelimeler = self.db.kelimelerigetir(id, zorluk)
        self.dosyaici_pencere.lineEdit_dosya.setText(self.filename)

        layout = self.dosyaici_pencere.gridLayout
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item and item.widget():
                item.widget().deleteLater()

        font = QFont("Arial", 14)
        headers = ["kelime", "anlami", "ornek cumle"]
        for idx, text in enumerate(headers):
            label = QLabel(text)
            label.setStyleSheet("background-color: #44475a; color: white; border-radius: 5px;")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(font)
            label.setFixedHeight(40)
            layout.addWidget(label, 0, idx)

        for row, kelime in enumerate(kelimeler, start=1):
            for col, text in enumerate(kelime[:3]):
                edit = QLineEdit()
                edit.setText(str(text))
                edit.setStyleSheet("background-color: #6272a4; color: white; border-radius: 5px; font-size: 14px; padding: 8px;")
                edit.setFixedHeight(40)
                layout.addWidget(edit, row, col)

        self.setUpdatesEnabled(True) 

    def geri(self):
        self.close()
        self.giris = dosyapencere()
        apply_theme(self.giris)
        self.giris.show()

    def anasayfa(self):
        self.close()
        self.giris = anapencere()
        apply_theme(self.giris)
        self.giris.show()

    def kaydet(self):
        yeni_dosya_adi = self.dosyaici_pencere.lineEdit_dosya.text().strip()

        if not yeni_dosya_adi:
            QMessageBox.warning(self, "Uyarı", "Dosya adı boş olamaz!")
            return

        if yeni_dosya_adi != self.filename:
            self.db.dosyaadiguncelle(self.filename, yeni_dosya_adi)
            self.filename = yeni_dosya_adi

        id = self.db.dosyaidgetir(self.filename)
        layout = self.dosyaici_pencere.gridLayout
        row_count = layout.rowCount()
        yeni_kelimeler = []

        for row in range(1, row_count):
            kelime_widget = layout.itemAtPosition(row, 0)
            anlami_widget = layout.itemAtPosition(row, 1)
            ornek_widget = layout.itemAtPosition(row, 2)

            if kelime_widget and anlami_widget:
                kelime = kelime_widget.widget().text().strip()
                anlami = anlami_widget.widget().text().strip()
                ornek = ornek_widget.widget().text().strip() if ornek_widget else ""

                if kelime and anlami:
                    yeni_kelimeler.append((kelime, anlami, ornek))

        self.db.tumkelimelerisil(id)

        for kelime, anlami, ornek in yeni_kelimeler:
            self.db.kelimeekle(kelime, anlami, id, ornek)

        QMessageBox.information(self, "Başarılı", "Dosya Kaydedildi")
        self.geri()

    def yeni(self):
        layout = self.dosyaici_pencere.gridLayout
        row_count = layout.rowCount()

        font = QFont("Arial", 14)
        for col in range(3):
            edit = QLineEdit()
            edit.setStyleSheet("background-color: #6272a4; color: white; border-radius: 5px; font-size: 14px; padding: 8px;")
            edit.setFixedHeight(40)
            edit.setFont(font)
            layout.addWidget(edit, row_count, col)

    def goruntule(self):
        self.zorluk = []
        if self.dosyaici_pencere.checkBox_hepsi.isChecked():
            self.kelimeleriyukle()
        else:
            self.zorluk = [
                1 if self.dosyaici_pencere.checkBox_biliyom.isChecked() else 0,
                2 if self.dosyaici_pencere.checkBox_orta.isChecked() else 0,
                3 if self.dosyaici_pencere.checkBox_bilmiyom.isChecked() else 0
            ]
            self.kelimeleriyukle(self.zorluk)