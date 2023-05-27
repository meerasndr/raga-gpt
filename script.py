import os
import sys
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import LLMChain
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this list based on your requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

template = "Can you list {n} carnatic ragas as a comma separated list? This is the format raga1, raga2, raga3.."
llm = OpenAI(model_name="text-davinci-003")
prompt = PromptTemplate(template=template, input_variables=['n'])
chain = LLMChain(llm=llm, prompt=prompt)

@app.get("/")
async def root():
	return {"message": "Hello"}

@app.post("/{num_ragas}")
async def post(num_ragas:int):
	try:
		if num_ragas < 21 and num_ragas > 1:
			input = {'n': num_ragas}
			raga_list_csv = chain.run(input)
		else:
			return {"message": "We are able to give you upto 20 ragas at a time. Enter a number less than 21 and more than 1"}

	except:
		return {"message" : "There's an unforeseen error. Try again later. \n Thanks for your patience. "}

	raga_list = raga_list_csv.replace(" ", "").strip().split(',')
	return {"message": raga_list}

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)







