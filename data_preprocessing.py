import re

# Example function to clean text (remove extra spaces, unwanted characters)
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()
    return text

# Function to chunk the text into smaller segments (e.g., 200-300 words each)
def chunk_text(text, chunk_size=300):
    words = text.split(' ')
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Example corpus (you can load your own corpus here)
corpus = [
    "Artificial Intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of 'intelligent agents': any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.",
    "Machine learning (ML) is a branch of AI that focuses on the development of algorithms that allow computers to learn and make decisions from data, without explicit programming."
]

# Preprocess and chunk the corpus
processed_corpus = []
for doc in corpus:
    cleaned_text = clean_text(doc)
    chunks = chunk_text(cleaned_text)
    processed_corpus.extend(chunks)

# Save processed chunks to a file (optional)
with open("chunks.txt", "w") as file:
    file.write("\n".join(processed_corpus))

print(f"Total chunks created: {len(processed_corpus)}")
