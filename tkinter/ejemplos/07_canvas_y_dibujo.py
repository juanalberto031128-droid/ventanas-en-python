"""
==============================================================================
07_canvas_y_dibujo.py - Gráficos 2D, Animaciones y Pizarra Interactiva (Canvas)
==============================================================================
El widget tk.Canvas es uno de los componentes más versátiles de Tkinter.
Permite dibujar primitivas vectoriales 2D, manipular objetos mediante identificadores
(IDs) o etiquetas (tags), crear animaciones temporizadas con .after() e implementar
interacciones como arrastrar y soltar (Drag and Drop).

Conceptos cubiertos:
- Métodos de dibujo:
  • create_line, create_rectangle, create_oval, create_polygon, create_arc, create_text
- Identificadores numéricos y etiquetas grupales (tags)
- Modificación en caliente: canvas.coords(), canvas.itemconfig(), canvas.move()
- Animación fluida de una pelota rebotando con root.after()
- Arrastrar y soltar objetos (Drag & Drop) con el ratón
- Pizarra de dibujo libre a mano alzada
==============================================================================
"""

import tkinter as tk
from tkinter import ttk, colorchooser


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en el monitor del usuario."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


class CanvasDemo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("07 - Gráficos 2D, Animación y Lienzo (Canvas) | Tkinter")
        centrar_ventana(self.root, 880, 680)
        self.root.minsize(800, 600)
        self.root.configure(bg="#0f172a")

        # Variables para dibujo
        self.color_pincel = "#38bdf8"
        self.grosor_pincel = 3
        self.ultimo_x = None
        self.ultimo_y = None

        # Variables para Drag and Drop
        self.objeto_arrastrado = None
        self.offset_x = 0
        self.offset_y = 0

        # Variables para Animación de Rebote
        self.animando = False
        self.vel_x = 4
        self.vel_y = 3
        self.ball_id = None

        self._crear_interfaz()
        self._dibujar_escenario_inicial()

    def _crear_interfaz(self) -> None:
        # Barra superior de herramientas
        toolbar = tk.Frame(self.root, bg="#1e293b", padx=15, pady=8)
        toolbar.pack(fill="x")

        tk.Label(toolbar, text="Modo:", bg="#1e293b", fg="#e2e8f0", font=("Segoe UI", 9, "bold")).pack(side="left", padx=(0, 5))

        self.modo_var = tk.StringVar(value="arrastrar")
        rb_drag = tk.Radiobutton(toolbar, text="Arrastrar Figuras", variable=self.modo_var, value="arrastrar",
                                 bg="#1e293b", fg="#e2e8f0", selectcolor="#0f172a", font=("Segoe UI", 9))
        rb_drag.pack(side="left", padx=5)

        rb_draw = tk.Radiobutton(toolbar, text="Pincel a Mano Alzada", variable=self.modo_var, value="dibujar",
                                 bg="#1e293b", fg="#e2e8f0", selectcolor="#0f172a", font=("Segoe UI", 9))
        rb_draw.pack(side="left", padx=5)

        ttk.Separator(toolbar, orient="vertical").pack(side="left", fill="y", padx=10)

        # Botón para cambiar color del pincel
        self.btn_color = tk.Button(
            toolbar,
            text="Color Pincel",
            bg=self.color_pincel,
            fg="#0f172a",
            font=("Segoe UI", 9, "bold"),
            padx=8,
            pady=2,
            command=self._elegir_color
        )
        self.btn_color.pack(side="left", padx=5)

        # Control de animación
        self.btn_animar = tk.Button(
            toolbar,
            text="Iniciar Rebote",
            bg="#10b981",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            padx=10,
            pady=2,
            command=self._toggle_animacion
        )
        self.btn_animar.pack(side="left", padx=10)

        # Botón limpiar
        btn_limpiar = tk.Button(
            toolbar,
            text="Reiniciar Lienzo",
            bg="#ef4444",
            fg="#ffffff",
            font=("Segoe UI", 9),
            padx=8,
            pady=2,
            command=self._reiniciar_lienzo
        )
        btn_limpiar.pack(side="right", padx=5)

        # Lienzo (Canvas) Principal
        self.canvas = tk.Canvas(
            self.root,
            bg="#020617",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True, padx=15, pady=10)

        # Eventos sobre el lienzo
        self.canvas.bind("<Button-1>", self._on_canvas_click)
        self.canvas.bind("<B1-Motion>", self._on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_canvas_release)

        # Barra de pie de página
        footer = tk.Label(
            self.root,
            text="💡 Consejo: En modo 'Arrastrar Figuras', haz clic sobre el círculo amarillo, el rectángulo azul o la estrella para moverlos.",
            font=("Segoe UI", 9),
            bg="#0f172a",
            fg="#94a3b8",
            pady=5
        )
        footer.pack()

    def _dibujar_escenario_inicial(self) -> None:
        """Dibuja figuras iniciales vectoriales en el lienzo."""
        self.canvas.delete("all")

        # Texto de título sobre el canvas
        self.canvas.create_text(
            20, 25,
            text="Canvas 2D - Primitivas Gráficas",
            fill="#64748b",
            anchor="w",
            font=("Segoe UI", 12, "bold")
        )

        # 1. Líneas y arcos decorativos
        self.canvas.create_line(20, 50, 400, 50, fill="#1e293b", width=2)
        self.canvas.create_arc(500, 20, 580, 100, start=30, extent=240, outline="#f43f5e", width=3, style="arc")

        # 2. Figuras interactivas arrastrables con tag 'movible'
        # Rectángulo azul
        self.canvas.create_rectangle(
            60, 90, 190, 180,
            fill="#2563eb", outline="#93c5fd", width=2,
            tags=("movible", "rectangulo")
        )
        self.canvas.create_text(
            125, 135,
            text="Rectángulo\n(Arrastrame)",
            fill="#ffffff",
            font=("Segoe UI", 9, "bold"),
            justify="center",
            tags=("movible", "texto_rect")
        )

        # Círculo verde
        self.canvas.create_oval(
            240, 90, 340, 190,
            fill="#10b981", outline="#a7f3d0", width=2,
            tags=("movible", "circulo")
        )
        self.canvas.create_text(
            290, 140,
            text="Círculo",
            fill="#ffffff",
            font=("Segoe UI", 9, "bold"),
            tags=("movible", "texto_circ")
        )

        # Polígono (Estrella/Rombo)
        puntos_rombo = [430, 90, 480, 140, 430, 190, 380, 140]
        self.canvas.create_polygon(
            puntos_rombo,
            fill="#8b5cf6", outline="#c4b5fd", width=2,
            tags=("movible", "rombo")
        )
        self.canvas.create_text(
            430, 140,
            text="Polígono",
            fill="#ffffff",
            font=("Segoe UI", 9, "bold"),
            tags=("movible", "texto_rombo")
        )

        # 3. Pelota para animación de rebote (con tag 'animada')
        self.ball_id = self.canvas.create_oval(
            50, 260, 90, 300,
            fill="#eab308", outline="#fef08a", width=2,
            tags=("pelota",)
        )

    def _on_canvas_click(self, event: tk.Event) -> None:
        modo = self.modo_var.get()
        if modo == "arrastrar":
            # Buscar el elemento más cercano debajo del cursor
            items = self.canvas.find_withtag("current")
            if items:
                self.objeto_arrastrado = items[0]
                self.ultimo_x = event.x
                self.ultimo_y = event.y
        elif modo == "dibujar":
            self.ultimo_x = event.x
            self.ultimo_y = event.y

    def _on_canvas_drag(self, event: tk.Event) -> None:
        modo = self.modo_var.get()
        if modo == "arrastrar" and self.objeto_arrastrado:
            # Calcular desplazamiento dx, dy
            dx = event.x - self.ultimo_x
            dy = event.y - self.ultimo_y
            self.canvas.move(self.objeto_arrastrado, dx, dy)
            self.ultimo_x = event.x
            self.ultimo_y = event.y
        elif modo == "dibujar":
            if self.ultimo_x is not None and self.ultimo_y is not None:
                self.canvas.create_line(
                    self.ultimo_x, self.ultimo_y, event.x, event.y,
                    fill=self.color_pincel,
                    width=self.grosor_pincel,
                    capstyle="round",
                    smooth=True
                )
            self.ultimo_x = event.x
            self.ultimo_y = event.y

    def _on_canvas_release(self, event: tk.Event) -> None:
        self.objeto_arrastrado = None
        self.ultimo_x = None
        self.ultimo_y = None

    def _elegir_color(self) -> None:
        color = colorchooser.askcolor(self.color_pincel)[1]
        if color:
            self.color_pincel = color
            self.btn_color.configure(bg=color)

    def _toggle_animacion(self) -> None:
        if not self.animando:
            self.animando = True
            self.btn_animar.configure(text="Pausar Rebote", bg="#f59e0b")
            self._animar_paso()
        else:
            self.animando = False
            self.btn_animar.configure(text="Reanudar Rebote", bg="#10b981")

    def _animar_paso(self) -> None:
        """Bucle de física elemental con detección de colisión con bordes."""
        if not self.animando:
            return

        coords = self.canvas.coords(self.ball_id)
        if not coords:
            return
        x1, y1, x2, y2 = coords

        ancho_w = self.canvas.winfo_width()
        alto_w = self.canvas.winfo_height()

        # Rebote en bordes horizontales
        if x2 >= ancho_w or x1 <= 0:
            self.vel_x = -self.vel_x

        # Rebote en bordes verticales
        if y2 >= alto_w or y1 <= 0:
            self.vel_y = -self.vel_y

        # Mover la pelota
        self.canvas.move(self.ball_id, self.vel_x, self.vel_y)

        # Planificar siguiente fotograma en ~16ms (~60 FPS)
        self.root.after(16, self._animar_paso)

    def _reiniciar_lienzo(self) -> None:
        self.animando = False
        self.btn_animar.configure(text="Iniciar Rebote", bg="#10b981")
        self._dibujar_escenario_inicial()


def main():
    root = tk.Tk()
    app = CanvasDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
