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

    payload = {
        "model": "llama3.2:3b",
        "prompt": f"{SYSTEM_PROMPT}\n\nUsuario: {prompt_usuario}\nMorgan:",
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