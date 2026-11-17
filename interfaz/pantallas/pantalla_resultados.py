
import tkinter as tk
from tkinter import ttk


def mostrar_resultados(ventana):
    ventana.limpiar_contenido()

    tk.Label(
        ventana.contenido,
        text="Resultados del diagnóstico",
        font=("Arial", 25, "bold"),
        bg=ventana.color_fondo,
        fg=ventana.color_texto
    ).pack(anchor="w")

    tk.Label(
        ventana.contenido,
        text=f"Categoría: {ventana.categoria_actual}",
        font=("Arial", 11),
        bg=ventana.color_fondo,
        fg=ventana.color_secundario
    ).pack(anchor="w", pady=(5, 20))

    mejor = ventana.resultados_actuales[0]

    # Hipótesis principal.
    tarjeta = tk.Frame(
        ventana.contenido,
        bg=ventana.color_tarjeta,
        padx=20,
        pady=20
    )
    tarjeta.pack(fill="x", pady=10)

    tk.Label(
        tarjeta,
        text="HIPÓTESIS PRINCIPAL",
        bg=ventana.color_tarjeta,
        fg=ventana.color_acento,
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    tk.Label(
        tarjeta,
        text=mejor["causa"],
        bg=ventana.color_tarjeta,
        fg=ventana.color_texto,
        font=("Arial", 17, "bold")
    ).pack(anchor="w", pady=8)

    tk.Label(
        tarjeta,
        text=f"Puntuación: {mejor['puntuacion']}",
        bg=ventana.color_tarjeta,
        fg=ventana.color_secundario,
        font=("Arial", 10)
    ).pack(anchor="w")

    tk.Label(
        tarjeta,
        text="Recomendación:",
        bg=ventana.color_tarjeta,
        fg=ventana.color_acento,
        font=("Arial", 10, "bold")
    ).pack(anchor="w", pady=(15, 5))

    tk.Label(
        tarjeta,
        text=mejor["solucion"],
        bg=ventana.color_tarjeta,
        fg=ventana.color_texto,
        font=("Arial", 10),
        wraplength=650,
        justify="left"
    ).pack(anchor="w")

    # Otras posibles causas.
    tk.Label(
        ventana.contenido,
        text="Otras posibles causas",
        bg=ventana.color_fondo,
        fg=ventana.color_texto,
        font=("Arial", 14, "bold")
    ).pack(anchor="w", pady=(15, 8))

    for indice, resultado in enumerate(
        ventana.resultados_actuales[1:],
        start=2
    ):
        tk.Label(
            ventana.contenido,
            text=(
                f"{indice}. {resultado['causa']} "
                f"— Puntuación: {resultado['puntuacion']}"
            ),
            bg=ventana.color_fondo,
            fg=ventana.color_secundario,
            font=("Arial", 10)
        ).pack(anchor="w", pady=3)

    # Confirmación de la causa.
    tk.Label(
        ventana.contenido,
        text="¿Cuál fue la causa confirmada?",
        bg=ventana.color_fondo,
        fg=ventana.color_texto,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(20, 8))

    opciones = [
        resultado["causa"]
        for resultado in ventana.resultados_actuales
    ]

    ventana.causa_seleccionada = tk.StringVar()

    selector = ttk.Combobox(
        ventana.contenido,
        textvariable=ventana.causa_seleccionada,
        values=opciones,
        state="readonly",
        width=45
    )
    selector.pack(anchor="w", pady=5)

    botones = tk.Frame(
        ventana.contenido,
        bg=ventana.color_fondo
    )
    botones.pack(anchor="w", pady=15)

    ttk.Button(
        botones,
        text="Confirmar y guardar",
        command=ventana.confirmar_diagnostico
    ).pack(side="left", padx=(0, 10))

    ttk.Button(
        botones,
        text="Todavía no lo sé",
        command=lambda: ventana.guardar_resultado(None)
    ).pack(side="left")
