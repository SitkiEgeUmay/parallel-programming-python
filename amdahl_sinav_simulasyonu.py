def sinav_okuma_simulasyonu():
    seri_sure = 60
    toplam_is = 600
    cekirdekler = [1, 2, 5, 10, 100, 1000]

    for c in cekirdekler:
        toplam_sure = seri_sure + (toplam_is / c)
        print(f"Çekirdek: {c:<5} | Toplam Süre: {toplam_sure:.2f} dk")

sinav_okuma_simulasyonu()
