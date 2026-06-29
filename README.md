# 🚀 SemanticRank AI — Intelligent Semantic Search System

SemanticRank AI is a full-stack AI-powered semantic search engine that combines **Sentence-BERT embeddings**, **FAISS vector search**, **BM25 retrieval**, **Hybrid Ranking**, and **Evidence-based Answer Extraction** to retrieve highly relevant documents from natural language queries.

The project demonstrates modern **Information Retrieval (IR)**, **Machine Learning**, and **Full-Stack Web Development** with a production-ready cloud deployment.

---

# 🌐 Live Demo

## 🖥️ Frontend (Vercel)

https://semantic-rank-search-system.vercel.app

---

## ⚙️ Backend API (Render)

**API**

https://semantic-rank-search-system-backend.onrender.com

**Health Check**

https://semantic-rank-search-system-backend.onrender.com

**Evaluation API**

https://semantic-rank-search-system-backend.onrender.com/api/evaluate

---

## 🧠 ML Service (Render)

https://semantic-rank-search-system-m.onrender.com

---

# 📂 GitHub Repository

https://github.com/sravyaakyana-prog/Semantic-rank-search-system

---

# ✨ Features

* 🔍 AI-powered Semantic Search
* 🧠 Sentence-BERT Embeddings
* ⚡ FAISS Vector Similarity Search
* 📚 BM25 Keyword Retrieval
* 🤝 Hybrid Ranking
* 🎯 Cross-Encoder Re-ranking (with automatic fallback)
* 📄 Evidence-based Answer Extraction
* 📈 Query Expansion
* 📊 Retrieval Evaluation Dashboard
* 🔐 JWT Authentication
* 👤 User Registration & Login
* 📝 Search History using MongoDB Atlas
* ☁️ Cloud Deployment (Vercel + Render)
* 🐳 Dockerized ML Service
* 🎨 Modern SaaS-inspired UI
* 📱 Fully Responsive Design

---

# 🏗️ System Architecture

```text
                    React + Vite (Frontend)
                              │
                              ▼
                    Node.js + Express API
                              │
             ┌────────────────┴─────────────────┐
             ▼                                  ▼
      MongoDB Atlas                     FastAPI ML Service
                                                │
           ┌────────────────────────────────────┐
           ▼                                    ▼
   Sentence-BERT                         BM25 Retrieval
           │                                    │
           └──────────── Hybrid Ranking ────────┘
                          │
                          ▼
                Cross-Encoder Re-ranking
                          │
                          ▼
                Evidence-based Answer
                          │
                          ▼
                     Search Results
```

---

# ⚙️ Tech Stack

## Frontend

* React
* Vite
* Tailwind CSS
* Axios
* React Router DOM

---

## Backend

* Node.js
* Express.js
* JWT Authentication
* MongoDB Atlas
* Mongoose

---

## Machine Learning

* FastAPI
* Sentence Transformers (SBERT)
* FAISS
* BM25
* NumPy
* Pandas
* Scikit-Learn
* NLTK

---

## Deployment

* Vercel
* Render
* Docker
* MongoDB Atlas

---

# 📂 Project Structure

```text
SemanticRank-Search-System
│
├── frontend/
├── backend/
├── ml service/
├── Screenshots/
│   ├── Login.png
│   ├── Signup.png
│   ├── home.png
│   ├── Search_results.png
│   ├── ranked_evidence.png
│   └── analytics.png
│
└── README.md
```

---

# 🧠 Semantic Search Pipeline

```text
User Query
      │
      ▼
Query Expansion
      │
      ▼
Sentence-BERT Embedding
      │
      ▼
FAISS Vector Search
      │
      ▼
BM25 Retrieval
      │
      ▼
Hybrid Ranking
      │
      ▼
Cross-Encoder Re-ranking
      │
      ▼
Evidence-based Answer Extraction
      │
      ▼
Top Ranked Results
```

---

# 📊 Retrieval Performance

| Metric            | Score |
| ----------------- | ----: |
| BM25 NDCG@10      | 0.612 |
| Semantic NDCG@10  | 0.744 |
| Hybrid NDCG@10    | 0.821 |
| Re-ranker NDCG@10 | 0.867 |
| Precision@10      |  0.78 |
| Recall@10         |  0.71 |
| MAP               |  0.79 |
| MRR               |  0.84 |
| Documents Indexed |  5183 |

---

# 📸 Screenshots

## 🔐 Login

Secure JWT-based user authentication.

![Login](Screenshots/Login.png)

---

## 📝 User Registration

Create a new account with MongoDB-backed authentication.

![Signup](Screenshots/Signup.png)

---

## 🏠 Home Page

Modern semantic search interface with recent searches and responsive design.

![Home](Screenshots/home.png)

---

## 🔍 Semantic Search Results

Displays the AI-generated answer, expanded query, latency, confidence score, and search statistics.

![Search Results](Screenshots/Search_results.png)

---

## 📚 Ranked Evidence

Top-ranked evidence retrieved using Semantic Search, BM25, Hybrid Ranking, and Cross-Encoder Re-ranking.

![Ranked Evidence](Screenshots/ranked_evidence.png)

---

## 📊 Retrieval Evaluation Dashboard

Performance comparison of BM25, Semantic Search, Hybrid Search, and Re-ranking.

![Analytics](Screenshots/analytics.png)

---

# 📈 Evaluation API

**Endpoint**

```
GET /api/evaluate
```

Example Response

```json
{
  "BM25_NDCG@10": 0.612,
  "Semantic_NDCG@10": 0.744,
  "Hybrid_NDCG@10": 0.821,
  "Reranker_NDCG@10": 0.867,
  "Improvement_over_BM25_%": 34.15,
  "Precision@10": 0.78,
  "Recall@10": 0.71,
  "MRR": 0.84,
  "MAP": 0.79,
  "queries_evaluated": 100
}
```

---

# 🚀 Running Locally

## Clone Repository

```bash
git clone https://github.com/sravyaakyana-prog/Semantic-rank-search-system.git

cd Semantic-rank-search-system
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Runs at:

```
http://localhost:5173
```

---

## Backend

```bash
cd backend

npm install

npm run dev
```

Runs at:

```
http://localhost:5000
```

---

## ML Service

```bash
cd "ml service"

pip install -r requirements.txt

python main.py
```

Runs at:

```
http://localhost:8000
```

---

# 🔑 Environment Variables

## Frontend (.env)

```env
VITE_API_URL=https://semantic-rank-search-system-backend.onrender.com
```

---

## Backend (.env)

```env
PORT=5000

MONGO_URI=YOUR_MONGODB_ATLAS_URI

JWT_SECRET=YOUR_SECRET_KEY

ML_SERVICE=https://semantic-rank-search-system-m.onrender.com
```

---

## ML Service

No additional environment variables are required.

---

# ☁️ Deployment

| Component  | Platform      |
| ---------- | ------------- |
| Frontend   | Vercel        |
| Backend    | Render        |
| ML Service | Render        |
| Database   | MongoDB Atlas |

---

# 🎯 Future Improvements

* Learning-to-Rank (LTR)
* Personalized Search
* Voice Search
* PDF Semantic Search
* Multi-language Semantic Retrieval
* Vector Database Integration (Milvus / Pinecone)
* Streaming AI Responses

---

# 👨‍💻 Author

**Sravya Akyana**

**GitHub:** https://github.com/sravyaakyana-prog


---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

# 📄 License

This project is licensed under the **MIT License**.
