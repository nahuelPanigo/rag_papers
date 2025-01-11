from db_connection import search_in_db
from constant import DB_NAME,MODEL_NAME,NUMBER_OF_RESULTS
from llm_connection import generate_answer
from utils import normalize_text


def make_string(results):
    docs = [document for document in results['documents']]
    metadatas = [metadata for metadata in results['metadatas']]
    result = ["Document: " + str(docs[i]) + "Metadata: " + str(metadatas[i])  for i in range(len(docs))]
    return "\n".join(result)


if __name__ == "__main__":
    query = "para que pueden ser utilizadas las redes neuronales convolucionales?"
    results = search_in_db(DB_NAME,query,NUMBER_OF_RESULTS)
    results =  make_string(results)
    answer = generate_answer(query,MODEL_NAME,results)
    #print(normalize_text(answer))
    print(answer)