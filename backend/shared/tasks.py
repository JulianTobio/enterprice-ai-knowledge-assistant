from pypdf import PdfReader
import chromadb
from ollama import Client
from app.models.file_metadata import FileMetadata
from app.core.config import CHROMA_DB_HOST, CHROMA_DB_PORT, CHROMA_DB_COLLECTION, OLLAMA_BASE_URL

def chunk_pdf(file: FileMetadata, chunk_size: int=150, chunk_overlap: int=30):
    reader = PdfReader(file.path)
    chunks = []
    text_buffer = ""

    for page_num, page in enumerate(reader.pages):
        
        text = page.extract_text()
        cleaned_text = " ".join(text.split())
        if cleaned_text:
            text_buffer += cleaned_text

        # Simple sliding window chunking by character length
        while len(text_buffer) >= chunk_size:
            chunk = text_buffer[:chunk_size]
            chunks.append(
                {
                    "text": chunk.strip(),
                    "metadata": {"source": file.file_name, "file_id": file.id, "page": page_num + 1},
                }
            )
            
            # Advance buffer by chunk_size minus overlap
            text_buffer = text_buffer[chunk_size - chunk_overlap :]

    if text_buffer.strip():
        chunks.append(
            {
                "text": text_buffer.strip(),
                "metadata": {"source": file.file_name, "file_id": file.id, "page": len(reader.pages)},
            }
        )

    return chunks

def file_embedding(metadata: FileMetadata):
    """Create vectors for the file using embeddings."""
    
    print(f"Extracting text from {metadata.file_name}...")
    chunks = chunk_pdf(file=metadata)
    print(f"Created {len(chunks)} text chunks.")

    # Chroma DB Config
    collection_name = CHROMA_DB_COLLECTION
    client = chromadb.HttpClient(host=CHROMA_DB_HOST, port=int(CHROMA_DB_PORT))
    collection = client.get_or_create_collection(name=collection_name)

    # Ollama Config
    embeding_client = Client(host=OLLAMA_BASE_URL)

    print(f"Generating embeddings using Ollama...")
    batch_response = embeding_client.embed(model="qwen3-embedding:0.6b", input=[chunk["text"] for chunk in chunks])

    print(f"Saving embeddings to Chroma...")
    ids = []
    embeddings = []
    metadatas = []
    documents = []
    
    for idx, chunk in enumerate(chunks):
        ids.append(f"id_{metadata.id}_{idx}")
        documents.append(chunk["text"])
        metadatas.append(chunk["metadata"])
        embeddings.append(batch_response["embeddings"][idx])

    collection.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents
    )
    
    print(f"Success! {len(chunks)} chunks successfully indexed into '{collection_name}'.")
    
    return