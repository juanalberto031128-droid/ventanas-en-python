"""
==============================================================================
04_ttk_widgets_modernos.py - Widgets Temáticos Avanzados con ttk
==============================================================================
El submódulo tkinter.ttk (Themed Tkinter) proporciona widgets modernos que
separan la lógica funcional del estilo visual, adoptando la apariencia nativa
del sistema operativo o permitiendo temas personalizados consistentes.

Widgets y conceptos cubiertos:
- ttk.Style: Selección de temas (clam, alt, default, vista) y estilización personalizada.
- ttk.Combobox: Listas desplegables con evento de selección <<ComboboxSelected>>.
- ttk.Progressbar: Modos determinista (progreso porcentual) e indeterminado (spinner continuo).
- ttk.Treeview: Tablas de datos relacionales con encabezados, ordenamiento y scrollbars.
- ttk.Scale: Deslizadores de rango numérico continuo con lectura en tiempo real.
- ttk.Spinbox: Selectores numéricos con botones integrados de incremento/decremento.
- ttk.Separator: Divisores visuales sutiles entre secciones.
==============================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en el monitor del usuario."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


class ModernTtkDemo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("04 - Widgets Temáticos Modernos (ttk) | Tkinter")
        centrar_ventana(self.root, 820, 680)
        self.root.minsize(750, 600)

        # ---------------------------------------------------------------------
        # Configuración del Motor de Temas y Estilos (ttk.Style)
        # ---------------------------------------------------------------------
        self.style = ttk.Style()
        temas_disponibles = self.style.theme_names()
        # Usamos clam o vista si están disponibles
        if "clam" in temas_disponibles:
            self.style.theme_use("clam")

        # Configurar estilos de fuentes y colores personalizados
        self.style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"), foreground="#1e293b")
        self.style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), foreground="#ffffff", background="#0284c7")
        self.style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))
        self.style.configure("Treeview", font=("Segoe UI", 9), rowheight=24)

        # Variables de control
        self.progreso_valor = tk.DoubleVar(value=35.0)
        self.scale_valor = tk.DoubleVar(value=50.0)
        self.spin_valor = tk.IntVar(value=5)

        self._construir_ui()

    def _construir_ui(self) -> None:
        # Encabezado
        header_frame = ttk.Frame(self.root, padding=(20, 15, 20, 10))
        header_frame.pack(fill="x")

        ttk.Label(header_frame, text="Catálogo de Widgets Temáticos (ttk)", style="Header.TLabel").pack(anchor="w")
        ttk.Label(
            header_frame,
            text="Demostración de Combobox, Progressbar, Treeview (tabla) y control de temas.",
            font=("Segoe UI", 9),
            foreground="#64748b"
        ).pack(anchor="w", pady=(2, 0))

        # Divisor horizontal
        ttk.Separator(self.root, orient="horizontal").pack(fill="x", padx=20, pady=5)

        # Contenedor dividido en dos columnas (Izquierda: controles, Derecha: Treeview)
        cuerpo = ttk.Frame(self.root, padding=20)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.columnconfigure(0, weight=1)
        cuerpo.columnconfigure(1, weight=2)
        cuerpo.rowconfigure(0, weight=1)

        # =====================================================================
        # COLUMNA IZQUIERDA: Combobox, Progressbar, Slider y Spinbox
        # =====================================================================
        panel_izq = ttk.LabelFrame(cuerpo, text=" Controles Interactivos ", padding=15)
        panel_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        # 1. Combobox (Selector de Tema)
        ttk.Label(panel_izq, text="Selector de Tema ttk (Combobox):", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        self.cbo_temas = ttk.Combobox(
            panel_izq,
            values=list(self.style.theme_names()),
            state="readonly"
        )
        self.cbo_temas.set(self.style.theme_use())
        self.cbo_temas.pack(fill="x", pady=(2, 12))
        self.cbo_temas.bind("<<ComboboxSelected>>", self._cambiar_tema)

        # 2. Progressbar (Determinista e Indeterminada)
        ttk.Label(panel_izq, text="Barra de Progreso (Progressbar):", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        self.pbar = ttk.Progressbar(panel_izq, variable=self.progreso_valor, maximum=100)
        self.pbar.pack(fill="x", pady=(2, 6))

        pbar_btns = ttk.Frame(panel_izq)
        pbar_btns.pack(fill="x", pady=(0, 12))
        ttk.Button(pbar_btns, text="+10%", width=6, command=lambda: self._ajustar_progreso(10)).pack(side="left", padx=2)
        ttk.Button(pbar_btns, text="-10%", width=6, command=lambda: self._ajustar_progreso(-10)).pack(side="left", padx=2)
        self.btn_animar = ttk.Button(pbar_btns, text="Animar", width=8, command=self._toggle_animacion_pbar)
        self.btn_animar.pack(side="left", padx=2)
        self.animando_pbar = False

        # 3. Scale (Deslizador)
        ttk.Label(panel_izq, text="Control Deslizante (Scale):", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        self.lbl_scale = ttk.Label(panel_izq, text=f"Valor actual: {self.scale_valor.get():.0f}%")
        self.lbl_scale.pack(anchor="w")
        scale = ttk.Scale(
            panel_izq,
            from_=0,
            to=100,
            orient="horizontal",
            variable=self.scale_valor,
            command=self._on_scale_change
        )
        scale.pack(fill="x", pady=(2, 12))

        # 4. Spinbox (Contador numérico)
        ttk.Label(panel_izq, text="Selector Numérico (Spinbox):", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        spin = ttk.Spinbox(
            panel_izq,
            from_=1,
            to=50,
            textvariable=self.spin_valor,
            wrap=True,
            state="readonly"
        )
        spin.pack(fill="x", pady=(2, 10))

        # =====================================================================
        # COLUMNA DERECHA: Treeview (Tabla de Datos con Scrollbars)
        # =====================================================================
        panel_der = ttk.LabelFrame(cuerpo, text=" Tabla de Datos (ttk.Treeview) ", padding=15)
        panel_der.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        panel_der.rowconfigure(0, weight=1)
        panel_der.columnconfigure(0, weight=1)

        # Definir columnas del Treeview
        columnas = ("id", "nombre", "categoria", "precio", "stock")
        self.tree = ttk.Treeview(panel_der, columns=columnas, show="headings", selectmode="browse")

        # Configurar encabezados y anchos
        self.tree.heading("id", text="ID", anchor="center")
        self.tree.heading("nombre", text="Producto", anchor="w")
        self.tree.heading("categoria", text="Categoría", anchor="w")
        self.tree.heading("precio", text="Precio ($)", anchor="e")
        self.tree.heading("stock", text="Stock", anchor="center")

        self.tree.column("id", width=45, anchor="center")
        self.tree.column("nombre", width=140, anchor="w")
        self.tree.column("categoria", width=100, anchor="w")
        self.tree.column("precio", width=75, anchor="e")
        self.tree.column("stock", width=55, anchor="center")

        # Scrollbars acopladas
        scroll_y = ttk.Scrollbar(panel_der, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll_y.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")

        # Cargar datos ficticios
        self._cargar_datos_treeview()

        # Evento de selección de fila
        self.tree.bind("<<TreeviewSelect>>", self._on_treeview_select)

        # Panel inferior del Treeview con acciones
        tree_actions = ttk.Frame(panel_der)
        tree_actions.grid(row=1, column=0, columnspan=2, fill="x", pady=(10, 0))

        self.lbl_seleccion = ttk.Label(tree_actions, text="Selecciona un producto para ver detalles.", font=("Segoe UI", 9, "italic"))
        self.lbl_seleccion.pack(side="left")

        btn_eliminar = ttk.Button(tree_actions, text="Eliminar Fila", command=self._eliminar_fila_seleccionada)
        btn_eliminar.pack(side="right")

    def _cargar_datos_treeview(self) -> None:
        """Inserta registros de ejemplo en la tabla."""
        productos = [
            (101, "Teclado Mecánico RGB", "Periféricos", 79.99, 14),
            (102, "Ratón Ergonómico Inalámbrico", "Periféricos", 45.50, 22),
            (103, "Monitor 27'' IPS 144Hz", "Pantallas", 289.00, 8),
            (104, "Auriculares con Cancelación", "Audio", 120.00, 19),
            (105, "Alfombrilla XXL Gamer", "Accesorios", 19.99, 35),
            (106, "Cámara Web Full HD 1080p", "Video", 62.30, 11),
            (107, "Micrófono USB Cardioide", "Audio", 85.00, 6),
        ]
        for prod in productos:
            self.tree.insert("", "end", values=prod)

    def _cambiar_tema(self, event=None) -> None:
        """Aplica el tema seleccionado desde el Combobox."""
        nuevo_tema = self.cbo_temas.get()
        try:
            self.style.theme_use(nuevo_tema)
        except tk.TclError as err:
            messagebox.showerror("Error de Tema", f"No se pudo cargar el tema {nuevo_tema}: {err}")

    def _ajustar_progreso(self, incremento: float) -> None:
        nuevo = max(0.0, min(100.0, self.progreso_valor.get() + incremento))
        self.progreso_valor.set(nuevo)

    def _toggle_animacion_pbar(self) -> None:
        """Inicia o detiene la animación indeterminada de la barra."""
        if not self.animando_pbar:
            self.pbar.configure(mode="indeterminate")
            self.pbar.start(15)  # Intervalo en ms
            self.btn_animar.configure(text="Detener")
            self.animando_pbar = True
        else:
            self.pbar.stop()
            self.pbar.configure(mode="determinate")
            self.btn_animar.configure(text="Animar")
            self.animando_pbar = False

    def _on_scale_change(self, valor_str: str) -> None:
        val = float(valor_str)
        self.lbl_scale.configure(text=f"Valor actual: {val:.0f}%")

    def _on_treeview_select(self, event=None) -> None:
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion[0])
            valores = item["values"]
            self.lbl_seleccion.configure(
                text=f"Seleccionado: #{valores[0]} {valores[1]} - ${valores[3]:.2f}",
                font=("Segoe UI", 9, "bold")
            )

    def _eliminar_fila_seleccionada(self) -> None:
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona primero una fila de la tabla.")
            return
        self.tree.delete(seleccion[0])
        self.lbl_seleccion.configure(text="Fila eliminada de la tabla.", font=("Segoe UI", 9, "italic"))


def main():
    root = tk.Tk()
    app = ModernTtkDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
