import tkinter as tk
import random
from tkinter import messagebox

def get_sorular():
    sorular = [
        {
            "soru": "Bir bilgisayarın ana belleğine ne denir?",
            "cevap": "ram",
            "ipucu": "Bilgisayarın geçici hafızası olarak da bilinir. Veriler burada işlenir."
        },
        {
            "soru": "Bir bilgisayara zarar vermek amacıyla yazılan kötücül kodlara ne ad verilir?",
            "cevap": "virüs",
            "ipucu": "Bilgisayar sistemlerine kendini kopyalayarak yayılan ve zarar veren yazılım türü."
        },
        {
            "soru": "Bir bilgisayar ağında iki cihazın doğrudan bağlanması için kullanılan kablo türü nedir?",
            "cevap": "ethernet",
            "ipucu": "Birbirine bağlanan cihazların doğrudan veri alışverişi yapmasını sağlayan kablo türü."
        },
        {
            "soru": "Bir bilgisayarın işletim sistemi veya yazılımının açıklarını ve güvenlik zaafiyetlerini tespit etmek için kullanılan saldırı türü nedir?",
            "cevap": "sızma testi",
            "ipucu": "Bir bilgisayar sistemini hedef alarak güvenlik açıklarını tespit etme ve giderme süreci."
        },
        {
            "soru": "Bir bilgisayar ağında diğer cihazları otomatik olarak taramak ve bulmak için kullanılan protokol hangisidir?",
            "cevap": "arp",
            "ipucu": "Bir ağdaki cihazların fiziksel adreslerini IP adreslerine çeviren protokol."
        },
        {
            "soru": "Bir bilgisayarın işlemci hızını artırmak için kullanılan veri depolama birimi nedir?",
            "cevap": "cache",
            "ipucu": "Bilgisayarın geçici verileri hızlı bir şekilde erişmek için kullandığı birim."
        },
        {
            "soru": "Bir bilgisayar ağında veri iletimi ve yönlendirmeyi sağlayan protokol hangisidir?",
            "cevap": "tcp/ip",
            "ipucu": "Bir ağdaki cihazların birbirleriyle veri alışverişi yapabilmelerini sağlayan protokol."
        },
        {
            "soru": "Bir bilgisayar ağında diğer cihazlara ağ bağlantısı sağlayan cihaz nedir?",
            "cevap": "gateway",
            "ipucu": "Bir ağdaki cihazlara dış dünya ile iletişim kurma imkanı sağlayan cihaz."
        },
        {
            "soru": "Bir bilgisayar ağında tüm cihazların merkezi olarak yönetilmesini sağlayan yazılım protokolü hangisidir?",
            "cevap": "snmp",
            "ipucu": "Ağdaki tüm cihazların bir büyücü gibi izlenip yönetildiği bir yazılım protokolü. Cihazların durumu, performansı ve hataları buradan takip edilir."
        },
        {
            "soru": "Bir bilgisayarın ana kartı üzerinde bulunan ve diğer bileşenleri birleştiren bileşen nedir?",
            "cevap": "ana kart",
            "ipucu": "Bir bilgisayarın tüm bileşenlerini bir arada tutan ve veri iletişimini sağlayan bileşen."
        }
    ]
    return sorular

def soru_sor():
    global suanki_soru, dogru_cevap_gosterildi
    if len(sorulan_soru_indeksleri) == len(sorular):
        entry.delete(0, tk.END)
        entry.config(state=tk.DISABLED)
        cevapla_button.config(state=tk.DISABLED)
        pas_gec_button.config(state=tk.DISABLED)
        ipucu_button.config(state=tk.DISABLED)
        ipucu_etiketi.config(text="")
        istatistikleri_goster()
    else:
        while True:
            soru_indeks = random.randint(0, len(sorular) - 1)
            if soru_indeks not in sorulan_soru_indeksleri:
                break

        suanki_soru = sorular[soru_indeks]
        sorulan_soru_indeksleri.add(soru_indeks)
        soru_etiketi.config(text=suanki_soru["soru"], fg="black")
        entry.delete(0, tk.END)
        entry.config(state=tk.NORMAL)
        cevapla_button.config(state=tk.NORMAL)
        pas_gec_button.config(state=tk.NORMAL)
        dogru_cevap_gosterildi = False
        ipucu_etiketi.config(text="", fg="blue")

def cevabi_kontrol_et():
    global dogru_cevap_gosterildi, dogru_cevaplar, yanlis_cevaplar
    kullanici_cevap = entry.get().strip().lower()
    if kullanici_cevap == suanki_soru["cevap"]:
        if not dogru_cevap_gosterildi:
            soru_etiketi.config(text="Doğru cevap!", fg="green")
            dogru_cevap_gosterildi = True
            dogru_cevaplar += 1
            app.after(1500, soru_sor)
    else:
        soru_etiketi.config(text="Yanlış cevap. Doğru cevap: " + suanki_soru["cevap"], fg="red")
        dogru_cevap_gosterildi = False
        yanlis_cevaplar += 1
        app.after(1500, soru_sor)

def soruyu_gec():
    global suanki_soru, bos_cevaplar
    soru_etiketi.config(text="Pas geçilen sorunun cevabı: " + suanki_soru["cevap"], fg="blue")
    bos_cevaplar += 1
    app.after(1500, soru_sor)

def ipucunu_goster():
    if "ipucu" in suanki_soru:
        ipucu_etiketi.config(text="İpucu: " + suanki_soru["ipucu"], fg="blue")

def istatistikleri_goster():
    istatistik = f"Doğru Cevaplar: {dogru_cevaplar} | Yanlış Cevaplar: {yanlis_cevaplar} | Boş Sorular: {bos_cevaplar}"
    messagebox.showinfo("İstatistikler", istatistik)

app = tk.Tk()
app.title("Bilgi Yarışması")
app.geometry("500x250")

sorular = get_sorular()
sorulan_soru_indeksleri = set()
suanki_soru = None
dogru_cevap_gosterildi = False
dogru_cevaplar = 0
yanlis_cevaplar = 0
bos_cevaplar = 0

soru_etiketi = tk.Label(app, text="Soru gelecek buraya", font=("Helvetica", 14), wraplength=450)
soru_etiketi.pack(pady=10)

ipucu_etiketi = tk.Label(app, text="", font=("Helvetica", 12), fg="blue", wraplength=450)
ipucu_etiketi.pack()

entry = tk.Entry(app, font=("Helvetica", 14))
entry.pack(pady=10)

cevapla_button = tk.Button(app, text="Cevapla", command=cevabi_kontrol_et, font=("Helvetica", 14))
cevapla_button.pack(side=tk.LEFT, padx=10)

pas_gec_button = tk.Button(app, text="Pas", command=soruyu_gec, font=("Helvetica", 14))
pas_gec_button.pack(side=tk.LEFT)

ipucu_button = tk.Button(app, text="İpucu", command=ipucunu_goster, font=("Helvetica", 14))
ipucu_button.pack(side=tk.LEFT)

soru_sor()

app.mainloop()
