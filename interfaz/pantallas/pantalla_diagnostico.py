
import tkinter as tk
from tkinter import ttk
from conocimiento import BASE_CONOCIMIENTO


def mostrar_diagnostico(ventana):
    ventana.limpiar_contenido()

    ventana.mostrar_titulo("Diagnosticar una falla")

    tk.Label(
        ventana.contenido,
        text="Selecciona la categoría del problema que deseas analizar.",
        bg=ventana.color_fondo,
        fg=ventana.color_secundario,
        font=("Arial", 11)
    ).pack(anchor="w", pady=(5, 20))

    # Selector de categorías.
    tk.Label(
        ventana.contenido,
        text="Categoría del problema",
        bg=ventana.color_fondo,
        fg=ventana.color_texto,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(0, 8))

    ventana.categoria_seleccionada = tk.StringVar()

    categorias = [
        f"{clave} - {datos['nombre']}"
        for clave, datos in BASE_CONOCIMIENTO.items()
    ]

    selector = ttk.Combobox(
        ventana.contenido,
        textvariable=ventana.categoria_seleccionada,
        values=categorias,
        state="readonly",
        font=("Arial", 11),
        width=40
    )
    selector.pack(anchor="w", pady=(0, 20))

    # Contenedor de preguntas.
    ventana.contenedor_preguntas = tk.Frame(
        ventana.contenido,
        bg=ventana.color_fondo
    )
    ventana.contenedor_preguntas.pack(
        fill="both",
        expand=True,
        anchor="w"
    )

    ventana.respuestas = {}

    def cargar_preguntas(event=None):
        for widget in ventana.contenedor_preguntas.winfo_children():
            widget.destroy()

        ventana.respuestas.clear()

        seleccion = ventana.categoria_seleccionada.get()

        if not seleccion:
            return

        clave = seleccion.split(" - ")[0]
        datos = BASE_CONOCIMIENTO[clave]

        tk.Label(
            ventana.contenedor_preguntas,
            text="Responde las siguientes preguntas:",
            bg=ventana.color_fondo,
            fg=ventana.color_acento,
            font=("Arial", 13, "bold")
        ).pack(anchor="w", pady=(0, 15))

        for sintoma, pregunta in datos["preguntas"]:
            tarjeta = tk.Frame(
                ventana.contenedor_preguntas,
                bg=ventana.color_tarjeta,
                padx=15,
                pady=12
            )
            tarjeta.pack(fill="x", pady=6)

            tk.Label(
                tarjeta,
                text=pregunta,
                bg=ventana.color_tarjeta,
                fg=ventana.color_texto,
                font=("Arial", 10)
            ).pack(anchor="w", pady=(0, 8))

            respuesta = tk.StringVar(value="")
            ventana.respuestas[sintoma] = respuesta

            opciones = tk.Frame(
                tarjeta,
                bg=ventana.color_tarjeta
            )
            opciones.pack(anchor="w")

            for valor, texto in [("si", "Sí"), ("no", "No")]:
                tk.Radiobutton(
                    opciones,
                    text=texto,
                    variable=respuesta,
                    value=valor,
                    bg=ventana.color_tarjeta,
                    fg=ventana.color_texto,
                    selectcolor=ventana.color_sidebar,
                    activebackground=ventana.color_tarjeta,
                    activeforeground=ventana.color_acento,
                    font=("Arial", 10)
                ).pack(side="left", padx=(0, 20))

    selector.bind("<<ComboboxSelected>>", cargar_preguntas)

    tk.Label(
        ventana.contenedor_preguntas,
        text="Primero selecciona una categoría para mostrar sus preguntas.",
        bg=ventana.color_fondo,
        fg=ventana.color_secundario,
        font=("Arial", 10)
    ).pack(anchor="w", pady=15)

    ttk.Button(
        ventana.contenido,
        text="Analizar diagnóstico",
        command=ventana.analizar_diagnostico
    ).pack(anchor="e", pady=15)
