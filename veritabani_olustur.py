import sqlite3

class DatabaseOlustur:
    
    def __init__(self, db_name="sahte_veri.db"):
        self.db_name = db_name

    def create_connection(self):
        """Veritabanı bağlantısı oluşturur."""
        connection = sqlite3.connect(self.db_name)
        return connection

    def create_tables(self):
        connection = self.create_connection()
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT,
            soyisim TEXT,
            adres TEXT,
            mail TEXT,
            telefon_no TEXT,
            yas INTEGER,
            ulke TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT,
            kategori TEXT,
            fiyat REAL,
            aciklama TEXT,
            stok BOOLEAN)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS makale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            author TEXT,
            date TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS filmler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baslik TEXT,
            yonetmen TEXT,
            aktor_1 TEXT,
            aktor_2 TEXT,
            aktor_3 TEXT,
            yayin_yili INTEGER,
            tur TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS sosyal_medya (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT,
            profil_resmi TEXT,
            biografi TEXT,
            takipci INTEGER,
            takip_ettikleri INTEGER,
            gonderi_sayisi INTEGER)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS sirketler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sirket_adi TEXT,
            adres TEXT,
            endustri TEXT,
            telefon_no TEXT,
        email TEXT,
        website TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS odemeler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kart_numarasi TEXT,
            son_kullanma_tarihi TEXT,
            cvv TEXT,
            iban TEXT,
            islem_miktari REAL)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS egitim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT,
            okul TEXT,
            derece TEXT,
            mezuniyet_yili INTEGER,
            kurs_1 TEXT,
            kurs_2 TEXT,
            kurs_3 TEXT,
            kurs_4 TEXT,
            kurs_5 TEXT,
            grade_math TEXT,
            grade_english TEXT,
            grade_history TEXT,
            grade_science TEXT,
            grade_art TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS seyahat (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           varis_noktasi TEXT,
           gidis_tarihi TEXT,
           donus_tarihi TEXT,
           ucus_numarasi TEXT,
           otel TEXT,
           oda_tipi TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS saglik (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           hasta_adi TEXT,
           yasi INTEGER,
           cinsiyeti TEXT,
           tibbi_gecmisi TEXT,
           doktor_adi TEXT,
           recete_1 TEXT,
           recete_2 TEXT,
           recete_3 TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS hava_durumu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sehir TEXT,
            tarih TEXT,
            sicaklik REAL,
            nem INTEGER,
            ruzgar REAL,
            durum TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS podcast (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baslik TEXT,
            konuk TEXT,
            kategori TEXT,
            yayim_tarihi TEXT,
            link TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS yorumlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            yorumcu TEXT,
            yorum TEXT,
            puan INTEGER,
            tarih TEXT,
            urun_adi TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS etkilesim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT,
            gonderi TEXT,
            begeniler INTEGER,
            yorumlar INTEGER,
            paylasim_sayisi INTEGER,
            tarih TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS eticaret (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            siparis_no TEXT,
            urun_adi TEXT,
            kategori TEXT,
            fiyat REAL,
            adedi INTEGER,
            siparis_tarihi TEXT,
            teslimat_adresi TEXT,
            odeme_yontemi TEXT,
            durum TEXT)''')

        connection.commit()
        #connection.close()

            # Diğer tabloları benzer şekilde oluşturabilirsiniz

        connection.commit()
        print("Veritabanı ve tablolar oluşturuldu.")
        
    def convert_dict_list_to_tuple(self,data_list, keys):
        """
        Sözlüklerden oluşan listeyi, verilen key sırasına göre tuple listesine çevirir.
        """
        return [tuple(item.get(key) for key in keys) for item in data_list]
    
        
    def insert_user_data(self, user_data, keys):
        """Kullanıcı verilerini kullanıcılar tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        # Convert the user_data list using the keys provided
        data_to_insert = self.convert_dict_list_to_tuple(user_data, keys)
    
        cursor.executemany('''INSERT INTO users (isim, soyisim, adres, mail, telefon_no, yas, ulke) 
                               VALUES (?,?,?,?,?,?,?)''', data_to_insert)
    
        connection.commit()
        connection.close()
        print(f"{len(user_data)} kullanıcı verisi veritabanına eklendi.")

        
    def insert_product_data(self, product_data, keys):
        """Ürün verilerini ürünler tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()

        product_to_insert = self.convert_dict_list_to_tuple(product_data, keys)


        cursor.executemany('''INSERT INTO products (isim, kategori, fiyat, aciklama, stok) 
                            VALUES (?,?,?,?,?)''', product_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(product_data)} ürün verisi veritabanına eklendi.")


    def insert_makale_data(self, makale_data, keys):
        """Makale verilerini makale tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()

        makale_to_insert = self.convert_dict_list_to_tuple(makale_data, keys)


        cursor.executemany('''INSERT INTO makale (title, content, author, date) 
                            VALUES (?,?,?,?)''', makale_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(makale_data)} makale verisi veritabanına eklendi.")

    def insert_filmler_data(self, filmler_data, keys):
        """Film verilerini filmler tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        filmler_to_insert = self.convert_dict_list_to_tuple(filmler_data, keys)


        cursor.executemany('''INSERT INTO filmler (baslik, yonetmen, aktor_1, aktor_2, aktor_3, yayin_yili, tur) 
                            VALUES (?,?,?,?,?,?,?)''', filmler_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(filmler_data)} film verisi veritabanına eklendi.")

    def insert_sosyal_medya_data(self, sosyal_medya_data,keys):
        """Sosyal medya verilerini sosyal_medya tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        sosyalmedia_to_insert = self.convert_dict_list_to_tuple(sosyal_medya_data, keys)


        cursor.executemany('''INSERT INTO sosyal_medya (kullanici_adi, profil_resmi, biografi, takipci, takip_ettikleri, gonderi_sayisi) 
                            VALUES (?,?,?,?,?,?)''', sosyalmedia_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(sosyal_medya_data)} sosyal medya verisi veritabanına eklendi.")

    def insert_sirketler_data(self, sirketler_data, keys):
        """Şirket verilerini şirketler tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        sirket_to_insert = self.convert_dict_list_to_tuple(sirketler_data, keys)


        cursor.executemany('''INSERT INTO sirketler (sirket_adi, adres, endustri, telefon_no, email, website) 
                            VALUES (?,?,?,?,?,?)''', sirket_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(sirketler_data)} şirket verisi veritabanına eklendi.")

    def insert_odemeler_data(self, odemeler_data, keys):
        """Ödeme verilerini odemeler tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        odeme_to_insert = self.convert_dict_list_to_tuple(odemeler_data, keys)


        cursor.executemany('''INSERT INTO odemeler (kart_numarasi, son_kullanma_tarihi, cvv, iban, islem_miktari) 
                            VALUES (?,?,?,?,?)''', odeme_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(odemeler_data)} ödeme verisi veritabanına eklendi.")

    def insert_egitim_data(self, egitim_data, keys):
        """Eğitim verilerini egitim tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        egitim_to_insert = self.convert_dict_list_to_tuple(egitim_data, keys)


        cursor.executemany('''INSERT INTO egitim (isim, okul, derece, mezuniyet_yili, kurs_1, kurs_2, kurs_3, kurs_4, kurs_5, 
                                                 grade_math, grade_english, grade_history, grade_science, grade_art) 
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', egitim_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(egitim_data)} eğitim verisi veritabanına eklendi.")

    def insert_seyahat_data(self, seyahat_data, keys):
        """Seyahat verilerini seyahat tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()

        seyahat_to_insert = self.convert_dict_list_to_tuple(seyahat_data, keys)


        cursor.executemany('''INSERT INTO seyahat (varis_noktasi, gidis_tarihi, donus_tarihi, ucus_numarasi, otel, oda_tipi) 
                            VALUES (?,?,?,?,?,?)''', seyahat_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(seyahat_data)} seyahat verisi veritabanına eklendi.")

    def insert_saglik_data(self, saglik_data, keys):
        """Sağlık verilerini saglik tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        saglik_to_insert = self.convert_dict_list_to_tuple(saglik_data, keys)


        cursor.executemany('''INSERT INTO saglik (hasta_adi, yasi, cinsiyeti, tibbi_gecmisi, doktor_adi, recete_1, recete_2, recete_3) 
                            VALUES (?,?,?,?,?,?,?,?)''', saglik_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(saglik_data)} sağlık verisi veritabanına eklendi.")

    def insert_hava_durumu_data(self, hava_durumu_data, keys):
        """Hava durumu verilerini hava_durumu tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        havadurumu_to_insert = self.convert_dict_list_to_tuple(hava_durumu_data, keys)


        cursor.executemany('''INSERT INTO hava_durumu (sehir, tarih, sicaklik, nem, ruzgar, durum) 
                            VALUES (?,?,?,?,?,?)''', havadurumu_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(hava_durumu_data)} hava durumu verisi veritabanına eklendi.")

    def insert_podcast_data(self, podcast_data, keys):
        """Podcast verilerini podcast tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        podcast_to_insert = self.convert_dict_list_to_tuple(podcast_data, keys)


        cursor.executemany('''INSERT INTO podcast (baslik, konuk, kategori, yayim_tarihi, link) 
                            VALUES (?,?,?,?,?)''', podcast_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(podcast_data)} podcast verisi veritabanına eklendi.")

    def insert_yorumlar_data(self, yorumlar_data, keys):
        """Yorumlar verilerini yorumlar tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()

        yorumlar_to_insert = self.convert_dict_list_to_tuple(yorumlar_data, keys)


        cursor.executemany('''INSERT INTO yorumlar (yorumcu, yorum, puan, tarih, urun_adi) 
                            VALUES (?,?,?,?,?)''', yorumlar_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(yorumlar_data)} yorum verisi veritabanına eklendi.")

    def insert_etkilesim_data(self, etkilesim_data, keys):
        """Etkileşim verilerini etkilesim tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        etkilesim_to_insert = self.convert_dict_list_to_tuple(etkilesim_data, keys)


        cursor.executemany('''INSERT INTO etkilesim (kullanici_adi, gonderi, begeniler, yorumlar, paylasim_sayisi, tarih) 
                            VALUES (?,?,?,?,?,?)''', etkilesim_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(etkilesim_data)} etkileşim verisi veritabanına eklendi.")

    def insert_eticaret_data(self, eticaret_data, keys):
        """E-ticaret verilerini eticaret tablosuna ekler."""
        connection = self.create_connection()
        cursor = connection.cursor()
        
        
        eticaret_to_insert = self.convert_dict_list_to_tuple(eticaret_data, keys)


        cursor.executemany('''INSERT INTO eticaret (siparis_no, urun_adi, kategori, fiyat, adedi, siparis_tarihi, teslimat_adresi, odeme_yontemi, durum) 
                            VALUES (?,?,?,?,?,?,?,?,?)''', eticaret_to_insert)

        connection.commit()
        connection.close()
        print(f"{len(eticaret_data)} e-ticaret verisi veritabanına eklendi.")
