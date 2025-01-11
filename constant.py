import os
DB_NAME = "papersdb"
DB_DIR = os.path.join(os.path.dirname(__file__), "db")
PAPERS_DIR = os.path.join(os.path.dirname(__file__), "papers")
MODEL_NAME = "gemini-1.5-flash-latest"

EMBEDDING_STRATEGY = 1 # 1 = local, 2 = gemini
MODEL_EMBEDDINGS_GENAI = "models/text-embedding-004"
MODEL_EMBEDDINGS_LOCAL = "all-MiniLM-L6-v2"
NUMBER_OF_RESULTS = 4


CHUNK_SIZE = 16384  #chars
METADATA_FILENAME = "metadata_ejemplo.json"

PROMPT = """You are a helpful assistant that answers questions based on a given context.
for each question you answer, you have to add the source of the answer from the metadata of the document.
this source has to added as apa citator."""