import streamlit as st
import importlib

# Sayfaları tanımla
PAGES = {
    "🏠 Ana Sayfa": "home",
    "📊 Keşifsel Veri Analizi": "eda",
    "🧠 Model Eğitimi": "model",
    "🔍 Tahmin": "prediction"
}

# Sidebar başlığı ve açıklama
st.sidebar.title("📌 Navigasyon Menüsü")
st.sidebar.markdown("Lütfen bir sayfa seçin:")

# Sayfa seçimi
selection = st.sidebar.radio("", list(PAGES.keys()))

# Üst kısım tasarımı
st.markdown("""
    <style>
        .title {
            font-size:40px !important;
            font-weight: bold;
            color: #2E8B57;
            text-align: center;
        }
        .subtitle {
            font-size:20px !important;
            text-align: center;
            color: #6c757d;
        }
        .spacer {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# st.markdown('<div class="title">🧠 Anksiyete Tahmin Uygulaması</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Makine Öğrenmesi ile Anksiyete Riskini Tahmin Edin</div>', unsafe_allow_html=True)
# st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Seçilen sayfayı yükle
page = importlib.import_module(PAGES[selection])
page.app()
