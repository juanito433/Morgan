import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os

modelo = whisper.load_model("small")

def escuchar():

    try:

        fs = 44100
        segundos = 5

        print("🎤 Escuchando...")

        audio = sd.rec(
            int(segundos * fs),
            samplerate=fs,
            channels=1
        )

        sd.wait()

        write(
            "temp.wav",
            fs,
            audio
        )

        resultado = modelo.transcribe(
            "temp.wav",
            language="es"
        )

        if os.path.exists("temp.wav"):
            os.remove("temp.wav")

        return resultado["text"]

    except Exception as e:

        print(f"Error Whisper: {e}")
        return None