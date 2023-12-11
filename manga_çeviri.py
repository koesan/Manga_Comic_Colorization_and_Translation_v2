import easyocr
from transformers import pipeline
import cv2
import textwrap
import os
from tqdm import tqdm

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

    output = translator(text, clean_up_tokenization_spaces=True)
    output = output[0]["translation_text"]
    # Türkçe karakterleri ingilizce karakterlere çevir
    cevirme_tablosu = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    output = output.translate(cevirme_tablosu)

    return output

# Beyaz kare oluşturan fonksiyon
def beyaz_kare_olustur(dizi, dizi2, img_path):

    img = cv2.imread(img_path)

    # Gerekli değişkenler
    değişken = 0
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    font_size = 0.7
    font_thickness = 1

    for eleman in dizi:

        # En büyük x değeri x1, en küçük y değeri y1'e, en küçük x değeri x2, en büyük y değeri ise y2'ye yerleştirilir
        all_x = [point[0] for sublist in eleman for point in sublist]
        all_y = [point[1] for sublist in eleman for point in sublist]
        x1, y1 = max(all_x), max(all_y)
        x2, y2 = min(all_x), min(all_y)
        # Aldığın kordinatlara beyaz bir kare çiz
        img = cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), thickness=cv2.FILLED)

        # Çevrilmiş metini yeni beyaz karenin üstüne yaz
        wrapped_text = textwrap.wrap(dizi2[değişken], width=15)
        for i, line in enumerate(wrapped_text):
            textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]
            gap = textsize[1] + 10
            y = int((y1 + y2) / 2) + i * gap
            x = int((x1 + x2 - textsize[0]) / 2)
            cv2.putText(img, line, (x, y), font, font_size, (0, 0, 0), font_thickness, lineType=cv2.LINE_AA)

        değişken += 1

    return img

# Ana işlevi gerçekleştiren fonksiyon
def main():

    # Pipline ve easyocr yapıları oluşturuyor 
    reader = easyocr.Reader(['en'], gpu=False)
    translator = pipeline(task="translation", model="Helsinki-NLP/opus-mt-tc-big-en-tr")

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

        dizi = reader.readtext(img)

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
                    string.append(str(dizi[a][1]))

                kordinatlar.append(kordinatlar_)
                konuşma_dizisi.append(translators(verileri_düzelt(string), translator))

            parçalar = resim_adı.split(".")

            resim = beyaz_kare_olustur(kordinatlar, konuşma_dizisi, resim_yolu)
            cv2.imwrite(f"{save}/{parçalar[0]}.{parçalar[1]}", resim)

if __name__ == "__main__":
    main()
