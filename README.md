
---

**🔮 Sahte Veri Üretici (Fake Data Generator)**

Bu Python uygulaması, sahte veri üretimi için geliştirilmiş kapsamlı ve esnek bir araçtır. Kullanıcı, ürün, şirket, sağlık, eğitim, ödeme, hava durumu, sosyal medya, makale, film, yorum gibi birçok kategoride anlamlı ve rastgele veriler oluşturabilir. Ayrıca bu veriler SQLite veritabanına kaydedilir ve GUI üzerinden görüntülenebilir.

---

**🧠 Özellikler**

- 15+ kategoride sahte veri üretimi  
- Oluşturulan verileri SQLite veritabanına kaydeder  
- Dark/Light mod destekli CustomTkinter GUI  
- Veri listesi canlı olarak arayüzde gösterilir  
- İleriye dönük dışa aktarım (JSON/CSV) altyapısı  
- Kolay kurulum ve kullanım  
- .exe dosyasına dönüştürülmüş taşınabilir yapı  

---

**📸 Ekran Görüntüsü**

(Ekran görüntüsü koymak istersen buraya ekleyebilirsin)

---

**🚀 Kurulum**

1. Projeyi klonla:
   ```bash
   git clone https://github.com/kullaniciadi/sahte-veri-uretici.git
   cd sahte-veri-uretici
   ```

2. Gerekli kütüphaneleri kur:
   ```bash
   pip install -r requirements.txt
   ```
> `requirements.txt` içeriği:
> ```
> customtkinter
> faker
> ```

---

## 🧪 Kullanım

```bash
python gui.py
```

Uygulama açıldıktan sonra:

1. Dark/Light tema seçimi yapabilirsiniz.
2. Açılır menüden veri kategorisini seçin (örneğin: `fake_user`).
3. İstenen parametreleri girin (`min_yas`, `max_yas`, `veri_sayisi` gibi).
4. “Veri Oluştur” butonuna tıklayın.
5. Oluşturulan veriler GUI üzerinde listelenir ve veritabanına kaydedilir.

---

## 🧩 Veri Kategorileri

| Fonksiyon              | Açıklama                             |
|------------------------|--------------------------------------|
| fake_user              | Sahte kullanıcı verisi               |
| fake_urun              | Ürün verisi                          |
| fake_makale            | Makale başlıkları ve içerikleri      |
| fake_filim             | Film isimleri ve türleri             |
| fake_sosyal_media      | Sosyal medya hesapları               |
| fake_sirket            | Şirket isimleri ve bilgileri         |
| fake_odeme             | Ödeme ve kart bilgileri              |
| fake_egitim            | Eğitim geçmişi verisi                |
| fake_seyahat           | Seyahat rotaları                     |
| fake_sagilik           | Sağlık bilgileri                     |
| fake_podcast           | Podcast listesi                      |
| fake_hava_durumu       | Hava durumu tahminleri               |
| fake_etkilesim         | Sosyal etkileşim verileri            |
| fake_eticaret          | E-ticaret siparişleri                |
| fake_yorum             | Yorum/feedback verileri              |

---

## 🗃️ Veritabanı

Tüm veriler SQLite üzerinde `veritabani.db` dosyasına yazılır. Tablo isimleri her kategoriye özel olarak belirlenmiştir (`users`, `products`, `makaleler`, `filmler`, vs.).

---

## 📦 .exe Versiyonu

Uygulama `pyinstaller` kullanılarak `.exe` formatında derlenebilir:

```bash
pyinstaller --noconsole --onefile --add-data="veritabani.db;." gui.py
```

---

## 📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyin.

---

## ✨ Katkı Sağla

- Projeyi çatalla
- Yeni veri kategorileri oluştur
- İyileştirme önerileri aç
- Pull request gönder

---

## 👤 Geliştirici

**Ad Soyad:** (adını buraya yaz)  
**LinkedIn / GitHub / Website:** (varsa link ekle)  

---

## 💬 Teşekkürler

Bu proje, veri bilimi, yazılım testi ve demo uygulamaları için hızlı veri üretimi ihtiyacına yönelik geliştirilmiştir. Açık kaynaklıdır ve herkesin katkısına açıktır.
```