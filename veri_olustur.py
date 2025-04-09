from faker import Faker
import json
import random

class SahteVeriOlustur(object):
    
    def __init__(self):
        self.f = None

    def set_country(self, country_code):
        self.f = Faker(country_code)

    def SahteKullaniciVerisi(self, min_yas, max_yas, veri_sayisi, ulke="Türkiye", dosya_adi="user_data.json"):
        self.set_country(self.get_country_code(ulke))

        users_list = []

        # Verilen veri sayısı kadar kullanıcı verisi oluştur
        for _ in range(veri_sayisi):
            user_data = {
                "isim": self.f.first_name(),
                "soyisim": self.f.last_name(),
                "adres": self.f.address().replace("\n", " "),  # Adresteki yeni satırları temizle
                "mail": self.f.email(),
                "telefon_no": self.f.phone_number(),
                "yas": self.f.random_int(min=min_yas, max=max_yas),
                "ulke": ulke  # Ülke bilgisini kullanıcıdan alıyoruz
            }
            
            # Kullanıcıyı listeye ekleyelim
            users_list.append(user_data)
        def key(data):
            anahtarlar = user_data.keys()
            return anahtarlar
        
        # JSON dosyasına kaydetme
        self.control(dosya_adi, users_list)
        return users_list, key(user_data)
    def SahteUrunVerisi(self, veri_sayisi, ulke="Türkiye", dosya_adi="urun_data.json"):
        # Faker'ı doğru dil ve ülke ile başlatıyoruz
        self.set_country(self.get_country_code(ulke))

        categories = ['Electronics', 'Clothing', 'Food', 'Home', 'Toys']

        urun_list = []
        
        for i in range(veri_sayisi):
            urun_data = {
                "isim": self.f.word(),
                "kategori": random.choice(categories),
                "fiyat": round(random.uniform(5, 500), 2),
                "aciklama": self.f.sentence(),
                "stok": random.choice([True, False])
            }

            urun_list.append(urun_data)
        
        # Verileri JSON dosyasına kaydetme
        self.control(dosya_adi, urun_list)    
        def key(data):
            anahtarlar = urun_data.keys()
            return anahtarlar
        
        return urun_list, key(urun_data)
        
            

    def RandomMakaleVerisi(self, veri_sayisi, ulke="Türkiye"):
        # Faker'ı doğru dil ve ülke ile başlatıyoruz
        self.set_country(self.get_country_code(ulke))

        makale_list = []
        
        for i in range(veri_sayisi):
            makale_data = {
                "title": self.f.sentence(),
                "content": self.f.text(),
                "author": self.f.name(),
                "date": self.f.date()
            }
            makale_list.append(makale_data)

        # Her makaleyi HTML formatında kaydetme
        #for i, article in enumerate(makale_list):
        #    with open(f'article_{i + 1}.html', 'w', encoding='utf-8') as f:
        #        f.write(f"<h1>{article['title']}</h1>\n")
        #        f.write(f"<p><em>By {article['author']} on {article['date']}</em></p>\n")
        #        f.write(f"<p>{article['content']}</p>\n")

        #print(f"{veri_sayisi} makale HTML formatında kaydedildi.")
        def key(data):
            anahtarlar = makale_data.keys()
            return anahtarlar
        
        return makale_list, key(makale_data)

    def SahteFilimVeritabani(self, veri_sayisi, ulke = "Türkiye", dosya_adi="movie_data.json"):
        
        
        self.set_country(self.get_country_code(ulke))
        
        genres = ['Action', 'Drama', 'Comedy', 'Horror', 'Thriller']
        
        movie_list = []
        
        for i in range(veri_sayisi):
            
            movie_data = {
                "baslik" : self.f.catch_phrase(),
                "yönetmen" : self.f.name(),
                "aktör" : [self.f.name() for i in range(3)],
                "yayin_yili" : random.randint(2000,2025),
                "tür" : random.choice(genres)
            }
            
            movie_list.append(movie_data)
            
            
        self.control(dosya_adi, movie_list)
        
        def key(data):
            anahtarlar = movie_data.keys()
            return anahtarlar
        
        return movie_list, key(movie_data)
        
    
    def SahteSosyalMediaHesaplari(self, veri_sayisi, ulke="Türkiye", dosya_adi="sosyal_media.json"):
        
        
        self.set_country(self.get_country_code(ulke))
        
        sosyal_media_list = []
        
        for i in range(veri_sayisi):
            
            sosyal_media_data = {
                "kullanici_adi" : self.f.user_name(),
                "profil_resmi" : self.f.image_url(),
                "biografi" : self.f.text(),
                "takipçi" : random.randint(100,100000),
                "takip_ettikleri" : random.randint(100,1000),
                "gönderi_sayisi" : random.randint(1,100)
            }
            
            sosyal_media_list.append(sosyal_media_data)
            
        self.control(dosya_adi, sosyal_media_list)
        
        def key(data):
            anahtarlar = sosyal_media_data.keys()
            return anahtarlar
        
        return sosyal_media_list, key(sosyal_media_data)
        
    
    def SahteSirketVerileri(self, veri_sayisi, ulke="Türkiye", dosya_adi= "sirket_verileri.json"):
        
        self.set_country(self.get_country_code(ulke))
            
        sirket_list = []
        
        for i in range(veri_sayisi):
            
            sirket_data = {
                "şirket_adi" : self.f.company(),
                "adres" : self.f.address(),
                "endüstüri" : self.f.job(),
                "telefon_no" : self.f.phone_number(),
                "email" : self.f.email(),
                "website": self.f.url()                
            }
            
            sirket_list.append(sirket_data)
            
        self.control(dosya_adi, sirket_list)

        def key(data):
            anahtarlar = sirket_data.keys()
            return anahtarlar
        
        return sirket_list, key(sirket_data)
        
    
    def SahteOdemeBilgileri(self, veri_sayisi, ulke="Türkiye", dosya_adi = "odeme_bilgileri.json"):
        
        self.set_country(self.get_country_code(ulke))
        
        odeme_list = []
        
        for i in range(veri_sayisi):
            odeme_data = {
                "kart_numarasi" : self.f.credit_card_number(card_type="mastercard"),
                "son_kullanma_tarihi" : self.f.credit_card_expire(),
                "cvv" : self.f.credit_card_security_code(),
                "iban" : self.f.iban(),
                "islem_miktari" : round(random.randint(10,10000), 2)
            }
            
            odeme_list.append(odeme_data)
            
            
        self.control(dosya_adi, odeme_list)
        
        def key(data):
            anahtarlar = odeme_data.keys()
            return anahtarlar
        
        return odeme_list, key(odeme_data)
        
    
    def SahteEgitimBilgileri(self, veri_sayisi, ulke="Türkiye", dosya_adi="egitim_bilgileri.json"):
        self.set_country(self.get_country_code(ulke))
        
        egitim_list = []
        
        for i in range(veri_sayisi):
            egitim_data = {
                "isim" : self.f.name(),
                "okul" : self.f.company(),
                "derece" : self.f.job(),
                "mezuniyet_yili" : random.randint(2000,2025),
                "kurslar" : [self.f.word() for i in range(5)],
                "grades": {course: random.choice(['A', 'B', 'C', 'D', 'F']) for course in ["Math", "English", "History", "Science", "Art"]},
            }
            egitim_list.append(egitim_data)
            
        self.control(dosya_adi, egitim_list)
        
        def key(data):
            anahtarlar = egitim_data.keys()
            return anahtarlar
        
        return egitim_list, key(egitim_data)
        
    
    def SahteSeyahatVerileri(self, veri_sayisi, ulke="Türkiye", dosya_adi="seyahat_bilgileri.json"):
        self.set_country(self.get_country_code(ulke))
        
        seyahat_list = []
        
        for i in range(veri_sayisi):
            seyahat_data = {
                "variş_noktasi" : self.f.city(),
                "gidis_tarihi" : self.f.date_this_year(),
                "donus_tarihi" : self.f.date_this_year(),
                "ucus_numarasi" : self.f.lexify(text='???###'),
                "otel" : self.f.company(),
                "oda_tipi":random.choice(['Single', 'Double', 'Suite'])
            }

            seyahat_list.append(seyahat_data)
            
        self.control(dosya_adi, seyahat_list)
        def key(data):
            anahtarlar = seyahat_data.keys()
            return anahtarlar
        
        return seyahat_list,  key(seyahat_data)
    
    def SahteSaglikVerileri(self, veri_sayisi, min_yas, max_yas, ulke="Türkiye", dosya_adi="sagilik_verileri.json"):
        self.set_country(self.get_country_code(ulke))
        
        sagilik_list = []
        
        for i in range(veri_sayisi):
            
            sagilik_data = {
                "hasta_adi" :self.f.name(),
                "yasi" : random.randint(min_yas, max_yas),
                "cinsiyeti" : random.choice(["Erkek", "Kadın"]),
                "tıbbi gecmisi" : self.f.text(),
                "doktor_adi" : self.f.name(),
                "recete" : [self.f.word() for i in range(3)]
            }
            
            sagilik_list.append(sagilik_data)
            
        self.control(dosya_adi, sagilik_list)
        
        def key(data):
            anahtarlar = sagilik_data.keys()
            return anahtarlar
        
        return sagilik_list, key(sagilik_data)
    
    def SahteHavaDurumuVerisi(self, veri_sayisi, ulke="Türkiye", dosya_adi="hava_durumu.json"):
        self.set_country(self.get_country_code(ulke))

        hava_durumu_listesi = []
    
        for i in range(veri_sayisi):
            hava_durumu_data = {
                "sehir": self.f.city(),
                "tarih": self.f.date_this_year(),
                "sicaklik": round(random.uniform(-10, 40), 1),  # Sıcaklık -10 ile 40 derece arasında
                "nem": random.randint(10, 90),  # Nem oranı
                "rüzgar": round(random.uniform(0, 20), 1),  # Rüzgar hızı
                "durum": random.choice(["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"])  # Hava durumu
            }
        
            hava_durumu_listesi.append(hava_durumu_data)
    
        self.control(dosya_adi, hava_durumu_listesi)
        
        def key(data):
            anahtarlar = hava_durumu_data.keys()
            return anahtarlar
        
        return hava_durumu_listesi, key(hava_durumu_data)

    
    def SahtePodcastVerileri(self, veri_sayisi, ulke="Türkiye", dosya_adi="podcast_verileri.json"):
        self.set_country(self.get_country_code(ulke))

        podcast_listesi = []

        for i in range(veri_sayisi):
            podcast_data = {
                "baslik": self.f.sentence(),
                "konuk": self.f.name(),
                "kategori": random.choice(["Technology", "Science", "Health", "Comedy", "Culture"]),
                "yayim_tarihi": self.f.date_this_year(),
                "link": self.f.url()
            }

            podcast_listesi.append(podcast_data)

        self.save_to_json(podcast_listesi, dosya_adi)
        
        def key(data):
            anahtarlar = podcast_data.keys()
            return anahtarlar
        
        return podcast_listesi, key(podcast_data)

    def SahteYorum(self, veri_sayisi, ulke="Türkiye", dosya_adi="yorum_verileri.json"):
        self.set_country(self.get_country_code(ulke))

        yorum_listesi = []

        for i in range(veri_sayisi):
            yorum_data = {
                "yorumcu": self.f.name(),
                "yorum": self.f.text(),
                "puan": random.randint(1, 5),  # 1 ile 5 arasında bir puan
                "tarih": self.f.date_this_year(),
                "ürün_adi": self.f.word()
            }

            yorum_listesi.append(yorum_data)

        self.save_to_json(yorum_listesi, dosya_adi)
        
        def key(data):
            anahtarlar = yorum_data.keys()
            return anahtarlar
        
        return yorum_listesi, key(yorum_data)

    def SahteEtkilesimVerileri(self, veri_sayisi, ulke="Türkiye", dosya_adi="etkilesim_verileri.json"):
        self.set_country(self.get_country_code(ulke))

        etkilesim_listesi = []

        for i in range(veri_sayisi):
            etkilesim_data = {
                "kullanici_adi": self.f.user_name(),
                "gonderi": self.f.text(),
                "beğeniler": random.randint(100, 10000),
                "yorumlar": random.randint(10, 500),
                "paylasim_sayisi": random.randint(1, 100),
                "tarih": self.f.date_this_year()
            }

            etkilesim_listesi.append(etkilesim_data)

        self.save_to_json(etkilesim_listesi, dosya_adi)
        def key(data):
            anahtarlar = etkilesim_data.keys()
            return anahtarlar
        
        return etkilesim_listesi, key(etkilesim_data)


    def SahteEticaretVerileri(self, veri_sayisi, ulke="Türkiye", dosya_adi="eticaret_verileri.json"):
        self.set_country(self.get_country_code(ulke))

        eticaret_listesi = []

        for i in range(veri_sayisi):
            eticaret_data = {
                "siparis_no": self.f.bothify(text="??######"),
                "urun_adi": self.f.word(),
                "kategori": random.choice(["Electronics", "Clothing", "Food", "Books", "Toys"]),
                "fiyat": round(random.uniform(10, 500), 2),
                "adedi": random.randint(1, 10),
                "siparis_tarihi": self.f.date_this_year(),
                "teslimat_adresi": self.f.address().replace("\n", " "),
                "odeme_yontemi": random.choice(["Credit Card", "PayPal", "Cash on Delivery"]),
                "durum": random.choice(["Pending", "Shipped", "Delivered", "Returned"])
            }

            eticaret_listesi.append(eticaret_data)

        self.save_to_json(eticaret_listesi, dosya_adi)
        
        def key(data):
            anahtarlar = eticaret_data.keys()
            return anahtarlar
        
        return eticaret_listesi, key(eticaret_data)


    def control(self, dosya_adi, veriler):
        if dosya_adi.endswith(".json"):
            self.save_to_json(veriler, dosya_adi)
        elif dosya_adi.endswith(".db"):
            self.save_to_db(veriler)

            
    def save_to_json(self, data, filename='user_data.json'):
        # JSON dosyasına verileri kaydetme
        with open(filename, 'w', encoding="utf-8") as f:  # encoding kısmını 'utf-8' olarak ayarlıyoruz
            json.dump(data, f, indent=4, ensure_ascii=False)  # ensure_ascii=False Türkçe karakterleri düzgün kaydeder
        print(f"Veriler '{filename}' dosyasına kaydedildi!")

    def get_country_code(self, country_name):
        # Ülke adlarına göre Faker'ın dil ve ülke kodlarını döndüren fonksiyon
        country_map = {
            "Türkiye": "tr_TR",
            "Amerika": "en_US",
            "Almanya": "de_DE",
            "Fransa": "fr_FR",
            "İngiltere": "en_GB",
            "İspanya": "es_ES",
            "İtalya": "it_IT",
            "Kanada": "en_CA",
            "Hindistan": "en_IN"
        }
        # Eğer ülke bulamazsa varsayılan olarak İngiltere verisi oluşturur
        return country_map.get(country_name, "en_US")
