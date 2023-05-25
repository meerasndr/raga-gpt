import os
import sys
from time import sleep
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import LLMChain
from fastapi import FastAPI
import uvicorn
app = FastAPI()


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

template = "Can you list {n} carnatic ragas as a comma separated list? This is the format raga1, raga2, raga3.."
llm = OpenAI(model_name="text-davinci-003")
prompt = PromptTemplate(template=template, input_variables=['n'])
chain = LLMChain(llm=llm, prompt=prompt)
input = {'n': 5}

@app.get("/")
async def root():
	try:
		raga_list_csv = chain.run(input)
	except:
		print("There's an unforeseen error. Try again later. \n Thanks for your patience. ")
		exit(0)
	raga_list = raga_list_csv.replace(" ", "").strip().split(',')
	message = ''
	return {"message": raga_list}

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)







