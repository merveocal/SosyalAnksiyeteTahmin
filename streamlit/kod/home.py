import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("📁 Sosyal Kaygı Veri Seti")

    st.markdown("""
    ### 📌 Proje Amacı:
    Bu projede, bireylerin psikolojik, fizyolojik ve yaşam tarzı verileri kullanılarak anksiyete düzeylerinin tahmin edilmesi hedeflenmiştir..

    **Adım adım yapılan işlemler:**
    1. Google Drive bağlantısı sağlandı ve veri seti okundu  
    2. Veri yapısı incelendi (`shape`, `head`, sınıf dağılımları)  
    3. Sayısal analiz ve görselleştirme ile EDA yapıldı  
    4. `Anxiety Level` sütununa göre sınıflandırma modelleri eğitildi  
    5. Eğitilen model ile yeni tahminler gerçekleştirildi  
    ---
    """)

    st.markdown("""
    ---
    🛠 **Kullanılan Teknolojiler**:
    - Python 🐍  
    - Pandas & Scikit-learn 📦  
    - Streamlit 🌐  
    - Matplotlib & Seaborn 📊  

    <br><br>

    🤖 **Kullanılan Makine Öğrenmesi Modelleri**:
    - Lojistik Regresyon  
    - XGBoost  
    - Rastgele Orman (Random Forest)  
    - Destek Vektör Makineleri (SVM)  
    - K-En Yakın Komşu (KNN)  
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📂 Veri dosyasını yükleyin (.csv)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Grafik 1 - Kafein vs Anksiyete
        st.subheader("☕ Kafein Tüketimi ile Anksiyete Seviyesi")
        st.markdown("Kafein tüketimi arttıkça anksiyete seviyesindeki değişimi gösteren regresyon grafiği:")
        fig1, ax1 = plt.subplots(figsize=(10,6))
        sns.regplot(x='Caffeine Intake (mg/day)', y='Anxiety Level (1-10)', data=df,
                    scatter_kws={'alpha':0.5, 'color':'#7E57C2'},
                    line_kws={'color':'#000000'}, ax=ax1)
        ax1.set_title('Kafein Tüketimi ile Anksiyete Seviyesi Arasındaki İlişki')
        ax1.set_xlabel('Kafein Tüketimi (mg/gün)')
        ax1.set_ylabel('Anksiyete Seviyesi (1-10)')
        st.pyplot(fig1)

        # Grafik 2 - Stres ve Anksiyete Yoğunluk Dağılımı
        st.subheader("😟 Stres ve Anksiyete Yoğunluk Dağılımı")
        st.markdown("Stres ve anksiyete seviyelerinin yoğunluklarını karşılaştıran KDE grafiği:")
        fig2, ax2 = plt.subplots(figsize=(8,5))
        sns.kdeplot(df['Stress Level (1-10)'], label='Stres', fill=True, color='#7E57C2', alpha=0.6, ax=ax2)
        sns.kdeplot(df['Anxiety Level (1-10)'], label='Anksiyete', fill=True, color='#81C784', alpha=0.6, ax=ax2)
        ax2.set_title('Stres ve Anksiyete Seviyelerinin Yoğunluk Dağılımı')
        ax2.set_xlabel('Seviye (1-10)')
        ax2.set_ylabel('Yoğunluk')
        ax2.legend()
        st.pyplot(fig2)

        # Grafik 3 - Fiziksel Aktivite ve Anksiyete
        st.subheader("🏃‍♀️ Fiziksel Aktivite ile Anksiyete Seviyesi")
        st.markdown("Fiziksel aktivite süresine göre anksiyete seviyesi ilişkisini gösteren regresyon grafiği:")
        fig3, ax3 = plt.subplots(figsize=(10,6))
        sns.regplot(x='Physical Activity (hrs/week)', y='Anxiety Level (1-10)', data=df,
                    scatter_kws={'alpha':0.5, 'color':'#7E57C2'},
                    line_kws={'color':'#000000'}, ax=ax3)
        ax3.set_title('Fiziksel Aktivite ve Anksiyete Seviyesi')
        ax3.set_xlabel('Fiziksel Aktivite (saat/hafta)')
        ax3.set_ylabel('Anksiyete Seviyesi (1-10)')
        st.pyplot(fig3)

    else:
        st.info("📎 Veri seti yüklenmedi. Yukarıdan bir dosya seçin.")

    st.markdown("""
    ---
    👨‍💻 **Geliştirici:** Merve Öcal  
    🔗 [GitHub](https://github.com/merveocal) | [LinkedIn](https://www.linkedin.com/in/merve-%C3%B6cal6232)
    """)
