# app/core/chunking.py
def chunk_text(text, chunk_size=500, overlap=50):
    """
    Divide un texto en chunks de tamaño 'chunk_size' con 'overlap' de solapamiento.
    """
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        start += chunk_size - overlap
    
    return chunks

if __name__ == "__main__":
    from pdf_loader import load_pdf
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.abspath(os.path.join(current_dir, '../../data/sample.pdf'))
    text = load_pdf(pdf_path)
    chunks = chunk_text(text)
    print(f"Total chunks: {len(chunks)}")
    print("Primer chunk:", chunks[0])