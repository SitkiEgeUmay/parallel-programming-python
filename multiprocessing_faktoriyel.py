from multiprocessing import Process
import os
import math

def agir_hesaplama(sayi):
    print(f">> Process ID: {os.getpid()} | Hedef: {sayi}")

    # Faktöriyel hesapla (CPU-bound iş)
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i

    # Basamak sayısını güvenli şekilde hesapla
    basamak = math.floor(math.log10(sonuc)) + 1

    print(f"<< {sayi}! hesaplandı ({basamak} basamak)")

if __name__ == "__main__":
    sayilar = [30000, 40000, 50000]
    processes = []

    for s in sayilar:
        p = Process(target=agir_hesaplama, args=(s,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
