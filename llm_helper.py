from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def generate_response_llm(text):
    questions = text.lower()
    response = llm.invoke(questions)
    return response.content

if __name__ == "__main__":
    response = generate_response_llm("What is the population of Tokyo?")
    print(response)
    
    





