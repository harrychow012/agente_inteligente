
from datetime import datetime
from memoria import guardar_memoria


def registrar_diagnostico(ventana, causa_confirmada):
    # Actualizar el aprendizaje cuando existe una causa confirmada.
    if causa_confirmada is not None:
        for resultado in ventana.resultados_actuales:
            clave = (
                f"{ventana.categoria_actual}|{resultado['causa']}"
            )

            if clave not in ventana.memoria["aprendizaje"]:
                ventana.memoria["aprendizaje"][clave] = {
                    "aciertos": 0,
                    "fallos": 0
                }

            if resultado["causa"] == causa_confirmada:
                ventana.memoria["aprendizaje"][clave]["aciertos"] += 1
            else:
                ventana.memoria["aprendizaje"][clave]["fallos"] += 1

    # Registrar el diagnóstico.
    caso = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "categoria": ventana.categoria_actual,
        "respuestas": ventana.respuestas_actuales,
        "hipotesis": ventana.resultados_actuales[0]["causa"],
        "causa_confirmada": causa_confirmada
    }

    ventana.memoria.setdefault("casos", []).append(caso)

    guardar_memoria(ventana.memoria)

    return caso
