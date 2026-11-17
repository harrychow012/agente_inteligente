
import tkinter as tk


def mostrar_inicio(ventana):
    ventana.limpiar_contenido()

    tk.Label(
        ventana.contenido,
        text="Panel principal",
        font=("Arial", 25, "bold"),
        bg=ventana.color_fondo,
        fg=ventana.color_texto
    ).pack(anchor="w")

    tk.Label(
        ventana.contenido,
        text="Bienvenido al Agente Inteligente de Diagnóstico Informático",
        font=("Arial", 11),
        bg=ventana.color_fondo,
        fg=ventana.color_secundario
    ).pack(anchor="w", pady=(5, 30))

    tarjetas = [
        ("Diagnóstico", "Identifica posibles fallas informáticas."),
        ("Memoria", "Consulta los casos registrados."),
        ("Estadísticas", "Visualiza los resultados del agente.")
    ]

    for titulo, descripcion in tarjetas:
        tarjeta = tk.Frame(
            ventana.contenido,
            bg=ventana.color_tarjeta,
            padx=20,
            pady=20
        )
        tarjeta.pack(fill="x", pady=8)

        tk.Label(
            tarjeta,
            text=titulo,
            font=("Arial", 15, "bold"),
            bg=ventana.color_tarjeta,
            fg=ventana.color_acento
        ).pack(anchor="w")

        tk.Label(
            tarjeta,
            text=descripcion,
            font=("Arial", 10),
            bg=ventana.color_tarjeta,
            fg=ventana.color_texto
        ).pack(anchor="w", pady=(8, 0))
