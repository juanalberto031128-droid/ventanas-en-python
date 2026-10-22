"""
==============================================================================
main.py - Lanzador Interactivo del Repositorio Tkinter Masterclass
==============================================================================
Este panel de control gráfico te permite explorar y ejecutar cualquiera de los
10 ejemplos del repositorio con un solo clic. Cada ejemplo se lanza en un
proceso independiente, permitiéndote interactuar con ellos en paralelo.
==============================================================================
"""

import os
import subprocess
import sys
import tkinter as tk
from tkinter import ttk, messagebox


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en el monitor del usuario."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


# Catálogo de demostraciones disponibles
DEMOS = [
    {
        "id": "01",
        "archivo": "01_ventana_basica.py",
        "titulo": "Ventana Básica y Propiedades",
        "dificultad": "Básico",
        "color_dificultad": "#10b981",
        "descripcion": "Inicialización con Tk(), centrado en pantalla, minsize/maxsize, protocolo WM_DELETE_WINDOW y cambio de tema claro/oscuro.",
    },
    {
        "id": "02",
        "archivo": "02_widgets_fundamentales.py",
        "titulo": "Widgets Fundamentales y Reactividad",
        "dificultad": "Básico",
        "color_dificultad": "#10b981",
        "descripcion": "Label, Entry (con ocultación de clave), Button, Checkbutton, Radiobutton, LabelFrame y variables reactivas (StringVar/trace_add).",
    },
    {
        "id": "03",
        "archivo": "03_layout_managers.py",
        "titulo": "Gestores de Geometría (pack, grid, place)",
        "dificultad": "Intermedio",
        "color_dificultad": "#0284c7",
        "descripcion": "Demostración visual comparativa de los tres administradores de diseño en pestañas (Notebook), con pesos y responsividad.",
    },
    {
        "id": "04",
        "archivo": "04_ttk_widgets_modernos.py",
        "titulo": "Widgets Temáticos Avanzados (ttk)",
        "dificultad": "Intermedio",
        "color_dificultad": "#0284c7",
        "descripcion": "Catálogo ttk con Treeview (tabla interactiva con columnas), Combobox con cambio de tema en vivo, Progressbar animada y Scale.",
    },
    {
        "id": "05",
        "archivo": "05_eventos_y_bindings.py",
        "titulo": "Sistema de Eventos y Atajos (bind)",
        "dificultad": "Intermedio",
        "color_dificultad": "#0284c7",
        "descripcion": "Laboratorio de eventos: clics de ratón, arrastres, teclado, atajos combinados (Ctrl+S, Ctrl+L), coordenadas y consola de inspección.",
    },
    {
        "id": "06",
        "archivo": "06_cuadros_de_dialogo.py",
        "titulo": "Cuadros de Diálogo Nativos",
        "dificultad": "Básico",
        "color_dificultad": "#10b981",
        "descripcion": "Uso de messagebox (alertas y confirmaciones), filedialog (abrir/guardar archivos/carpetas), colorchooser y simpledialog.",
    },
    {
        "id": "07",
        "archivo": "07_canvas_y_dibujo.py",
        "titulo": "Gráficos 2D, Animación y Drag & Drop",
        "dificultad": "Avanzado",
        "color_dificultad": "#8b5cf6",
        "descripcion": "Lienzo Canvas con primitivas vectoriales, física de rebote con .after(), arrastrar y soltar figuras, y pizarra a mano alzada.",
    },
    {
        "id": "08",
        "archivo": "08_menus_y_navegacion.py",
        "titulo": "Menús, Toolbar y Barra de Estado",
        "dificultad": "Intermedio",
        "color_dificultad": "#0284c7",
        "descripcion": "Barra de menú principal con cascadas, aceleradores, checkbuttons, menú contextual con clic derecho, toolbar y statusbar reactiva.",
    },
    {
        "id": "09",
        "archivo": "09_editor_texto_avanzado.py",
        "titulo": "Editor de Texto con Tags y Formato",
        "dificultad": "Avanzado",
        "color_dificultad": "#8b5cf6",
        "descripcion": "Widget Text multilínea con formato por etiquetas (negrita, cursiva, subrayado, resaltado), búsqueda por texto, undo/redo y estadísticas.",
    },
    {
        "id": "10",
        "archivo": "10_app_poo_to_do.py",
        "titulo": "Gestor de Tareas POO con Persistencia",
        "dificultad": "Avanzado",
        "color_dificultad": "#8b5cf6",
        "descripcion": "Aplicación completa orientada a objetos (POO), arquitectura modular, separación de capas, persistencia JSON y filtrado dinámico.",
    },
]


class LanzadorRepositorio:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tkinter Masterclass - Lanzador Interactivo de Ejemplos")
        centrar_ventana(self.root, 960, 720)
        self.root.minsize(860, 600)
        self.root.configure(bg="#f1f5f9")

        self.directorio_base = os.path.dirname(os.path.abspath(__file__))
        self.directorio_ejemplos = os.path.join(self.directorio_base, "ejemplos")

        self.filtro_texto = tk.StringVar()
        self.filtro_texto.trace_add("write", lambda *args: self._poblar_tarjetas())

        self._crear_encabezado()
        self._crear_barra_busqueda()
        self._crear_area_scroll()
        self._poblar_tarjetas()

    def _crear_encabezado(self) -> None:
        header = tk.Frame(self.root, bg="#0f172a", padx=30, pady=20)
        header.pack(fill="x")

        tk.Label(
            header,
            text="🚀 Tkinter Masterclass - Repositorio de Ejemplos en Python",
            font=("Segoe UI", 16, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Explora 10 ejemplos prácticos y completos diseñados para dominar el desarrollo de GUIs de escritorio con Python.",
            font=("Segoe UI", 10),
            bg="#0f172a",
            fg="#94a3b8"
        ).pack(anchor="w", pady=(4, 0))

    def _crear_barra_busqueda(self) -> None:
        frame_busqueda = tk.Frame(self.root, bg="#f1f5f9", padx=30, pady=12)
        frame_busqueda.pack(fill="x")

        tk.Label(frame_busqueda, text="Filtrar ejemplos:", font=("Segoe UI", 10, "bold"), bg="#f1f5f9", fg="#334155").pack(side="left", padx=(0, 8))

        entry_buscar = ttk.Entry(frame_busqueda, textvariable=self.filtro_texto, font=("Segoe UI", 10), width=35)
        entry_buscar.pack(side="left")

        btn_limpiar = ttk.Button(frame_busqueda, text="Limpiar", command=lambda: self.filtro_texto.set(""))
        btn_limpiar.pack(side="left", padx=8)

        self.lbl_contador = tk.Label(frame_busqueda, text="", font=("Segoe UI", 9, "italic"), bg="#f1f5f9", fg="#64748b")
        self.lbl_contador.pack(side="right")

    def _crear_area_scroll(self) -> None:
        contenedor = tk.Frame(self.root, bg="#f1f5f9")
        contenedor.pack(fill="both", expand=True, padx=30, pady=(0, 15))

        self.canvas_scroll = tk.Canvas(contenedor, bg="#f1f5f9", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=self.canvas_scroll.yview)
        self.frame_tarjetas = tk.Frame(self.canvas_scroll, bg="#f1f5f9")

        self.frame_tarjetas.bind(
            "<Configure>",
            lambda e: self.canvas_scroll.configure(scrollregion=self.canvas_scroll.bbox("all"))
        )

        self.canvas_window = self.canvas_scroll.create_window((0, 0), window=self.frame_tarjetas, anchor="nw")
        self.canvas_scroll.configure(yscrollcommand=self.scrollbar.set)

        # Ajustar ancho del contenido al tamaño del canvas
        self.canvas_scroll.bind(
            "<Configure>",
            lambda e: self.canvas_scroll.itemconfig(self.canvas_window, width=e.width)
        )

        # Soporte para rueda del ratón
        self.canvas_scroll.bind_all("<MouseWheel>", self._on_mousewheel)

        self.canvas_scroll.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(self, event) -> None:
        self.canvas_scroll.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _poblar_tarjetas(self) -> None:
        # Limpiar tarjetas existentes
        for widget in self.frame_tarjetas.winfo_children():
            widget.destroy()

        filtro = self.filtro_texto.get().strip().lower()
        demos_filtradas = [
            d for d in DEMOS
            if filtro in d["titulo"].lower() or filtro in d["descripcion"].lower() or filtro in d["dificultad"].lower()
        ]

        self.lbl_contador.configure(text=f"Mostrando {len(demos_filtradas)} de {len(DEMOS)} ejemplos")

        for demo in demos_filtradas:
            self._crear_tarjeta_demo(demo)

    def _crear_tarjeta_demo(self, demo: dict) -> None:
        card = tk.Frame(self.frame_tarjetas, bg="#ffffff", bd=1, relief="solid", padx=16, pady=14)
        card.pack(fill="x", pady=6)

        # Fila superior de la tarjeta: Título + Badge de Dificultad
        fila_sup = tk.Frame(card, bg="#ffffff")
        fila_sup.pack(fill="x")

        lbl_titulo = tk.Label(
            fila_sup,
            text=f"{demo['id']}. {demo['titulo']}",
            font=("Segoe UI", 11, "bold"),
            bg="#ffffff",
            fg="#0f172a"
        )
        lbl_titulo.pack(side="left")

        badge_dificultad = tk.Label(
            fila_sup,
            text=f" {demo['dificultad']} ",
            font=("Segoe UI", 8, "bold"),
            bg=demo["color_dificultad"],
            fg="#ffffff",
            padx=6,
            pady=2
        )
        badge_dificultad.pack(side="right")

        # Fila media: Descripción y nombre de archivo
        lbl_desc = tk.Label(
            card,
            text=demo["descripcion"],
            font=("Segoe UI", 9),
            bg="#ffffff",
            fg="#475569",
            justify="left",
            wraplength=700
        )
        lbl_desc.pack(anchor="w", pady=(6, 8))

        # Fila inferior: Ruta de archivo y botón de lanzamiento
        fila_inf = tk.Frame(card, bg="#ffffff")
        fila_inf.pack(fill="x")

        lbl_archivo = tk.Label(
            fila_inf,
            text=f"📁 ejemplos/{demo['archivo']}",
            font=("Consolas", 9),
            bg="#ffffff",
            fg="#0284c7"
        )
        lbl_archivo.pack(side="left")

        btn_lanzar = tk.Button(
            fila_inf,
            text="▶ Ejecutar Demo",
            bg="#0284c7",
            fg="#ffffff",
            activebackground="#0369a1",
            activeforeground="#ffffff",
            font=("Segoe UI", 9, "bold"),
            padx=14,
            pady=4,
            cursor="hand2",
            bd=0,
            command=lambda arch=demo["archivo"]: self._ejecutar_script(arch)
        )
        btn_lanzar.pack(side="right")

    def _ejecutar_script(self, nombre_archivo: str) -> None:
        """Lanza el archivo de Python en un subproceso independiente."""
        ruta_script = os.path.join(self.directorio_ejemplos, nombre_archivo)
        if not os.path.exists(ruta_script):
            messagebox.showerror("Error", f"No se encontró el archivo: {ruta_script}")
            return

        try:
            # sys.executable asegura que use el mismo intérprete de Python
            subprocess.Popen([sys.executable, ruta_script], cwd=self.directorio_base)
        except Exception as e:
            messagebox.showerror("Fallo al Ejecutar", f"Ocurrió un error al lanzar el ejemplo:\n{e}")


def main():
    root = tk.Tk()
    app = LanzadorRepositorio(root)
    root.mainloop()


if __name__ == "__main__":
    main()
