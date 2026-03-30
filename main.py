from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.core.pdf_loader import load_pdf
from app.core.chunking import chunk_text
from app.core.embeddings import generate_embeddings
from app.core.vector_store import search_vector_store

app = FastAPI(title="LLM-RAG System")

memory = {}  # Para guardar PDF y embeddings temporalmente

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = load_pdf(content, from_bytes=True)  # Necesitarás adaptar load_pdf a bytes
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)
    memory["chunks"] = chunks
    memory["embeddings"] = embeddings
    return {"status": "PDF cargado", "total_chunks": len(chunks)}

@app.post("/query/")
async def query_pdf(query: str = Form(...)):
    if "chunks" not in memory:
        return JSONResponse(status_code=400, content={"error": "No hay PDF cargado"})
    result = search_vector_store(query, memory["chunks"], memory["embeddings"])
    return {"query": query, "result": result}