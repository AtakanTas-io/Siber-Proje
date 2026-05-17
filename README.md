# 🔒 Çok Katmanlı Kimlik Doğrulama Güvenliği ve Akıllı Brute-Force Laboratuvarı

Bu proje, web tabanlı kimlik doğrulama panellerine yönelik gerçekleştirilen gelişmiş **Çevrimiçi Kaba Kuvvet (Online Brute-Force)** saldırılarını ve bu saldırılara karşı geliştirilen kurumsal savunma mimarilerini (Hız Sınırlama & IP Tabanlı Proaktif Ban) simüle eden nesne yönelimli (OOP) bir siber güvenlik laboratuvarıdır.

## 🚀 Proje Mimarisi

Proje, birbiriyle entegre çalışan 4 temel Python modülünden oluşmaktadır:

- **`veri_tabani.py`**: Yüksek entropili, kurumsal şifre politikalarına uygun sahte veri havuzu.
- **`app_zayif.py`**: Herhangi bir güvenlik duvarı veya frekans denetimi barındırmayan savunmasız sistem baseline'ı.
- **`app_guclu.py`**: Bünyesinde Regex şifre kontrolü, milisaniyelik **Rate Limiting** ve proaktif **IP Blacklisting** algoritmaları barındıran kurumsal kalkan.
- **`attacker.py`**: Sözlük listesindeki verileri kurallara göre dinamik olarak mutasyona uğratan (Rule-Based Mutation) ve hedef paneli farklı hız senaryolarıyla tarayan akıllı atak otomasyonu.

## 📊 Laboratuvar Deney Senaryoları

Laboratuvarda 3 farklı kontrollü senaryo test edilmiştir:

1. **Savunmasız Durum (Baseline):** Herhangi bir koruma katmanı olmadığında otomasyon araçlarının milisaniyeler içinde sistemi suistimal edebildiği doğrulanmıştır.
2. **Agresif Saldırı ve Proaktif IP Banı:** Saldırgan gecikmesiz (hızlı) saldırdığında, sistem hız ihlali tespit ettiği için isteği kimlik doğrulama katmanına sokmadan `429 Too Many Requests` ile havada bloklar ve saldırgan IP'sini kara listeye alır. **(Doğru şifre gönderilse dahi sistem geçit vermez).**
3. **Sinsi Saldırı (Low and Slow):** Saldırganın hız sınırının altında kalacak şekilde (0.5sn gecikmeyle) yavaş istekler atarak Rate Limiting katmanını bypass edebildiği ve kümülatif hata sınırına ulaşmadan şifreyi kırabildiği siber güvenlik zafiyeti/sınırlılığı simüle edilmiştir.

## 🛠️ Kurulum ve Çalıştırma

Proje yerel çalışma ortamında (localhost) izole bellekte test edilmiştir. Harici hiçbir canlı sisteme veya ağ trafiğine müdahale edilmemiştir.

```bash
# Projeyi klonlayın
git clone [https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git)

# Proje dizinine girin
cd PROJE_ADINIZ

# Laboratuvarı çalıştırın (attacker.py içindeki deney senaryolarını değiştirerek test edebilirsiniz)
python attacker.py
```
