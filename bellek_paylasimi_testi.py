import threading
from multiprocessing import Process

ortak_liste = []

def thread_isi():
    ortak_liste.append("Thread Verisi")
    print("[Thread] Liste:", ortak_liste)

def process_isi():
    ortak_liste.append("Process Verisi")
    print("[Process] Liste:", ortak_liste)

if __name__ == "__main__":
    t = threading.Thread(target=thread_isi)
    t.start()
    t.join()

    print("Ana Program (Thread sonrası):", ortak_liste)

    ortak_liste = []

    p = Process(target=process_isi)
    p.start()
    p.join()

    print("Ana Program (Process sonrası):", ortak_liste)
