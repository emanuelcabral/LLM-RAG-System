# 📄🔍 LLM RAG System

> 🚀 Sistema de **búsqueda semántica sobre PDFs** usando embeddings y FAISS.
> Permite subir un documento, procesarlo y hacer consultas inteligentes basadas en su contenido.

---

## 🧠 ¿Qué hace este proyecto?

Este proyecto implementa un pipeline completo de **RAG (Retrieval-Augmented Generation)** desde cero:

* 📄 Lee archivos PDF
* ✂️ Divide el texto en fragmentos (chunks)
* 🧮 Genera embeddings semánticos
* 🗂️ Almacena vectores en un índice FAISS
* 🔎 Permite hacer consultas inteligentes sobre el contenido

👉 En lugar de buscar texto exacto, el sistema entiende el **significado** de la consulta.

---

## ⚙️ ¿Cómo funciona?

### Flujo completo:

1. 📥 **Carga del PDF**

   * Se extrae el texto usando `pypdf`

2. ✂️ **Chunking**

   * El texto se divide en partes más pequeñas para mejorar la búsqueda

3. 🧠 **Embeddings**

   * Se convierten los chunks en vectores usando `sentence-transformers`

4. 📦 **Vector Store**

   * Se almacenan los vectores en un índice FAISS

5. 🔍 **Consulta**

   * El usuario hace una pregunta
   * Se transforma en embedding
   * Se buscan los chunks más relevantes

---

## 🛠️ Tecnologías utilizadas

* 🐍 Python
* ⚡ FastAPI
* 🧠 sentence-transformers
* 📦 FAISS (Facebook AI Similarity Search)
* 📄 pypdf

---

## 📁 Estructura del proyecto

```
app/
├── core/
│   ├── pdf_loader.py      # Carga y extracción de texto del PDF
│   ├── chunking.py        # División del texto en chunks
│   ├── embeddings.py      # Generación de embeddings
│   ├── vector_store.py    # Índice vectorial con FAISS
│   └── rag_pipeline.py    # Pipeline completo RAG
│
├── main.py                # API con FastAPI
└── routes.py              # (pendiente / no implementado)

data/
└── sample.pdf             # PDF de prueba
```

---

## 📦 Instalación

```bash
git clone https://github.com/emanuelcabral/LLM-RAG-System.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

Iniciar el servidor:

```bash
uvicorn main:app --reload
```

---

## 📡 Endpoints

### 📤 Subir PDF

```
POST /upload-pdf/
```

* Recibe un archivo PDF
* Extrae texto, genera chunks y embeddings

Respuesta:

```json
{
  "status": "PDF cargado",
  "total_chunks": 120
}
```

---

### 🔍 Consultar

```
POST /query/
```

* Recibe una query del usuario
* Devuelve los fragmentos más relevantes

Ejemplo:

```json
{
  "query": "¿Quien es el principito?",
  "result": [...]
}
```

---

## 🧪 Ejemplo de uso

1. Subir un PDF
2. Hacer una consulta como:

```
¿Cuales son los personajes involucrados?
```

👉 El sistema devuelve los fragmentos más relevantes del documento.

---

## ⚠️ Limitaciones actuales

* 🧠 No genera respuestas con LLM (solo recuperación)
* 💾 Almacenamiento en memoria (no persistente)
* 📄 Soporte básico de PDF (puede fallar con PDFs complejos)

---

## 🚀 Próximas mejoras

* Integración con LLM (OpenAI / local)
* Base de datos vectorial persistente
* Mejor chunking semántico
* UI web

---

## 🔐 Notas importantes

* No subir `.env`
* Ignorar `env/` (entorno virtual)
* Optimizar tamaño de chunks según el caso

---

## 👨‍💻 Autor

Hecho con 💻 por **Emanuel Cabral**

---

## ⭐ Valor del proyecto

Este proyecto demuestra:

* Implementación real de RAG desde cero
* Uso de embeddings y búsqueda semántica
* Integración backend con FastAPI
* Arquitectura modular escalable

---

## 📜 Licencia

MIT
