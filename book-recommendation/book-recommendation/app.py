# Step 1: Install required libraries
!pip install sentence-transformers pandas numpy tabulate
# Step 2: Import libraries
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from tabulate import tabulate
# Step 3: Load AI embedding model
ai_model = SentenceTransformer('all-MiniLM-L6-v2')
# Step 4: Load large book dataset
url = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"
df = pd.read_csv(url)

# Combine title and authors into a searchable description
df["description"] = df["title"] + " by " + df["authors"]
# Step 5: Generate embeddings for all books
book_embeddings = ai_model.encode(df["description"].tolist(), show_progress_bar=True)
# Step 6: Define recommendation function
def recommend_books(query, top_n=5):
    # Convert user query to embedding
    query_embedding = ai_model.encode([query])[0]

    # Compute similarity between query and all book embeddings
    similarities = np.dot(book_embeddings, query_embedding)

    # Get indices of top N most similar books
    best_indices = np.argsort(similarities)[-top_n:][::-1]

    # Return DataFrame with top books
    return df.iloc[best_indices][["title","authors","average_rating"]]
  query = input("Enter the type of book you want: ")
results = recommend_books(query)

# Display results in a nice table using tabulate
print("\nTop Book Recommendations:")
print(tabulate(results, headers='keys', tablefmt='fancy_grid', showindex=False))
