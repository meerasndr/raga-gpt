import os
import sys
from time import sleep
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import LLMChain
from fastapi import FastAPI
app = FastAPI()


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

question = "Can you list 10 carnatic ragas as a comma separated list? This is the format raga1, raga2, raga3.."
llm = OpenAI(model_name="text-davinci-003")

@app.get("/")
async def root():
	try:
		raga_list_csv = llm(question)
	except:
		print("There's an unforeseen error. Try again later. \n Thanks for your patience. ")
		exit(0)
	raga_list = raga_list_csv.replace(" ", "").strip().split(',')
	message = ''
	#for item in raga_list:
		#message += item
	return {"message": raga_list}







