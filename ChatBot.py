import openai
from fastapi import FastAPI

app = FastAPI()

# Configuración de OpenAI
openai.api_key = "TU_API_KEY"

@app.post("/chatbot/")
async def chatbot(pregunta: str):
    respuesta = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Eres un asistente de RRHH que responde preguntas sobre políticas de empresa."},
                  {"role": "user", "content": pregunta}]
    )
    return {"respuesta": respuesta['choices'][0]['message']['content']}

# Para ejecutar: uvicorn nombre_archivo:app --reload
