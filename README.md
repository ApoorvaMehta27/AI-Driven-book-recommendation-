# 📚 AI Book Recommendation System using Endee

## 📌 Overview
This project is an AI-powered book recommendation system that uses semantic search to suggest books based on user input.

It leverages embeddings and a vector database to find similar books efficiently.

---

## 🚀 Features
- 🔍 Semantic Search (understands meaning, not just keywords)
- ⚡ Fast retrieval using Endee vector database
- 🤖 AI-based recommendations using embeddings
- 📊 Clean tabular output using tabulate

---

## 🧠 Tech Stack
- Python
- Sentence Transformers
- Endee Vector Database
- Pandas, NumPy

---

## ⚙️ How It Works
1. Load book dataset  
2. Convert book titles into embeddings  
3. Store embeddings in Endee  
4. Convert user query into embedding  
5. Perform similarity search  
6. Return top recommended books  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
