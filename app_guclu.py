# ==============================================================================
# MODÜL 3: KURUMSAL GÜÇLÜ SİSTEM MİMARİSİ
# ==============================================================================

import time
import re
from collections import defaultdict
from veri_tabani import KULLANICI_VERILERI

class KurumsalGucluSistem:
    def __init__(self):
        # Ortak veri tabanına bağlanıyoruz
        self.veri_tabani = KULLANICI_VERILERI

        # IP Tabanlı Kara Liste Hafızası -> IP: [Hatalı Deneme Sayısı, Ban Başlangıç Zamanı]
        self.ip_havuzu = defaultdict(lambda: [0, 0])
        self.son_istek_zamani = {}

        # Güvenlik Politikası Eşikleri
        self.MAX_IP_HATA = 5
        self.BAN_SURESI = 20  # Saniye cinsinden ceza süresi
        self.MIN_ISTEK_ARALIGI = 0.4  # İki istek arası minimum bekleme (sn)

    def sifre_karmaşiklik_kontrolu(self, sifre):
        """Şifrenin kurumsal standartlara (Regex) uyup uymadığını denetler"""
        if len(sifre) < 8:
            return False
        if not re.search("[a-z]", sifre):
            return False
        if not re.search("[A-Z]", sifre):
            return False
        if not re.search("[0-9]", sifre):
            return False
        if not re.search("[_@\\.!\\?]|\\!|\\.", sifre):
            return False
        return True

    def giris_yap(self, kullanici_adi, sifre, ip_adresi):
        su_anki_zaman = time.time()

        #  KATMAN 1: IP TABANLI KARA LİSTE KONTROLÜ
        hatali_sayisi, ban_zamani = self.ip_havuzu[ip_adresi]
        if hatali_sayisi >= self.MAX_IP_HATA:
            if su_anki_zaman - ban_zamani < self.BAN_SURESI:
                kalan = self.BAN_SURESI - (su_anki_zaman - ban_zamani)
                return f"CRITICAL_BLOCK: IP Adresiniz ({ip_adresi}) Askıya Alındı! Kalan Süre: {kalan:.1f}sn"
            else:
                # Ban süresi dolmuşsa IP'yi sıfırla
                self.ip_havuzu[ip_adresi] = [0, 0]

        #  KATMAN 2: AGRESİF HIZ SINIRLAMASI (Rate Limiting)
        if ip_adresi in self.son_istek_zamani:
            if su_anki_zaman - self.son_istek_zamani[ip_adresi] < self.MIN_ISTEK_ARALIGI:
                self.son_istek_zamani[ip_adresi] = su_anki_zaman
                return "HATA: 429 Too Many Requests! (Hız Sınırı Aşıldı)"
        self.son_istek_zamani[ip_adresi] = su_anki_zaman

        #  KATMAN 3: KİMLİK DOĞRULAMA (Kullanıcı Adı & Şifre Eşleşmesi)
        if kullanici_adi in self.veri_tabani and self.veri_tabani[kullanici_adi] == sifre:
            self.ip_havuzu[ip_adresi] = [0, 0]  # Başarılı girişte ceza puanını sıfırla
            return "SUCCESS: Kurumsal Sisteme Giriş Başarılı!"
        else:
            # Hatalı girişte doğrudan istek atan IP'ye ceza puanı yazılır
            self.ip_havuzu[ip_adresi][0] += 1
            mevcut_hata = self.ip_havuzu[ip_adresi][0]

            if mevcut_hata >= self.MAX_IP_HATA:
                self.ip_havuzu[ip_adresi][1] = su_anki_zaman
                return f"SECURITY_ALERT: Üst üste {mevcut_hata} hatalı istek! IP ({ip_adresi}) TAMAMEN BLOKLANDI!"

            return f"FAIL: Hatalı Kimlik Bilgileri! (IP Hata Skoru: {mevcut_hata}/{self.MAX_IP_HATA})"