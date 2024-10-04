# Manga Comic Colorization and Translation v2 (Manga ve Çizgi Roman Çevirici ve Renklendirici)

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

## Kurulum

Projeyi çalıştırmadan önce, sanal bir Python ortamı oluşturup kütüphaneleri yüklemek için şu adımları izleyin:

1. Sanal ortamı oluşturun:
    ```bash
    python3 -m venv myenv
    ```

2. Sanal ortamı aktif hale getirin:

    - **Linux/MacOS**:
      ```bash
      source myenv/bin/activate
      ```
    - **Windows**:
      ```bash
      .\myenv\Scripts\activate
      ```

3. Sanal ortam aktif hale geldikten sonra, gerekli kütüphaneleri şu komutla yükleyin:

    ```bash
    pip install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 pillow==9.5.0
    ```
2. **Repoyu Clonelayın**  
   Sanal ortamı oluşturduktan sonra, projeyi GitHub'dan klonlayın:

   ```bash
   git clone https://github.com/koesan/Manga_Comic_Colorization_and_Translation_v2.git
   ```

4. **Gerekli Dosyaları İndirin**  
   [generator.zip](https://drive.google.com/file/d/1qmxUEKADkEM4iYLp1fpPLLKnfZ6tcF-t/view) dosyasını indirip, klonladığınız repodaki `networks` klasörünün içine yerleştirin.

5. **Manga Dosyalarını Yerleştirin**  
   Renklendirmek ve çevirmek istediğiniz manga dosyalarını `manga` klasörünün içine ekleyin. Desteklenen dosya formatları: `.jpg`, `.jpeg`, `.png`, `.webp`.

6. **Projeyi Çalıştırma**  
   Sanal ortamı aktif edin ve proje klasörüne gidin:

   - **Linux/MacOS**:
     ```bash
     source myvenv/bin/activate
     cd ./Manga_Comic_Colorization_and_Translation_v2
     ```

   - **Windows**:
     ```bash
     .\myvenv\Scripts\activate
     cd .\Manga_Comic_Colorization_and_Translation_v2
     ```

7. **Projeyi Başlatın**  
   Sanal ortam aktif hale getirildikten ve doğru dizine girildikten sonra projeyi çalıştırmak için şu komutu kullanın:

   ```bash
   python3 main.py
   ```

8. **Sonuçlar**  
   Çevrilen ve renklendirilen manga sayfaları `result` klasörünün içinde kaydedilecektir.


# İnput:

![1](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/1.jpg)

![2](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/2.jpg)

![3](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/3.png)

# Output:

![1](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/4.jpg)

![2](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/5.jpg)

![3](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/6.png)
