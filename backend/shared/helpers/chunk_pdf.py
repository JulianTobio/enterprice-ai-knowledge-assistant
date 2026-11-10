from pypdf import PdfReader

def chunk_pdf(file_path: str, file_name:str, file_id: int, chunk_size: int=1000, chunk_overlap: int=200):
    reader = PdfReader(file_path)
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
                    "metadata": {"source": file_name, "file_id": file_id, "page": page_num + 1},
                }
            )
            
            # Advance buffer by chunk_size minus overlap
            text_buffer = text_buffer[chunk_size - chunk_overlap :]

    if text_buffer.strip():
        chunks.append(
            {
                "text": text_buffer.strip(),
                "metadata": {"source": file_name, "file_id": file_id, "page": len(reader.pages)},
            }
        )

    return chunks