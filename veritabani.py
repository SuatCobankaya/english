import sqlite3
import os
import random
class database():
    def baglantiac(self):
            self.con = sqlite3.connect("veritabani.db")
            self.cursor = self.con.cursor()
    def dosyalarigetir(self):
         self.baglantiac()
         self.cursor.execute("SELECT FileName FROM Files")
         dosyalar = self.cursor.fetchall()
         self.baglantikapat()
         return [row[0] for row in dosyalar]
    def ara(self,kelime):
         kelime = kelime.lower()
         self.baglantiac()
         self.cursor.execute("SELECT Meaning FROM WORDS WHERE EnglishWord = ?", (kelime,))
         anlamlar = self.cursor.fetchall()
         self.baglantikapat()
         return [row[0] for row in anlamlar]
    def kelimelerigetir(self,a):
         self.baglantiac()
         self.cursor.execute("SELECT EnglishWord, Meaning, ExampleSentences FROM WORDS WHERE FileId = ?", (a,))
         kelimeler = self.cursor.fetchall()
         self.baglantikapat()
         return kelimeler
    def randomyeni(self,dosyaid,sayi):
         self.baglantiac()
         self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ?", (dosyaid,))
         rastgele = self.cursor.fetchall()
         self.baglantikapat()
         if len(rastgele) < sayi:
          return rastgele
         else:
          rastgele = random.sample(rastgele, sayi)
          return rastgele
    def kelimevarmi(self,dosyaadi):
         db = database()
         dosyaid = db.dosyaidgetir(dosyaadi)
         self.baglantiac()
         self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ? AND zorluk = ?", (dosyaid,2))
         zorluk2 = self.cursor.fetchall()
         sayi2 = len(zorluk2)
         self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ? AND zorluk = ?", (dosyaid,3))
         zorluk3 = self.cursor.fetchall()
         sayi3 = len(zorluk3)
         return sayi2+sayi3
    def tekrarvarmi(self,dosyaadi):
        db = database()
        dosyaid = db.dosyaidgetir(dosyaadi)
        self.baglantiac()
        self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ? AND zorluk IS NULL", (dosyaid,))
        kelimeler = self.cursor.fetchall()
        sayi = len(kelimeler)
        return sayi
    def randomtekrar(self,dosyaid,sayi):
         kontrol = 0
         tekrarsayaci = 1
         tum2kelimeler = []
         tum3kelimeler = []
         kalan = sayi % 2
         if kalan == 1:
             yarim3 = (sayi // 2)+1
         else:
             yarim3 = sayi // 2
         yarim2 = sayi // 2
         self.baglantiac()
         self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ? AND zorluk = ?", (dosyaid,2))
         zorluk2 = self.cursor.fetchall()
         sayi2 = len(zorluk2)
         self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ? AND zorluk = ?", (dosyaid,3))
         zorluk3 = self.cursor.fetchall()
         sayi3 = len(zorluk3)
         if sayi2<yarim2:
             yarim3 = yarim3 + (yarim2-sayi2)
             yarim2 = sayi2
         elif sayi3<yarim3:
             yarim2 = yarim2 + (yarim3-sayi3)
             yarim3 = sayi3
         while kontrol == 0:
             self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ? AND zorluk = ? AND tekrar = ?", (dosyaid,2,tekrarsayaci))
             zorluk2 = self.cursor.fetchall()
             kosul = len(zorluk2)+len(tum2kelimeler)
             if kosul>=yarim2:
                 rastgele = yarim2-len(tum2kelimeler)
                 if rastgele != 0:
                     tum2kelimeler = tum2kelimeler+random.sample(zorluk2, rastgele)
                 else:
                     tum2kelimeler = tum2kelimeler + zorluk2
                 kontrol = 1

             else:
                 tum2kelimeler = tum2kelimeler + zorluk2
                 tekrarsayaci = tekrarsayaci+1

         kontrol = 0
         tekrarsayaci = 1

         while kontrol == 0:
             self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ? AND zorluk = ? AND tekrar = ?", (dosyaid,3,tekrarsayaci))
             zorluk3 = self.cursor.fetchall()
             kosul = len(zorluk3)+len(tum3kelimeler)
             if kosul>=yarim3:
                 rastgele = yarim3-len(tum3kelimeler)
                 if rastgele != 0:
                     tum3kelimeler = tum3kelimeler+random.sample(zorluk3, rastgele)
                 else:
                     tum3kelimeler = tum3kelimeler + zorluk3
                 kontrol = 1

             else:
                 tum3kelimeler = tum3kelimeler + zorluk3
                 tekrarsayaci = tekrarsayaci+1

         self.baglantikapat()
         tumkelimeler = tum2kelimeler+tum3kelimeler
         return tumkelimeler
    def dosyaekle(self,dosyaadi):
         self.baglantiac()
         self.cursor.execute("""INSERT INTO Files (FileName) VALUES (?);""", (dosyaadi,))
         self.con.commit()
         self.baglantikapat()
    def dosyasil(self,dosyaismi):
         id = self.dosyaidgetir(dosyaismi)
         self.baglantiac()
         self.cursor.execute("""DELETE FROM Files WHERE FileName = ?;""", (dosyaismi,))
         self.cursor.execute("""DELETE FROM WORDS WHERE FileId = ?;""", (id,))
         self.con.commit()
         self.baglantikapat()
    def dosyaidgetir(self,a):
         self.baglantiac()
         self.cursor.execute("SELECT FileId FROM Files WHERE FileName = ?", (a,))
         id = self.cursor.fetchall()
         self.baglantikapat()
         return id[0][0]
    def kelimeekle(self,kelime,anlam,dosyaid,cumle=None):
         self.baglantiac()
         self.cursor.execute("""INSERT INTO WORDS (EnglishWord, Meaning, FileId, ExampleSentences) VALUES (?, ?, ?, ?);""", (kelime,anlam,dosyaid,cumle))
         self.con.commit()
         self.baglantikapat()
    def baglantikapat(self):
        self.con.close()
    def kelimesil(self,id):
        self.baglantiac()
        self.cursor.execute("""DELETE FROM WORDS WHERE FileId = ?;""", (id,))
        self.con.commit()
        self.baglantikapat()


