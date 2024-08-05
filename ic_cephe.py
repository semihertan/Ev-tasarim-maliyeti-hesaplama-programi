luks = 5
guzel = 3
idare_eder = 1.5

def metrekare_hesapla():
    global metrekare
    en = int(input("İÇ CEPHE İÇİN EVİN ENİNİ METRE CİNSİNDEN GİRİN: "))
    boy = int(input("İÇ CEPHE İÇİN EVİN BOYUNU METRE CİNSİNDEN GİRİN: "))
    metrekare = en * boy

def düzenleme_katsayisi():
    global kisas
    düzen = input("İÇ CEPHE DÜZENİ İÇİN BİR KISAS GİRİN (LÜKS, GÜZEL, İDARE EDER): ")
    if düzen.lower() == "lüks":
        kisas = luks
    elif düzen.lower() == "güzel":
        kisas = guzel
    elif düzen.lower() == "idare eder":
        kisas = idare_eder

def ic_cephe_fiyat():
    global ic_son
    ic_son = metrekare * kisas * 1000
    return ic_son


