import os
from dotenv import load_dotenv

load_dotenv() # load values from .env to main

print("dotenv loaded")
#print("Your API Key:", os.environ["OPEN_AI_API_KEY"])
'''
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
'''

#----------------------------------

#1. Take User Question
user_queston = input("Enter your question: ")

# 2. Convert to Prompt
# there are 2 prompt templates in LC: standard and message
from langchain.prompts import PromptTemplate
# system prompt
text = """ You are a tollywood fancy chatbot. Always reply with single tollywood dialogue.Do not exceed more than 2 points answer.
Below is your question: {question}

"""
# to integrate sys prompt and u.qs 
prompt = PromptTemplate(
    input_variables=["question"],
    template = text
)

#3. Make LLM call

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
#from langchain_ollama import ChaOtllama

# llm = ChatOpenAI(model = "gpt-4o")
llm = ChatGroq(model = "deepseek-r1-distill-llama-70b")

#create chain
chain = prompt | llm


#4.response
result = chain.invoke({"question": user_queston})
print(result)
print(type(result))
print("--------------------")
print(result.content)
