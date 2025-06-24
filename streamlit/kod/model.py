import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def app():
    st.title("📊 Modellerin Accuracy ve F1 Score Karşılaştırması")

    # st.subheader("📊 Model Karşılaştırma Grafiği")
    st.image("C:/Users/EXCALIBUR/streamlit/f1_acc.png", caption="Accuracy ve F1 Score Karşılaştırması", use_container_width=True)

    # 📌 Confusion Matrix görsellerini 2'şerli olarak göster
    st.subheader("📉 Confusion Matrix Görselleri")
    col1, col2 = st.columns(2)

    with col1:
        st.image("C:/Users/EXCALIBUR/streamlit/knn.png", caption="KNN Confusion Matrix", use_container_width=True)

    with col2:
        st.image("C:/Users/EXCALIBUR/streamlit/lg.png", caption="Logistic Regression CM", use_container_width=True)

    # Diğer 2'liyi alttan devam ettir
    col3, col4 = st.columns(2)

    with col3:
        st.image("C:/Users/EXCALIBUR/streamlit/rf.png", caption="Random Forest CM", use_container_width=True)

    with col4:
        st.image("C:/Users/EXCALIBUR/streamlit/xgb.png", caption="XGBoost CM", use_container_width=True)

    # Son modeli tek sütun göster (SVM)
    st.image("C:/Users/EXCALIBUR/streamlit/svm.png", caption="SVM Confusion Matrix", use_container_width=True)


    # Genel değerlendirme
    st.subheader("📊 Model Performans Değerlendirmesi")
    st.markdown("""
    **✅ Genel Karşılaştırma**
   Genel Karşılaştırma

    Logistic Regression, yüksek doğruluk oranı (Accuracy: 0.7891) ve dengeli F1 skoru ile güçlü bir temel model olduğunu göstermektedir. Özellikle "High" sınıfındaki başarı dikkat çekicidir. Açıklanabilirlik açısından da avantajlıdır.
    
    Random Forest, benzer doğruluk ve F1 skorlarıyla Logistic Regression’a yakın performans sergilemiştir. “High” sınıfını başarıyla sınıflandırması modelin güçlü yönlerindendir. Özellik önemleri üzerinden analiz yapılabilir.
    
    XGBoost, yüksek F1 skoru (0.8149) ve başarılı “High” sınıf tahminleriyle dikkat çeker. Dengesiz sınıflarda güçlü bir alternatiftir, ancak daha karmaşıktır ve hiperparametre ayarı gerektirir.
    
    K-Nearest Neighbors (KNN), daha düşük doğruluk ve F1 skorlarıyla bu veri setinde yeterince iyi performans gösterememiştir. Sınıflar arası karışıklık oranı yüksektir.
    
    Support Vector Machine (SVM), doğruluk ve F1 skorları açısından ortalama bir modeldir. “Moderate” ve “High” sınıflarında zayıf kalmıştır.
    """)

    st.markdown("""
    **🏆 Sonuç ve Öneri**

    Model seçiminde sadece doğruluk değil, özellikle “High” sınıfının doğru sınıflandırılması kritik önem taşımaktadır.
    
    Random Forest ve XGBoost, hem genel başarı oranı hem de “High” sınıfındaki performanslarıyla öne çıkmaktadır.
    
    Logistic Regression, daha sade ve açıklanabilir model isteyenler için güçlü bir seçenektir.
    
    KNN ve SVM bu veri seti için zayıf performans göstermiştir.
    
    Önerilen Modeller:
    Random Forest veya XGBoost tercih edilmelidir. Hem genel dengeyi iyi kurmakta hem de riskli grubu (High) isabetli şekilde tahmin etmektedirler.




        """)

