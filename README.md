## KONUŞMACI TANIMA PROJESİ


Proje, konuşmacının kimliğini belirlemek için ses dosyalarını kullanır ve Ysa1.ipynb dosyası kullanılarak önceden eğitilmiştir. TensorFlow kullanılarak geliştirilmiştir ve 2 ana konuşmacı (emr,sel) ile 18 diğer konuşmacıyı temsil edecek şekilde toplam 20 konuşmacı tanıyabilir.

### KURULUM

Gereksinimleri Yükleyin: 
Gerekli Python kütüphanelerini yükleyin.
import ile başlayan tüm kütüphaneler

```pip install kutuphaneadi```

şeklinde yüklenmelidir.

Model Ağırlıklarını İndirin: Önceden eğitilmiş model ağırlıklarını indirip proje dizinine koyun. Dosya adı "weights.h5" olmalıdır.

### KULLANIM

Sunucuyu Başlatın: Aşağıdaki komutu kullanarak Flask sunucusunu başlatın:
python app.py

Web Arayüzüne Erişin: Proje dizinindeki index.html dosyasına tıklayarak web arayüzüne erişin.

Ses Dosyasını Yükleyin: Web arayüzünde yeni bir ses dosyası yükleyin. Yükleme tamamlandığında, konuşmacının adı görüntülenecektir.

### DOSYA YAPISI

app.py: Flask uygulamasını çalıştırır ve web arayüzünü sağlar.
model.py: Konuşmacı tanıma modelini yükler ve çalıştırır.
Ysa1.ipynb: Modelin eğitildiği Jupyter Notebook dosyası.
weights.h5: Önceden eğitilmiş model ağırlıkları.
index.html: Ses dosyasının yüklendiği web arayüzü.

archive: archive.zip'i dışarı çıkararak yeniden eğitimde kullanabilirsiniz.Dosya boyutu yüksek olduğundan aşağıda drive linki mevcut. 
https://drive.google.com/file/d/1Sp68VHftP_Z_1SdVaKZEeLF95i-NZadn/view?usp=drive_link

### GELİŞTİRME

Proje üzerinde değişiklik yapmak isterseniz, aşağıdaki adımları izleyerek yerel bir geliştirme ortamı kurabilirsiniz:

Depoyu Kopyalayın:
git clone https://github.com/kullanici-adi/proje-adi.git
cd proje-adi

Sanal Ortam Oluşturun:

### Linux için
python -m venv venv
source venv/bin/activate  
### Windows için: 
venv\Scripts\activate

