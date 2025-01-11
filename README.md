## Rag Papers

This project is a research project that uses the [ChromaDB](https://www.trychroma.com/) library to create a search engine for scientific papers. The goal is to provide a search engine that can answer questions about scientific papers based on the content of the papers.

The project is divided into three main components:

1. Data collection: This component involves collecting scientific papers from various sources and organizing them into a database. The data is collected using the [ChromaDB](https://www.trychroma.com/) library, which allows for efficient storage and retrieval of large amounts of data.

2. Search engine: This component involves creating a search engine that can answer questions about scientific papers based on the content of the papers. The search engine uses the collected data to retrieve relevant papers and their metadata. Its use embeddings models, which are used to generate embeddings for the papers, to retrieve the most relevant chunks of text from the papers.

3. LLM: This component involves using a large language model (LLM) to generate answers to questions about scientific papers. The LLM is used to generate answers based on the retrieved papers and their metadata. The LLM is implemented using the [Generative AI](https://github.com/chroma-core/generativeai-python) library. But it is easily customizable with new llms integrations, which must be done in the llm_connection file 


## Installation

To install the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/nahuelPanigo/rag_papers.git
```

2. Install the required dependencies:

** The requirements included sentence-transformers if you want to use "models/text-embedding-004" from ai studio you can delete or comment this line from requirements**

```bash
pip install -r requirements.txt
```

3. Set up the environment variables:

    create a file .env in the root file with the GOOGLE_API_KEY


6. Configure the LLM:

   - Go to the [Generative AI](https://github.com/chroma-core/generativeai-python) repository.
   - Follow the instructions to set up the project.
   - Copy the API key to the GOOGLE_API_KEY environment variable.

   for other models make the same function and chain in  llm_connection

7. Run the project:

After running you have to load the papers in papers folder and the metadata, for the metadata you can use the metadata_ejemplo.json as example. if you change the name of the file you have to change it in the constant.py file.

The first time you run the project, it will create the database and the embeddings for the papers, so it will take some time. for this execute:
```bash
    charge_db.py
```
After that you can run the project:

```bash
python main.py
```

## Usage

To use the project, follow these steps:

1. Run the project:

```bash
python main.py
```
in constant.py you can change all the parameters of the project, including prompt, model, number of results, embedding strategy, and the model of embeddings.
