import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(file_path):

  # load the telecom churn dataset
  df = pd.read_csv(file_path)

  # drop customer id columns from the dataset
  df = df.drop('customerID',axis=1)

  # separate categorical and numerical columns
  categorical_columns = df.select_dtypes(include=['object'])
  numerical_columns = df.select_dtypes(include=['int64','float64'])


  # encode categorical Columns:
  le = LabelEncoder()
  for cat in categorical_columns:
      df[cat] = le.fit_transform(df[cat])

  # standardize the numerical columns
  scaler = StandardScaler()
  df[numerical_columns.columns] = scaler.fit_transform(df[numerical_columns.columns])

  df.to_csv('preprocessed_telecom_churn_data.csv',index=False)
  return df


filepath = "telecom_churn_dataset.csv"
df = preprocess_data(filepath)
print("Preprocessed Data is saved as 'preprocessed_telecom_churn_data.csv")