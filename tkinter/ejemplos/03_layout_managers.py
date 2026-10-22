"""
==============================================================================
03_layout_managers.py - Los Tres Gestores de Geometría en Tkinter
==============================================================================
En Tkinter existen tres gestores de geometría para posicionar widgets:
1. pack(): Empaqueta elementos secuencialmente contra los lados de un contenedor.
2. grid(): Organiza widgets en una cuadrícula bidimensional de filas y columnas.
3. place(): Posiciona widgets con precisión exacta de píxeles o porcentajes relativos.

IMPORTANTE: ¡Nunca mezcles pack() y grid() dentro del MISMO marco contenedor padre!
Hacerlo provocará que la aplicación se congele en un bucle infinito de re-cálculo.

Este script contiene demostraciones visuales interactivas de cada uno mediante
pestañas (ttk.Notebook).
==============================================================================
"""

import tkinter as tk
from tkinter import ttk


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en el monitor del usuario."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


class LayoutManagersDemo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("03 - Gestores de Geometría (pack, grid, place) | Tkinter")
        centrar_ventana(self.root, 800, 620)
        self.root.minsize(700, 500)

        # Configuración de estilos ttk
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Contenedor de pestañas principal
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=15)

        # Crear pestañas individuales
        self._crear_pestana_pack()
        self._crear_pestana_grid()
        self._crear_pestana_place()
        self._crear_pestana_comparativa()

    # =========================================================================
    # PESTAÑA 1: GESTOR PACK()
    # =========================================================================
    def _crear_pestana_pack(self) -> None:
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="1. Gestor pack()")

        lbl_desc = tk.Label(
            tab,
            text="pack(): Ideal para interfaces lineales (de arriba a abajo o izquierda a derecha).\n"
                 "Parámetros clave: side (TOP, BOTTOM, LEFT, RIGHT), fill (X, Y, BOTH), expand (True/False).",
            font=("Segoe UI", 10, "italic"),
            fg="#475569",
            justify="left"
        )
        lbl_desc.pack(fill="x", pady=(0, 10))

        # Contenedor de demostración visual
        visor = tk.Frame(tab, bg="#e2e8f0", bd=2, relief="sunken")
        visor.pack(fill="both", expand=True, pady=10)

        # Barra Superior
        top_bar = tk.Label(visor, text="side=TOP, fill=X", bg="#3b82f6", fg="#ffffff", font=("Segoe UI", 10, "bold"), pady=8)
        top_bar.pack(side="top", fill="x")

        # Barra Inferior
        bottom_bar = tk.Label(visor, text="side=BOTTOM, fill=X", bg="#64748b", fg="#ffffff", font=("Segoe UI", 10, "bold"), pady=8)
        bottom_bar.pack(side="bottom", fill="x")

        # Panel Izquierdo
        left_panel = tk.Label(visor, text="side=LEFT\nfill=Y", bg="#10b981", fg="#ffffff", font=("Segoe UI", 10, "bold"), padx=15)
        left_panel.pack(side="left", fill="y", padx=(0, 5))

        # Panel Central Expandible
        center_panel = tk.Label(visor, text="side=LEFT\nfill=BOTH, expand=True\n(Toma todo el espacio libre)", bg="#f59e0b", fg="#ffffff", font=("Segoe UI", 11, "bold"))
        center_panel.pack(side="left", fill="both", expand=True)

        # Panel Derecho
        right_panel = tk.Label(visor, text="side=RIGHT\nfill=Y", bg="#8b5cf6", fg="#ffffff", font=("Segoe UI", 10, "bold"), padx=15)
        right_panel.pack(side="right", fill="y", padx=(5, 0))

    # =========================================================================
    # PESTAÑA 2: GESTOR GRID()
    # =========================================================================
    def _crear_pestana_grid(self) -> None:
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="2. Gestor grid()")

        lbl_desc = tk.Label(
            tab,
            text="grid(): El más potente para formularios y vistas estructuradas en filas y columnas.\n"
                 "Parámetros: row, column, rowspan, columnspan, sticky ('n', 's', 'e', 'w', 'nsew').\n"
                 "Para que sea responsivo, se debe usar columnconfigure() y rowconfigure() con 'weight'.",
            font=("Segoe UI", 10, "italic"),
            fg="#475569",
            justify="left"
        )
        lbl_desc.pack(fill="x", pady=(0, 10))

        grid_frame = tk.Frame(tab, bg="#f8fafc", bd=2, relief="groove", padx=10, pady=10)
        grid_frame.pack(fill="both", expand=True)

        # Configurar pesos de columnas y filas para adaptabilidad
        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=2)
        grid_frame.columnconfigure(2, weight=1)
        grid_frame.rowconfigure(0, weight=1)
        grid_frame.rowconfigure(1, weight=1)
        grid_frame.rowconfigure(2, weight=2)

        # Casillas de ejemplo
        celda1 = tk.Label(grid_frame, text="Fila 0, Col 0\nsticky='nsew'", bg="#0284c7", fg="white", font=("Segoe UI", 9, "bold"))
        celda1.grid(row=0, column=0, padx=4, pady=4, sticky="nsew")

        celda2 = tk.Label(grid_frame, text="Fila 0, Col 1\nsticky='nsew'", bg="#0ea5e9", fg="white", font=("Segoe UI", 9, "bold"))
        celda2.grid(row=0, column=1, padx=4, pady=4, sticky="nsew")

        celda3 = tk.Label(grid_frame, text="Fila 0, Col 2\nsticky='nsew'", bg="#38bdf8", fg="white", font=("Segoe UI", 9, "bold"))
        celda3.grid(row=0, column=2, padx=4, pady=4, sticky="nsew")

        # Elemento con Columnspan (abarca 2 columnas)
        celda_span_col = tk.Label(
            grid_frame,
            text="Fila 1, Col 0 a 1 (columnspan=2)\nOcupa dos columnas horizontales completas",
            bg="#8b5cf6",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        celda_span_col.grid(row=1, column=0, columnspan=2, padx=4, pady=4, sticky="nsew")

        # Elemento con Rowspan (abarca 2 filas)
        celda_span_row = tk.Label(
            grid_frame,
            text="Col 2\nFila 1 a 2\n(rowspan=2)\nOcupa 2 filas",
            bg="#ec4899",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        celda_span_row.grid(row=1, column=2, rowspan=2, padx=4, pady=4, sticky="nsew")

        # Celda inferior
        celda_inf = tk.Label(
            grid_frame,
            text="Fila 2, Col 0 a 1 (columnspan=2, weight=2 en fila)\nSe expande proporcionalmente al estirar la ventana",
            bg="#10b981",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        celda_inf.grid(row=2, column=0, columnspan=2, padx=4, pady=4, sticky="nsew")

    # =========================================================================
    # PESTAÑA 3: GESTOR PLACE()
    # =========================================================================
    def _crear_pestana_place(self) -> None:
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="3. Gestor place()")

        lbl_desc = tk.Label(
            tab,
            text="place(): Permite posicionamiento milimétrico absoluto o porcentual (relativo).\n"
                 "Parámetros: x, y, width, height (absolutos en px) o relx, rely, relwidth, relheight (0.0 a 1.0).",
            font=("Segoe UI", 10, "italic"),
            fg="#475569",
            justify="left"
        )
        lbl_desc.pack(fill="x", pady=(0, 10))

        lienzo = tk.Frame(tab, bg="#1e293b", bd=2, relief="sunken")
        lienzo.pack(fill="both", expand=True)

        # 1. Coordenadas absolutas
        badge_abs = tk.Label(
            lienzo,
            text="Absoluto: x=30, y=30\nwidth=160, height=70",
            bg="#f43f5e",
            fg="white",
            font=("Segoe UI", 9, "bold")
        )
        badge_abs.place(x=30, y=30, width=160, height=70)

        # 2. Centrado relativo con relx=0.5, rely=0.5, anchor='center'
        badge_center = tk.Label(
            lienzo,
            text="Exactamente al Centro\nrelx=0.5, rely=0.5\nanchor='center'",
            bg="#06b6d4",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        badge_center.place(relx=0.5, rely=0.5, anchor="center", width=220, height=90)

        # 3. Ancho relativo (barra inferior al 90% del ancho)
        badge_rel_w = tk.Label(
            lienzo,
            text="Barra relativa: relx=0.05, rely=0.82, relwidth=0.90, height=45",
            bg="#eab308",
            fg="#0f172a",
            font=("Segoe UI", 9, "bold")
        )
        badge_rel_w.place(relx=0.05, rely=0.82, relwidth=0.90, height=45)

    # =========================================================================
    # PESTAÑA 4: GUÍA COMPARATIVA
    # =========================================================================
    def _crear_pestana_comparativa(self) -> None:
        tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(tab, text="Resumen y Consejos")

        texto_comparativo = (
            "¿CUÁNDO USAR CADA GESTOR DE GEOMETRÍA?\n\n"
            "1. pack():\n"
            "   ✔ Ideal para apilar widgets de arriba a abajo o de izquierda a derecha (ej. barras de menú,\n"
            "     botones inferiores de diálogo, o colocar paneles principales).\n"
            "   ✘ Se vuelve difícil de manejar cuando requieres alinear campos en tablas o formularios complejos.\n\n"
            "2. grid():\n"
            "   ✔ Es el más recomendado para el 80% de interfaces de usuario en el mundo real.\n"
            "   ✔ Excelente para formularios (etiqueta a la izquierda, campo a la derecha) y dashboards.\n"
            "   ✔ Permite adaptabilidad fluida mediante columnconfigure() y rowconfigure() con pesos (weight).\n\n"
            "3. place():\n"
            "   ✔ Ideal para casos específicos donde necesitas superponer widgets sobre imágenes, crear juegos 2D\n"
            "     sencillos o diagramas con posiciones fijas en píxeles.\n"
            "   ✘ Muy poco responsivo: al cambiar el tamaño de ventana o en pantallas con distinto DPI puede verse cortado.\n\n"
            "REGLA DE ORO DE TKINTER:\n"
            "¡NUNCA uses pack() y grid() sobre el mismo widget contenedor/Frame padre!"
        )

        lbl_info = tk.Label(
            tab,
            text=texto_comparativo,
            font=("Consolas", 10),
            bg="#f8fafc",
            fg="#0f172a",
            justify="left",
            padx=15,
            pady=15,
            bd=1,
            relief="groove"
        )
        lbl_info.pack(fill="both", expand=True)


def main():
    root = tk.Tk()
    app = LayoutManagersDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
