<img width="1920" height="1080" alt="output6" src="https://github.com/user-attachments/assets/8e146fc5-a6ee-419b-a3a6-8e4ea4d30652" />
<img width="1920" height="1080" alt="output5" src="https://github.com/user-attachments/assets/46584ca3-5224-4133-8e4a-d8cab623abc4" />
<img width="1920" height="1080" alt="output4" src="https://github.com/user-attachments/assets/d0747396-00a1-4133-ba61-358d764439eb" />
<img width="1920" height="1080" alt="output3" src="https://github.com/user-attachments/assets/10d69406-ffd8-4973-93c9-fe8026d9c47a" />
<img width="1920" height="1080" alt="output2" src="https://github.com/user-attachments/assets/bf92ee07-946b-487b-8a3e-ce43b63cba75" />
<img width="1920" height="1080" alt="output1" src="https://github.com/user-attachments/assets/63730585-97ec-478e-8dc5-62a604509e0e" />
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
