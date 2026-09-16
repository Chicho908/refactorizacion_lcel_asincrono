# Refactorizacion a LCEL Asincrono

Ejercicio opcional del Modulo 2 (CoderHouse - Desarrollo de aplicaciones con LLMs). Migra la
llamada imperativa al SDK crudo del Modulo 1 (Pre-entrega 1) a una cadena declarativa con
LangChain Expression Language (LCEL), ejecutada de forma asincrona.

## Que hace

Define una cadena `prompt | model | parser` y la ejecuta con `await`:

1. **`ChatPromptTemplate`** con roles `system` / `human` definidos, en vez de armar el mensaje
   a mano como en el SDK crudo.
2. **`ChatAnthropic`** como modelo, envuelto como un `Runnable` mas de la cadena (no una llamada
   aislada a la API).
3. **`StrOutputParser`** para que la salida final sea texto plano, no el objeto `AIMessage`
   completo.
4. Ejecucion asincrona con `await chain.ainvoke({"pregunta": "..."})` dentro de una funcion
   `async def main()`, corrida con `asyncio.run(main())`.

## Como correrlo

```bash
python -m venv venv
venv\Scripts\activate        # en Windows
# source venv/bin/activate   # en Linux/Mac
pip install -r requirements.txt
copy .env.example .env       # completar con tu ANTHROPIC_API_KEY real
python main.py
```

## Estructura del proyecto

```
.
├── main.py            # cadena LCEL (prompt | model | parser) y ejecucion async
├── requirements.txt   # dependencias: langchain, langchain-anthropic, python-dotenv
├── .env.example        # plantilla de variables de entorno (sin la key real)
├── .gitignore          # excluye .env, venv/ y __pycache__/
└── README.md
```

## Decisiones de diseno

- Se uso `ChatAnthropic` en vez de `ChatOpenAI` porque ya esta la API key de Anthropic probada
  en vivo desde la Pre-entrega 1. Cambiar de proveedor implica tocar una sola linea (el import
  y la clase) sin modificar el resto de la cadena — esa intercambiabilidad es justamente lo que
  da usar el protocolo `Runnable` de LCEL en vez de llamar al SDK crudo directamente.
- El diccionario que recibe `ainvoke` (`{"pregunta": ...}`) coincide exactamente con la variable
  `{pregunta}` declarada en el `ChatPromptTemplate` — es el error mas comun al armar cadenas
  LCEL (variable de entrada que no matchea con el placeholder del prompt).
- La clave `.env` con la API key real nunca se sube al repo (esta en `.gitignore`); solo se
  versiona `.env.example` como plantilla para quien clone el proyecto.
