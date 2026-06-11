from core.brain import generar_respuesta
from core.memory import guardar_interaccion
from core.voice import hablar

from ui.terminal import (
    mostrar_inicio,
    mostrar_usuario,
    mostrar_morgan
)
from ui.desktop import iniciar_app

def iniciar_morgan():

    mostrar_inicio()

    saludo = (
        "Buenos días Señor. "
        "Morgan está en línea y lista para ayudar."
    )

    mostrar_morgan(saludo)
    hablar(saludo)

    while True:

        pregunta = input("\nTú > ")

        if pregunta.lower() == "salir":

            despedida = (
                "Apagando sistemas. "
                "Hasta luego Señor."
            )

            mostrar_morgan(despedida)
            hablar(despedida)

            break

        if not pregunta.strip():
            continue

        respuesta = generar_respuesta(
            pregunta
        )

        guardar_interaccion(
            pregunta,
            respuesta
        )

        mostrar_morgan(
            respuesta
        )

        hablar(
            respuesta
        )

if __name__ == "__main__":
    iniciar_app()