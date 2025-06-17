SMS Spam Classifier
Project Overview
This project is an SMS Spam Classifier built using a Kaggle SMS Spam dataset. It involves data cleaning, exploratory data analysis (EDA), text preprocessing, model building, evaluation, and a user interface to classify SMS as spam or ham.
Features

Data Cleaning: Removed unnecessary columns, renamed columns, encoded the categorical target column, handled missing values, and checked for duplicates.
Exploratory Data Analysis (EDA): Analyzed target column distribution with a pie chart, added features like number of characters, words, and sentences, performed descriptive statistics, and visualized relationships using pair plots, heatmaps, and target-based plots.
Text Preprocessing: Applied lowercasing, tokenization, removal of special characters, stop words, and punctuation, and stemming. Visualized word clouds and most common words for spam and ham SMS.
Feature Engineering: Converted text into numerical vectors using CountVectorizer and TF-IDF Vectorizer.
Model Building: Implemented Gaussian Naive Bayes, Multinomial Naive Bayes, and Bernoulli Naive Bayes models.
Model Evaluation: Achieved accuracies of 0.88 (Gaussian NB), 0.97 (Multinomial NB), and 0.98 (Bernoulli NB), with precisions of 0.54, 1.0, and 0.99 respectively.
User Interface: Developed an interface for users to input SMS and classify it as spam or ham.

Dataset
The dataset used is the SMS Spam Collection Dataset from Kaggle, containing labeled SMS messages as spam or ham.
Installation

Clone the repository:git clone https://github.com/your-username/sms-spam-classifier.git


Install required dependencies:pip install -r requirements.txt


Run the Jupyter notebook or Python script to explore the project.

Dependencies

Python 3.x
Libraries: pandas, numpy, nltk, scikit-learn, matplotlib, seaborn, wordcloud, jupyter

Usage

Open the sms_spam_classifier.ipynb notebook to view data processing, EDA, and model training.
Run the interface.py script to launch the user interface and classify SMS.python interface.py


Enter an SMS in the interface to get a spam/ham prediction.

Results

Gaussian Naive Bayes: Accuracy: 0.88, Precision: 0.54
Multinomial Naive Bayes: Accuracy: 0.97, Precision: 1.0
Bernoulli Naive Bayes: Accuracy: 0.98, Precision: 0.99

Visualizations

Pie chart of target distribution
Pair plots and heatmaps of numerical features
Word clouds and most common words for spam/ham
Target vs. numerical features (characters, words, sentences)

Future Improvements

Experiment with advanced models like SVM or LSTM.
Optimize hyperparameters using GridSearchCV.
Enhance the UI with a web-based deployment using Flask or Streamlit.

License
This project is licensed under the MIT License.
Contact
Feel free to reach out for questions or feedback: [Your Email Address]
