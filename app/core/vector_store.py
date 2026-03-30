# app/core/vector_store.py
import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        # Índice L2 (distancia euclidiana)
        self.index = faiss.IndexFlatL2(dimension)
        self.text_chunks = []

    def add_embeddings(self, chunks, embeddings):
        """
        Agrega chunks y sus embeddings al índice.
        """
        self.text_chunks.extend(chunks)
        self.index.add(np.array(embeddings, dtype='float32'))

    def search(self, query_vector, top_k=3):
        """
        Busca los top_k chunks más similares a query_vector
        """
        query_vector = np.array([query_vector], dtype='float32')
        distances, indices = self.index.search(query_vector, top_k)
        results = [(self.text_chunks[i], distances[0][idx]) for idx, i in enumerate(indices[0])]
        return results

if __name__ == "__main__":
    from embeddings import generate_embeddings
    from chunking import chunk_text
    from pdf_loader import load_pdf
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.abspath(os.path.join(current_dir, '../../data/sample.pdf'))

    text = load_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    # Crear vector store
    store = VectorStore(dimension=len(embeddings[0]))
    store.add_embeddings(chunks, embeddings)

    # Ejemplo de búsqueda: usamos el primer embedding como query
    results = store.search(embeddings[0], top_k=3)
    for chunk, dist in results:
        print(f"Distancia: {dist:.4f}, Texto: {chunk[:100]}...")