# Manga ve Çizgi Roman Çevirici ve Renklendirici

Bu proje, yapay zeka kullanarak farklı dillerdeki mangaları veya çizgi romanları herhangi bir dile çevirir ve renksiz mangaları renklendirir. Proje, çeşitli aşamalardan oluşmaktadır ve farklı işlevleri gerçekleştirmek için çeşitli kütüphaneleri kullanır.
Renkli manga veya çizgi romanları çevirir, renksiz manga veya çizgi romanları çevirir ve istenilirse renklendirebilir.

Kodda yapılacak değişiklik ile farklı diller arası çevri işlemide gereçekleştirilebilinir.

# ÖZELLİKLER


* OCR

Resimlerdeki metinleri çıkarmak için OCR kullanılmaktadır. Bu projede PaddleOCR kütüphanesi tercih ettim. 
Paddleocr kütüphanesi diğer ocr kütüphanelerinden (EasyOCR, Pytesseract) daha hızlı ve daha iyi sonuç verdiği için projede kullanmaya karar verdim.

* Çevri 

Çevri için öncelikle transformırs kütüphanesi ile farklı dil modellerini çevri için kullanmayı planlıyordum. Testlerim sonucunda istediğim başarıda sonuç vermediği için deepl api kullanmaya karar verdim. 
Deepl api kullanmak için  https://www.deepl.com/en/pro-api sayfasından kaydolun ve anahtarınızı alın.
Kodda 13. satırdaki api = "APİ-KEY" kısmına anahtarınızı ekleyin

* İnpanting

Resme çevrilmiş metinleri eklemek için önce resim üzerindeki metinlerin kaldırılması gerekiyor. Bunun için simple-lama-inpainting kütüphanesi ile metinlerin üzerine kareler yerleştirerek yapay zekanın kapalı kısımları doldurması sağlanıyor.

* Renklendirme

siyah beyaz resimleri renklendirmek için https://github.com/qweasdd/manga-colorization-v2 projeden yararladnım. bu projeyi kendi koduma uyarlıyarak renksiz resimleri renklendirdim.
kodda 12. satırdaki renklendir = 1 ise reimleri renklendirir. renklendir = 0 ise resimleri renklendirmez.



# Gereksinimler

Öncelikle, [generator.zip](https://drive.google.com/file/d/1qmxUEKADkEM4iYLp1fpPLLKnfZ6tcF-t/view) dosyasını indirip "networks" klasörünün içine koymalısın.

deepl==1.17.0

paddleocr==2.7.3

paddlepaddle==2.6.1

simple-lama-inpainting==0.1.0

torch==2.2.2

torchvision==0.17.2

tqdm==4.66.2

textwrap3==0.9.2 

pillow==9.5.0




# İnput:

![1](https://github.com/koesan/manga_cizgi_roman_ceviri/tree/main/resimler/1.jpg)

![2](https://github.com/koesan/manga_cizgi_roman_ceviri/tree/main/resimler/2.jpg)

![3](https://github.com/koesan/manga_cizgi_roman_ceviri/tree/main/resimler/3.png)





# Output:

![1](https://github.com/koesan/manga_cizgi_roman_ceviri/tree/main/resimler/4.jpg)

![2](https://github.com/koesan/manga_cizgi_roman_ceviri/tree/main/resimler/5.jpg)

![3](https://github.com/koesan/manga_cizgi_roman_ceviri/tree/main/resimler/6.png)
