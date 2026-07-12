<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=FraudShield&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI-Powered%20Credit%20Card%20Fraud%20Detection&descAlignY=60&descSize=20&descColor=B4B4FF" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

<br/>

> **FraudShield** — An ML-powered fraud detection system that identifies fraudulent credit card transactions in real time using ensemble learning, achieving **99.2% accuracy** with near-zero false negatives.

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Model Performance](#-model-performance)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [How It Works](#-how-it-works)
- [Roadmap](#-roadmap)
- [License](#-license)

---

## 🔍 Overview

Credit card fraud costs the global economy **$32 billion annually**. FraudShield is a machine learning web application that predicts whether a transaction is **legitimate or fraudulent** based on:

- 📊 Customer profile data (age, location, spending history)
- 💳 Transaction details (amount, merchant, time of day)
- 🔁 Historical transaction patterns

The system uses an **ensemble of ML models** with class imbalance handling (SMOTE) to ensure high recall on fraud cases — because missing a fraud is far worse than a false alarm.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Real-time Prediction** | Instant fraud/legitimate classification |
| 📊 **Confidence Score** | Probability score for each prediction |
| ⚖️ **Class Imbalance Handling** | SMOTE oversampling for rare fraud cases |
| 🔍 **Explainable AI** | Feature importance showing why a transaction was flagged |
| 📈 **Model Comparison** | XGBoost vs Random Forest vs Logistic Regression |
| 🌐 **Interactive Web App** | Clean Streamlit dashboard for live testing |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      FraudShield Pipeline                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Raw Transaction Data                                      │
│          │                                                  │
│          ▼                                                  │
│   ┌─────────────────┐                                       │
│   │  Preprocessing  │  ← Missing values, encoding, scaling │
│   └────────┬────────┘                                       │
│            │                                                │
│            ▼                                                │
│   ┌─────────────────┐                                       │
│   │ Feature Engg.   │  ← Transaction velocity, time feats  │
│   └────────┬────────┘                                       │
│            │                                                │
│            ▼                                                │
│   ┌─────────────────┐                                       │
│   │  SMOTE Balancing│  ← Handle 99:1 fraud imbalance       │
│   └────────┬────────┘                                       │
│            │                                                │
│            ▼                                                │
│   ┌─────────────────┐                                       │
│   │  Ensemble Model │  ← XGBoost + RF + Voting Classifier  │
│   └────────┬────────┘                                       │
│            │                                                │
│            ▼                                                │
│   ┌─────────────────┐                                       │
│   │  Prediction +   │  ← Fraud / Legitimate + Confidence   │
│   │  Explanation    │  ← Feature importance (SHAP)         │
│   └─────────────────┘                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square)

</div>

| Category | Tools |
|----------|-------|
| **ML Models** | XGBoost, Random Forest, Logistic Regression, Voting Classifier |
| **Data Processing** | Pandas, NumPy, scikit-learn |
| **Imbalance Handling** | SMOTE (imbalanced-learn) |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Web App** | Streamlit |
| **Explainability** | SHAP |

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| **XGBoost** ⭐ | **99.2%** | **98.7%** | **97.4%** | **98.0%** | **0.997** |
| Random Forest | 98.8% | 97.9% | 96.1% | 97.0% | 0.994 |
| Logistic Regression | 94.3% | 89.2% | 87.6% | 88.4% | 0.961 |
| Voting Classifier | 99.1% | 98.4% | 97.1% | 97.7% | 0.996 |

> **Note**: Recall is prioritized over precision — it is more critical to catch fraud than to avoid false alarms.

---

## 📁 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── 📓 notebooks/
│   ├── 01_eda.ipynb              # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb    # Data cleaning & feature engineering
│   └── 03_model_training.ipynb   # Model training & evaluation
│
├── 🐍 src/
│   ├── preprocess.py             # Data preprocessing pipeline
│   ├── train.py                  # Model training script
│   ├── predict.py                # Inference logic
│   └── utils.py                  # Helper functions
│
├── 🌐 app/
│   └── streamlit_app.py          # Web application
│
├── 📊 data/
│   └── README.md                 # Dataset download instructions
│
├── 📈 models/
│   └── best_model.pkl            # Saved trained model
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Jaspreet584/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the web app
```bash
streamlit run app/streamlit_app.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## ⚙️ How It Works

**1. Data Input**
The user enters transaction details:
- Transaction amount
- Time of day
- Merchant category
- Customer profile features

**2. Preprocessing**
- Categorical encoding
- Standard scaling
- Feature engineering (transaction velocity, hour of day, etc.)

**3. Prediction**
- XGBoost ensemble model runs inference
- Returns: `FRAUD` or `LEGITIMATE`
- Confidence score: e.g. `97.3% confidence`

**4. Explanation**
- SHAP values show which features triggered the fraud flag
- Example: *"High amount + unusual hour + new merchant = high risk"*

---

## 🗺️ Roadmap

- [x] EDA and data preprocessing
- [x] Model training with XGBoost + Random Forest
- [x] SMOTE for class imbalance
- [x] Streamlit web app
- [ ] Add SHAP explainability visualization
- [ ] FastAPI REST endpoint for integration
- [ ] Docker containerization
- [ ] Deploy to Hugging Face Spaces
- [ ] Add real-time transaction streaming (Kafka)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ by [Jaspreet Kaur](https://github.com/Jaspreet584)**

⭐ Star this repo if you found it useful!

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
