from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=1200):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

def create_vector_store(chunks):
    embeddings = embedding_model.encode(chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index, embeddings

def retrieve_relevant_chunks(question,chunks,index,top_k=3):
    question_embedding = embedding_model.encode([question])
    distances, indices = index.search(np.array(question_embedding),top_k)
    relevant_chunks = [chunks[i] for i in indices[0]]
    return relevant_chunks