# 💳 FraudShield: AI-Powered Credit Card Fraud Detection System

FraudShield is an interactive, real-time machine learning web application designed to detect and analyze fraudulent credit card transactions. Powered by a Machine Learning model (Random Forest) and built with Streamlit, the application evaluates transaction details and computes the fraud risk level to help protect financial transactions.

## 🚀 Features

- **Real-Time Transaction Analysis**: Enter credit card transaction details and get instant predictions.
- **Risk Level Assessment**: Categorizes transactions into **Low Risk**, **Medium Risk**, or **High Risk** based on probability scores.
- **Visual Metrics Dashboard**: Clean display of transaction statistics and key performance indicators.
- **Interactive UI**: User-friendly sidebar inputs for custom merchant, category, customer profile, and amount variables.
- **Automated Decision System**: Automatically recommends whether to approve or block a transaction.

---

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (Python Web Framework)
- **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/) (Random Forest Classifier)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Model Deserialization**: [Joblib](https://joblib.readthedocs.io/)

---

## 📦 Project Structure

```bash
├── app.py              # Main Streamlit web application
├── fraud_model.pkl     # Pre-trained Random Forest model
├── encoders.pkl        # Label Encoders for categorical inputs
├── requirements.txt    # Python dependencies
└── .gitignore          # Git exclusion rules
```

---

## 💻 Installation & Local Setup

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository
If you haven't already, clone this repository:
```bash
git clone <your-repository-url>
cd frauddetect
```

### 2. Create a Virtual Environment (Recommended)
Create and activate a virtual environment to manage dependencies cleanly:
* **Windows (PowerShell)**:
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Install all required libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```
This will spin up a local development server. A browser tab should open automatically at `http://localhost:8501`.

---

## 📊 How It Works
1. **Input Parameters**: Provide the card number, amount, customer gender, merchant, transaction category, occupation, ZIP code, and local city population via the sidebar.
2. **Feature Mapping**: Categorical variables are mapped using pre-trained label encoders (`encoders.pkl`).
3. **ML Prediction**: The pre-trained Random Forest model evaluates the risk of fraud.
4. **Output Results**: The system outputs a clean risk report displaying the probability of fraud, risk level, and recommended action (Approve/Block).
