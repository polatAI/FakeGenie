import customtkinter as ctk
from main import Main  # Dışarıdan gelen sınıf
import tkinter.messagebox as mb

# Tema ayarları
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Uygulama(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Veri Oluşturucu")
        self.state("zoomed")

        self.main = Main()

        self.fonksiyonlar = {
            "fake_user": ["min_yas", "max_yas", "veri_sayisi"],
            "fake_urun": ["veri_sayisi"],
            "fake_makale": ["veri_sayisi"],
            "fake_filim": ["veri_sayisi"],
            "fake_sosyal_media": ["veri_sayisi"],
            "fake_sirket": ["veri_sayisi"],
            "fake_odeme": ["veri_sayisi"],
            "fake_egitim": ["veri_sayisi"],
            "fake_seyahat": ["veri_sayisi"],
            "fake_sagilik": ["veri_sayisi", "min_yas", "max_yas"],
            "fake_podcast": ["veri_sayisi"],
            "fake_hava_durumu": ["veri_sayisi"],
            "fake_etkilesim": ["veri_sayisi"],
            "fake_eticaret": ["veri_sayisi"],
            "fake_yorum": ["veri_sayisi"]
        }

        self.create_widgets()

    def create_widgets(self):
        # Tema seçimi
        self.theme_option = ctk.CTkOptionMenu(self, values=["Dark", "Light"], command=self.change_theme)
        self.theme_option.pack(pady=10)

        # Veri oluşturma alanı
        self.data_frame = ctk.CTkFrame(self)
        self.data_frame.pack(side="left", padx=20, pady=20, fill="y")

        ctk.CTkLabel(self.data_frame, text="Veri Türü Seç").pack(pady=5)
        self.veri_turu_combo = ctk.CTkComboBox(self.data_frame, values=list(self.fonksiyonlar.keys()), command=self.update_params)
        self.veri_turu_combo.pack(pady=5)

        self.param_entries = {}
        self.param_frame = ctk.CTkFrame(self.data_frame)
        self.param_frame.pack(pady=10)

        self.create_btn = ctk.CTkButton(self.data_frame, text="Veri Oluştur", command=self.veri_olustur)
        self.create_btn.pack(pady=10)

        # Listbox (veri gösterim)
        self.listbox = ctk.CTkTextbox(self, width=800, height=500)
        self.listbox.pack(side="top", pady=20)

    def change_theme(self, mode):
        ctk.set_appearance_mode(mode)

    def update_params(self, secilen):
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        self.param_entries.clear()

        if secilen in self.fonksiyonlar:
            for param in self.fonksiyonlar[secilen]:
                ctk.CTkLabel(self.param_frame, text=param).pack(pady=2)
                entry = ctk.CTkEntry(self.param_frame)
                entry.pack(pady=2)
                self.param_entries[param] = entry

    def veri_olustur(self):
        self.listbox.delete("1.0", "end")  # Listbox'u temizler

        secilen = self.veri_turu_combo.get()
        if not secilen:
            mb.showwarning("Uyarı", "Lütfen bir veri türü seçin.")
            return

        try:
            args = []
            for param in self.fonksiyonlar[secilen]:
                val = self.param_entries[param].get()
                args.append(int(val))

            func = getattr(self.main, secilen)

            veriler = func(*args)  # Return edilen verileri al

            self.listbox.insert("end", f"{secilen} verisi oluşturuldu. Toplam: {len(veriler)} kayıt.\n")
            for veri in veriler:
                for anahtar, deger in veri.items():
                    self.listbox.insert("end", f"{anahtar}: {deger}\n")
                self.listbox.insert("end", "-" * 40 + "\n")  # Ayraç çizgisi

        except Exception as e:
            mb.showerror("Hata", str(e))

if __name__ == "__main__":
    app = Uygulama()
    app.mainloop()
