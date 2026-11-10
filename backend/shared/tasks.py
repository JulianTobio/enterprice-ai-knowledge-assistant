from shared.db.chromadb import get_collection
from shared.dependencies import get_llm_repository
from shared.helpers.chunk_pdf import chunk_pdf
from shared.helpers.metadata_api import MetadataApi, MetadataStatus

async def file_embedding(file_path: str, file_name:str, file_id: int):
    """Create vectors for the file using embeddings."""

    try:

        metadata_api = MetadataApi(file_id=file_id)
        metadata_api.set_status(MetadataStatus.PROCESSING)
        
        print(f"Extracting text from {file_name}...")
        chunks = chunk_pdf(file_path=file_path, file_name=file_name, file_id=file_id)
        print(f"Created {len(chunks)} text chunks.")

        # Get Chroma DB collection
        collection = get_collection()

        # Get LLM repo
        llm_repo = get_llm_repository()

        print(f"Generating embeddings using Ollama...")
        batch_response = await llm_repo.embed(input=[chunk["text"] for chunk in chunks])

        print(f"Saving embeddings to Chroma...")
        ids = []
        embeddings = []
        metadatas = []
        documents = []
        
        for idx, chunk in enumerate(chunks):
            ids.append(f"id_{file_id}_{idx}")
            documents.append(chunk["text"])
            metadatas.append(chunk["metadata"])
            embeddings.append(batch_response[idx])

        collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )

        metadata_api.set_status(MetadataStatus.PROCESSED)
        
        print(f"Success! {len(chunks)} chunks successfully indexed.")

    except Exception as ex:
        print(ex)

        metadata_api.set_status(MetadataStatus.ERROR)
    
    return