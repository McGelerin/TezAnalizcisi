import fitz

class HataKontrolleri:

    def __init__(self, tez_nesnesi, tez_yolu):
        self.tez_nesnesi = tez_nesnesi
        self.tez_yolu = tez_yolu
        self.Tezi_Ac()

    @property
    def Kontrol_Baslat(self):
        islem_numarasi = []
        message = []

        if (self.Baslik_Kontrolu(self.tez_nesnesi.tez_basligi) == False):
            islem_numarasi.append(1)
            message.append("1-Başlıktaki her kelimenin ilk harfi büyük yazılmamış.")

        if (self.Giris_Yazisi_Kontrolu(self.tez_nesnesi.giris_nesnesi.giris_yazisi) == False):
            islem_numarasi.append(2)
            message.append("2-Giriş Sayfasının İlk Paragrafında Teşekkür İbaresi Yer Almıyor..")

        if (self.Sekil_Sayfa_Uyum_Kontrolu(self.tez_nesnesi.sekiller_nesnesi) == False):
            islem_numarasi.append(3)
            message.append("3-Şekiller Listesindeki Şekil Açıklaması, Numarasıyla Eşleşmiyor")

        if (self.Cizelge_Sayfa_Uyum_Kontrolu(self.tez_nesnesi.cizelgeler_nesnesi) == False):
            islem_numarasi.append(4)
            message.append("4-Program Tanımlaması Program Listesindeki Numarayla Eşleşmiyor")

        if (self.Icindekiler_Kontrolu(self.tez_nesnesi.icindekiler_nesnesi) == False):
            islem_numarasi.append(5)
            message.append("5-İçerikteki Sayfa Numaraları Doğru Değil")

        if (self.Cift_Tirnak_Kontrolu(self.tez_nesnesi.icerik_nesnesi.sayfalar_listesi) == False):
            islem_numarasi.append(6)
            message.append("6-İki Çift Alıntı Arasında Kullanılan 50'den Fazla Kelime")

        if (self.Paragraf_Satir_Kontrolu(self.tez_nesnesi.icerik_nesnesi.sayfalar_listesi) == False):
            islem_numarasi.append(7)
            message.append("7-Paragraf İki Satırdan ve / veya İkiden Az Satırdan Oluşur")

        if len(message) < 1:
            message.append("8-Herhangi bir sorun bulunamadı.")
            islem_numarasi = [8]
        return islem_numarasi, message

    def Baslik_Kontrolu(self, baslik_yazisi):
        baslik_yazisi = baslik_yazisi.split(" ")
        for kelime in baslik_yazisi:
            if len(kelime) > 0 and kelime[0].islower():
                return False
        return True

    def Giris_Yazisi_Kontrolu(self, giris_yazisi):
        ilk_paragraf = ""
        satirlar = giris_yazisi.splitlines()
        i = 0
        while i < len(satirlar) and len(satirlar[i]) >= 5:
            ilk_paragraf = ilk_paragraf + satirlar[i]
            i = i + 1

        if "Teşekkür" in ilk_paragraf or "teşekkür" in ilk_paragraf:
            return False
        return True

    def Sekil_Sayfa_Uyum_Kontrolu(self, sekiller_nesnesi):
        sekiller_listesi = sekiller_nesnesi.sekiller_listesi

        for sekil in sekiller_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(sekiller_listesi[sekil])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if sekil not in sayfa_yazisi:
                return False
        return True

    def Cizelge_Sayfa_Uyum_Kontrolu(self, cizelgeler_nesnesi):
        cizelgeler_listesi = cizelgeler_nesnesi.cizelgeler_listesi

        for cizelge in cizelgeler_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(cizelgeler_listesi[cizelge])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if cizelge not in sayfa_yazisi:
                return False
        return True

    def Icindekiler_Kontrolu(self, icindekiler_nesnesi):
        icindekiler_listesi = icindekiler_nesnesi.icindekiler_listesi
        for icindeki in icindekiler_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(icindekiler_listesi[icindeki])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if (icindeki not in sayfa_yazisi):
                return False
        return True

    def Cift_Tirnak_Kontrolu(self, icerik_sayfa_numaralari):
        for sayfa_numarasi in icerik_sayfa_numaralari:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(sayfa_numarasi)
            sayfa_yazisi = sayfa_nesnesi.getText()
            sayfa_yazisi = sayfa_yazisi.split("“")
            if (len(sayfa_yazisi) > 2):
                if (len(sayfa_yazisi[1].split(" ")) >= 50):
                    return False
        return True

    def Paragraf_Satir_Kontrolu(self, icerik_sayfa_numaralari):
        for sayfa_numarasi in icerik_sayfa_numaralari:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(sayfa_numarasi)
            sayfa_yazisi = sayfa_nesnesi.getText()
            sayfa_satirlari = sayfa_yazisi.splitlines()
            satir_sayaci = 0
            for i in range(len(sayfa_satirlari) - 1):
                if (len(sayfa_satirlari[i]) >= 5):
                    satir_sayaci = satir_sayaci + 1
                else:
                    satir_sayaci = 0

                if len(sayfa_satirlari[i + 1]) < 5 and satir_sayaci <= 2:
                    return False
        return True

    def Tezi_Ac(self):
        self.pdf_nesnesi = fitz.open(self.tez_yolu)
        print(self.pdf_nesnesi)