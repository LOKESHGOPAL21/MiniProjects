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
