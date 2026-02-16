# 📘 Comparative Sentiment Analysis  
## Classical Machine Learning vs Deep Learning Architectures

---

## 📌 1. Introduction

Sentiment Analysis is a Natural Language Processing (NLP) task that classifies text based on emotional tone — typically **positive** or **negative**.

This project compares:

### 🔹 Classical Machine Learning
- **TF-IDF + Logistic Regression**

### 🔹 Deep Learning
- **Word2Vec + 2-Layer LSTM**
- **Word2Vec + 2-Layer Bidirectional LSTM (BiLSTM)**

### 🎯 Objective
To evaluate whether deep contextual sequence modeling significantly outperforms traditional sparse vector approaches on a structured sentiment dataset.

---

## 📂 2. Dataset Description

**Dataset Used:** IMDb 50K Movie Reviews (Kaggle)

### Dataset Properties
- 50,000 total reviews
- Binary sentiment labels (Positive / Negative)
- Balanced dataset:
  - 25,000 Positive
  - 25,000 Negative

Each record contains:
- Review text
- Sentiment label

---

## 🧹 3. Data Preprocessing Pipeline

A custom preprocessing pipeline was implemented:

1. Lowercasing  
2. HTML tag removal  
3. Special character removal  
4. Tokenization  
5. Stopword removal (negations retained: *not, no, never*)  
6. Rare word filtering (min frequency = 5)

### Vocabulary Statistics
- Original vocabulary size: ~99,265  
- Filtered vocabulary size: ~39,129  

### Benefits
- Cleaner tokens  
- Reduced noise  
- Better generalization  
- Improved computational efficiency  

---

## 📊 4. Baseline Model — TF-IDF + Logistic Regression

### Feature Engineering

TF-IDF formula:

\[
TF\text{-}IDF = TF \times \log\left(\frac{N}{df}\right)
\]

Where:
- **TF** = Term Frequency  
- **df** = Document Frequency  
- **N** = Total number of documents  

### Vectorization Parameters
- `max_features = 10000`
- `min_df = 5`

### Model
- Logistic Regression
- Linear classifier
- Optimized via Maximum Likelihood
- Evaluated using **5-fold Stratified Cross Validation**

### 📈 Baseline Performance
- Accuracy: ~89%
- F1 Score: ~0.89

### 🔎 Observation
Linear models perform competitively on structured sentiment datasets.

---

## 🧠 5. Word2Vec Embedding Training

Instead of sparse TF-IDF vectors, dense embeddings were learned using:

**Word2Vec (Skip-gram architecture)**

### Parameters
- `vector_size = 100`
- `window = 5`
- `min_count = 5`
- `sg = 1` (Skip-gram)

### Example Learned Semantics
- *good* → similar to *great, decent*
- *bad* → similar to *terrible, awful*

⚠ Important Insight:  
Word2Vec captures **contextual similarity**, not sentiment polarity directly.

---

## 🤖 6. Deep Learning Setup

All deep models used:

- Embedding layer initialized with Word2Vec
- Sequence length = 300
- Trainable embeddings
- Adam optimizer
- Binary cross-entropy loss
- Early stopping

### Data Split
- 80% Training
- 10% Validation
- 10% Test

---

## 🔹 7. Model 1 — 2-Layer LSTM

### Architecture


Embedding
↓
LSTM(128)
↓
Dropout
↓
LSTM(64)
↓
Dropout
↓
Dense(1, sigmoid)


### 📊 Results
- Accuracy: **89.74%**
- F1 Score: **0.899**

Confusion Matrix:
- False Positives: 264
- False Negatives: 249

### 🔎 Observation
Stacking LSTM layers increases abstraction but does not drastically outperform the baseline.

---

## 🔹 8. Model 2 — 2-Layer Bidirectional LSTM (Best Model)

### Architecture


Embedding
↓
BiLSTM(128)
↓
Dropout
↓
BiLSTM(64)
↓
Dropout
↓
Dense(1, sigmoid)


### 📊 Results
- Accuracy: **90.6%**
- Precision: **0.907**
- Recall: **0.907**
- F1 Score: **0.907**

### Confusion Matrix

|              | Pred Neg | Pred Pos |
|--------------|----------|----------|
| Actual Neg   | 2227     | 235      |
| Actual Pos   | 235      | 2303     |

Balanced misclassification across classes.

---

## 📊 9. Comparative Analysis

| Model | Accuracy | F1 Score |
|--------|----------|----------|
| TF-IDF + Logistic Regression | 0.89 | 0.89 |
| 2-Layer LSTM | 0.897 | 0.899 |
| ⭐ 2-Layer BiLSTM | **0.906** | **0.907** |

### 🔎 Key Insights
- Classical models remain highly competitive.
- Deep learning improves performance modestly.
- Bidirectional modeling provides measurable gains.
- Contextual modeling improves negation handling.
- Improvement from baseline to best model: ~1.6%.

---

## 🎓 10. Key Learnings

- Sparse representations (TF-IDF) are strong for structured datasets.
- Word2Vec embeddings improve semantic representation.
- Bidirectional context improves sentiment classification.
- Depth alone does not guarantee major improvements.
- Evaluation must include precision, recall, and F1-score — not just accuracy.

---

## ⚠ 11. Limitations

- IMDb dataset is relatively clean.
- Gains may be larger on noisier datasets.
- No attention mechanism implemented.
- No hyperparameter grid search performed.

---

## 🚀 12. Future Improvements

- Add Attention Mechanism
- Try GRU
- Use GloVe embeddings
- Implement Transformer-based models (BERT)
- Perform hyperparameter tuning
- Use learning rate schedulers

---

## 🏁 13. Conclusion

This project demonstrates that while classical machine learning methods provide strong baselines in sentiment classification, deep learning models — particularly stacked Bidirectional LSTMs — achieve improved performance by capturing long-range contextual dependencies.

However, improvements are incremental rather than dramatic, highlighting that model selection should consider dataset characteristics and computational trade-offs.

---

## 💡 Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- Gensim
- TensorFlow / Keras
- Matplotlib / Seaborn

---

## 👨‍💻 Author

Lokesh Gopal Meka  
Aspiring Machine Learning Engineer