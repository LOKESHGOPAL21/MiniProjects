
# 📊 Customer Churn Prediction and Retention Dashboard

## 🧠 Introduction

This project builds a **Customer Churn Prediction and Retention Dashboard** to identify customers at risk of churning and recommend actionable retention strategies.

* **Dataset**: [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (from Kaggle)
* **Model**: XGBoost Classifier (with hyperparameter tuning)
* **Interface**: Streamlit
* **Visualizations**: Plotly, Seaborn, Matplotlib

🔍 Key Features:

* Predicts churn probability
* Displays churn drivers and retention strategies
* Visual, interactive dashboard for business insights
* Applicable across industries like **telecom**, **e-commerce**, and **SaaS**

---

## 📦 Models & Components

* **🔮 XGBoost Classifier**: Predicts churn probability with tuned hyperparameters
* **💡 Rule-Based Retention System**: Offers strategies like discounts, follow-ups, loyalty rewards
* **📈 Streamlit Dashboard**: Interactive app for real-time predictions and customer engagement
* **📊 Plotly Visualizations**: Insights into churn distribution and feature importance

---

## 📂 Data Collection

* Dataset: `WA_Fn-UseC_-Telco-Customer-Churn.csv` from Kaggle
* **Selected Features**:

  * `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`, `Churn`
* **Preprocessing Steps**:

  * Handled missing values
  * Encoded categorical variables
  * Scaled numerical features
* **Train-Test Split**: 80% training, 20% testing

---

## ⚙️ Model Development

### 3.1 XGBoost Classifier

* Implemented using `xgboost`
* Hyperparameter tuning via `GridSearchCV`

  * Tuned: `max_depth`, `learning_rate`, `n_estimators`
* Evaluated with 5-fold cross-validation (metric: **ROC-AUC**)
* Saved model as `churn_model.pkl`

### 3.2 Rule-Based Retention System

* Implemented in `retention_strategy.py`
* Strategies based on:

  * `Churn probability`
  * `Customer attributes` (e.g., tenure, contract)
* Suggestions: discounts, follow-ups, rewards

### 3.3 Streamlit Dashboard

* Interactive form for customer input
* Real-time predictions using saved model
* Shows:

  * Retention strategies
  * Churn visualizations (via Plotly)

### 3.4 Exploratory Data Analysis (EDA)

* Implemented in `eda.py`
* Tools: `seaborn`, `matplotlib`
* Visualizations include:

  * Churn distribution
  * Correlation heatmap
  * Tenure vs. Churn patterns

---

## 📊 Performance Evaluation

* **Test Set Metrics**:

  * Accuracy: \~0.82
  * Precision: \~0.65
  * Recall: \~0.58
  * ROC-AUC: \~0.77

📌 **Insights**:

* Top churn predictors: `tenure`, `contract type`, `monthly charges`
* Retention strategies help mitigate risk in key customer segments

---

## 🛠️ Installation & Usage

### ✅ Requirements

Install dependencies:

```bash
pip install pandas numpy scikit-learn xgboost joblib streamlit plotly seaborn matplotlib
```

### ▶️ Running the Project

```bash
# Clone the repository
git clone https://github.com/your-username/customer-churn-prediction
cd customer-churn-prediction

# Preprocess data and train model
python preprocess_data.py
python train_model.py

# Launch Streamlit dashboard
streamlit run app.py
```

Access the app at: `http://localhost:8501`

---

## 🚀 Deployment (Render)

1. Push all files to GitHub:

   * `app.py`, `preprocess_data.py`, `train_model.py`, `retention_strategy.py`, `churn_model.pkl`, `preprocessed_telco_data.csv`, `requirements.txt`
2. Create a **Render Web Service**:

   * **Runtime**: Python 3
   * **Build Command**:

     ```bash
     pip install -r requirements.txt
     ```
   * **Start Command**:

     ```bash
     streamlit run app.py 
     ```


