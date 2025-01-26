from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load the pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to encode chunks into embeddings
def encode_chunks(chunks):
    return model.encode(chunks)

# Function to store embeddings in Faiss
def store_embeddings(embeddings):
    dim = embeddings.shape[1]  # Dimension of the embedding vectors
    index = faiss.IndexFlatL2(dim)  # Faiss index for L2 distance (Euclidean)
    index.add(embeddings)  # Add embeddings to the index
    return index

# Function to retrieve the top-k most relevant chunks
def retrieve_relevant_chunks(query_embedding, index, k=5):
    distances, indices = index.search(query_embedding, k)
    return indices

# Load preprocessed chunks from the file
with open("chunks.txt", "r") as file:
    chunks = file.readlines()

# Encode chunks into embeddings
embeddings = encode_chunks(chunks)

# Convert embeddings to numpy array
embeddings = np.array(embeddings).astype(np.float32)

# Store embeddings in Faiss
index = store_embeddings(embeddings)

# Save Faiss index to disk
faiss.write_index(index, "faiss_index.index")
print("Embeddings stored in Faiss index.")
