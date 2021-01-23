class Icindekiler:
    icindekiler_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        baslik = eleman_yazisi[0]
        icerik = baslik.strip()
        self.icindekiler_listesi[icerik] = sayfa_numarasi


class Sekiller:
    sekiller_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        baslik = eleman_yazisi[0]
        icerik = baslik.strip()
        self.sekiller_listesi[icerik] = sayfa_numarasi


class Cizelgeler:
    cizelgeler_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        baslik = eleman_yazisi[0]
        icerik = baslik.strip()
        self.cizelgeler_listesi[icerik] = sayfa_numarasi


class Giris:
    giris_yazisi = ""

    def eleman_ekle(self, eleman_yazisi):
        self.giris_yazisi = self.giris_yazisi + " \n " + eleman_yazisi


# indisler 0 dan başlıyor fakat 0 = sayfa 1 anlamına gelmektedir
class Icerik:
    sayfalar_listesi = []

    def icerigi_guncelle(self, icerik_baslangic_sayfasi, icerik_bitis_sayfasi):
        for i in range(icerik_baslangic_sayfasi, icerik_bitis_sayfasi):
            self.sayfalar_listesi.append(i)


class Tez:
    icindekiler_nesnesi = ""
    sekiller_nesnesi = ""

    cizelgeler_nesnesi = ""

    giris_nesnesi = ""
    icerik_nesnesi = ""
    tez_basligi = ""

    def __init__(self, tez_basligi, icindekiler_nesnesi, sekiller_nesnesi,
                 cizelgeler_nesnesi, giris_nesnesi, icerik_nesnesi):
        self.icindekiler_nesnesi = icindekiler_nesnesi
        self.sekiller_nesnesi = sekiller_nesnesi
        self.giris_nesnesi = giris_nesnesi
        self.icerik_nesnesi = icerik_nesnesi
        self.cizelgeler_nesnesi = cizelgeler_nesnesi
        self.tez_basligi = tez_basligi
