from veritabani_olustur import DatabaseOlustur
from veri_olustur import SahteVeriOlustur

class Main:
    
    def __init__(self):
        self.db = DatabaseOlustur()
        self.db.create_tables()
        self.fk = SahteVeriOlustur()       
    def fake_user(self,min_yas,max_yas,veri_sayisi):
        
        veriler_user, basliklar_user = self.fk.SahteKullaniciVerisi(min_yas, max_yas, veri_sayisi)
        baslik_listesi_user = list(basliklar_user)
        self.db.insert_user_data(veriler_user, baslik_listesi_user)
        return veriler_user
        
    
    def fake_urun(self, veri_sayisi):
        
        veriler_urun, basliklar_urun = self.fk.SahteUrunVerisi(veri_sayisi)
        baslik_listesi_urun = list(basliklar_urun)
        self.db.insert_product_data(veriler_urun, baslik_listesi_urun)
        return veriler_urun
    
    def fake_makale(self, veri_sayisi):
        veriler_makale, basliklar_makale = self.fk.RandomMakaleVerisi(veri_sayisi)
        baslik_listesi_makale = list(basliklar_makale)
        self.db.insert_makale_data(veriler_makale, baslik_listesi_makale)
        return veriler_makale

    def fake_filim(self,veri_sayisi):
        
        veriler_filim, basliklar_filim = self.fk.SahteFilimVeritabani(veri_sayisi)
        basliklar_listesi_filim = list(basliklar_filim)
        self.db.insert_filmler_data(veriler_filim, basliklar_listesi_filim)
        return veriler_filim
        
    def fake_sosyal_media(self,veri_sayisi):
        veriler_sosyal_media, basliklar_sosyalmedia = self.fk.SahteSosyalMediaHesaplari(veri_sayisi)
        basliklar_listesi_sosyalmedia = list(basliklar_sosyalmedia)
        self.db.insert_sosyal_medya_data(veriler_sosyal_media, basliklar_listesi_sosyalmedia)
        return veriler_sosyal_media
        
    def fake_sirket(self,veri_sayisi):
        veriler_sirket, basliklar_sirket = self.fk.SahteSirketVerileri(veri_sayisi)
        basliklar_listesi_sirket = list(basliklar_sirket)
        self.db.insert_sirketler_data(veriler_sirket, basliklar_listesi_sirket)
        return veriler_sirket
    
    def fake_odeme(self,veri_sayisi):
        veriler_odeme, basliklar_odeme = self.fk.SahteOdemeBilgileri(veri_sayisi)
        basliklar_listesi_odeme = list(basliklar_odeme)
        self.db.insert_odemeler_data(veriler_odeme, basliklar_listesi_odeme)
        return veriler_odeme
        
    
    def fake_egitim(self,veri_sayisi):
        veriler_egitim, basliklar_egitim = self.fk.SahteEgitimBilgileri(veri_sayisi)
        baslikar_listesi_egitim = list(basliklar_egitim)
        self.db.insert_egitim_data(veriler_egitim, baslikar_listesi_egitim)
        return veriler_egitim
        
    
    def fake_seyahat(self,veri_sayisi):
        veriler_seyahat, basliklar_seyahat = self.fk.SahteSeyahatVerileri(veri_sayisi)
        basliklar_listesi_seyahat = list(basliklar_seyahat)
        self.db.insert_seyahat_data(veriler_seyahat, basliklar_listesi_seyahat)
        return veriler_seyahat
    
    def fake_sagilik(self,veri_sayisi, min_yas, max_yas):
        veriler_sagilik, basliklar_saglik = self.fk.SahteSaglikVerileri(veri_sayisi,min_yas, max_yas)
        basliklar_listesi_saglik = list(basliklar_saglik)
        self.db.insert_saglik_data(veriler_sagilik, basliklar_listesi_saglik)
        return veriler_sagilik
        
    def fake_podcast(self, veri_sayisi):
        veriler_podcast, basliklar_podcast = self.fk.SahtePodcastVerileri(veri_sayisi)
        basliklar_listesi_podcast = list(basliklar_podcast)
        self.db.insert_podcast_data(veriler_podcast, basliklar_listesi_podcast)
        return veriler_podcast
    def fake_hava_durumu(self,veri_sayisi):
        veriler_havadurumu, basliklar_havadurumu = self.fk.SahteHavaDurumuVerisi(veri_sayisi)
        basliklar_listesi_havadurumu = list(basliklar_havadurumu)
        self.db.insert_hava_durumu_data(veriler_havadurumu, basliklar_listesi_havadurumu)
        return veriler_havadurumu
        
    def fake_etkilesim(self,veri_sayisi):
        veriler_etkilesim, basliklar_etkilesim = self.fk.SahteEtkilesimVerileri(veri_sayisi)
        basliklar_listesi_etkilesim = list(veriler_etkilesim)
        self.db.insert_etkilesim_data(veriler_etkilesim, basliklar_listesi_etkilesim)
        return veriler_etkilesim
        
    
    def fake_eticaret(self,veri_sayisi):
        veriler_eticaret , basliklar_eticaret = self.fk.SahteEticaretVerileri(veri_sayisi)
        basliklar_listesi_eticaret = list(basliklar_eticaret)
        self.db.insert_eticaret_data(veriler_eticaret, basliklar_listesi_eticaret)
        return veriler_eticaret
    def fake_yorum(self,veri_sayisi):
        veriler_yorum, basliklar_yorum = self.fk.SahteYorum(veri_sayisi)
        basliklar_listesi_yorum = list(basliklar_yorum)
        self.db.insert_yorumlar_data(veriler_yorum, basliklar_listesi_yorum)
        return veriler_yorum
    
    
    def save_to_json():
        pass
    