WeaponDetector

📌 Proje Açıklaması

WeaponDetector, derin öğrenme tabanlı bir model kullanarak silah ve bıçak tespiti yapmayı amaçlayan bir bilgisayarla görme uygulamasıdır. Kamera görüntülerinden nesneleri tanıyıp, tehlikeli nesneleri algılayarak güvenlik sistemlerinde kullanılabilir.

🚀 Özellikler

✅ Gerçek zamanlı silah ve bıçak tespiti

✅ TensorFlow/Keras tabanlı derin öğrenme modeli

✅ OpenCV ile görüntü işleme

✅ Uyarı sistemleri (Sesli ve görsel bildirimler)

🔧 Kurulum

📌 Gereksinimler

🐍 Python 3.8 veya daha yeni bir sürüm

📦 TensorFlow, OpenCV, NumPy, Matplotlib

📥 Gerekli Paketlerin Kurulumu

Aşağıdaki komutu kullanarak gerekli bağımlılıkları yükleyebilirsiniz:

```
pip install -r requirements.txt
```

🔗 Projeyi Klonlama

```
git clone https://github.com/didaryilmaz/WeaponDetector.git
cd WeaponDetector
```

📂 Veri Kümesi

Modelin eğitimi için kullanılan veri kümesini datasets/ klasörüne ekleyin. Eğer hazır eğitilmiş modeli kullanacaksanız, models/ klasörüne önceden eğitilmiş model dosyanızı yerleştirin.

🛠 Kullanım

🏋️ Modeli Eğitme

```
python train.py
```

Bu komut, veri kümesini kullanarak modeli eğitir ve models/weapon_detector.h5 olarak kaydeder.

🎯 Modeli Çalıştırma

Gerçek zamanlı tespit için aşağıdaki komutu çalıştırın:

```
python detect.py
```

Bu komut, bilgisayarın kamerasını kullanarak anlık tespit yapacaktır.

🤝 Katkıda Bulunma

Katkıda bulunmak için aşağıdaki adımları takip edebilirsiniz:

📌 Bu depoyu forklayın.

🔄 Yeni bir dal (branch) oluşturun.

📝 Değişikliklerinizi yapın ve commit edin.

📩 Bir çekme isteği (pull request) gönderin.

