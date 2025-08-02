import xgboost as xgb
import matplotlib.pyplot as plt
import joblib
import pandas as pd


def plot_feature_importance(model_path, feature_names):
    # Load model
    model = joblib.load(model_path)
    
    # Plot feature importance
    plt.figure(figsize=(10, 6))
    xgb.plot_importance(model, max_num_features=10)
    plt.title('Feature Importance')
    plt.savefig('feature_importance.png')
    plt.close()


file_path = "preprocessed_telecom_churn_data.csv"   
df = pd.read_csv(file_path)
feature_names = df.drop('Churn', axis=1).columns
plot_feature_importance('churn_model.pkl', feature_names)
print("Feature importance plot saved as 'feature_importance.png'")