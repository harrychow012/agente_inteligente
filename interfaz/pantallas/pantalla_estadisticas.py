
import tkinter as tk
from memoria import cargar_memoria


def mostrar_estadisticas(ventana):
    ventana.limpiar_contenido()

    # Cargar los datos actualizados.
    ventana.memoria = cargar_memoria()

    ventana.mostrar_titulo("Estadísticas del agente")

    casos = ventana.memoria.get("casos", [])
    aprendizaje = ventana.memoria.get("aprendizaje", {})

    # Calcular estadísticas generales.
    total_casos = len(casos)

    casos_confirmados = [
        caso for caso in casos
        if caso.get("causa_confirmada") is not None
    ]

    total_confirmados = len(casos_confirmados)

    coincidencias = sum(
        1 for caso in casos_confirmados
        if caso.get("hipotesis") == caso.get("causa_confirmada")
    )

    if total_confirmados > 0:
        porcentaje = (coincidencias / total_confirmados) * 100
    else:
        porcentaje = 0

    # Calcular aciertos y fallos.
    total_aciertos = sum(
        datos.get("aciertos", 0)
        for datos in aprendizaje.values()
    )

    total_fallos = sum(
        datos.get("fallos", 0)
        for datos in aprendizaje.values()
    )

    tk.Label(
        ventana.contenido,
        text="Resumen del rendimiento y aprendizaje del agente.",
        bg=ventana.color_fondo,
        fg=ventana.color_secundario,
        font=("Arial", 11)
    ).pack(anchor="w", pady=(5, 20))

    # Contenedor de tarjetas.
    contenedor_tarjetas = tk.Frame(
        ventana.contenido,
        bg=ventana.color_fondo
    )
    contenedor_tarjetas.pack(fill="x")

    estadisticas = [
        ("Diagnósticos realizados", total_casos),
        ("Casos confirmados", total_confirmados),
        ("Coincidencias iniciales", coincidencias),
        ("Porcentaje de coincidencias", f"{porcentaje:.1f}%")
    ]

    for indice, (titulo, valor) in enumerate(estadisticas):
        fila = indice // 2
        columna = indice % 2

        tarjeta = tk.Frame(
            contenedor_tarjetas,
            bg=ventana.color_tarjeta,
            padx=20,
            pady=20
        )

        tarjeta.grid(
            row=fila,
            column=columna,
            sticky="nsew",
            padx=7,
            pady=7
        )

        tk.Label(
            tarjeta,
            text=titulo,
            bg=ventana.color_tarjeta,
            fg=ventana.color_secundario,
            font=("Arial", 10)
        ).pack(anchor="w")

        tk.Label(
            tarjeta,
            text=str(valor),
            bg=ventana.color_tarjeta,
            fg=ventana.color_acento,
            font=("Arial", 23, "bold")
        ).pack(anchor="w", pady=(8, 0))

    contenedor_tarjetas.grid_columnconfigure(0, weight=1)
    contenedor_tarjetas.grid_columnconfigure(1, weight=1)

    # Resumen del aprendizaje.
    tk.Label(
        ventana.contenido,
        text="Aprendizaje acumulado",
        bg=ventana.color_fondo,
        fg=ventana.color_texto,
        font=("Arial", 15, "bold")
    ).pack(anchor="w", pady=(25, 12))

    tarjeta_aprendizaje = tk.Frame(
        ventana.contenido,
        bg=ventana.color_tarjeta,
        padx=20,
        pady=20
    )
    tarjeta_aprendizaje.pack(fill="x")

    tk.Label(
        tarjeta_aprendizaje,
        text=f"Aciertos registrados: {total_aciertos}",
        bg=ventana.color_tarjeta,
        fg="#4ADE80",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", pady=5)

    tk.Label(
        tarjeta_aprendizaje,
        text=f"Fallos registrados: {total_fallos}",
        bg=ventana.color_tarjeta,
        fg="#F87171",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", pady=5)

    # Explicación del porcentaje.
    tk.Label(
        ventana.contenido,
        text=(
            "El porcentaje de coincidencias compara la primera hipótesis "
            "del agente con la causa confirmada por el usuario. "
            "No representa una probabilidad de diagnóstico."
        ),
        bg=ventana.color_fondo,
        fg=ventana.color_secundario,
        font=("Arial", 9),
        wraplength=750,
        justify="left"
    ).pack(anchor="w", pady=20)
