from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from son_arayuz import Ui_MainWindows


class MainWindowApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindows()
        self.ui.setupUi(self)
        self.test()
        self.initSlots()
        self.initParameters()
        self.control()
        self.ui.txt_dosya_yolu.setEnabled(False)

    def initSlots(self):
        self.ui.dosya_sec.clicked.connect(self.dosya_sec)
        self.ui.btn_kontrol.clicked.connect(self.getParameters)

    def initParameters(self):
        self.icindekiler_listesi_sayfa_numaralari = []
        self.sekiller_listesi_sayfa_numaralari = []
        self.cizelgeler_listesi_sayfa_numaralari = []
        self.giris_sayfa_numaralari = []
        self.tez_baslangic_sayfasi = None
        self.baslik_sayfasi = []

    def getParameters(self):

        if len(self.ui.txt_giris_sayfalari.text()) > 0:
            for i in self.ui.txt_giris_sayfalari.text().split(","):
                print(i)
                self.giris_sayfa_numaralari.append(int(i))

        if len(self.ui.txt_baslik_sayfasi.text()) > 0:
            self.baslik_sayfasi = int(self.ui.txt_baslik_sayfasi.text())

        if len(self.ui.txt_cizelge_sayfalari.text()) > 0:
            for i in self.ui.txt_cizelge_sayfalari.text().split(","):
                self.cizelgeler_listesi_sayfa_numaralari.append(int(i))

        if len(self.ui.txt_icindekiler_sayfasi.text()) > 0:
            for i in self.ui.txt_icindekiler_sayfasi.text().split(","):
                self.icindekiler_listesi_sayfa_numaralari.append(int(i))

        if len(self.ui.txt_baslangic_sayfasi.text()) > 0:
            self.tez_baslangic_sayfasi = int(self.ui.txt_baslangic_sayfasi.text())

        if len(self.ui.txt_sekiller_sayfalari.text()) > 0:
            for i in self.ui.txt_sekiller_sayfalari.text().split(","):
                self.sekiller_listesi_sayfa_numaralari.append(int(i))

        self.analiz_baslat()

    def test(self):
        pass
        # self.ui.txt_giris_sayfalari.setText("12,13,14")
        # self.ui.txt_baslik_sayfasi.setText("1")
        # self.ui.txt_cizelge_sayfalari.setText("9,10")
        # self.ui.txt_sekiller_sayfalari.setText("11")
        # self.ui.txt_baslangic_sayfasi.setText("12")
        # self.ui.txt_icindekiler_sayfasi.setText("7,8")

    def dosya_sec(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.pdf)")
        self.tez_yolu = fname[0]
        self.ui.txt_dosya_yolu.setText(self.tez_yolu)
        self.control()

    def control(self):
        if len(self.ui.txt_dosya_yolu.text()) < 5:
            self.ui.btn_kontrol.setEnabled(False)
        else:
            self.ui.btn_kontrol.setEnabled(True)

    def analiz_baslat(self):
        from HataKontrol import HataKontrolleri
        from TezAnalizi import PdfIslemleri
        pdf_islemleri = PdfIslemleri(
            self.baslik_sayfasi,
            self.tez_yolu,
            self.icindekiler_listesi_sayfa_numaralari,
            self.sekiller_listesi_sayfa_numaralari,
            self.cizelgeler_listesi_sayfa_numaralari,
            self.giris_sayfa_numaralari,
            self.tez_baslangic_sayfasi
        )
        tez = pdf_islemleri.Tez_Nesnesi_Olustur()
        hata_kontrol_nesnesi = HataKontrolleri(tez, self.tez_yolu)
        self.result, self.message = hata_kontrol_nesnesi.Kontrol_Baslat
        print(self.result)
        print(type(self.result))
        self.message2 = pdf_islemleri.messageBox
        self.addItemToListWidget()

    def addItemToListWidget(self):
        self.ui.listWidget.addItems(self.message2)
        self.ui.listWidget.addItem("")
        self.ui.listWidget.addItems(self.message)
        # self.ui.listWidget.addItems(self.result)
        print(self.result)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = MainWindowApp()
    loginWindow.show()
    sys.exit(app.exec_())
