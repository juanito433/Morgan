from gtts import gTTS
import pygame
import os
import time

pygame.mixer.init()

def hablar(texto):

    try:

        archivo = "voz_morgan.mp3"

        tts = gTTS(
            text=texto,
            lang="es",
            tld="com.mx"
        )

        tts.save(archivo)

        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()

        if os.path.exists(archivo):
            os.remove(archivo)

    except Exception as e:
        print(f"[ERROR DE VOZ]: {e}")