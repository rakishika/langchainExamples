import os
import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = PromptTemplate(
    input_variables=["destinationType", "touristType"],
    template="What are the top {destinationType} destinations for {touristType}? Show five results.",
)

llm = ChatOpenAI(
          model_name="gpt-3.5-turbo", # default model
          temperature=0.9) #temperature dictates how whacky the output should be

llmchain = LLMChain(llm=llm, prompt=prompt)

print(prompt.format(destinationType="beach", touristType="family"))
response = llmchain.run({"destinationType": "beach", "touristType": "family"})
print(response)

