# app/core/rag_pipeline.py

from pdf_loader import load_pdf
from chunking import chunk_text
from embeddings import generate_embeddings
from vector_store import VectorStore
import os

class RAGPipeline:
    def __init__(self, pdf_path):
        # Cargar PDF
        self.text = load_pdf(pdf_path)

        # Dividir en chunks
        self.chunks = chunk_text(self.text)

        # Generar embeddings
        self.embeddings = generate_embeddings(self.chunks)

        # Crear vector store
        self.store = VectorStore(dimension=len(self.embeddings[0]))
        self.store.add_embeddings(self.chunks, self.embeddings)

    def query(self, user_query, top_k=3):
        """
        Realiza búsqueda semántica en los chunks usando la query del usuario.
        """
        # Generar embedding de la consulta
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_vector = model.encode([user_query])[0]

        # Buscar en vector store
        results = self.store.search(query_vector, top_k=top_k)
        return results


if __name__ == "__main__":
    # Ruta del PDF
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.abspath(os.path.join(current_dir, '../../data/sample.pdf'))

    # Crear pipeline
    rag = RAGPipeline(pdf_path)

    # Hacer una consulta de ejemplo
    query_text = "¿Cuál es la percepción de Ingresos Brutos en Buenos Aires?"
    results = rag.query(query_text, top_k=3)

    for chunk, dist in results:
        print(f"Distancia: {dist:.4f}, Texto: {chunk[:200]}...")