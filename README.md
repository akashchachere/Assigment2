# Retrieval-Augmented Generation (RAG) Chatbot

Overview

Data Preprocessing: Cleaning and chunking input text into smaller segments.
Embedding: Using the sentence-transformers model to generate embeddings for text chunks.
Vector Store: Storing the embeddings in a Faiss index to enable efficient retrieval.
Answer Generation: Using the GPT-2 model to generate responses by providing retrieved context along with the user query.
Flask API: Serving the chatbot through a simple API with endpoints for querying and retrieving chat history.
MySQL: Storing chat history, including user queries and generated answers.

Requirements

The following dependencies are required to run the chatbot:

flask: A micro web framework for Python.
sentence-transformers: For generating embeddings from the text.
faiss-cpu: A vector database library for efficient similarity search.
transformers: A library by Hugging Face for using pre-trained language models.
mysql-connector-python: A library to connect Python to MySQL.

Setup Instructions
1. Clone the Repository
2. Setup MySQL Database
3. Prepare the Data
4. Generate Embedding
5. Run the Flask API

API Endpoints

1. POST /chat
2. GET /history

