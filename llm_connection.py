from constant import PROMPT
import google.generativeai as genai
import os
from dotenv import load_dotenv


def generate_answer(query,model_name,results):
    load_dotenv()
    GOOGLE_API_KEY = GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(model_name)
    prompt = f"{PROMPT} QUESTION:{query} PAPPERS: {results}"
    answer = model.generate_content(prompt)
    return answer.text

##for other models make the same function and chain in main