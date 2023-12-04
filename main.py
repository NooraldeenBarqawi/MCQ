from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

Subject="math"
quiz_template=""""Write a 5 multiple-choice questions about {Subject} Each question should have at
least 4 answers ,the output should be structures like this json{{question1:the question,answers:[],answer:the correct answer}}
"""
quiz_prompt_template=PromptTemplate(input_variables=["Subject"],template=quiz_template)

llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

chain=LLMChain(llm=llm,prompt=quiz_prompt_template)
print(chain.run(Subject=Subject))