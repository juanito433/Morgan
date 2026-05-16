import requests
import json
import sys

def preguntar_a_cerebro(propor_texto):
    # 'host.docker.internal' es la llave para salir de Docker hacia tu Windows
    url = "http://host.docker.internal:11434/api/generate"
    
    payload = {
        "model": "llama3.2:3b",
        "prompt": propor_texto,
        "stream": False  # False para que nos traiga la respuesta completa de un solo golpe
    }
    
    print("\nMorgan está procesando la petición...")
    
    try:
        # Enviamos la pregunta a Ollama en Windows
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "No recibí texto de respuesta.")
        else:
            return f"Error de conexión con el cerebro (Código: {response.status_code})"
            
    except requests.exceptions.ConnectionError:
        return "Error crítico: No me pude conectar con Ollama. Asegúrate de que Ollama está abierto en Windows."

def inicializar_morgan():
    print("--- SISTEMA MORGAN: CONECTANDO CON EL CEREBRO ---")
    print(f"Versión de Python del Agente: {sys.version.split()[0]}")
    
    # El primer pensamiento autónomo de Morgan
    primer_prompt = "Preséntate brevemente con el nombre de Morgan. Di que eres un asistente en desarrollo y que estás listo para ayudar a Juan Carlos."
    
    respuesta = preguntar_a_cerebro(primer_prompt)
    
    print("\n====================================")
    print(f"RESPUESTA DE MORGAN:\n{respuesta}")
    print("====================================\n")

if __name__ == "__main__":
    inicializar_morgan()