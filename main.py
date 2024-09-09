from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
key = os.getenv("OPENAI_API_KEY")

messages = [
    SystemMessage ("Translate this text to Portuguese"),
    HumanMessage("Help me with LangChain, OpenAI")
]

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()



template_message = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user","{texto}")
])



chain = template_message | model | parser

