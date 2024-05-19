from simple_lama_inpainting import SimpleLama
import deepl
from tqdm import tqdm
import numpy as np
import textwrap3
from paddleocr import PaddleOCR
import cv2
from colorizator import MangaColorizator
import os
from PIL import ImageFont, ImageDraw, Image

renklendir = 1
api = "19977363-aef8-46f6-b48f-ec8bd21580d8:fx"

# Yakın kelimeleri bulan fonksiyon
def yakın_kelimeleri_bul(kordinatlar):

    sonuclar = []
    a = []
    thres = 65
    while len(kordinatlar) >= 1:
        a.append(kordinatlar[0])
        for i in kordinatlar[1:]:
            if (a[-1][0] - thres <= i[0] and a[-1][0] + thres >= i[0]) and a[-1][1] + thres > i[1]:
                a.append(i)
                kordinatlar.remove(i)
        sonuclar.append(a)
        kordinatlar.pop(0)
        a = []

    return sonuclar

# Kordinatların orta noktasını bulan fonksiyon
def orta_nokta_bul(koordinatlar):

    x_toplam = sum(x for x, y in koordinatlar)
    y_toplam = sum(y for x, y in koordinatlar)
    ortalama_x = x_toplam / len(koordinatlar)
    ortalama_y = y_toplam / len(koordinatlar)

    return (ortalama_x, ortalama_y)

# İki dizinin ortak elemanlarının indekslerini bulan fonksiyon
def indexleri_bul(dizi1, dizi2):

    indeksler = []
    for elemanlar in dizi2:
        eleman_indeksleri = []
        for eleman in elemanlar:
            if eleman in dizi1:
                eleman_indeksleri.append(dizi1.index(eleman))
        indeksler.append(eleman_indeksleri)

    return indeksler
#auto spale chacke
# Metni düzeltme fonksiyonu
def verileri_düzelt(dizi):
    duzeltilmis_elemanlar = []
    i = 0
    while i < len(dizi):

        eleman = dizi[i]
        if '-' in eleman:
            parcalar = eleman.split('-')

            if i + 1 < len(dizi):
                duzeltilmis_eleman = (parcalar[0] + dizi[i+1]).strip()
                i += 1  
            else:
                duzeltilmis_eleman = parcalar[0].strip()
        else:
            duzeltilmis_eleman = eleman

        duzeltilmis_elemanlar.append(duzeltilmis_eleman)
        i += 1 
    # Kelimeleri birleştir
    birlesik_string = ' '.join([eleman.lower() for eleman in duzeltilmis_elemanlar])

    return birlesik_string

# Çeviri işlemini gerçekleştiren fonksiyon
def translators(text, translator):
 
    output = str(translator.translate_text(text, target_lang="TR"))
    # Türkçe karakterleri ingilizce karakterlere çevir
    #cevirme_tablosu = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    #output = output.translate(cevirme_tablosu)
    return output

def img_mask(dizi, dizi2, img_path):
    
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    img = np.zeros((height, width, 1), dtype=np.uint8)

    for eleman in dizi:

        all_x = [point[0] for sublist in eleman for point in sublist]
        all_y = [point[1] for sublist in eleman for point in sublist]
        x1, y1 = max(all_x), max(all_y)
        x2, y2 = min(all_x), min(all_y)

        img = cv2.rectangle(img, (int(x1+7), int(y1+7)), (int(x2-7), int(y2-7)), (255, 255, 255), thickness=cv2.FILLED)

    return img
    
# Beyaz kare oluşturan fonksiyon
def beyaz_kare_olustur(dizi, dizi2, img_path, simple_lama):
    
    img = cv2.imread(img_path)
    mask = img_mask(dizi, dizi2, img_path)
    
    img = simple_lama(img, mask)
    değişken = 0
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Arial.ttf", 16)
    for eleman in dizi:
    # En büyük x değeri x1, en küçük y değeri y1'e, en küçük x değeri x2, en büyük y değeri ise y2'ye yerleştirilir
        all_x = [point[0] for sublist in eleman for point in sublist]
        all_y = [point[1] for sublist in eleman for point in sublist]
        x1, y1 = max(all_x), max(all_y)
        x2, y2 = min(all_x), min(all_y)
        # Aldığın kordinatlara beyaz bir kare çiz
        #img = cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), thickness=cv2.FILLED)

        # Çevrilmiş metini yeni beyaz karenin üstüne yaz
        wrapped_text = textwrap3.wrap(dizi2[değişken], width=20)
        for i, line in enumerate(wrapped_text):
            y = int((y1 + y2) / 2) + i * 20
            x = int((x1 + x2 - int(draw.textlength(line, font=font))) / 2)
            draw.text((x,y-20), line, fill=(0,0,0), font=font)
        değişken += 1

    img = np.array(img)
    return img

def unicod_textwrap(metin):
    satirlar = []
    satir = ""
    genislik = 15
    kelime_listesi = metin.split()
    
    for kelime in kelime_listesi:
        if len(satir) + len(kelime) <= genislik:
            satir += kelime + " "
        else:
            satirlar.append(satir.strip())
            satir = kelime + " "
    
    if satir:
        satirlar.append(satir.strip())
    
    return satirlar

# Ana işlevi gerçekleştiren fonksiyon
def main():

    #resimi renklendirmek için
    colorizator = MangaColorizator("cpu", 'networks/generator.zip','networks/extractor.pth')
    
    # Pipline ve easyocr yapıları oluşturuyor 
    reader = PaddleOCR(lang='en')
    translator = deepl.Translator(api)
    simple_lama = SimpleLama()
    path = "manga"
    save = "cevri_manga"
    dosya_listesi = os.listdir(path)
    resimler = [dosya for dosya in dosya_listesi if dosya.endswith(('.jpg', '.jpeg', '.png', ".webp"))]

    for resim_adı in tqdm(resimler, desc="İşleniyor", unit="resim"):

        resim_yolu = os.path.join(path, resim_adı)
        img = cv2.imread(resim_yolu, 0)

        # 150'nin üstündeki pikselleri 255 e yuvarlayacak
        img[img>=150] = 255
        #kernel = np.ones((3, 3), np.uint8)
        #erosion = cv2.erode(img, kernel, iterations=1)
        #dilation = cv2.dilate(erosion, kernel, iterations=1)
        #opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        dizi = reader.ocr(img)
        #dizi = sum(dizi, [])
        dizi = [item for sublist in dizi if sublist is not None for item in sublist]
        
        if len(dizi) > 1:

            kordinatlar = [orta_nokta_bul(i[0]) for i in dizi]
            kordinatlar_ = kordinatlar.copy()

            sonuclar = yakın_kelimeleri_bul(kordinatlar)
            indexler = indexleri_bul(kordinatlar_, sonuclar)

            kordinatlar = []
            konuşma_dizisi = []

            for i in indexler:
                kordinatlar_ = []
                string = []

                for a in i:
                    kordinatlar_.append(dizi[a][0])
                    string.append(str(dizi[a][1][0]))

                kordinatlar.append(kordinatlar_)
                konuşma_dizisi.append(translators(verileri_düzelt(string), translator))

            parçalar = resim_adı.split(".")

            resim = beyaz_kare_olustur(kordinatlar, konuşma_dizisi, resim_yolu, simple_lama)
            
            if renklendir == 1:
                if resim.shape[1] % 32 != 0:

                    width = 32 * (resim.shape[1] // 32)
                
                else:
                    width =resim.shape[1]
                colorizator.set_image(resim, width, True, 25)

                resim = colorizator.colorize()

                resim *= 255
                resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)
                
                #plt.imsave(f"{save}/{parçalar[0]}.{parçalar[1]}", resim)
            cv2.imwrite(f"{save}/{parçalar[0]}.{parçalar[1]}", resim)

if __name__ == "__main__":
    main()
