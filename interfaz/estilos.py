
# Colores de la aplicación
COLORES = {
    "fondo": "#111827",
    "sidebar": "#1F2937",
    "tarjeta": "#273449",
    "texto": "#F9FAFB",
    "secundario": "#9CA3AF",
    "acento": "#38BDF8"
}


def configurar_estilos():
    from tkinter import ttk

    estilo = ttk.Style()
    estilo.theme_use("clam")

    estilo.configure(
        "TButton",
        font=("Arial", 11),
        padding=10,
        background=COLORES["tarjeta"],
        foreground=COLORES["texto"]
    )

    estilo.map(
        "TButton",
        background=[("active", COLORES["acento"])],
        foreground=[("active", COLORES["fondo"])]
    )

    estilo.configure(
        "Memoria.Treeview",
        background=COLORES["tarjeta"],
        foreground=COLORES["texto"],
        fieldbackground=COLORES["tarjeta"],
        rowheight=32,
        font=("Arial", 10)
    )

    estilo.configure(
        "Memoria.Treeview.Heading",
        background=COLORES["sidebar"],
        foreground=COLORES["texto"],
        font=("Arial", 10, "bold")
    )
