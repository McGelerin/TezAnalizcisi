import fitz
from Fonksiyonlar import Icindekiler, Sekiller, Giris, Cizelgeler, Icerik, Tez


class PdfIslemleri:
    tez_yolu = ""
    tez_okuyucu = ""
    tez_nesnesi = ""
    icindekiler_listesi_sayfa_numaralari = []
    sekiller_listesi_sayfa_numaralari = []
    giris_sayfa_numaralari = []
    cizelgeler_sayfa_numaralari = []
    tez_baslangic_sayfasi = 0
    baslik_sayfa_numarasi = 0
    baslik = ""
    icindekiler_nesnesi = Icindekiler()
    sekiller_nesnesi = Sekiller()
    giris_nesnesi = Giris()
    cizelgeler_nesnesi = Cizelgeler()
    icerik_nesnesi = Icerik()

    def __init__(self, tez_baslik_sayfa_numarasi, pdf_tez_yolu, icindekiler_sayfalari, sekiller_sayfalari,
                 cizelgeler_sayfalari, giris_sayfalari,
                 tez_baslangic_sayfasi):
        self.tez_yolu = pdf_tez_yolu
        self.icindekiler_listesi_sayfa_numaralari = icindekiler_sayfalari
        self.sekiller_listesi_sayfa_numaralari = sekiller_sayfalari
        self.giris_sayfa_numaralari = giris_sayfalari
        self.cizelgeler_listesi_sayfa_numaralari = cizelgeler_sayfalari
        self.tez_baslangic_sayfasi = tez_baslangic_sayfasi - 1
        self.baslik_sayfa_numarasi = tez_baslik_sayfa_numarasi - 1
        self.messageBox = []
        self.Tezi_Ac()

    def Tezi_Ac(self):
        self.tez_nesnesi = fitz.open(self.tez_yolu)
        self.Tezi_Parcala()

    def Tez_Nesnesi_Olustur(self):

        return Tez(self.baslik,
                   self.icindekiler_nesnesi,
                   self.sekiller_nesnesi,
                   self.cizelgeler_nesnesi,
                   self.giris_nesnesi,
                   self.icerik_nesnesi)

    def Tezi_Parcala(self):

        en_buyuk_giris_sayfasi = 0

        if len(self.icindekiler_listesi_sayfa_numaralari) > 0:
            for sayfa_numarasi in self.icindekiler_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.icindekiler_nesnesi.eleman_ekle(baslik + " " + numara, self.tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir[0].isdigit() and (guncel_satir[1] == '.' or guncel_satir[2] == '.')):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            print(self.icindekiler_nesnesi.icindekiler_listesi)
            print("İçerik Oluşturuldu..")
            self.messageBox.append("İçerik Oluştu...")

        if len(self.sekiller_listesi_sayfa_numaralari) > 0:
            for sayfa_numarasi in self.sekiller_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.sekiller_nesnesi.eleman_ekle(baslik + " " + numara, self.tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir.split(" ")[0] == "Şekil"):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            print(self.sekiller_nesnesi.sekiller_listesi)
            print("Şekiller oluşturuldu")
            self.messageBox.append("Şekiller oluştu..")

        if len(self.cizelgeler_listesi_sayfa_numaralari) > 0:
            for sayfa_numarasi in self.cizelgeler_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.cizelgeler_nesnesi.eleman_ekle(baslik + " " + numara, self.tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir.split(" ")[0] == "Çizelge"):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            # print(self.cizelgeler_nesnesi.cizelgeler_listesi)
            print("Çizelgeler OLuşturuldu..")
            self.messageBox.append("Çizelgeler Oluşturuldu..")

        if len(self.giris_sayfa_numaralari) > 0:
            for sayfa_numarasi in self.giris_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                self.giris_nesnesi.eleman_ekle(sayfa_yazisi)
            # print(str(len(self.giris_nesnesi.giris_yazisi)) + " adet harf içeriyor")



        sayfa_nesnesi = self.tez_nesnesi.loadPage(self.baslik_sayfa_numarasi)
        sayfa_yazisi = sayfa_nesnesi.getText()
        sayfa_satirlari = sayfa_yazisi.splitlines()
        bos_satir_sayisi = 0
        baslik_satiri_baslangici = 0
        for i in range(len(sayfa_satirlari)):
            if (len(sayfa_satirlari[i]) < 2):
                bos_satir_sayisi = bos_satir_sayisi + 1
            if (len(sayfa_satirlari[i]) >= 5 and bos_satir_sayisi >= 3):
                baslik_satiri_baslangici = i
                break

        while baslik_satiri_baslangici < len(sayfa_satirlari) and len(sayfa_satirlari[baslik_satiri_baslangici]) >= 5:
            self.baslik = self.baslik + sayfa_satirlari[baslik_satiri_baslangici] + " "
            baslik_satiri_baslangici = baslik_satiri_baslangici + 1
        print("Başlık Kısmı Oluşturldu")
        self.messageBox.append("Başlık Kısmı Başarılı")
