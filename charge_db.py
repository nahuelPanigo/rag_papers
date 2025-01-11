
import os
from constant import PAPERS_DIR,DB_NAME,CHUNK_SIZE,METADATA_FILENAME
from db_connection import crete_db
from llama_index.core import Document
from llama_index.readers.file import PDFReader
from utils import read_json,normalize_text

def read_and_chunk_papers(directory, metadata_file, chunk_size=CHUNK_SIZE):
    reader = PDFReader()
    metadata = read_json(PAPERS_DIR + "/"+ metadata_file)  
    chunks = []
    for filename in [x for x in os.listdir(directory) if x.endswith('.pdf')]:
        file_path = os.path.join(directory, filename)
        docs = reader.load_data(file_path)
        for document in docs:
            text = document.text
            text =  normalize_text(text)
            for i in range(0, len(text), chunk_size):
                chunk_text = text[i:i+chunk_size]
                chunk_metadata = metadata.get(filename, {})
                chunk_document = Document(
                    text=chunk_text,
                    metadata=chunk_metadata
                )
                chunks.append(chunk_document)
    return chunks

if __name__ == "__main__":
    db = crete_db(DB_NAME)
    docs = read_and_chunk_papers(PAPERS_DIR,METADATA_FILENAME,CHUNK_SIZE)
    documents = [chunk.text for chunk in docs]  # Extrae el texto de cada chunk
    metadatas = [chunk.metadata for chunk in docs] 
    db.add(documents= documents,
            ids= [str(x) for x in range(len(docs))], 
            metadatas= metadatas)
    print(db.peek(1))
    print(db.count())   
    
