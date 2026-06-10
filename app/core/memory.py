import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MEMORY_FILE = os.path.join(
    BASE_DIR,
    "data",
    "memory.json"
)

def cargar_memoria():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as archivo:

        return json.load(archivo)

def guardar_interaccion(usuario, respuesta):

    memoria = cargar_memoria()

    memoria.append({
        "usuario": usuario,
        "respuesta": respuesta
    })

    memoria = memoria[-15:]

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            memoria,
            archivo,
            indent=4,
            ensure_ascii=False
        )