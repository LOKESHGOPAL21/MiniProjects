import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(file_path):
  df = pd.read_csv(file_path)

  # target variable churn distribution
  plt.figure(figsize=(12,6))
  sns.countplot(x='Churn',data=df)
  plt.title("Churn distribution")
  plt.savefig('Churn_distibution.png')
  plt.close()

  # correlation between the columns of the dataframe
  plt.figure(figsize=(12,6))
  sns.heatmap(df.corr(),annot = True,cmap = 'coolwarm',fmt = '.2f')
  plt.title("Correlation between the columns")
  plt.savefig('correlation_heatmap.png')
  plt.close()


  # tenure vs churn 
  plt.figure(figsize=(8, 6))
  sns.boxplot(x='Churn', y='tenure', data=df)
  plt.title('Tenure vs Churn')
  plt.savefig('tenure_vs_churn.png')
  plt.close()


file_path = "preprocessed_telecom_churn_data.csv"
perform_eda(file_path)
print("EDA plots are saved as : Churn_distibution.png,correlation_heatmap.png,tenure_vs_churn.png")