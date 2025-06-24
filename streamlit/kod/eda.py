import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("🔍 Keşifsel Veri Analizi")

    uploaded_file = st.file_uploader("CSV dosyasını yükleyin", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("📄 Veri Önizleme")
        st.dataframe(df.head())

        st.subheader("🔍 Veri Kümesi Genel Bilgisi")
        st.write(f"Veri Kümesi Boyutu: {df.shape[0]} satır, {df.shape[1]} sütun")
        st.write("📌 Veri Türleri:")
        st.write(df.dtypes)

        
        
        st.subheader("📈 Temel İstatistiksel Özellikler")
        st.dataframe(df.describe().T)
        
        
        numeric_cols = df.select_dtypes(include='number').columns
        st.subheader("🔢 Sayısal Değişkenlerin Dağılımı")
        selected_col = st.selectbox("Bir değişken seçin:", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, color='#9575CD', ax=ax)
        ax.set_title(f"{selected_col} Dağılımı")
        st.pyplot(fig)
        
        
        categorical_cols = df.select_dtypes(include='object').columns
        st.subheader("🗂️ Kategorik Değişkenlerin Dağılımı")
        selected_cat = st.selectbox("Bir kategorik değişken seçin:", categorical_cols)
        fig2, ax2 = plt.subplots()
        df[selected_cat].value_counts().plot(kind='bar', color='#81C784', ax=ax2)
        ax2.set_title(f"{selected_cat} Sıklığı")
        st.pyplot(fig2)
        
        
        st.subheader("🔗 Korelasyon Matrisi")
        corr = df.corr(numeric_only=True)

        fig3, ax3 = plt.subplots(figsize=(20, 16))
        sns.heatmap(
            corr,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
            square=False,
            linewidths=1,
            linecolor='white',
            cbar_kws={"shrink": 0.8},
            annot_kws={"size": 12}
        )
        ax3.set_title("Aykırı Değerler Temizlendikten Sonra Korelasyon Matrisi", fontsize=16)
        plt.xticks(rotation=45, ha="right", fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        st.pyplot(fig3)

        
        
        st.markdown("""
        ### 📌 İlk Gözlemler:
        - Kafein tüketimi ile anksiyete arasında pozitif bir ilişki görülüyor.
        - Fiziksel aktivite arttıkça anksiyete seviyelerinde düşüş gözlemleniyor.
        - Stres seviyesi yüksek olan bireylerde anksiyete düzeyi de yüksek.
        """)



