
from datetime import datetime

from conocimiento import BASE_CONOCIMIENTO
from memoria import guardar_memoria
from motor import obtener_puntuacion


def preguntar_si_no(pregunta):
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()

        if respuesta in ("s", "si", "sí"):
            return True
        elif respuesta == "n":
            return False
        else:
            print("Respuesta no válida. Escribe s o n.")


def diagnosticar(memoria):
    print("\n===== DIAGNÓSTICO INFORMÁTICO =====")

    categorias = list(BASE_CONOCIMIENTO.keys())

    for clave in categorias:
        nombre = BASE_CONOCIMIENTO[clave]["nombre"]
        print(f"{clave}. {nombre}")

    while True:
        opcion = input("Selecciona una categoría: ").strip()

        if opcion in categorias:
            categoria = opcion
            break

        print("Opción no válida. Selecciona una categoría de la lista.")

    datos = BASE_CONOCIMIENTO[categoria]
    nombre_categoria = datos["nombre"]
    respuestas = {}

    print(f"\nCategoría seleccionada: {nombre_categoria}")
    print("Responde las siguientes preguntas:\n")

    for sintoma, pregunta in datos["preguntas"]:
        respuestas[sintoma] = preguntar_si_no(pregunta)

    resultados = []

    for causa, informacion in datos["causas"].items():
        puntuacion = obtener_puntuacion(
            memoria,
            nombre_categoria,
            causa,
            respuestas,
            informacion,
        )

        resultados.append({
            "causa": causa,
            "puntuacion": puntuacion,
            "solucion": informacion["solucion"],
        })

    resultados.sort(
        key=lambda resultado: resultado["puntuacion"],
        reverse=True,
    )

    if not resultados:
        print("No hay causas configuradas para esta categoría.")
        return

    print("\n===== RESULTADOS =====")

    for i, resultado in enumerate(resultados, start=1):
        print(
            f"{i}. {resultado['causa']} "
            f"(puntuación: {resultado['puntuacion']})"
        )

    mejor = resultados[0]

    print("\n===== HIPÓTESIS PRINCIPAL =====")
    print(f"Posible causa: {mejor['causa']}")
    print(f"Recomendación: {mejor['solucion']}")

    print("\n¿Cuál fue la causa confirmada?")

    for i, resultado in enumerate(resultados, start=1):
        print(f"{i}. {resultado['causa']}")

    print("0. Todavía no lo sé")

    while True:
        try:
            seleccion = int(input("Selecciona una opción: "))

            if 0 <= seleccion <= len(resultados):
                break

            print("Selecciona un número de la lista.")
        except ValueError:
            print("Debes escribir un número.")

    causa_confirmada = None

    if seleccion != 0:
        causa_confirmada = resultados[seleccion - 1]["causa"]

        for resultado in resultados:
            clave_aprendizaje = (
                f"{nombre_categoria}|{resultado['causa']}"
            )

            if clave_aprendizaje not in memoria["aprendizaje"]:
                memoria["aprendizaje"][clave_aprendizaje] = {
                    "aciertos": 0,
                    "fallos": 0,
                }

            if resultado["causa"] == causa_confirmada:
                memoria["aprendizaje"][clave_aprendizaje]["aciertos"] += 1
            else:
                memoria["aprendizaje"][clave_aprendizaje]["fallos"] += 1

        print("\nAprendizaje actualizado.")

    caso = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "categoria": nombre_categoria,
        "respuestas": respuestas,
        "hipotesis": mejor["causa"],
        "causa_confirmada": causa_confirmada,
    }

    memoria.setdefault("casos", []).append(caso)
    guardar_memoria(memoria)

    print("Diagnóstico guardado en la memoria.")


def mostrar_estadisticas(memoria):
    print("\n===== MEMORIA Y ESTADÍSTICAS =====")

    casos = memoria.get("casos", [])

    print(f"Total de diagnósticos realizados: {len(casos)}")

    if not casos:
        print("Todavía no hay diagnósticos registrados.")
        return

    confirmados = [
        caso for caso in casos
        if caso.get("causa_confirmada") is not None
    ]

    coincidencias = sum(
        1
        for caso in confirmados
        if caso["hipotesis"] == caso["causa_confirmada"]
    )

    print(f"Diagnósticos con causa confirmada: {len(confirmados)}")
    print(f"Hipótesis iniciales acertadas: {coincidencias}")

    if confirmados:
        porcentaje = coincidencias / len(confirmados) * 100
        print(f"Coincidencia de hipótesis: {porcentaje:.1f}%")

    print("\nHistorial de diagnósticos:")

    for i, caso in enumerate(casos, start=1):
        confirmada = caso.get("causa_confirmada") or "Sin confirmar"

        print(f"\n{i}. Fecha: {caso.get('fecha', 'Desconocida')}")
        print(f"   Categoría: {caso.get('categoria', 'Desconocida')}")
        print(f"   Hipótesis: {caso.get('hipotesis', 'Desconocida')}")
        print(f"   Causa confirmada: {confirmada}")
