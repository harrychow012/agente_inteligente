
def obtener_puntuacion(memoria, categoria, causa, respuestas, datos):
    puntuacion = 0

    # Obtener los pesos de los síntomas de la causa evaluada.
    reglas = datos["sintomas"]

    for sintoma, respuesta in respuestas.items():
        peso = reglas.get(sintoma, 0)

        if respuesta:
            puntuacion += peso
        else:
            puntuacion -= peso

    # Ajustar la puntuación según el aprendizaje anterior.
    clave = f"{categoria}|{causa}"

    aprendizaje = memoria.get("aprendizaje", {}).get(
        clave,
        {"aciertos": 0, "fallos": 0},
    )

    puntuacion += 2 * aprendizaje.get("aciertos", 0)
    puntuacion -= 2 * aprendizaje.get("fallos", 0)

    return puntuacion
