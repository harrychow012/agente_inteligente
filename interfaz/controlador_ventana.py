
import tkinter as tk
from tkinter import messagebox

from memoria import cargar_memoria

from interfaz.estilos import COLORES, configurar_estilos

from interfaz.pantallas.pantalla_inicio import mostrar_inicio as construir_inicio
from interfaz.pantallas.pantalla_informacion import mostrar_informacion as construir_informacion
from interfaz.pantallas.pantalla_estadisticas import mostrar_estadisticas as construir_estadisticas
from interfaz.pantallas.pantalla_memoria import mostrar_memoria as construir_memoria
from interfaz.pantallas.pantalla_diagnostico import mostrar_diagnostico as construir_diagnostico
from interfaz.pantallas.pantalla_resultados import mostrar_resultados as construir_resultados

from interfaz.servicios.servicio_diagnostico import analizar_diagnostico as ejecutar_analisis
from interfaz.servicios.servicio_registro import registrar_diagnostico


class VentanaPrincipal:
    def __init__(self, root):
        self.memoria = cargar_memoria()
        self.root = root
        self.root.title("Agente Inteligente | Diagnóstico Informático")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.root.configure(bg="#111827")

        # Colores
       # Cargar colores de la aplicación
        self.color_fondo = COLORES["fondo"]
        self.color_sidebar = COLORES["sidebar"]
        self.color_tarjeta = COLORES["tarjeta"]
        self.color_texto = COLORES["texto"]
        self.color_secundario = COLORES["secundario"]
        self.color_acento = COLORES["acento"]

        configurar_estilos()
        self.crear_interfaz()
       
    def crear_interfaz(self):
        # Contenedor principal
        contenedor = tk.Frame(
            self.root,
            bg=self.color_fondo
        )
        contenedor.pack(fill="both", expand=True)

        # Barra lateral
        self.sidebar = tk.Frame(
            contenedor,
            bg=self.color_sidebar,
            width=230
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.crear_sidebar()

        # Área de contenido
        self.contenido = tk.Frame(
            contenedor,
            bg=self.color_fondo
        )
        self.contenido.pack(
            side="right",
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        self.mostrar_inicio()

    def crear_sidebar(self):
        tk.Label(
            self.sidebar,
            text="AGENTE IA",
            font=("Arial", 20, "bold"),
            bg=self.color_sidebar,
            fg=self.color_acento
        ).pack(pady=(35, 5))

        tk.Label(
            self.sidebar,
            text="Diagnóstico informático",
            font=("Arial", 9),
            bg=self.color_sidebar,
            fg=self.color_secundario
        ).pack(pady=(0, 35))

        opciones = [
            ("Inicio", self.mostrar_inicio),
            ("Diagnosticar falla", self.mostrar_diagnostico),
            ("Memoria", self.mostrar_memoria),
            ("Estadísticas", self.mostrar_estadisticas),
            ("Información", self.mostrar_informacion)
        ]

        for texto, comando in opciones:
            boton = tk.Button(
                self.sidebar,
                text=texto,
                command=comando,
                font=("Arial", 11),
                bg=self.color_sidebar,
                fg=self.color_texto,
                activebackground=self.color_acento,
                activeforeground="#111827",
                relief="flat",
                anchor="w",
                padx=25,
                pady=13,
                cursor="hand2"
            )
            boton.pack(fill="x", padx=10, pady=3)

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        construir_inicio(self)
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Panel principal",
            font=("Arial", 25, "bold"),
            bg=self.color_fondo,
            fg=self.color_texto
        ).pack(anchor="w")

        tk.Label(
            self.contenido,
            text="Bienvenido al Agente Inteligente de Diagnóstico Informático",
            font=("Arial", 11),
            bg=self.color_fondo,
            fg=self.color_secundario
        ).pack(anchor="w", pady=(5, 30))

        tarjetas = [
            ("Diagnóstico", "Identifica posibles fallas informáticas."),
            ("Memoria", "Consulta los casos registrados."),
            ("Estadísticas", "Visualiza los resultados del agente.")
        ]

        for titulo, descripcion in tarjetas:
            tarjeta = tk.Frame(
                self.contenido,
                bg=self.color_tarjeta,
                padx=20,
                pady=20
            )
            tarjeta.pack(fill="x", pady=8)

            tk.Label(
                tarjeta,
                text=titulo,
                font=("Arial", 15, "bold"),
                bg=self.color_tarjeta,
                fg=self.color_acento
            ).pack(anchor="w")

            tk.Label(
                tarjeta,
                text=descripcion,
                font=("Arial", 10),
                bg=self.color_tarjeta,
                fg=self.color_texto
            ).pack(anchor="w", pady=(8, 0))





    def analizar_diagnostico(self):
        if not self.categoria_seleccionada.get():
            messagebox.showwarning(
                "Categoría requerida",
                "Primero selecciona una categoría."
            )
            return

        if any(
            not respuesta.get()
            for respuesta in self.respuestas.values()
        ):
            messagebox.showwarning(
                "Respuestas incompletas",
                "Debes responder todas las preguntas."
            )
            return

        resultado = ejecutar_analisis(self)

        if resultado is None:
            return

        self.resultados_actuales = resultado["resultados"]
        self.categoria_actual = resultado["categoria"]
        self.respuestas_actuales = resultado["respuestas"]
        self.resultado_guardado = False

        self.mostrar_resultados()


    def mostrar_resultados(self):
        construir_resultados(self)

    def confirmar_diagnostico(self):
        causa = self.causa_seleccionada.get()

        if not causa:
            messagebox.showwarning(
                "Confirmación requerida",
                "Selecciona la causa confirmada."
            )
            return

        self.guardar_resultado(causa)



    def guardar_resultado(self, causa_confirmada):
        if self.resultado_guardado:
            return

        registrar_diagnostico(self, causa_confirmada)

        self.resultado_guardado = True

        messagebox.showinfo(
            "Diagnóstico guardado",
            "El diagnóstico se guardó correctamente en la memoria."
        )

    def mostrar_diagnostico(self):
        construir_diagnostico(self)
    
    def mostrar_memoria(self):
        construir_memoria(self)

    
    def mostrar_estadisticas(self):
        construir_estadisticas(self)
        
    def mostrar_informacion(self):
        construir_informacion(self)

    def mostrar_titulo(self, titulo):
        tk.Label(
            self.contenido,
            text=titulo,
            font=("Arial", 25, "bold"),
            bg=self.color_fondo,
            fg=self.color_texto
        ).pack(anchor="w")
