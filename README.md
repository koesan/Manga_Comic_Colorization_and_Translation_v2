# Manga Comic Colorization and Translation v2 (Manga ve Çizgi Roman Çevirici ve Renklendirici)

***

his project use artificial intelligence to translate mangas or comics in different languages to any language. It also colorizes black and white mangas. It translates color mangas or comics and translates black and white mangas or comics. If desired, it can also colorize. The project has different steps.

With simple change in code, it can translate between different languages.

***

Bu proje, yapay zeka kullanarak farklı dillerdeki mangaları veya çizgi romanları herhangi bir dile çevirir ve renksiz mangaları renklendirir. Renkli manga veya çizgi romanları çevirir, renksiz manga veya çizgi romanları çevirir ve istenilirse renklendirebilir. Proje, çeşitli aşamalardan oluşmaktadır


Kodda yapılacak değişiklik ile farklı diller arası çevri işlemide gereçekleştirilebilinir.

***

## FEATURES(ÖZELLİKLER)

***

* OCR

To extract text from images, OCR is used. In this project, I choose PaddleOCR library. PaddleOCR is faster and gives better result than other OCR libraries like EasyOCR or Pytesseract, so I decided to use it in the project.

* Translation

For translation, I first plan to use transformers library with different language models. After tests, I did not get the results I wanted, so I decided to use DeepL API. To use DeepL API, register at https://www.deepl.com/en/pro-api and get your key. Add your key in the code at line 13 where it says api = "API-KEY".

* Inpainting

To add translated text in image, first we need to remove text from image. For this, simple-lama-inpainting library places boxes over text and AI fills in closed areas.

* Colorization

To colorize black and white images, I used the project from https://github.com/qweasdd/manga-colorization-v2. I adapted this project to my code to colorize black and white images. If you set colorize = 1 at line 12, it will color images. If colorize = 0, it will not color images.

***

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

***

## Installation(Kurulum)

Before running the project, follow these steps to create a virtual Python environment and install libraries:

1. Create virtual environment:
    ```bash
    python3 -m venv myenv
    ```

2. Activate virtual environment:

    - **Linux/MacOS**:
      ```bash
      source myenv/bin/activate
      ```
    - **Windows**:
      ```bash
      .\myenv\Scripts\activate
      ```

3. After activating virtual environment, install necessary libraries with this command:

    ```bash
    pip install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 pillow==9.5.0
    ```

4. **Clone Repository**  
   After creating virtual environment, clone the project from GitHub:

   ```bash
   git clone https://github.com/koesan/Manga_Comic_Colorization_and_Translation_v2.git
   ```

5. **Download Necessary Files**  
   Download [generator.zip](https://drive.google.com/file/d/1qmxUEKADkEM4iYLp1fpPLLKnfZ6tcF-t/view) and place it in `networks` folder of the cloned repository.

6. **Place Manga Files**  
   Add manga files you want to color and translate into `manga` folder. Supported formats are: `.jpg`, `.jpeg`, `.png`, `.webp`.

7. **Run Project**  
   Activate virtual environment and go to project folder:

   - **Linux/MacOS**:
     ```bash
     source myenv/bin/activate
     cd ./Manga_Comic_Colorization_and_Translation_v2
     ```

   - **Windows**:
     ```bash
     .\myenv\Scripts\activate
     cd .\Manga_Comic_Colorization_and_Translation_v2
     ```

8. **Start Project**  
   After activating virtual environment and entering correct directory, run the project with this command:

   ```bash
   python3 main.py
   ```

9. **Results**  
   Translated and colorized manga pages will be saved in `result` folder.

***

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

***

| İnputs                       | Outputs                   |
|-------------------------------|---------------------------------|
| ![1](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/1.jpg) | ![1](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/4.jpg) |
| ![2](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/2.jpg) | ![2](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/5.jpg) |
| ![3](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/3.png) | ![3](https://github.com/koesan/manga_cizgi_roman_ceviri/raw/main/resimler/6.png) |

***
