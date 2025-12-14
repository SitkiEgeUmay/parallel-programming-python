import threading
import time

def salata_hazirla():
    adimlar = ["Marullar yıkanıyor", "Domatesler doğranıyor", "Sos ekleniyor", "Salata Hazır!"]
    for adim in adimlar:
        print(f"[Aşçı 1 - Salata]: {adim}")
        time.sleep(1)

def corba_pisir():
    adimlar = ["Su kaynatılıyor", "Mercimek ekleniyor", "Baharat atılıyor", "Çorba Hazır!"]
    for adim in adimlar:
        print(f"[Aşçı 2 - Çorba]: {adim}")
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=salata_hazirla)
    t2 = threading.Thread(target=corba_pisir)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Tüm siparişler hazır.")
