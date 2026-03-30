# app/core/embeddings.py
from sentence_transformers import SentenceTransformer

# Carga un modelo pequeño y gratuito
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
    """
    Recibe una lista de chunks y devuelve una lista de vectores.
    """
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings

if __name__ == "__main__":
    from chunking import chunk_text
    from pdf_loader import load_pdf
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.abspath(os.path.join(current_dir, '../../data/sample.pdf'))
    text = load_pdf(pdf_path)
    chunks = chunk_text(text)
    vectors = generate_embeddings(chunks)
    
    print(f"Total vectores: {len(vectors)}")
    print("Primer vector:", vectors[0][:10], "...")  # Muestra los primeros 10 valores