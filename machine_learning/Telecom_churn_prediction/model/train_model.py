import xgboost as xgb
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score,
    f1_score,
    confusion_matrix,
    classification_report
)
import joblib


def train_model(file_path):
  df = pd.read_csv(file_path)

  # split the dataset feature and target
  X = df.drop('Churn',axis=1)
  y = df['Churn']

  # split dataset into train and test
  X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

  # train xgboost model
  base_model = xgb.XGBClassifier(use_label_encoder=False,eval_metrics='logloss')

  param_grid = {
      'max_depth':[3,5,7],
      'learning_rate':[0.01,0.1,0.3],
      'n_estimators':[100,200]
  }

  # perfomring  gris search sv for hyperparameter tuning
  grid_search = GridSearchCV(estimator=base_model,param_grid=param_grid,
                             cv = 5,scoring='roc_auc',n_jobs=1,verbose=1)
  grid_search.fit(X_train,y_train) 
 
  # get the best model
  best_model = grid_search.best_estimator_

  # Evaluate the model 
  y_train_pred = best_model.predict(X_train)

   # Evaluate model on training set
  y_train_pred = best_model.predict(X_train)
  train_metrics = {
        'accuracy': accuracy_score(y_train, y_train_pred),
        'precision': precision_score(y_train, y_train_pred),
        'recall': recall_score(y_train, y_train_pred),
        'roc_auc': roc_auc_score(y_train, y_train_pred)
  }
    
    # Evaluate model on test set
  y_pred = best_model.predict(X_test)
  test_metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred)
  }
  print(f"Test Accuracy: {test_metrics['accuracy']:.2f}")
  print(f"Test Precision: {test_metrics['precision']:.2f}")
  print(f"Test Recall: {test_metrics['recall']:.2f}")
  print(f"Test ROC-AUC: {test_metrics['roc_auc']:.2f}")
    
    # Save model
  joblib.dump(best_model, 'churn_model.pkl')
    
  return best_model

file_path = "preprocessed_telecom_churn_data.csv"
model = train_model(file_path)
print("Model saved as 'churn_model.pkl'")


model = train_model(file_path)
print("Model saved as 'churn_model.pkl'")
