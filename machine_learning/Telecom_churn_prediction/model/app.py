import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
from get_retention_strategy import get_retention_strategy

# Set page configuration
st.set_page_config(page_title="Customer Churn Prediction Dashboard", layout="wide")

# Load model and data
model = joblib.load('churn_model.pkl')
df = pd.read_csv('preprocessed_telecom_churn_data.csv')

# Title
st.title("Customer Churn Prediction Dashboard")

# Sidebar for customer input
st.sidebar.header("Enter Customer Data")
def get_customer_input():
    customer = {
        'gender': st.sidebar.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female"),
        'SeniorCitizen': st.sidebar.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
        'Partner': st.sidebar.selectbox("Partner", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
        'Dependents': st.sidebar.selectbox("Dependents", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
        'tenure': st.sidebar.slider("Tenure (months)", 0.0, 72.0, 12.0),
        'PhoneService': st.sidebar.selectbox("Phone Service", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
        'MultipleLines': st.sidebar.selectbox("Multiple Lines", [0, 1, 2], format_func=lambda x: ["No phone service", "No", "Yes"][x]),
        'InternetService': st.sidebar.selectbox("Internet Service", [0, 1, 2], format_func=lambda x: ["DSL", "Fiber optic", "No"][x]),
        'OnlineSecurity': st.sidebar.selectbox("Online Security", [0, 1, 2], format_func=lambda x: ["No", "Yes", "No internet service"][x]),
        'OnlineBackup': st.sidebar.selectbox("Online Backup", [0, 1, 2], format_func=lambda x: ["No", "Yes", "No internet service"][x]),
        'DeviceProtection': st.sidebar.selectbox("Device Protection", [0, 1, 2], format_func=lambda x: ["No", "Yes", "No internet service"][x]),
        'TechSupport': st.sidebar.selectbox("Tech Support", [0, 1, 2], format_func=lambda x: ["No", "Yes", "No internet service"][x]),
        'StreamingTV': st.sidebar.selectbox("Streaming TV", [0, 1, 2], format_func=lambda x: ["No", "Yes", "No internet service"][x]),
        'StreamingMovies': st.sidebar.selectbox("Streaming Movies", [0, 1, 2], format_func=lambda x: ["No", "Yes", "No internet service"][x]),
        'Contract': st.sidebar.selectbox("Contract", [0, 1, 2], format_func=lambda x: ["Month-to-month", "One year", "Two year"][x]),
        'PaperlessBilling': st.sidebar.selectbox("Paperless Billing", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
        'PaymentMethod': st.sidebar.selectbox("Payment Method", [0, 1, 2, 3], format_func=lambda x: ["Electronic check", "Mailed check", "Bank transfer", "Credit card"][x]),
        'MonthlyCharges': st.sidebar.slider("Monthly Charges ($)", 0.0, 120.0, 50.0),
        'TotalCharges': st.sidebar.slider("Total Charges ($)", 0.0, 8000.0, 1000.0)
    }
    return pd.DataFrame([customer])

# Main content
col1, col2 = st.columns(2)

# Left column: Prediction and Retention Strategies
with col1:
    st.header("Predict Churn")
    customer_data = get_customer_input()
    if st.button("Predict"):
        churn_prob = model.predict_proba(customer_data)[:, 1][0]
        strategies = get_retention_strategy(churn_prob, customer_data.iloc[0].to_dict())
        st.subheader("Prediction Results")
        st.write(f"**Churn Probability**: {churn_prob:.2%}")
        st.write("**Retention Strategies**:")
        for strategy in strategies:
            st.write(f"- {strategy}")

# Right column: Visualizations
with col2:
    st.header("Churn Insights")
    
    # Churn Distribution
    churn_counts = df['Churn'].value_counts().reset_index()
    churn_counts.columns = ['Churn', 'Count']
    churn_counts['Churn'] = churn_counts['Churn'].map({0: 'No', 1: 'Yes'})
    fig1 = px.bar(churn_counts, x='Churn', y='Count', title="Churn Distribution")
    st.plotly_chart(fig1)
    
    # Feature Importance
    importance = model.feature_importances_
    feature_names = df.drop('Churn', axis=1).columns
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance})
    importance_df = importance_df.sort_values('Importance', ascending=False).head(10)
    fig2 = px.bar(importance_df, x='Importance', y='Feature', title="Top 10 Feature Importance")
    st.plotly_chart(fig2)

# Customer Data Table
st.header("Customer Data Overview")
st.dataframe(df.head(10))  # Display first 10 rows