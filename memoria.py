
import json
import os

ARCHIVO_MEMORIA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "memoria.json"
)


def cargar_memoria():
    if not os.path.exists(ARCHIVO_MEMORIA):
        return {"casos": [], "aprendizaje": {}}

    try:
        with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as archivo:
            memoria = json.load(archivo)

        memoria.setdefault("casos", [])
        memoria.setdefault("aprendizaje", {})
        return memoria

    except (json.JSONDecodeError, OSError):
        print("Aviso: no se pudo leer la memoria. Se iniciará vacía.")
        return {"casos": [], "aprendizaje": {}}


def guardar_memoria(memoria):
    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as archivo:
        json.dump(memoria, archivo, indent=4, ensure_ascii=False)
