from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import json


def creatQuestions(Subject,num):
    quiz_template = """"Write a {num} multiple-choice questions about {Subject} Each question should have at
    least 4 answers ,the output should be structures like this json{{question1:the question,answers:[],answer:the correct answer}}
    """
    quiz_prompt_template = PromptTemplate(input_variables=["Subject","num"], template=quiz_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo",openai_api_key="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")

    chain = LLMChain(llm=llm, prompt=quiz_prompt_template)
    return (chain.run(Subject=Subject,num=num))



