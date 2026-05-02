import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = None
index = None
chunks = None

def initialize_rag():
    global model, index, chunks

    if model is None:
        print("🔄 Loading RAG model...")

        model = SentenceTransformer("all-MiniLM-L6-v2")

        with open("data/sample.txt", "r", encoding="utf-8") as f:
            text = f.read()

        chunks = text.split("\n")

        embeddings = model.encode(chunks)

        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings))

        print("✅ RAG initialized")


def search(query):
    initialize_rag()

    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=2)

    results = [chunks[i] for i in I[0]]
    return "\n".join(results)