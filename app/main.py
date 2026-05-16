import requests
import json
import sys

def preguntar_a_cerebro(prompt_usuario):
    url = "http://host.docker.internal:11434/api/generate"
    
    # Aquí configuramos el "System Prompt" para darle personalidad a Morgan
    system_prompt = (
        "Eres Morgan, un asistente virtual avanzado e inteligente creado por Juan Carlos López Surian. "
        "Tus respuestas deben ser claras, eficientes y con un toque profesional pero cercano. "
        "Responde siempre en español."
        "Siempre te dirigiras a tu creador como Señor López."
        "Preguntaras que tal mi día, y en que puedes ayudar."
        "El señor lopez es ingeniero en informática y necesita tu ayuda para resolver problemas técnicos, aprender nuevas tecnologías y mantenerse actualizado en el mundo de la informática."
        "El señor Lopez hace mantenimeinto de su PC, y le gusta la reparación de celulares, y la tecnología en general."
        "Tu objetivo es ayudar al señor López a resolver sus dudas, proporcionarle información útil y mantener una conversación fluida y agradable."
        "Ayudarle con su agenda y simepre sugerirle como amigo en que puede mejorar su día a día, y como puede aprovechar mejor su tiempo."
        "Cuando te presentes a ti mismo, hazlo de forma breve y solo con la pregunta ¿En qué puedo ayudarle hoy, Señor López?"
    )
    
    # Unimos la personalidad con la pregunta del usuario
    prompt_final = f"<|system|>\n{system_prompt}\n<|user|>\n{prompt_usuario}\n<|assistant|>\n"

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt_final,
        "stream": False
    }
    
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            return response.json().get("response", "No recibí respuesta.")
        else:
            return f"Error en el cerebro (Código: {response.status_code})"
    except requests.exceptions.ConnectionError:
        return "Error: Conexión perdida con Ollama."

def modo_chat_interactivo():
    print("==================================================")
    print("--- SISTEMA MORGAN: MODO INTERACTIVO INICIADO ---")
    print("Escribe 'salir' para apagar a Morgan.")
    print("==================================================\n")
    
    while True:
        # Capturamos lo que tú escribas en la terminal
        user_input = input("Tú 👤 > ")
        
        # Condición para apagar el sistema
        if user_input.lower() == 'salir':
            print("\nApagando sistemas de Morgan... Hasta pronto, señor López.")
            break
            
        # Si el usuario no escribe nada, ignoramos
        if not user_input.strip():
            continue
            
        # Morgan procesa y responde
        respuesta_morgan = preguntar_a_cerebro(user_input)
        print(f"\nMorgan> {respuesta_morgan}\n")

if __name__ == "__main__":
    modo_chat_interactivo()