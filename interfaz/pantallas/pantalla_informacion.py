
import tkinter as tk


def mostrar_informacion(ventana):
    ventana.limpiar_contenido()

    ventana.mostrar_titulo("Información del proyecto")

    tk.Label(
        ventana.contenido,
        text="Conoce el funcionamiento del agente inteligente.",
        bg=ventana.color_fondo,
        fg=ventana.color_secundario,
        font=("Arial", 11)
    ).pack(anchor="w", pady=(5, 20))

    secciones = [
        (
            "Nombre del proyecto",
            "Agente Inteligente para Diagnosticar Fallas Informáticas"
        ),
        (
            "Objetivo",
            "Ayudar a identificar posibles causas de fallas informáticas "
            "mediante preguntas sobre los síntomas y un sistema de "
            "razonamiento basado en reglas."
        ),
        (
            "Categorías de diagnóstico",
            "• Redes e Internet\n"
            "• Computadoras\n"
            "• Aplicaciones\n"
            "• Bases de datos"
        ),
        (
            "Funcionamiento",
            "El usuario selecciona una categoría y responde preguntas "
            "sobre los síntomas. El agente calcula puntuaciones, ordena "
            "las posibles causas y presenta una recomendación. "
            "Posteriormente, el usuario puede confirmar el resultado "
            "para actualizar la memoria."
        ),
        (
            "Memoria y aprendizaje",
            "El sistema almacena los casos y registra aciertos y fallos "
            "en memoria.json. Esta información permite ajustar las "
            "puntuaciones de futuros diagnósticos."
        ),
        (
            "Tecnologías utilizadas",
            "Python, Tkinter y almacenamiento JSON."
        ),
        (
            "Asignatura",
            "Fundamentos de Inteligencia Artificial"
        ),
        (
            "Integrantes",
            "Alvaro Ortiz Cuz\nHarry Chow Duarte"
        )
    ]

    for titulo, descripcion in secciones:
        tarjeta = tk.Frame(
            ventana.contenido,
            bg=ventana.color_tarjeta,
            padx=18,
            pady=14
        )
        tarjeta.pack(fill="x", pady=6)

        tk.Label(
            tarjeta,
            text=titulo,
            bg=ventana.color_tarjeta,
            fg=ventana.color_acento,
            font=("Arial", 11, "bold")
        ).pack(anchor="w")

        tk.Label(
            tarjeta,
            text=descripcion,
            bg=ventana.color_tarjeta,
            fg=ventana.color_texto,
            font=("Arial", 10),
            justify="left",
            wraplength=750
        ).pack(anchor="w", pady=(6, 0))
