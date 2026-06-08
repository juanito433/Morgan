import requests
import json
import os
import time
from gtts import gTTS
import pygame

# Inicializamos el mezclador de audio de pygame
pygame.mixer.init()

def preguntar_a_cerebro(prompt_usuario):
    # Apuntamos a localhost ya que el script se ejecuta en tu entorno local
    url = "http://localhost:11434/api/generate"
    
    system_prompt = (
        "Eres Morgan, un asistente virtual avanzado e inteligente creado por Juan Carlos López Surian. "
        "Tus respuestas deben ser claras, eficientes y con un toque profesional pero cercano. "
        "Responde siempre en español. "
        "Siempre te dirigiras a tu creador como Señor. "
        "Preguntaras que tal mi día, y en que puedes ayudar. "
        "El señor es Ingeniero Informático y necesita tu ayuda para resolver problemas técnicos, aprender nuevas tecnologías y mantenerse actualizado. "
        "El señor hace mantenimiento de su PC, y le gusta la reparación de celulares, y la tecnología en general. "
        "Tu objetivo es ayudar al señor a resolver sus dudas, proporcionarle información útil y mantener una conversación fluida y agradable. "
        "Ayudarle con su agenda y siempre sugerirle como amigo en que puede mejorar su día a día, y como puede aprovechar mejor su tiempo. "
        "Cuando te presentes a ti mismo, hazlo de forma breve"
    )
    
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
        return "Error: Conexión perdida con Ollama. Verifica que el servicio esté activo en localhost."

def reproducir_voz(texto):
    """Convierte el texto a voz y lo reproduce."""
    try:
        # Genera el audio. tld='com.mx' le da un tono más natural para México.
        tts = gTTS(text=texto, lang='es', tld='com.mx')
        archivo_audio = "voz_morgan.mp3"
        tts.save(archivo_audio)
        
        # Carga y reproduce el archivo temporal
        pygame.mixer.music.load(archivo_audio)
        pygame.mixer.music.play()
        
        # Mantiene el programa pausado mientras Morgan habla
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        # Descarga el archivo de la memoria y lo elimina para mantener limpio el sistema
        pygame.mixer.music.unload()
        os.remove(archivo_audio)
    except Exception as e:
        print(f"\n[Error de audio]: No se pudo reproducir la voz. Detalles: {e}")

def modo_chat_interactivo():
    print("==================================================")
    print("--- SISTEMA MORGAN: MODO INTERACTIVO INICIADO ---")
    print("Escribe 'salir' para apagar a Morgan.")
    print("==================================================\n")
    
    while True:
        user_input = input("Tú 👤 > ")
        
        if user_input.lower() == 'salir':
            despedida = "Apagando sistemas de Morgan... Hasta pronto, Señor López."
            print(f"\nMorgan> {despedida}")
            reproducir_voz(despedida)
            break
            
        if not user_input.strip():
            continue
            
        # Procesamos la respuesta con Ollama
        respuesta_morgan = preguntar_a_cerebro(user_input)
        print(f"\nMorgan> {respuesta_morgan}\n")
        
        # Le damos voz a la respuesta
        reproducir_voz(respuesta_morgan)

if __name__ == "__main__":
    modo_chat_interactivo()