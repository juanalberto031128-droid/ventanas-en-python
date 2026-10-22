"""
==============================================================================
08_menus_y_navegacion.py - Menús Principales, Menú Contextual, Toolbar y Statusbar
==============================================================================
Las aplicaciones de escritorio estándar requieren estructuras de navegación
consistentes:
1. Barra de Menú Principal (Menu con cascadas: Archivo, Edición, Ver, Ayuda).
2. Elementos interactivos dentro de menús: comandos, atajos, separadores,
   casillas de verificación (add_checkbutton) y opciones (add_radiobutton).
3. Menú contextual (Popup Menu): Desplegado mediante clic derecho (<Button-3>).
4. Barra de herramientas superior (Toolbar): Acceso directo a acciones frecuentes.
5. Barra de estado inferior (Statusbar): Indicadores en tiempo real.
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


class MenusNavegacionDemo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("08 - Menús, Barra de Herramientas y Estado | Tkinter")
        centrar_ventana(self.root, 800, 560)
        self.root.minsize(700, 480)

        # Variables de estado
        self.var_modo_oscuro = tk.BooleanVar(value=False)
        self.var_nivel_zoom = tk.StringVar(value="100%")
        self.var_auto_guardado = tk.BooleanVar(value=True)

        self._crear_menu_principal()
        self._crear_toolbar()
        self._crear_statusbar()
        self._crear_area_trabajo()
        self._crear_menu_contextual()

        # Atajos de teclado vinculados
        self.root.bind("<Control-n>", lambda e: self._accion("Nuevo Archivo"))
        self.root.bind("<Control-s>", lambda e: self._accion("Guardar Archivo"))

    # =========================================================================
    # 1. BARRA DE MENÚ PRINCIPAL
    # =========================================================================
    def _crear_menu_principal(self) -> None:
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # --- Menú Archivo ---
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=lambda: self._accion("Nuevo Archivo"))
        menu_archivo.add_command(label="Abrir...", accelerator="Ctrl+O", command=lambda: self._accion("Abrir Archivo"))
        menu_archivo.add_command(label="Guardar", accelerator="Ctrl+S", command=lambda: self._accion("Guardar Archivo"))
        menu_archivo.add_separator()
        menu_archivo.add_checkbutton(label="Guardado Automático", variable=self.var_auto_guardado,
                                     command=lambda: self._actualizar_status("Autoguardado actualizado"))
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)

        # --- Menú Edición ---
        menu_edicion = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Edición", menu=menu_edicion)

        menu_edicion.add_command(label="Deshacer", accelerator="Ctrl+Z", command=lambda: self._accion("Deshacer"))
        menu_edicion.add_command(label="Rehacer", accelerator="Ctrl+Y", command=lambda: self._accion("Rehacer"))
        menu_edicion.add_separator()
        menu_edicion.add_command(label="Cortar", accelerator="Ctrl+X", command=lambda: self._accion("Cortar"))
        menu_edicion.add_command(label="Copiar", accelerator="Ctrl+C", command=lambda: self._accion("Copiar"))
        menu_edicion.add_command(label="Pegar", accelerator="Ctrl+V", command=lambda: self._accion("Pegar"))

        # --- Menú Ver (con Radiobuttons para Zoom) ---
        menu_ver = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ver", menu=menu_ver)

        menu_ver.add_checkbutton(label="Tema Oscuro", variable=self.var_modo_oscuro, command=self._toggle_tema)
        menu_ver.add_separator()

        menu_zoom = tk.Menu(menu_ver, tearoff=0)
        menu_ver.add_cascade(label="Zoom", menu=menu_zoom)
        for nivel in ["50%", "75%", "100%", "125%", "150%"]:
            menu_zoom.add_radiobutton(label=nivel, variable=self.var_nivel_zoom, value=nivel,
                                      command=lambda n=nivel: self._actualizar_status(f"Zoom cambiado a {n}"))

        # --- Menú Ayuda ---
        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Documentación", command=lambda: messagebox.showinfo("Ayuda", "Consulta el README.md del repositorio para más información."))
        menu_ayuda.add_command(label="Acerca de Tkinter...", command=self._mostrar_acerca_de)

    # =========================================================================
    # 2. BARRA DE HERRAMIENTAS SUPERIOR (Toolbar)
    # =========================================================================
    def _crear_toolbar(self) -> None:
        self.toolbar = ttk.Frame(self.root, padding=4)
        self.toolbar.pack(side="top", fill="x")

        # Botones de acceso rápido
        btn_nuevo = ttk.Button(self.toolbar, text="📄 Nuevo", command=lambda: self._accion("Nuevo"))
        btn_nuevo.pack(side="left", padx=2)

        btn_abrir = ttk.Button(self.toolbar, text="📂 Abrir", command=lambda: self._accion("Abrir"))
        btn_abrir.pack(side="left", padx=2)

        btn_guardar = ttk.Button(self.toolbar, text="💾 Guardar", command=lambda: self._accion("Guardar"))
        btn_guardar.pack(side="left", padx=2)

        ttk.Separator(self.toolbar, orient="vertical").pack(side="left", fill="y", padx=6, pady=2)

        btn_copiar = ttk.Button(self.toolbar, text="📋 Copiar", command=lambda: self._accion("Copiar"))
        btn_copiar.pack(side="left", padx=2)

        btn_pegar = ttk.Button(self.toolbar, text="📌 Pegar", command=lambda: self._accion("Pegar"))
        btn_pegar.pack(side="left", padx=2)

    # =========================================================================
    # 3. BARRA DE ESTADO INFERIOR (Statusbar)
    # =========================================================================
    def _crear_statusbar(self) -> None:
        self.statusbar = tk.Frame(self.root, bg="#e2e8f0", bd=1, relief="sunken")
        self.statusbar.pack(side="bottom", fill="x")

        self.lbl_status = tk.Label(self.statusbar, text="Listo", anchor="w", bg="#e2e8f0", fg="#334155", font=("Segoe UI", 9))
        self.lbl_status.pack(side="left", padx=10, pady=2)

        self.lbl_status_zoom = tk.Label(self.statusbar, text="Zoom: 100%", anchor="e", bg="#e2e8f0", fg="#64748b", font=("Segoe UI", 9))
        self.lbl_status_zoom.pack(side="right", padx=10, pady=2)

    # =========================================================================
    # 4. ÁREA CENTRAL DE TRABAJO
    # =========================================================================
    def _crear_area_trabajo(self) -> None:
        self.area_central = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        self.area_central.pack(fill="both", expand=True)

        self.lbl_info = tk.Label(
            self.area_central,
            text="Haz clic derecho en cualquier lugar de esta área\npara abrir el Menú Contextual (Popup Menu)",
            font=("Segoe UI", 12),
            bg="#ffffff",
            fg="#475569"
        )
        self.lbl_info.pack(expand=True)

    # =========================================================================
    # 5. MENÚ CONTEXTUAL (Clic Derecho)
    # =========================================================================
    def _crear_menu_contextual(self) -> None:
        self.menu_contextual = tk.Menu(self.root, tearoff=0)
        self.menu_contextual.add_command(label="Cortar", command=lambda: self._accion("Cortar"))
        self.menu_contextual.add_command(label="Copiar", command=lambda: self._accion("Copiar"))
        self.menu_contextual.add_command(label="Pegar", command=lambda: self._accion("Pegar"))
        self.menu_contextual.add_separator()
        self.menu_contextual.add_command(label="Seleccionar Todo", command=lambda: self._accion("Seleccionar Todo"))

        # Vincular botón derecho tanto en Windows/Linux (<Button-3>) como macOS (<Button-2>)
        self.area_central.bind("<Button-3>", self._mostrar_menu_contextual)
        self.lbl_info.bind("<Button-3>", self._mostrar_menu_contextual)

    def _mostrar_menu_contextual(self, event: tk.Event) -> None:
        try:
            self.menu_contextual.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu_contextual.grab_release()

    def _accion(self, nombre: str) -> None:
        self._actualizar_status(f"Comando ejecutado: '{nombre}'")

    def _actualizar_status(self, mensaje: str) -> None:
        self.lbl_status.configure(text=f"Estado: {mensaje}")
        self.lbl_status_zoom.configure(text=f"Zoom: {self.var_nivel_zoom.get()}")

    def _toggle_tema(self) -> None:
        oscuro = self.var_modo_oscuro.get()
        bg = "#1e293b" if oscuro else "#ffffff"
        fg = "#f8fafc" if oscuro else "#475569"
        self.area_central.configure(bg=bg)
        self.lbl_info.configure(bg=bg, fg=fg)
        self._actualizar_status("Tema Oscuro Activado" if oscuro else "Tema Claro Activado")

    def _mostrar_acerca_de(self) -> None:
        messagebox.showinfo(
            "Acerca de",
            "Módulo 08: Menús y Navegación\nDemostración de Tkinter con Python\nLicencia MIT - 2026"
        )


def main():
    root = tk.Tk()
    app = MenusNavegacionDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
