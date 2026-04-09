# 🔎 SemanticRank: Intelligent Search & Answer System

> A production-style semantic search system (Demo) with evaluation and answer extraction.

SemanticRank is an advanced **semantic search and answer retrieval system** that combines Sentence-BERT embeddings with ranking techniques to retrieve, rank, and extract the most relevant answers from a document collection.

The system also evaluates performance against a **BM25 baseline using NDCG@10**, providing measurable improvements in search quality.

---

## 📌 Overview

This project demonstrates a **real-world Information Retrieval (IR) pipeline**:

* Semantic understanding of queries
* Retrieval of relevant documents
* Intelligent ranking
* Answer extraction
* Performance evaluation

It is designed as a **production-style ML system demo**.

---

## 🚀 Features

✅ **Semantic Search (Sentence-BERT)**
→ Understands meaning, not just keywords

✅ **BM25 Baseline Retrieval**
→ Traditional keyword-based ranking

✅ **Learning-to-Rank Model (XGBoost)** *(optional)*
→ Improves ranking using ML

✅ **Answer Extraction**
→ Extracts the most relevant sentence

✅ **Evaluation Metrics (NDCG@10)**
→ Measures ranking quality

✅ **Interactive UI (Streamlit)**
→ Real-time query input and results visualization

---

## 🧠 System Architecture

```
User Query
   ↓
Semantic Search (Sentence-BERT)
   ↓
Top Relevant Documents
   ↓
(Optional) Learning-to-Rank Model
   ↓
Answer Extraction
   ↓
Evaluation (NDCG@10 vs BM25)
```

---

## 📊 Results

| Metric           | Value |
| ---------------- | ----- |
| Semantic NDCG@10 | ~0.85 |
| BM25 NDCG@10     | ~0.58 |
| Improvement      | ~46%  |

👉 Demonstrates clear improvement of **semantic retrieval over keyword-based search**

---

## 🚀 Key Result

Achieved **~46% improvement in NDCG@10 over BM25 baseline** using semantic search.

---

## 🛠️ Tech Stack

### Backend

* Python
* Sentence-Transformers (BERT)
* XGBoost (Learning-to-Rank)
* Rank-BM25
* Scikit-learn
* Pandas, NumPy

### Frontend

* Streamlit

---

## 📂 Project Structure

```
SemanticRank-Search-System/
│
├── app.py
├── test_run.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── bm25.py
│   ├── semantic_search.py
│   ├── evaluation.py
│
├── data/
│   ├── demo_data.csv
```

---

## ⚙️ Installation

### Prerequisites

* Python 3.8+
* pip
* Virtual environment (recommended)

---

### Steps

1. Clone the repository:

```bash
git clone https://github.com/sravyaakyana-prog/semantic-rank-search-system.git
cd semantic-rank-search-system
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python -m streamlit run app.py
```

4. Open in browser:

```
http://localhost:8501
```

---

## ▶️ Usage

```bash
python -m streamlit run app.py
```

---

## 💡 Example Queries

* cell tower
* mobile signal
* machine learning
* birds raised
* internet

---

## 📸 Demo

### 🔹 Main UI

![Main UI](assets/screenshot1.png)

### 🔹 Results & Evaluation

![Results](assets/screenshot2.png)

---

## 🧪 Evaluation

The system evaluates ranking quality using:

* DCG (Discounted Cumulative Gain)
* NDCG@10

Comparison:

* BM25 (baseline)
* Semantic Search (BERT)

---

## 🎯 Key Highlights

✔ Combines semantic search + ranking + evaluation
✔ Implements real-world IR techniques
✔ Demonstrates measurable improvement
✔ Built with scalable ML pipeline design

---

## 🔮 Future Scope

🔥 Hybrid Search (Semantic + ML Ranking)
🔥 Larger datasets (MS MARCO full)
🔥 Transformer-based QA models
🔥 Streamlit Cloud deployment

---

## 👤 Author

**Sravya Akyana**
Machine Learning Enthusiast 🚀

---


