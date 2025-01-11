from chromadb import PersistentClient,Documents,EmbeddingFunction,Embeddings
from constant import DB_NAME,DB_DIR,MODEL_EMBEDDINGS_GENAI,EMBEDDING_STRATEGY
from emb_generation import LocalEmbeddingModel
import google.generativeai as genai


class CustomEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.model = LocalEmbeddingModel()
    def __call__(self, input:Documents) -> Embeddings:
        return self.model.generate_embeddings(input)



class GeminiEmbeddingFunction(EmbeddingFunction):

    def __init__(self,document_mode=True):
        self.document_mode=document_mode

    def __call__(self, input:Documents) -> Embeddings:

        if self.document_mode:
            embedding_task =  "retrieval_document"
        else:
            embedding_task = "retrieval_query"
        
        response = genai.embed_content(
            content=input,
            model=MODEL_EMBEDDINGS_GENAI,
            task_type=embedding_task,
        )
        return response["embedding"]


def embedding_function():
    if int(EMBEDDING_STRATEGY) == 1:
        return CustomEmbeddingFunction()
    else:   
        return GeminiEmbeddingFunction()


def get_or_open_db(collection_name=DB_NAME):
    chroma_client = PersistentClient(
    path=DB_DIR
    )
    # Acceder a la colección ya existente
    return chroma_client.get_collection(name=collection_name)


def crete_db(collection_name="my_collection"):
    chroma_client = PersistentClient(
            path=DB_DIR
    )
    return chroma_client.create_collection(name=collection_name, embedding_function=embedding_function())



def search_in_db(collection_name, query,results=5):
    emb_function = embedding_function() 
    query_embedding = emb_function([query])
    db =  get_or_open_db(collection_name)
    search_results = db.query(
    query_embeddings=query_embedding,
    n_results=results
    )
    return search_results


