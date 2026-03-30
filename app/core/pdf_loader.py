import os
from pypdf import PdfReader

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

if __name__ == "__main__":
    # Carpeta donde está este archivo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Ruta correcta al PDF en la carpeta raíz 'data'
    pdf_path = os.path.abspath(os.path.join(current_dir, '../../data/sample.pdf'))
    
    content = load_pdf(pdf_path)
    print(content[:500])