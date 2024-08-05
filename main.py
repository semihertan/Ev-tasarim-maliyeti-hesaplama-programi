import dis_cephe
import ic_cephe

toplam = 0
sayi = 1

while True:
    dis_cephe.bölge()
    dis_cephe.puanlama()

    ic_cephe.metrekare_hesapla()
    ic_cephe.düzenleme_katsayisi()

    genel_fiyat = dis_cephe.dis_cephe_fiyat() * 40 + ic_cephe.ic_cephe_fiyat() * 60

    print("-------------------------------------------------")
    print("İSTENİLEN EVİN GENEL FİYATI:", genel_fiyat, "TL")
    print("-------------------------------------------------")

    tekrar = str(input("YENİ BİR TANE DAHA HESAPLAMA YAPMAK İSTER MİSİNİZ? : "))
    print("-------------------------------------------------")
    if tekrar.lower() == "h":
        toplam += genel_fiyat
        print("ORTALAMA EV FİYATI:", (toplam / sayi), "TL")
        break
    else:
        toplam += genel_fiyat
        sayi += 1
