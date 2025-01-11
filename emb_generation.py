from sentence_transformers import SentenceTransformer
from chromadb import Documents,Embeddings
from constant import MODEL_EMBEDDINGS_LOCAL

class LocalEmbeddingModel:
    def __init__(self, model_name: str = MODEL_EMBEDDINGS_LOCAL):
        # Cargar el modelo de embeddings una sola vez
        self.model = SentenceTransformer(model_name)
        
    def generate_embeddings(self, documents: Documents) -> Embeddings:
        """
        Genera embeddings para una lista de documentos usando el modelo local.
        """
        return self.model.encode(documents)
    

