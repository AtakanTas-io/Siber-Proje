# ==============================================================================
# MODÜL 2: SAVUNMASIZ SİSTEM MİMARİSİ
# Dosya Adı: app_zayif.py
# ==============================================================================

from veri_tabani import KULLANICI_VERILERI

class ZayifSistem:
    def __init__(self):
        # Ortak veri tabanına bağlanıyoruz
        self.veri_tabani = KULLANICI_VERILERI

    def giris_yap(self, kullanici_adi, sifre, ip_adresi=None):
        """
        Zayıf Giriş Paneli: İstek frekansına veya IP adresine bakmaz.
        """
        if kullanici_adi in self.veri_tabani and self.veri_tabani[kullanici_adi] == sifre:
            return "SUCCESS: Giriş Başarılı!"
        else:
            return "FAIL: Hatalı Şifre!"