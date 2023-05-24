import os
import sys
from time import sleep
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

question = "Can you list 10 carnatic ragas as a comma separated list? This is the format raga1, raga2, raga3.."
llm = OpenAI(model_name="text-davinci-003")

try:
	raga_list_csv = llm(question)

except:
	print("There's an unforeseen error. \n Thanks for your patience. ")
	exit(0)

raga_list = raga_list_csv.split(',')
for item in raga_list:
	print(item)
	sleep(10)
