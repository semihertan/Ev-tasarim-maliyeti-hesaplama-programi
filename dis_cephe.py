import math

def bölge():
    global bölge_katsayisi
    bölge_katsayisi = input("EV HANGİ BÖLGEDE? (DENİZ KENARI--1) (ŞEHİR MERKEZİ--2) (KIRSAL--3) : ")

    if bölge_katsayisi == "1":
        bölge_katsayisi = 2
    elif bölge_katsayisi == "2":
        bölge_katsayisi = 1.5
    elif bölge_katsayisi == "3":
        bölge_katsayisi = 0.75

def puanlama():
    global son_puan
    tasarim = input("NASIL BİR DIŞ CEPHE TASARIMI OLSUN? (MODERN, GELENEKSEL, ESKİ): ")
    puan = int(input("DIŞ CEPHE TASARIMI KALİTE SEVİYESİ İÇİN 1 İLE 5 ARASINDA BİR SAYI GİRİN: "))

    if tasarim.lower() == "modern":
        son_puan = puan * puan
    elif tasarim.lower() == "geleneksel":
        son_puan = puan * math.pi
    elif tasarim.lower() == "eski":
        son_puan = puan * math.exp(1)

def dis_cephe_fiyat():
    global dis_son
    dis_son = bölge_katsayisi*son_puan*500
    return dis_son