"""
==============================================================================
05_eventos_y_bindings.py - Sistema de Eventos, Atajos de Teclado y Ratón
==============================================================================
Tkinter maneja las interacciones del usuario mediante secuencias de eventos
vinculadas con el método .bind(secuencia, callback).

Secuencias y conceptos cubiertos:
- Ratón:
  • <Button-1>: Clic izquierdo
  • <Button-2>: Clic central (rueda)
  • <Button-3>: Clic derecho
  • <Double-Button-1>: Doble clic
  • <Motion>: Movimiento del cursor
  • <B1-Motion>: Arrastrar manteniendo presionado clic izquierdo
  • <Enter> y <Leave>: Entrada y salida del cursor sobre un widget
- Teclado:
  • <Key>: Cualquier tecla presionada
  • <Return>: Tecla Enter
  • <Escape>: Tecla Esc
  • Modificadores: <Control-s>, <Control-z>, <Shift-Up>
- Objeto Event: Inspección de x, y, x_root, y_root, keysym, keycode, char.
- Propagación y detención con return 'break'.
- Desvinculación con .unbind().
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


class EventosBindingsDemo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("05 - Manejo de Eventos y Atajos (bind) | Tkinter")
        centrar_ventana(self.root, 840, 680)
        self.root.minsize(780, 600)
        self.root.configure(bg="#0f172a")

        self._crear_interfaz()
        self._configurar_bindings_globales()

    def _crear_interfaz(self) -> None:
        # Encabezado
        header = tk.Frame(self.root, bg="#1e293b", padx=20, pady=12)
        header.pack(fill="x")

        tk.Label(
            header,
            text="Laboratorio Interactivo de Eventos en Tkinter",
            font=("Segoe UI", 14, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Pasa el ratón, haz clic, arrastra o escribe para registrar los eventos en vivo.",
            font=("Segoe UI", 9),
            bg="#1e293b",
            fg="#94a3b8"
        ).pack(anchor="w")

        # Contenedor central dividido
        cuerpo = tk.Frame(self.root, bg="#0f172a", padx=15, pady=12)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.columnconfigure(0, weight=3)
        cuerpo.columnconfigure(1, weight=2)
        cuerpo.rowconfigure(0, weight=1)

        # =====================================================================
        # ÁREA DE PRUEBAS INTERACTIVA (Canvas interactivo)
        # =====================================================================
        panel_lienzo = tk.LabelFrame(
            cuerpo,
            text=" Área de Pruebas de Ratón y Teclado ",
            font=("Segoe UI", 10, "bold"),
            bg="#1e293b",
            fg="#e2e8f0",
            padx=10,
            pady=10
        )
        panel_lienzo.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        self.canvas_interactivo = tk.Canvas(
            panel_lienzo,
            bg="#020617",
            highlightthickness=1,
            highlightbackground="#334155"
        )
        self.canvas_interactivo.pack(fill="both", expand=True)

        # Instrucción sobre el canvas
        self.instruccion_id = self.canvas_interactivo.create_text(
            220, 150,
            text="Haz Clic Izquierdo, Derecho, Doble Clic,\nArrastra el cursor o pulsa teclas aquí\n\n(Atajos globales: Ctrl+S, Ctrl+L, Esc)",
            fill="#64748b",
            font=("Segoe UI", 11, "italic"),
            justify="center"
        )

        # Barra inferior de coordenadas
        self.lbl_coords = tk.Label(
            panel_lienzo,
            text="Coordenadas cursor: X=-- | Y=--",
            font=("Consolas", 9),
            bg="#1e293b",
            fg="#38bdf8",
            anchor="w"
        )
        self.lbl_coords.pack(fill="x", pady=(6, 0))

        # =====================================================================
        # CONSOLA DE REGISTRO DE EVENTOS (Log en tiempo real)
        # =====================================================================
        panel_log = tk.LabelFrame(
            cuerpo,
            text=" Registro de Eventos (Event Inspector) ",
            font=("Segoe UI", 10, "bold"),
            bg="#1e293b",
            fg="#e2e8f0",
            padx=10,
            pady=10
        )
        panel_log.grid(row=0, column=1, sticky="nsew")

        # Widget Text para el registro
        self.log_text = tk.Text(
            panel_log,
            bg="#020617",
            fg="#22c55e",
            font=("Consolas", 8),
            wrap="none",
            bd=0
        )
        scroll_log = ttk.Scrollbar(panel_log, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scroll_log.set)

        self.log_text.pack(side="left", fill="both", expand=True)
        scroll_log.pack(side="right", fill="y")

        # Botón para limpiar consola
        btn_limpiar = tk.Button(
            self.root,
            text="Limpiar Registro (Ctrl+L)",
            bg="#334155",
            fg="#f8fafc",
            activebackground="#475569",
            activeforeground="#ffffff",
            font=("Segoe UI", 9),
            bd=0,
            padx=12,
            pady=5,
            cursor="hand2",
            command=self._limpiar_log
        )
        btn_limpiar.pack(pady=(0, 10))

    def _configurar_bindings_globales(self) -> None:
        """Asocia todos los eventos a controladores específicos."""
        # 1. Movimiento del ratón
        self.canvas_interactivo.bind("<Motion>", self._on_mouse_move)

        # 2. Clics del ratón
        self.canvas_interactivo.bind("<Button-1>", lambda e: self._on_mouse_click(e, "Clic Izquierdo (<Button-1>)"))
        self.canvas_interactivo.bind("<Button-2>", lambda e: self._on_mouse_click(e, "Clic Central (<Button-2>)"))
        self.canvas_interactivo.bind("<Button-3>", lambda e: self._on_mouse_click(e, "Clic Derecho (<Button-3>)"))
        self.canvas_interactivo.bind("<Double-Button-1>", lambda e: self._on_mouse_click(e, "Doble Clic (<Double-Button-1>)"))

        # 3. Arrastre del ratón con botón 1 presionado
        self.canvas_interactivo.bind("<B1-Motion>", self._on_drag)

        # 4. Entrada y salida del área del widget
        self.canvas_interactivo.bind("<Enter>", lambda e: self._registrar_log("RATÓN", "Cursor ENTRÓ en el Canvas"))
        self.canvas_interactivo.bind("<Leave>", lambda e: self._registrar_log("RATÓN", "Cursor SALIÓ del Canvas"))

        # 5. Teclado enfocado en el canvas o en la ventana principal
        self.canvas_interactivo.focus_set()
        self.canvas_interactivo.bind("<Key>", self._on_key_press)

        # 6. Atajos de Teclado con Modificadores
        self.root.bind("<Control-s>", self._atajo_guardar)
        self.root.bind("<Control-S>", self._atajo_guardar)
        self.root.bind("<Control-l>", lambda e: self._limpiar_log())
        self.root.bind("<Control-L>", lambda e: self._limpiar_log())
        self.root.bind("<Escape>", lambda e: self._registrar_log("ATAJO", "Tecla ESC presionada"))

        # 7. Redimensión de ventana (<Configure>)
        self.root.bind("<Configure>", self._on_window_resize)

    def _on_mouse_move(self, event: tk.Event) -> None:
        self.lbl_coords.configure(text=f"Coordenadas cursor: X={event.x:3d} | Y={event.y:3d}")

    def _on_mouse_click(self, event: tk.Event, descripcion: str) -> None:
        # Dibujar una marca visual temporal en el punto del clic
        radio = 8
        color = "#38bdf8" if "Izquierdo" in descripcion else ("#eab308" if "Central" in descripcion else "#ec4899")
        if "Doble" in descripcion:
            radio = 14
            color = "#a855f7"

        circulo = self.canvas_interactivo.create_oval(
            event.x - radio, event.y - radio,
            event.x + radio, event.y + radio,
            outline=color,
            width=2
        )
        # Desvanecer la marca tras 1.2 segundos
        self.root.after(1200, lambda: self.canvas_interactivo.delete(circulo))

        self._registrar_log("CLIC", f"{descripcion} en ({event.x}, {event.y})")

    def _on_drag(self, event: tk.Event) -> None:
        # Dibujar rastro de arrastre
        p = self.canvas_interactivo.create_rectangle(
            event.x - 2, event.y - 2, event.x + 2, event.y + 2,
            fill="#38bdf8", outline=""
        )
        self.root.after(800, lambda: self.canvas_interactivo.delete(p))
        self._registrar_log("ARRASTRE", f"B1-Motion en ({event.x}, {event.y})")

    def _on_key_press(self, event: tk.Event) -> None:
        char = repr(event.char) if event.char else "N/A"
        self._registrar_log(
            "TECLADO",
            f"Key: {event.keysym:12} | Char: {char:6} | Code: {event.keycode}"
        )

    def _atajo_guardar(self, event: tk.Event) -> str:
        self._registrar_log("ATAJO", "¡Combinación Ctrl+S detectada! (Simulando guardado)")
        # Devolver 'break' previene que el evento siga propagándose a otros manejadores
        return "break"

    def _on_window_resize(self, event: tk.Event) -> None:
        # Sólo reaccionar si el evento proviene de la ventana principal
        if event.widget == self.root:
            # Centrar el texto de instrucción si la ventana cambia de tamaño
            w = self.canvas_interactivo.winfo_width()
            h = self.canvas_interactivo.winfo_height()
            if w > 10 and h > 10:
                self.canvas_interactivo.coords(self.instruccion_id, w // 2, h // 2)

    def _registrar_log(self, categoria: str, mensaje: str) -> None:
        linea = f"[{categoria:8}] {mensaje}\n"
        self.log_text.insert("end", linea)
        self.log_text.see("end")  # Auto-scroll hacia el final

    def _limpiar_log(self) -> None:
        self.log_text.delete("1.0", "end")
        self._registrar_log("SISTEMA", "Registro reiniciado.")


def main():
    root = tk.Tk()
    app = EventosBindingsDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
