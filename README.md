# 🛡️ UPI Fraud Detection System

An ML-based UPI transaction fraud detection system that estimates fraud risk and uses **business-cost-based threshold tuning** to make fraud decisions.

## 🚀 Live Demo

🔗 **Streamlit App:** Add your deployed Streamlit URL here

---

## 📌 Overview

Financial fraud detection is an **imbalanced classification problem**, where fraudulent transactions are much less common than legitimate transactions.

A model that focuses only on accuracy can be misleading. For example, predicting every transaction as legitimate could produce high accuracy while detecting almost no fraud.

This project focuses on:

- Fraud probability estimation
- Imbalanced classification
- Precision and recall
- False-positive and false-negative costs
- Business-cost-based threshold selection
- Interactive Streamlit deployment

---

## 🧠 Project Workflow

```text
Transaction Input
       ↓
Data Preprocessing
       ↓
Machine Learning Model
       ↓
Fraud Probability
       ↓
Business Cost Evaluation
       ↓

⚙️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Random Forest
GitHub
Streamlit Cloud
📊 Dataset

The project uses a UPI transaction dataset containing features such as:

Transaction ID
User ID
Transaction Amount
Transaction Type
Time of Transaction
Device Used
Location
Previous Fraudulent Transactions
Account Age
Number of Transactions in Last 24 Hours
Payment Method
Fraudulent Label

The target variable is:

Fraudulent

where:

0 → Legitimate
1 → Fraudulent
⚖️ Handling Imbalanced Data

Fraudulent transactions represent a smaller portion of the dataset than legitimate transactions.

Therefore, accuracy alone is not used as the primary evaluation metric.

The project considers:

Fraud Recall
Precision
False Positive Rate
ROC-AUC
Average Precision
Confusion Matrix

The Random Forest model uses class balancing to give more importance to the minority fraud class.

🎯 Business-Cost-Based Thresholding

Instead of automatically using:

Probability ≥ 0.50 → Fraud

the system evaluates different probability thresholds.

For example:

Probability ≥ 0.30 → Potential Fraud
Probability < 0.30 → Legitimate

The best threshold depends on the business cost of:

False Negative

A fraudulent transaction is allowed through.

This can result in financial loss.

False Positive

A legitimate transaction is incorrectly flagged.

This can result in unnecessary reviews or customer friction.

The application therefore allows the decision threshold to be selected based on these relative costs.

🖥️ Streamlit Application

The application provides an interactive interface where users can enter transaction information and receive:

Fraud probability
Risk level
Decision threshold
Fraud/legitimate prediction
Business-cost information

Example:

🚨 Potential Fraud Detected

Fraud Risk Score: 78.4%
Decision Threshold: 35%

Risk Level: HIGH

or:

✅ Transaction Appears Legitimate

Fraud Risk Score: 12.7%
Decision Threshold: 35%

Risk Level: LOW
📈 Model Performance

The current dataset has relatively weak predictive signal.

Validation performance:

ROC-AUC ≈ 0.514

This means the current dataset/model combination has limited ability to distinguish fraudulent transactions from legitimate ones.

This project therefore demonstrates the fraud-detection pipeline and business-cost-based thresholding methodology, rather than claiming production-level fraud detection performance.

No artificial performance claims are made from this dataset.

🧪 Test Transactions
🚨 Fraud Case — T7
Transaction Amount: ₹544.81
Transaction Type: Bill Payment
Time: 02:00
Device: Tablet
Location: Boston
Previous Fraudulent Transactions: 3
Account Age: 6
Transactions Last 24H: 9
Payment Method: UPI

Actual Dataset Label: Fraudulent
🚨 Fraud Case — T28
Transaction Amount: ₹4519.04
Transaction Type: Bill Payment
Time: 13:00
Device: Tablet
Location: Boston
Previous Fraudulent Transactions: 0
Account Age: 81
Transactions Last 24H: 10
Payment Method: Credit Card

Actual Dataset Label: Fraudulent
🚨 Fraud Case — T44
Transaction Amount: ₹4413.05
Transaction Type: Bank Transfer
Time: 21:00
Device: Desktop
Location: Boston
Previous Fraudulent Transactions: 4
Account Age: 46
Transactions Last 24H: 11
Payment Method: Credit Card

Actual Dataset Label: Fraudulent
✅ Example Legitimate Transaction — T1
Transaction Amount: ₹1292.76
Transaction Type: ATM Withdrawal
Time: 16:00
Device: Tablet
Location: San Francisco
Previous Fraudulent Transactions: 0
Account Age: 119
Transactions Last 24H: 13
Payment Method: Debit Card

Actual Dataset Label: Legitimate
📁 Project Structure
upi-fraud-detection/
│
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
🔧 Installation

Clone the repository:

git clone https://github.com/anujkumardubey152-bot/upi-fraud-detection2.git
cd upi-fraud-detection2

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

The application will open in your browser.

📦 Requirements
streamlit
pandas
numpy
scikit-learn
joblib
☁️ Streamlit Cloud Deployment
Push the project to GitHub.
Open Streamlit Community Cloud.
Select the GitHub repository.
Select the main branch.
Set the main file to:
app.py
Deploy the application.

Make sure these files are in the same directory:

app.py
model.pkl
requirements.txt
🔮 Future Improvements

The project can be improved by:

Using a dataset with stronger behavioral fraud signals
Feature engineering from transaction history
Time-based fraud patterns
User spending behavior analysis
Anomaly detection
XGBoost / LightGBM models
Precision-Recall optimization
Cost-sensitive learning
SHAP-based explainability
Real-time fraud monitoring
Model drift detection
API deployment
Database integration
🎓 Key ML Concepts Demonstrated

This project demonstrates practical understanding of:

Supervised Machine Learning
Binary Classification
Imbalanced Classification
Random Forest
Probability-Based Prediction
Precision
Recall
ROC-AUC
False Positives
False Negatives
Decision Threshold Optimization
Business Cost Optimization
Model Deployment
Streamlit
👨‍💻 Author

Anuj Kumar Dubey

B.Tech CSE Student
Interested in AI/ML, Generative AI, LLMs, RAG and MLOps.

GitHub:
https://github.com/anujkumardubey152-bot

LinkedIn:
https://www.linkedin.com/in/anuj-kumar-dubey-58043b377/

⭐ Note

This project is intended for educational and demonstration purposes.

The current dataset has weak predictive signal, so the model should not be considered suitable for real-world financial fraud prevention without further data collection, feature engineering, validation and testing.




Optimized Decision Threshold
       ↓
Fraud / Legitimate Decision
