# ==============================================================================
# MODÜL 4: KURAL TABANLI AKILLI SALDIRGAN OTOMASYONU
# Dosya Adı: attacker.py
# ==============================================================================

import time
from app_guclu import KurumsalGucluSistem
from app_zayif import ZayifSistem

def akilli_brute_force(hedef_kullanici, gecikme=0.0):
    sistem = KurumsalGucluSistem()
    wordlist_yolu = "wordlist.txt"
    sahte_ip = "10.0.0.45"
    deneme_sayisi = 0
    baslangic = time.time()

    print(f"\n[🔥] AKILLI VE KURALLI BRUTE-FORCE SALDIRISI BAŞLADI [🔥]")
    print(f"[*] Hedef: {hedef_kullanici} | Kaynak IP: {sahte_ip}")
    print(f"[*] Yapilandirilan Gecikme Suresi: {gecikme}sn")
    print("-" * 75)

    try:
        with open(wordlist_yolu, "r") as dosya:
            for satir in dosya:
                temel_kelime = satir.strip()

                # --- AKILLI MUTASYON MOTORU (Rule-Based Mutation) ---
                varyasyonlar = [
                    temel_kelime,                                # düz hali (atakan)
                    temel_kelime.capitalize() + "1!",            # Atakan1!
                    temel_kelime.capitalize() + ".Siber.01!",     # Atakan.Siber.01! (Gerçek şifre)
                    temel_kelime + "2026?"                       # atakan2026?
                ]

                for mutasyonlu_sifre in varyasyonlar:
                    deneme_sayisi += 1

                    if gecikme > 0:
                        time.sleep(gecikme)

                    # İsteği kurumsal sisteme gönderiyoruz
                    yanit = sistem.giris_yap(hedef_kullanici, mutasyonlu_sifre, sahte_ip)
                    print(f"[Istek #{deneme_sayisi}] Şifre: '{mutasyonlu_sifre}' -> Yanıt: {yanit}")

                    if "SUCCESS" in yanit:
                        print("-" * 75)
                        print(f"[+] ŞİFRE BAŞARIYLA KIRILDI: {mutasyonlu_sifre}")
                        print(f"[+] Toplam İstek Sayısı: {deneme_sayisi} | Süre: {time.time() - baslangic:.4f}sn")
                        return

                    if "CRITICAL_BLOCK" in yanit or "SECURITY_ALERT" in yanit:
                        print("-" * 75)
                        print("[-] SALDIRI SEYRİ: Saldırgan IP adresi sistem tarafından tamamen BANLANDI.")
                        print(f"[-] Dogru sifreye ulasilamadan sistem saldiriyi kesti. Toplam Istek: {deneme_sayisi}")
                        return

    except FileNotFoundError:
        print("[-] Error: wordlist.txt bulunamadı!")


def zayif_sistem_testi(hedef_kullanici):
    """Laboratuvardaki ilk karşılaştırma (Deney 1) için zayıf sistemi test eden fonksiyon"""
    sistem = ZayifSistem()
    print(f"\n[!] SAVUNMASIZ SİSTEME SALDIRI BAŞLATILDI [!]")
    print(f"[*] Hedef Kullanıcı: {hedef_kullanici}")
    print("-" * 75)

    # Doğrudan deneme simülasyonu
    yanit_1 = sistem.giris_yap(hedef_kullanici, "yanlis_sifre")
    print(f"[Deneme #1] Şifre: 'yanlis_sifre' -> Yanıt: {yanit_1}")

    yanit_2 = sistem.giris_yap(hedef_kullanici, "Atakan.Siber.01!")
    print(f"[Deneme #2] Şifre: 'Atakan.Siber.01!' -> Yanıt: {yanit_2}")
    print(f"[+] BAŞARILI! Şifre 2. denemede KIRILDI.")


if __name__ == "__main__":
    # ===========================================================================
    # HANGİ DENEYİ ÇALIŞTIRMAK İSTİYORSANIZ O SATIRIN BAŞINDAKİ # İŞARETİNİ KALDIRIN
    # ===========================================================================

    # [DENEY 1] - Savunmasız Durum Testi
    # zayif_sistem_testi(hedef_kullanici="atan")

    # [DENEY 2] - Agresif Hızlı Saldırı (Rate Limit ve IP Ban'a takılan senaryo)
    #akilli_brute_force(hedef_kullanici="atan", gecikme=0.0)

    # [DENEY 3] - Sinsi Yavaş Saldırı (Rate Limit'i aşan ama şifreyi çözen senaryo)
     akilli_brute_force(hedef_kullanici="atan", gecikme=0.5)