import whisper
import sounddevice as sd
from scipy.io.wavfile import write

modelo = whisper.load_model("base")

def escuchar():

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

    return resultado["text"]