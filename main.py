# print("hello World")

from inference import model_inference

import os

from dotenv import load_dotenv

load_dotenv(r'E:\end to end\nlp_pro_1\.env')

openai_key = os.getenv("OPENAI_KEY")

print(openai_key) 

# model = openai("gpt4", api_key = openai_key)
import pandas 

df=pd.read_csv("") 

