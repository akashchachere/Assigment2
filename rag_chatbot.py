import faiss
from flask import Flask, request, jsonify
from transformers import pipeline
import mysql.connector
import numpy as np
from embed_store import retrieve_relevant_chunks  # Function to retrieve chunks from Faiss
from sentence_transformers import SentenceTransformer

# Initialize Flask app
app = Flask(__name__)

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize text generation model (e.g., GPT-2)
generator = pipeline("text-generation", model="gpt-2")


# MySQL connection setup
def connect_db():
    return mysql.connector.connect(host='localhost', user='root', password='Akash@2001', database='chatbot')


# Function to store chat history in MySQL
def store_chat_history(role, content):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO chat_history (role, content) VALUES (%s, %s)", (role, content))
    connection.commit()
    cursor.close()
    connection.close()


# Route to handle the chatbot query
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data['query']

    # Convert query to embedding
    query_embedding = model.encode([user_query])

    # Retrieve relevant chunks from Faiss index
    index = faiss.read_index("faiss_index.index")
    relevant_chunk_indices = retrieve_relevant_chunks(query_embedding, index, k=5)

    # Retrieve the actual text chunks from the indices
    relevant_chunks = [chunks[i] for i in relevant_chunk_indices[0]]

    # Generate an answer using GPT-2
    context = " ".join(relevant_chunks)
    prompt = f"Question: {user_query}\nContext: {context}\nAnswer:"
    answer = generator(prompt, max_length=100)[0]['generated_text']

    # Store chat history
    store_chat_history('user', user_query)
    store_chat_history('system', answer)

    return jsonify({'answer': answer})


# Route to fetch chat history
@app.route('/history', methods=['GET'])
def history():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM chat_history")
    history_data = cursor.fetchall()
    connection.close()

    return jsonify(history_data)


if __name__ == '__main__':
    app.run(debug=True)
