import asyncio

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatAnthropic(model_name="claude-sonnet-4-5", temperature=0.3)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente que responde de forma clara y concisa."),
    ("human", "{pregunta}")
])

parser = StrOutputParser()

chain = prompt | model | parser


async def main():
    respuesta = await chain.ainvoke(
        {"pregunta": "¿Qué ventaja tiene LCEL sobre llamar al SDK directo?"}
    )
    print(respuesta)


if __name__ == "__main__":
    asyncio.run(main())
