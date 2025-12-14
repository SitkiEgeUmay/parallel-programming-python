# parallel-programming-python
Threading, Multiprocessing ve Amdahl Yasası – Python Uygulamaları  
Python ile Kavramsal ve Uygulamalı Anlatım

Bu repository’de Threading, Multiprocessing ve Amdahl Yasası kavramları;  
slaytlardaki teorik anlatımlar temel alınarak günlük hayattan özgün senaryolar  
ve Python uygulamaları ile açıklanmıştır.

## Amaç
- Sadece kod yazmak değil  
- Paralel programlama mantığını **doğru kavradığımı göstermek**

---

## 1️- Threading – Restoran Mutfak Senaryosu

Bu uygulamada restoran mutfağı senaryosu üzerinden threading kavramı
anlatılmaktadır. Salata ve çorba hazırlama işlemleri ayrı görevler olarak
düşünülmüş ve her biri farklı bir thread ile temsil edilmiştir.
Thread’ler aynı bellek alanını paylaşır ve işlemci, bir görev bekleme
durumundayken diğer göreve geçerek zamanı daha verimli kullanır.
Bu yapı, özellikle bekleme süresi olan I/O ağırlıklı işlemlerde
threading kullanımının avantajlarını göstermektedir.

---

## 2️- Multiprocessing – Faktöriyel Hesaplama (CPU-Bound)

Bu uygulamada işlemciyi yoğun şekilde kullanan faktöriyel hesaplaması
multiprocessing yapısı kullanılarak paralel hale getirilmiştir.
Her faktöriyel hesabı ayrı bir process olarak çalıştırılmıştır.
Bu sayede Python’daki GIL kısıtı aşılmış ve birden fazla çekirdeğin
gerçek anlamda paralel çalışması sağlanmıştır.
Bu örnek, CPU-bound işlemler için multiprocessing kullanımının
neden daha uygun olduğunu göstermektedir.

---

## 3️- Thread ve Process Arasındaki Bellek Paylaşımı Farkı

Bu senaryoda thread ve process yapılarının bellek yönetimi karşılaştırılmıştır.
Thread’ler aynı bellek alanını paylaştıkları için global bir veri yapısı
üzerinde yapılan değişiklikler ana programa yansımaktadır.
Process’ler ise birbirinden izole bellek alanlarına sahiptir ve
process içerisinde yapılan değişiklikler ana programı etkilemez.
Bu fark, güvenlik ve veri tutarlılığı açısından önemli bir ayrımdır.

---

## 4- Amdahl Yasası – Sınav Okuma Senaryosu

Bu uygulamada Amdahl Yasası, sınav okuma süreci üzerinden açıklanmıştır.
Cevap anahtarının hazırlanması seri bir işlem olarak ele alınmıştır ve
paralelleştirilemez. Sınav okuma işlemi ise asistanlara bölünerek
paralel hale getirilebilir.
Asistan (çekirdek) sayısı artırılsa bile seri kısım nedeniyle
toplam sürede belirli bir sınırın altına inilememektedir.
Bu durum Amdahl Yasasının temel prensibini açıkça ortaya koymaktadır.

---

## Genel Değerlendirme

- Threading, bekleme süresi olan ve I/O ağırlıklı işlemler için uygundur  
- Multiprocessing, işlemci yoğun (CPU-bound) işlemler için gerçek paralellik sağlar  
- Process yapısı daha güvenli olmakla birlikte daha fazla kaynak tüketir  
- Seri kısımlar, paralel programların hızlanma oranını sınırlar  

Bu çalışma, paralel programlama konularının teorik bilgiyle sınırlı kalmayıp
uygulamalı örnekler ve senaryolar üzerinden anlaşıldığını göstermektedir.
