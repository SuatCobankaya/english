from PyQt5.QtWidgets import *
from ui_istatislik import Ui_MainWindow
from veritabani import database
from PyQt5.QtCore import Qt

class istatislikpencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.istatislik_pencere = Ui_MainWindow()
        self.istatislik_pencere.setupUi(self)
        self.setCentralWidget(self.istatislik_pencere.centralwidget)

        # Veritabanı bağlantısı
        self.db = database()

        # Butonlar
        self.istatislik_pencere.pushButton_geri.clicked.connect(self.geri)
        self.istatislik_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)

        # Tablolar
        self.tablo_test = self.istatislik_pencere.tableWidget_test
        self.tablo_eslestirme = self.istatislik_pencere.tableWidget_eslestirme
        self._setup_table(self.tablo_test)
        self._setup_table(self.tablo_eslestirme)

        # Verileri yükle
        self.verileri_doldur()

        # Çift tıklama ile detay göster
        self.tablo_test.cellDoubleClicked.connect(self.ayrinti_goster)
        self.tablo_eslestirme.cellDoubleClicked.connect(self.ayrinti_goster)

    def geri(self):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()

    def anasayfa(self):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close()

    def _setup_table(self, tablo):
        header = tablo.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignCenter)
        header.setSectionResizeMode(QHeaderView.Stretch)
        tablo.setEditTriggers(QTableWidget.NoEditTriggers)
        tablo.verticalHeader().setDefaultSectionSize(28)
        tablo.verticalHeader().setVisible(True)

    def verileri_doldur(self):
        self.db.baglantiac()
        self.db.cursor.execute("SELECT tarih, dogru, yanlis FROM TestSonuclari WHERE tip = ?", ("test",))
        self.veri_test = self.db.cursor.fetchall()

        self.db.cursor.execute("SELECT tarih, dogru, yanlis FROM TestSonuclari WHERE tip = ?", ("eslestirme",))
        self.veri_eslestirme = self.db.cursor.fetchall()
        self.db.baglantikapat()

        self.tablo_doldur(self.tablo_test, self.veri_test)
        self.tablo_doldur(self.tablo_eslestirme, self.veri_eslestirme)
        toplam_deneme = len(self.veri_test) + len(self.veri_eslestirme)
        toplam_dogru = 0
        toplam_yanlis = 0
        for veri in self.veri_test + self.veri_eslestirme:
            dogrular = veri[1].split(",") if veri[1] else []
            yanlislar = veri[2].split(",") if veri[2] else []
            toplam_dogru += len(dogrular)
            toplam_yanlis += len(yanlislar)

        oran = round((toplam_dogru / toplam_deneme) * 100, 2) if toplam_deneme > 0 else 0
        self.istatislik_pencere.label_deneme.setText(f"Toplam Deneme: {toplam_deneme}")
        self.istatislik_pencere.label_dogruluk.setText(f"Genel Doğruluk: {oran} %")

    def tablo_doldur(self, tablo, veri):
        tablo.setRowCount(len(veri))
        for row, (tarih, dogrular, yanlislar) in enumerate(veri):
            dogru_liste = dogrular.split(",") if dogrular else []
            yanlis_liste = yanlislar.split(",") if yanlislar else []
            dogru_sayisi = len(dogru_liste)
            yanlis_sayisi = len(yanlis_liste)
            oran = round(dogru_sayisi / (dogru_sayisi + yanlis_sayisi) * 100, 2) if (dogru_sayisi + yanlis_sayisi) > 0 else 0

            for col, deger in enumerate([tarih, dogru_sayisi, yanlis_sayisi, oran]):
                item = QTableWidgetItem(str(deger))
                item.setTextAlignment(Qt.AlignCenter)
                if col == 0:
                    item.setData(Qt.UserRole, {"dogru": dogru_liste, "yanlis": yanlis_liste})
                tablo.setItem(row, col, item)

    def ayrinti_goster(self, row, col):
        tablo = self.sender()
        item = tablo.item(row, 0)
        data = item.data(Qt.UserRole)
        if data:
            dogru_raw = str(data['dogru'])
            yanlis_raw = str(data['yanlis'])
            dogru_temiz = dogru_raw.replace("[", "").replace("]", "").replace("'", "").replace('"', '')
            yanlis_temiz = yanlis_raw.replace("[", "").replace("]", "").replace("'", "").replace('"', '')
            QMessageBox.information(
                self,
                f"Ayrıntı – {item.text()}",
                f"<b>Doğru:</b> {dogru_temiz or '–'}<br><br><b>Yanlış:</b> {yanlis_temiz or '–'}"
            )
