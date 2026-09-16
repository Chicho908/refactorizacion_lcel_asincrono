"""
Refactorizacion a LCEL Asincrono - Modulo 2 CoderHouse.
Migra la llamada al SDK crudo (Modulo 1) a una cadena declarativa LCEL,
ejecutada de forma asincrona.
"""
import asyncio

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Modelo: un Runnable mas dentro de la cadena, no una llamada aislada al SDK
model = ChatAnthropic(model_name="claude-sonnet-4-5", temperature=0.3)

# Prompt con roles definidos (system/human)
prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente que responde de forma clara y concisa."),
    ("human", "{pregunta}")
])

# Parser: devuelve texto plano en vez del objeto AIMessage completo
parser = StrOutputParser()

# Composicion LCEL con el operador pipe
chain = prompt | model | parser


async def main() -> None:
    respuesta = await chain.ainvoke(
        {"pregunta": "¿Qué ventaja tiene LCEL sobre llamar al SDK directo?"}
    )
    print(respuesta)


if __name__ == "__main__":
    asyncio.run(main())
