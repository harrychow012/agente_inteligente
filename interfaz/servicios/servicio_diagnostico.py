
from conocimiento import BASE_CONOCIMIENTO
from motor import obtener_puntuacion


def analizar_diagnostico(ventana):
    seleccion = ventana.categoria_seleccionada.get()

    if not seleccion:
        return None

    if any(
        not respuesta.get()
        for respuesta in ventana.respuestas.values()
    ):
        return None

    clave = seleccion.split(" - ")[0]
    datos = BASE_CONOCIMIENTO[clave]
    nombre_categoria = datos["nombre"]

    # Convertir las respuestas a valores booleanos.
    respuestas = {
        sintoma: respuesta.get() == "si"
        for sintoma, respuesta in ventana.respuestas.items()
    }

    resultados = []

    # Evaluar cada posible causa.
    for causa, informacion in datos["causas"].items():
        puntuacion = obtener_puntuacion(
            ventana.memoria,
            nombre_categoria,
            causa,
            respuestas,
            informacion
        )

        resultados.append({
            "causa": causa,
            "puntuacion": puntuacion,
            "solucion": informacion["solucion"]
        })

    # Ordenar de mayor a menor puntuación.
    resultados.sort(
        key=lambda resultado: resultado["puntuacion"],
        reverse=True
    )

    return {
        "resultados": resultados,
        "categoria": nombre_categoria,
        "respuestas": respuestas
    }
