from app.rag.llm import get_llm
from app.rag.prompt import get_prompt
from langchain_core.output_parsers import StrOutputParser
llm = get_llm()

prompt = get_prompt()

parser = StrOutputParser()

def generate_answer(context, question):

    chain = prompt | llm | parser

    return chain.invoke({

        "context": context,

        "question": question

    })
