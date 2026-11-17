
import tkinter as tk
from tkinter import ttk
from memoria import cargar_memoria


def mostrar_memoria(ventana):
    ventana.limpiar_contenido()

    # Recargar los datos guardados.
    ventana.memoria = cargar_memoria()

    ventana.mostrar_titulo("Memoria del agente")

    casos = ventana.memoria.get("casos", [])

    tk.Label(
        ventana.contenido,
        text="Historial de diagnósticos registrados por el agente.",
        bg=ventana.color_fondo,
        fg=ventana.color_secundario,
        font=("Arial", 11)
    ).pack(anchor="w", pady=(5, 15))

    # Total de casos.
    tk.Label(
        ventana.contenido,
        text=f"Total de diagnósticos registrados: {len(casos)}",
        bg=ventana.color_tarjeta,
        fg=ventana.color_acento,
        font=("Arial", 12, "bold"),
        padx=15,
        pady=15
    ).pack(fill="x", pady=(0, 20))

    # Comprobar si existen registros.
    if not casos:
        tk.Label(
            ventana.contenido,
            text="Todavía no existen diagnósticos registrados.",
            bg=ventana.color_fondo,
            fg=ventana.color_secundario,
            font=("Arial", 11)
        ).pack(anchor="w", pady=20)
        return

    # Contenedor de la tabla.
    contenedor_tabla = tk.Frame(
        ventana.contenido,
        bg=ventana.color_fondo
    )
    contenedor_tabla.pack(fill="both", expand=True)

    columnas = (
        "fecha",
        "categoria",
        "hipotesis",
        "causa"
    )

    tabla = ttk.Treeview(
        contenedor_tabla,
        columns=columnas,
        show="headings",
        height=12,
        style="Memoria.Treeview"
    )

    tabla.heading("fecha", text="Fecha")
    tabla.heading("categoria", text="Categoría")
    tabla.heading("hipotesis", text="Hipótesis inicial")
    tabla.heading("causa", text="Causa confirmada")

    tabla.column("fecha", width=150, anchor="center")
    tabla.column("categoria", width=150, anchor="center")
    tabla.column("hipotesis", width=200, anchor="w")
    tabla.column("causa", width=200, anchor="w")

    # Barra de desplazamiento.
    scrollbar = ttk.Scrollbar(
        contenedor_tabla,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(yscrollcommand=scrollbar.set)

    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Insertar los registros más recientes primero.
    for caso in reversed(casos):
        causa = caso.get("causa_confirmada")

        if causa is None:
            causa = "Sin confirmar"

        tabla.insert(
            "",
            "end",
            values=(
                caso.get("fecha", "Sin fecha"),
                caso.get("categoria", "Sin categoría"),
                caso.get("hipotesis", "Sin hipótesis"),
                causa
            )
        )
