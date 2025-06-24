import streamlit as st
import pandas as pd
import joblib

def app():  # 👈 Bu satırı ekledik
    # Model dosyalarını yükle (dosya yollarını kendine göre değiştir)
    model = joblib.load("C:/Users/EXCALIBUR/streamlit/rf_Grid_models.pkl")
    scaler = joblib.load("C:/Users/EXCALIBUR/streamlit/sele2_scaler.pkl")
    model_features = joblib.load("C:/Users/EXCALIBUR/streamlit/model_features.pkl")

    st.title("🧠 Anksiyete Tahmini")

    # Kullanıcıdan giriş alınacak özellikler:
    inputs = {
        "Age": st.number_input("Age", min_value=0, max_value=64, value=0),
        "Smoking": 1 if st.selectbox("Do you smoke?", ["No", "Yes"]) == "Yes" else 0,
        "Stress Level (1-10)": st.slider("Stress Level (1-10)", min_value=0, max_value=10, value=5),
        "Therapy Sessions (per month)": st.number_input("Therapy Sessions (per month)", min_value=0.0, max_value=8.5, value=0.0),
        "Medication": 1 if st.selectbox("Are you on medication?", ["No", "Yes"]) == "Yes" else 0,
        "Family History of Anxiety": 1 if st.selectbox("Family History of Anxiety?", ["No", "Yes"]) == "Yes" else 0,
        "Sleep Hours": st.number_input("Sleep Hours", min_value=0.0, max_value=10.0, value=0.0),
        "Sleep Category": st.selectbox("Sleep Category", ["Short", "Normal", "Long"]),
        "Physical Activity (hrs/week)": st.number_input("Physical Activity (hrs/week)", min_value=0.0, max_value=8.25, value=0.0),
        "Caffeine Intake (mg/day)": st.number_input("Caffeine Intake (mg/day)", min_value=0, max_value=599, value=000),
        "Diet Quality (1-10)": st.slider("Diet Quality (1-10)", min_value=0, max_value=10, value=0),
        "Alcohol Consumption (drinks/week)": st.number_input("Alcohol Consumption (drinks/week)", min_value=0, max_value=20, value=0),
        "Recent Major Life Event": 1 if st.selectbox("Recent Major Life Event?", ["No", "Yes"]) == "Yes" else 0,
    }

    # Sleep Category encoding
    sleep_cat_map = {"Short": 0, "Normal": 1, "Long": 2}
    inputs["Sleep Category"] = sleep_cat_map[inputs["Sleep Category"]]

    # Girdi dataframe'i oluştur
    input_df = pd.DataFrame([inputs], columns=model_features)

    # Eksik sütunları sıfırla
    for col in model_features:
        if col not in input_df.columns:
            input_df[col] = 0

    # Ölçekleme (sadece sayısal)
    numeric_cols = input_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    # Tahmin butonu
    if st.button("Tahmin Et"):
        proba = model.predict_proba(input_df)[0][1]
        st.success(f"🧾 Anksiyete Pozitif Sınıf Olasılığı: %{proba * 100:.2f}")
