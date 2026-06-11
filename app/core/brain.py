from core.memory import cargar_memoria
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
Eres Morgan.

Un asistente virtual avanzado creado por Juan Carlos López Surian.

Siempre respondes en español.

Te diriges al usuario como Señor.

Características:

- Profesional.
- Amigable.
- Inteligente.
- Preciso.
- Breve cuando sea necesario.

Conoces:

- Python
- Laravel
- React Native
- Inteligencia Artificial
- Redes
- Linux
- Bases de datos
- Ciberseguridad

Ayudas a organizar tareas y mejorar la productividad.
"""

def generar_respuesta(prompt_usuario):
    historial = cargar_memoria()

    contexto = ""

    for item in historial:
        contexto += f"""
            Usuario: {item['usuario']}
            Morgan: {item['respuesta']}
            """

    payload = {
        "model": "llama3.2:3b",
        "prompt": f"""
    {SYSTEM_PROMPT}

    Historial:
    {contexto}

    Usuario:
    {prompt_usuario}

    Morgan:
    """,
        "stream": False
    }
    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        if response.status_code == 200:

            return response.json()["response"]

        return "No pude comunicarme con mi cerebro."

    except Exception as e:

        return f"Error: {e}"