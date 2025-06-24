# 🧠 Sosyal Anksiyete (Kaygı) Tahmin Projesi

Bu proje, bireylerin sosyal kaygı (anksiyete) düzeylerini davranışsal, yaşam tarzı ve psikolojik verilere dayanarak makine öğrenmesi ile tahmin etmeyi amaçlamaktadır.

## 🎯 Proje Amacı

Sosyal anksiyete, bireylerin toplumsal ortamlarda stres ve kaçınma davranışları göstermesine yol açan yaygın bir ruhsal bozukluktur. Bu proje ile aşağıdaki hedefler doğrultusunda modeller geliştirilmiştir:

- Erken psikolojik müdahale için tahmin sistemleri oluşturmak
- Sosyal kaygıya etki eden risk faktörlerini belirlemek
- Kişiselleştirilmiş öneriler sunmak (uyku, aktivite vs.)
- Eğitim kurumlarında rehberlik hizmetlerini güçlendirmek

---

## 📊 Kullanılan Veri Seti

- 10.000+ gözlem içeren sentetik bir veri seti
- Psikolojik anketler, davranışsal ölçümler ve yaşam tarzı bilgilerini içerir
- Hedef değişken: **Anksiyete seviyesi (1-10 arası bir değer)**

### Değişken Grupları:

- Demografik Bilgiler (yaş, cinsiyet, meslek)
- Yaşam Tarzı (uyku süresi, fiziksel aktivite, diyet)
- Sağlık Göstergeleri (kalp atış hızı, solunum hızı, baş dönmesi)
- Psikolojik Durum (terapi sıklığı, ailede anksiyete öyküsü)
- Yaşam Olayları (iş kaybı, taşınma vb.)

---

## 🔧 Veri Hazırlama

- Eksik veriler ortalama, medyan veya mod ile dolduruldu
- Kategorik değişkenler sayısallaştırıldı (LabelEncoder, OneHotEncoder)
- Sayısal değişkenler normalize edildi (StandardScaler)

---

## 🤖 Kullanılan Modeller

Tahmin sürecinde aşağıdaki sınıflandırma algoritmaları uygulanmıştır:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- KNN
- SVM

Veri, %80 eğitim / %20 test oranında bölünerek eğitildi. Hiperparametre optimizasyonu için `GridSearchCV` kullanıldı.

---

## 📈 Değerlendirme Metrikleri

- Accuracy
- Precision / Recall
- F1-score

> Yüksek anksiyete seviyesindeki bireyleri doğru tahmin etmek için özellikle **Recall** ve **F1-score**'a odaklanılmıştır.

---

## 🌐 Streamlit Uygulaması

Modelin tahmin gücünü görselleştirmek ve kullanıcı etkileşimini sağlamak amacıyla **Streamlit** ile web tabanlı bir arayüz geliştirildi.

- Kullanıcı verileri giriş formu ile alınır (yaş, cinsiyet, sigara, terapi vb.)
- "Predict" butonu ile model tahmin yapar
- Sonuç kullanıcıya sade ve sezgisel biçimde sunulur

---

## 💡 Hedef Kitle

- Psikologlar / Psikolojik danışmanlar
- Eğitim kurumları
- Akademisyenler
- Kendi sosyal kaygı seviyesini öğrenmek isteyen bireyler

---

## 🗂️ Klasör Yapısı

