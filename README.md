# Manga Comic Colorization and Translation v2

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-v2.2.2-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

<div align="center">
  
**An AI-powered solution for manga and comic translation and colorization**

*Yapay zeka destekli manga ve çizgi roman çeviri ve renklendirme çözümü*

[English](#english) | [Türkçe](#türkçe)

</div>

---

## English

### Overview

This project combines advanced computer vision and natural language processing techniques to automatically translate and colorize manga and comic pages. The system utilizes state-of-the-art OCR technology, neural machine translation, image inpainting, and deep learning-based colorization to transform black and white manga pages into translated, colorized versions.

### Key Features

#### 🔍 Optical Character Recognition (OCR)
- **Technology**: PaddleOCR engine for superior text extraction
- **Performance**: Optimized for manga-style text detection
- **Accuracy**: Higher precision compared to EasyOCR and PyTesseract
- **Language Support**: Multi-language text recognition capabilities

#### 🌐 Advanced Translation System
- **Primary Engine**: DeepL API for professional-grade translations
- **Quality**: Human-level translation accuracy
- **Flexibility**: Easily configurable for different language pairs
- **Fallback Support**: Built-in error handling and retry mechanisms

#### 🎨 AI-Powered Image Inpainting
- **Technology**: Simple-LAMA inpainting algorithm
- **Function**: Seamlessly removes original text from speech bubbles
- **Quality**: Context-aware background reconstruction
- **Efficiency**: Fast processing without quality compromise

#### 🌈 Neural Network Colorization
- **Architecture**: Custom ResNeXt-based generator network
- **Source**: Adapted from manga-colorization-v2 project
- **Quality**: Professional-grade colorization results
- **Control**: Optional colorization with simple configuration toggle

### Technical Architecture

```
Input Image → OCR Processing → Text Extraction → Translation → Inpainting → Text Overlay → [Optional] Colorization → Output
```

#### Core Components

1. **Text Detection Pipeline**
   - Image preprocessing and noise reduction
   - Advanced OCR with PaddleOCR
   - Text region identification and grouping
   - Coordinate-based text positioning

2. **Translation Engine**
   - DeepL API integration
   - Text preprocessing and cleaning
   - Language detection and conversion
   - Error handling and validation

3. **Image Processing Pipeline**
   - LAMA-based inpainting for text removal
   - Custom font rendering for translated text
   - Adaptive text sizing and positioning
   - Quality preservation throughout processing

4. **Colorization Network**
   - ResNeXt-based generator architecture
   - FFDNet denoiser for image enhancement
   - Spectral normalization for stable training
   - Multi-scale feature extraction

### Requirements

#### System Requirements
- **Python**: 3.8 or higher
- **GPU**: CUDA-compatible GPU (recommended for faster processing)
- **RAM**: Minimum 8GB, 16GB recommended
- **Storage**: At least 2GB free space for models and processing

#### Dependencies
```bash
deepl==1.17.0
paddleocr==2.7.3
paddlepaddle==2.6.1
simple-lama-inpainting==0.1.0
torch==2.2.2
torchvision==0.17.2
tqdm==4.66.2
textwrap3==0.9.2
pillow==9.5.0
opencv-python>=4.5.0
numpy>=1.21.0
```

### Installation Guide

#### Step 1: Environment Setup
Create and activate a virtual environment:

**Linux/macOS:**
```bash
python3 -m venv manga_env
source manga_env/bin/activate
```

**Windows:**
```bash
python -m venv manga_env
manga_env\Scripts\activate
```

#### Step 2: Install Dependencies
```bash
pip install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 pillow==9.5.0
```

#### Step 3: Clone Repository
```bash
git clone https://github.com/koesan/Manga_Comic_Colorization_and_Translation_v2.git
cd Manga_Comic_Colorization_and_Translation_v2
```

#### Step 4: Download Model Files
1. Download the [generator.zip](https://drive.google.com/file/d/1qmxUEKADkEM4iYLp1fpPLLKnfZ6tcF-t/view) file
2. Extract and place the contents in the `networks/` directory
3. Ensure the following structure:
   ```
   networks/
   ├── generator.zip (extracted contents)
   ├── extractor.py
   └── models.py
   ```

#### Step 5: API Configuration
1. Register for a DeepL API account at [DeepL Pro API](https://www.deepl.com/en/pro-api)
2. Obtain your API key
3. Open `main.py` and replace the empty string on line 13:
   ```python
   api = "YOUR_DEEPL_API_KEY_HERE"
   ```

### Usage Instructions

#### Basic Usage

1. **Prepare Input Files**
   - Place manga pages in the `manga/` directory
   - Supported formats: `.jpg`, `.jpeg`, `.png`, `.webp`

2. **Configure Settings**
   - **Colorization**: Set `renklendir = 1` (line 12) to enable, `0` to disable
   - **API Key**: Ensure your DeepL API key is configured (line 13)

3. **Run Processing**
   ```bash
   python3 main.py
   ```

4. **Retrieve Results**
   - Processed images will be saved in the `result/` directory
   - Filenames will match the original input files

#### Advanced Configuration

**Translation Language Pairs**
Modify the translation target language in the `translators` function (line 84):
```python
output = str(translator.translate_text(text, target_lang="TR"))  # Change "TR" to desired language
```

**Supported Language Codes**
- EN (English)
- DE (German)
- FR (French)
- ES (Spanish)
- IT (Italian)
- JA (Japanese)
- TR (Turkish)
- And many more...

### Project Structure

```
Manga_Comic_Colorization_and_Translation_v2/
├── main.py                 # Main execution script
├── colorizator.py         # Colorization model implementation
├── denoising/            # Image denoising components
│   ├── denoiser.py       # FFDNet denoiser implementation
│   ├── models.py         # Denoising model architectures
│   ├── functions.py      # Utility functions
│   └── utils.py          # Helper utilities
├── networks/             # Neural network models
│   ├── models.py         # Generator and discriminator models
│   ├── extractor.py      # Feature extraction networks
│   └── generator.zip     # Pre-trained model weights
├── manga/               # Input directory for manga files
├── result/              # Output directory for processed files
├── resimler/           # Sample images for demonstration
└── README.md           # Project documentation
```

### Performance Optimization

#### GPU Acceleration
For faster processing with CUDA-enabled GPUs:
```python
colorizator = MangaColorizator("cuda", 'networks/generator.zip','networks/extractor.pth')
```

#### Batch Processing
The system automatically processes all supported images in the `manga/` directory with progress tracking via tqdm.

#### Memory Management
- Images are automatically resized to optimize memory usage
- Processing occurs in sequential batches to prevent memory overflow
- Temporary variables are properly cleaned up after processing

### Troubleshooting

#### Common Issues

**1. CUDA Out of Memory**
```python
# Switch to CPU processing
colorizator = MangaColorizator("cpu", 'networks/generator.zip','networks/extractor.pth')
```

**2. DeepL API Quota Exceeded**
- Check your API usage in the DeepL console
- Consider upgrading your plan for higher limits

**3. Font Rendering Issues**
Ensure Arial font is available on your system:
- **Linux**: `sudo apt-get install ttf-mscorefonts-installer`
- **Windows**: Font should be available by default
- **macOS**: Install Microsoft fonts or modify font path in code

**4. OCR Accuracy Issues**
- Ensure input images have sufficient resolution (minimum 300 DPI recommended)
- Check that text regions are clearly visible and not heavily stylized

### Contributing

We welcome contributions to improve the project. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

### License

This project is released under the MIT License. See the LICENSE file for details.

### Acknowledgments

- Original colorization network based on [manga-colorization-v2](https://github.com/qweasdd/manga-colorization-v2)
- OCR functionality powered by [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- Inpainting implementation using [Simple-LAMA-Inpainting](https://github.com/enesmsahin/simple-lama-inpainting)
- Translation services provided by [DeepL API](https://www.deepl.com/docs-api)

### Sample Results

| Input | Output |
|-------|---------|
| ![Input 1](resimler/1.jpg) | ![Output 1](resimler/4.jpg) |
| ![Input 2](resimler/2.jpg) | ![Output 2](resimler/5.jpg) |
| ![Input 3](resimler/3.png) | ![Output 3](resimler/6.png) |

---

## Türkçe

### Genel Bakış

Bu proje, manga ve çizgi roman sayfalarını otomatik olarak çevirmek ve renklendirmek için gelişmiş bilgisayarlı görü ve doğal dil işleme tekniklerini birleştirir. Sistem, en son OCR teknolojisi, sinir ağı tabanlı makine çevirisi, görüntü tamamlama ve derin öğrenme tabanlı renklendirme kullanarak siyah beyaz manga sayfalarını çevrilmiş ve renklendirilmiş versiyonlara dönüştürür.

### Temel Özellikler

#### 🔍 Optik Karakter Tanıma (OCR)
- **Teknoloji**: Üstün metin çıkarma için PaddleOCR motoru
- **Performans**: Manga tarzı metin algılama için optimize edilmiş
- **Doğruluk**: EasyOCR ve PyTesseract'a kıyasla daha yüksek hassasiyet
- **Dil Desteği**: Çok dilli metin tanıma yetenekleri

#### 🌐 Gelişmiş Çeviri Sistemi
- **Ana Motor**: Profesyonel kalitede çeviriler için DeepL API
- **Kalite**: İnsan seviyesinde çeviri doğruluğu
- **Esneklik**: Farklı dil çiftleri için kolay yapılandırma
- **Yedek Destek**: Dahili hata yönetimi ve yeniden deneme mekanizmaları

#### 🎨 Yapay Zeka Destekli Görüntü Tamamlama
- **Teknoloji**: Simple-LAMA tamamlama algoritması
- **İşlev**: Konuşma balonlarından orijinal metni sorunsuz bir şekilde kaldırır
- **Kalite**: Bağlam farkında arka plan yeniden yapılandırması
- **Verimlilik**: Kaliteden ödün vermeden hızlı işleme

#### 🌈 Sinir Ağı Renklendirmesi
- **Mimari**: Özel ResNeXt tabanlı üretici ağ
- **Kaynak**: manga-colorization-v2 projesinden uyarlanmış
- **Kalite**: Profesyonel kalitede renklendirme sonuçları
- **Kontrol**: Basit yapılandırma anahtarıyla isteğe bağlı renklendirme

### Teknik Mimari

```
Giriş Görüntüsü → OCR İşlemesi → Metin Çıkarma → Çeviri → Tamamlama → Metin Ekleme → [İsteğe Bağlı] Renklendirme → Çıkış
```

#### Ana Bileşenler

1. **Metin Algılama Hattı**
   - Görüntü ön işlemesi ve gürültü azaltma
   - PaddleOCR ile gelişmiş OCR
   - Metin bölgesi tanımlama ve gruplama
   - Koordinat tabanlı metin konumlandırma

2. **Çeviri Motoru**
   - DeepL API entegrasyonu
   - Metin ön işlemesi ve temizleme
   - Dil algılama ve dönüştürme
   - Hata yönetimi ve doğrulama

3. **Görüntü İşleme Hattı**
   - Metin kaldırma için LAMA tabanlı tamamlama
   - Çevrilmiş metin için özel font görselleştirme
   - Uyarlanabilir metin boyutlandırma ve konumlandırma
   - İşlem boyunca kalite korunması

4. **Renklendirme Ağı**
   - ResNeXt tabanlı üretici mimari
   - Görüntü iyileştirme için FFDNet gürültü giderici
   - Kararlı eğitim için spektral normalleştirme
   - Çok ölçekli özellik çıkarma

### Gereksinimler

#### Sistem Gereksinimleri
- **Python**: 3.8 veya üzeri
- **GPU**: CUDA uyumlu GPU (daha hızlı işleme için önerilen)
- **RAM**: Minimum 8GB, 16GB önerilen
- **Depolama**: Model ve işleme için en az 2GB boş alan

#### Bağımlılıklar
```bash
deepl==1.17.0
paddleocr==2.7.3
paddlepaddle==2.6.1
simple-lama-inpainting==0.1.0
torch==2.2.2
torchvision==0.17.2
tqdm==4.66.2
textwrap3==0.9.2
pillow==9.5.0
opencv-python>=4.5.0
numpy>=1.21.0
```

### Kurulum Kılavuzu

#### Adım 1: Ortam Kurulumu
Sanal ortam oluşturun ve etkinleştirin:

**Linux/macOS:**
```bash
python3 -m venv manga_env
source manga_env/bin/activate
```

**Windows:**
```bash
python -m venv manga_env
manga_env\Scripts\activate
```

#### Adım 2: Bağımlılıkları Yükleyin
```bash
pip install deepl==1.17.0 paddleocr==2.7.3 paddlepaddle==2.6.1 simple-lama-inpainting==0.1.0 torch==2.2.2 torchvision==0.17.2 tqdm==4.66.2 textwrap3==0.9.2 pillow==9.5.0
```

#### Adım 3: Depoyu Klonlayın
```bash
git clone https://github.com/koesan/Manga_Comic_Colorization_and_Translation_v2.git
cd Manga_Comic_Colorization_and_Translation_v2
```

#### Adım 4: Model Dosyalarını İndirin
1. [generator.zip](https://drive.google.com/file/d/1qmxUEKADkEM4iYLp1fpPLLKnfZ6tcF-t/view) dosyasını indirin
2. İçeriği çıkarın ve `networks/` dizinine yerleştirin
3. Aşağıdaki yapının olduğundan emin olun:
   ```
   networks/
   ├── generator.zip (çıkarılan içerik)
   ├── extractor.py
   └── models.py
   ```

#### Adım 5: API Yapılandırması
1. [DeepL Pro API](https://www.deepl.com/en/pro-api) adresinden bir DeepL API hesabı oluşturun
2. API anahtarınızı alın
3. `main.py` dosyasını açın ve 13. satırdaki boş string'i değiştirin:
   ```python
   api = "DEEPL_API_ANAHTARINIZ_BURAYA"
   ```

### Kullanım Talimatları

#### Temel Kullanım

1. **Giriş Dosyalarını Hazırlayın**
   - Manga sayfalarını `manga/` dizinine yerleştirin
   - Desteklenen formatlar: `.jpg`, `.jpeg`, `.png`, `.webp`

2. **Ayarları Yapılandırın**
   - **Renklendirme**: Etkinleştirmek için `renklendir = 1` (12. satır), devre dışı bırakmak için `0`
   - **API Anahtarı**: DeepL API anahtarınızın yapılandırıldığından emin olun (13. satır)

3. **İşlemi Çalıştırın**
   ```bash
   python3 main.py
   ```

4. **Sonuçları Alın**
   - İşlenmiş görüntüler `result/` dizinine kaydedilecek
   - Dosya adları orijinal giriş dosyalarıyla eşleşecek

#### Gelişmiş Yapılandırma

**Çeviri Dil Çiftleri**
`translators` fonksiyonunda çeviri hedef dilini değiştirin (84. satır):
```python
output = str(translator.translate_text(text, target_lang="TR"))  # "TR"yi istenen dile değiştirin
```

**Desteklenen Dil Kodları**
- EN (İngilizce)
- DE (Almanca)
- FR (Fransızca)
- ES (İspanyolca)
- IT (İtalyanca)
- JA (Japonca)
- TR (Türkçe)
- Ve daha fazlası...

### Proje Yapısı

```
Manga_Comic_Colorization_and_Translation_v2/
├── main.py                 # Ana yürütme scripti
├── colorizator.py         # Renklendirme modeli implementasyonu
├── denoising/            # Görüntü gürültü giderme bileşenleri
│   ├── denoiser.py       # FFDNet gürültü giderici implementasyonu
│   ├── models.py         # Gürültü giderme model mimarileri
│   ├── functions.py      # Yardımcı fonksiyonlar
│   └── utils.py          # Yardımcı araçlar
├── networks/             # Sinir ağı modelleri
│   ├── models.py         # Üretici ve ayırıcı modeller
│   ├── extractor.py      # Özellik çıkarma ağları
│   └── generator.zip     # Önceden eğitilmiş model ağırlıkları
├── manga/               # Manga dosyaları için giriş dizini
├── result/              # İşlenmiş dosyalar için çıkış dizini
├── resimler/           # Gösteri için örnek görüntüler
└── README.md           # Proje belgelendirmesi
```

### Performans Optimizasyonu

#### GPU Hızlandırma
CUDA etkin GPU'lar ile daha hızlı işleme için:
```python
colorizator = MangaColorizator("cuda", 'networks/generator.zip','networks/extractor.pth')
```

#### Toplu İşleme
Sistem, tqdm aracılığıyla ilerleme takibi ile `manga/` dizinindeki tüm desteklenen görüntüleri otomatik olarak işler.

#### Bellek Yönetimi
- Görüntüler bellek kullanımını optimize etmek için otomatik olarak yeniden boyutlandırılır
- Bellek taşmasını önlemek için işleme sıralı toplu işlemler halinde gerçekleşir
- Geçici değişkenler işlem sonrası düzgün bir şekilde temizlenir

### Sorun Giderme

#### Yaygın Sorunlar

**1. CUDA Bellek Yetersizliği**
```python
# CPU işlemesine geçin
colorizator = MangaColorizator("cpu", 'networks/generator.zip','networks/extractor.pth')
```

**2. DeepL API Kotası Aşıldı**
- DeepL konsolunda API kullanımınızı kontrol edin
- Daha yüksek limitler için planınızı yükseltmeyi düşünün

**3. Font Görselleştirme Sorunları**
Sisteminizde Arial fontunun mevcut olduğundan emin olun:
- **Linux**: `sudo apt-get install ttf-mscorefonts-installer`
- **Windows**: Font varsayılan olarak mevcut olmalı
- **macOS**: Microsoft fontlarını yükleyin veya koddaki font yolunu değiştirin

**4. OCR Doğruluk Sorunları**
- Giriş görüntülerinin yeterli çözünürlükte olduğundan emin olun (minimum 300 DPI önerilen)
- Metin bölgelerinin açık bir şekilde görünür ve aşırı stilize edilmediğini kontrol edin

### Katkıda Bulunma

Projeyi geliştirmek için katkılarınızı memnuniyetle karşılıyoruz. Lütfen şu yönergeleri takip edin:

1. Depoyu fork edin
2. Özellik dalı oluşturun (`git checkout -b feature/iyilestirme`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik ekle'`)
4. Dala push edin (`git push origin feature/iyilestirme`)
5. Pull Request oluşturun

### Lisans

Bu proje MIT Lisansı altında yayınlanmıştır. Ayrıntılar için LICENSE dosyasına bakın.

### Teşekkürler

- Orijinal renklendirme ağı [manga-colorization-v2](https://github.com/qweasdd/manga-colorization-v2) tabanlı
- OCR işlevselliği [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) tarafından desteklenmektedir
- Tamamlama implementasyonu [Simple-LAMA-Inpainting](https://github.com/enesmsahin/simple-lama-inpainting) kullanılarak yapılmıştır
- Çeviri hizmetleri [DeepL API](https://www.deepl.com/docs-api) tarafından sağlanmaktadır

### Örnek Sonuçlar

| Giriş | Çıkış |
|-------|-------|
| ![Giriş 1](resimler/1.jpg) | ![Çıkış 1](resimler/4.jpg) |
| ![Giriş 2](resimler/2.jpg) | ![Çıkış 2](resimler/5.jpg) |
| ![Giriş 3](resimler/3.png) | ![Çıkış 3](resimler/6.png) |

---

<div align="center">

**Made with ❤️ for the manga community**

*Manga topluluğu için ❤️ ile yapılmıştır*

</div>
