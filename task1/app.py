import streamlit as st
import pandas as pd
import joblib
import time
from datetime import datetime

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="FraudShield",
    page_icon="💳",
    layout="wide"
)

# ---------------- LOAD MODEL & ENCODERS ---------------- #

try:
    model = joblib.load("fraud_model.pkl")
    encoders = joblib.load("encoders.pkl")
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# ---------------- HEADER ---------------- #

st.title("💳 FraudShield")
st.subheader("AI-Powered Credit Card Fraud Detection System")

st.success("✅ APP LOADED")

st.markdown("""
This system analyzes transaction details and predicts whether a
credit card transaction is **Legitimate** or **Fraudulent**.
""")

st.markdown("---")

# ---------------- SIDEBAR INPUTS ---------------- #

st.sidebar.header("📝 Transaction Details")

cc_num = st.sidebar.text_input(
    "Credit Card Number",
    "1234567890123456"
)

amount = st.sidebar.number_input(
    "Transaction Amount ($)",
    min_value=0.0,
    value=100.0,
    step=10.0
)

gender = st.sidebar.selectbox(
    "Customer Gender",
    list(encoders['gender'].classes_)
)

merchant = st.sidebar.selectbox(
    "Merchant",
    list(encoders['merchant'].classes_)
)

category = st.sidebar.selectbox(
    "Transaction Category",
    list(encoders['category'].classes_)
)

occupation = st.sidebar.selectbox(
    "Occupation",
    list(encoders['job'].classes_)
)

zip_code = st.sidebar.number_input(
    "ZIP Code",
    min_value=10000,
    value=10001
)

city_pop = st.sidebar.number_input(
    "City Population",
    min_value=1,
    value=50000
)

transaction_hour = st.sidebar.slider(
    "Transaction Hour",
    0,
    23,
    datetime.now().hour
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Select realistic transaction details for prediction."
)

# ---------------- DISPLAY METRICS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Transaction Amount",
        f"${amount:,.2f}"
    )

with col2:
    st.metric(
        "Transaction Hour",
        f"{transaction_hour}:00"
    )

with col3:
    st.metric(
        "City Population",
        f"{city_pop:,}"
    )

st.markdown("---")

# ---------------- PREDICTION ---------------- #

if st.button("🔍 Analyze Transaction"):

    try:

        merchant_encoded = encoders['merchant'].transform([merchant])[0]
        category_encoded = encoders['category'].transform([category])[0]
        gender_encoded = encoders['gender'].transform([gender])[0]
        job_encoded = encoders['job'].transform([occupation])[0]

        unix_time = int(time.time())

        # Default coordinates (same values every time)
        customer_lat = 40.7128
        customer_long = -74.0060

        merchant_lat = 40.7130
        merchant_long = -74.0065

        input_df = pd.DataFrame([[
            int(cc_num),
            merchant_encoded,
            category_encoded,
            amount,
            gender_encoded,
            zip_code,
            customer_lat,
            customer_long,
            city_pop,
            job_encoded,
            unix_time,
            merchant_lat,
            merchant_long
        ]], columns=[
            'cc_num',
            'merchant',
            'category',
            'amt',
            'gender',
            'zip',
            'lat',
            'long',
            'city_pop',
            'job',
            'unix_time',
            'merch_lat',
            'merch_long'
        ])

        with st.spinner("Analyzing transaction..."):
            time.sleep(2)

        prediction = model.predict(input_df)[0]

        try:
            fraud_probability = model.predict_proba(input_df)[0][1]
        except:
            fraud_probability = 0.0

        st.subheader("📊 Prediction Report")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Fraud Probability",
                f"{fraud_probability * 100:.2f}%"
            )

        with c2:

            if fraud_probability >= 0.80:
                risk = "🔴 High Risk"
            elif fraud_probability >= 0.40:
                risk = "🟡 Medium Risk"
            else:
                risk = "🟢 Low Risk"

            st.metric("Risk Level", risk)

        with c3:
            decision = (
                "❌ Blocked"
                if prediction == 1
                else "✅ Approved"
            )

            st.metric("Decision", decision)

        st.progress(int(fraud_probability * 100))

        if prediction == 1:
            st.error(
                "⚠ Fraudulent Transaction Detected"
            )

            st.warning(
                "Recommendation: Verify customer before approving."
            )

        else:
            st.success(
                "✅ Legitimate Transaction"
            )

            st.info(
                "Recommendation: Transaction can be approved."
            )

        st.markdown("---")

        st.subheader("🧾 Transaction Summary")

        summary = pd.DataFrame({
            "Field": [
                "Card Number",
                "Merchant",
                "Category",
                "Amount",
                "Gender",
                "Occupation",
                "ZIP Code",
                "City Population"
            ],
            "Value": [
                cc_num,
                merchant,
                category,
                f"${amount:,.2f}",
                gender,
                occupation,
                zip_code,
                city_pop
            ]
        })

        st.table(summary)

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# ---------------- FOOTER ---------------- #

st.markdown("---")
st.caption(
    "FraudShield © 2026 | Random Forest + Streamlit"
)