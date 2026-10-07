import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import confusion_matrix

st.set_page_config(page_title="UPI Fraud Detection", page_icon="🛡️", layout="centered")

@st.cache_resource
def load_bundle():
    return joblib.load("model (1).pkl")

bundle = load_bundle()
model = bundle["model"]
threshold_table = bundle["threshold_table"]
features = bundle["features"]

st.title("🛡️ UPI Fraud Detection System")
st.caption("ML fraud-risk scoring with business-cost-based threshold tuning")

with st.sidebar:
    st.header("Business costs")
    fn_cost = st.number_input(
        "Cost of missing a fraud (FN)",
        min_value=1.0, value=10.0, step=1.0,
        help="Higher value makes the system more sensitive to fraud."
    )
    fp_cost = st.number_input(
        "Cost of wrongly flagging a genuine transaction (FP)",
        min_value=0.1, value=1.0, step=0.5
    )

# Choose threshold that minimizes cost on the held-out validation set.
cost = threshold_table[:, 3] * fn_cost + threshold_table[:, 2] * fp_cost
best_idx = int(np.argmin(cost))
threshold = float(threshold_table[best_idx, 0])

st.sidebar.metric("Selected threshold", f"{threshold:.2f}")
st.sidebar.caption("Threshold is selected by minimizing FN × FN-cost + FP × FP-cost on validation data.")

with st.form("transaction_form"):
    amount = st.number_input("Transaction Amount", min_value=0.0, value=1500.0, step=100.0)
    tx_type = st.selectbox("Transaction Type", [
        "ATM Withdrawal", "Bill Payment", "POS Payment", "Bank Transfer", "Online Purchase"
    ])
    time = st.number_input("Time of Transaction (0–23)", min_value=0.0, max_value=23.0, value=14.0, step=1.0)
    device = st.selectbox("Device Used", ["Mobile", "Desktop", "Tablet", "Unknown Device"])
    location = st.selectbox("Location", [
        "San Francisco", "New York", "Chicago", "Los Angeles", "Miami",
        "Boston", "Houston", "Seattle"
    ])
    previous_fraud = st.number_input("Previous Fraudulent Transactions", min_value=0, value=0, step=1)
    account_age = st.number_input("Account Age (days)", min_value=0, value=60, step=1)
    tx_24h = st.number_input("Transactions in Last 24H", min_value=0, value=5, step=1)
    payment = st.selectbox("Payment Method", ["UPI", "Credit Card", "Net Banking", "Debit Card", "Invalid Method"])
    submitted = st.form_submit_button("Check Transaction")

if submitted:
    row = pd.DataFrame([{
        "Transaction_Amount": amount,
        "Transaction_Type": tx_type,
        "Time_of_Transaction": time,
        "Device_Used": device,
        "Location": location,
        "Previous_Fraudulent_Transactions": previous_fraud,
        "Account_Age": account_age,
        "Number_of_Transactions_Last_24H": tx_24h,
        "Payment_Method": payment
    }], columns=features)

    probability = float(model.predict_proba(row)[0, 1])
    is_fraud = probability >= threshold

    st.divider()
    st.subheader("Prediction")
    st.metric("Fraud probability", f"{probability:.2%}")
    st.progress(min(max(probability, 0.0), 1.0))

    if is_fraud:
        st.error("🚨 Potential Fraud Detected")
        st.write(f"The score ({probability:.2%}) is above the selected threshold ({threshold:.2%}).")
    else:
        st.success("✅ Transaction Appears Legitimate")
        st.write(f"The score ({probability:.2%}) is below the selected threshold ({threshold:.2%}).")

st.divider()
st.subheader("Model information")
st.write(f"Validation ROC-AUC: **{bundle['auc']:.3f}**")
st.caption(
    "Important: the supplied dataset has very weak predictive signal. "
    "This app demonstrates the ML pipeline and business-cost thresholding, "
    "but the current dataset is not strong enough to support an 85% fraud-capture claim."
)
