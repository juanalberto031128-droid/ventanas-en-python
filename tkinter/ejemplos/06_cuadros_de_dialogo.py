"""
==============================================================================
06_cuadros_de_dialogo.py - Cuadros de Mensajes, Archivos y Selectores
==============================================================================
Tkinter incluye módulos integrados para interactuar con cuadros de diálogo
nativos del sistema operativo:
1. messagebox: Alertas informativas, advertencias, errores y preguntas binarias.
2. filedialog: Explorador para abrir y guardar archivos o seleccionar carpetas.
3. colorchooser: Paleta del sistema operativo para seleccionar códigos de color RGB/Hex.
4. simpledialog: Diálogos modales para solicitar entradas rápidas (texto, enteros, flotantes).

Este script presenta un panel interactivo para disparar y examinar el retorno de cada uno.
==============================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser, simpledialog


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en el monitor del usuario."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


class DialogosDemo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("06 - Cuadros de Diálogo Nativos | Tkinter")
        centrar_ventana(self.root, 820, 680)
        self.root.minsize(760, 600)
        self.root.configure(bg="#f8fafc")

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        # Encabezado
        header = tk.Frame(self.root, bg="#ffffff", padx=20, pady=12, bd=1, relief="groove")
        header.pack(fill="x")

        tk.Label(
            header,
            text="Diálogos Nativos del Sistema (messagebox, filedialog, colorchooser)",
            font=("Segoe UI", 14, "bold"),
            bg="#ffffff",
            fg="#1e293b"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Haz clic en cualquier botón para invocar el cuadro modal correspondiente y observar su valor de retorno.",
            font=("Segoe UI", 9),
            bg="#ffffff",
            fg="#64748b"
        ).pack(anchor="w")

        # Contenedor principal con dos columnas
        cuerpo = tk.Frame(self.root, bg="#f8fafc", padx=15, pady=10)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.columnconfigure(0, weight=1)
        cuerpo.columnconfigure(1, weight=1)

        # =====================================================================
        # SECCIÓN 1: MESSAGEBOX (Mensajes y Confirmaciones)
        # =====================================================================
        frame_msg = tk.LabelFrame(
            cuerpo,
            text=" 1. Diálogos de Mensajes (messagebox) ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#0284c7",
            padx=10,
            pady=8
        )
        frame_msg.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        ttk.Button(frame_msg, text="showinfo() - Información", command=self._demo_showinfo).pack(fill="x", pady=3)
        ttk.Button(frame_msg, text="showwarning() - Advertencia", command=self._demo_showwarning).pack(fill="x", pady=3)
        ttk.Button(frame_msg, text="showerror() - Error Crítico", command=self._demo_showerror).pack(fill="x", pady=3)
        ttk.Button(frame_msg, text="askyesno() - Pregunta Sí / No", command=self._demo_askyesno).pack(fill="x", pady=3)
        ttk.Button(frame_msg, text="askokcancel() - Aceptar / Cancelar", command=self._demo_askokcancel).pack(fill="x", pady=3)
        ttk.Button(frame_msg, text="askretrycancel() - Reintentar", command=self._demo_askretrycancel).pack(fill="x", pady=3)

        # =====================================================================
        # SECCIÓN 2: FILEDIALOG (Archivos y Directorios)
        # =====================================================================
        frame_file = tk.LabelFrame(
            cuerpo,
            text=" 2. Selector de Archivos (filedialog) ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#0284c7",
            padx=10,
            pady=8
        )
        frame_file.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        ttk.Button(frame_file, text="askopenfilename() - Abrir un Archivo", command=self._demo_open_file).pack(fill="x", pady=3)
        ttk.Button(frame_file, text="askopenfilenames() - Abrir Múltiples", command=self._demo_open_files).pack(fill="x", pady=3)
        ttk.Button(frame_file, text="asksaveasfilename() - Guardar Como", command=self._demo_save_file).pack(fill="x", pady=3)
        ttk.Button(frame_file, text="askdirectory() - Seleccionar Carpeta", command=self._demo_open_folder).pack(fill="x", pady=3)

        # =====================================================================
        # SECCIÓN 3: COLORCHOOSER (Selector de Color)
        # =====================================================================
        frame_color = tk.LabelFrame(
            cuerpo,
            text=" 3. Selector de Color (colorchooser) ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#0284c7",
            padx=10,
            pady=8
        )
        frame_color.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        ttk.Button(frame_color, text="askcolor() - Elegir Color", command=self._demo_choose_color).pack(fill="x", pady=3)
        self.muestra_color = tk.Label(
            frame_color,
            text="Muestra de Color",
            bg="#3b82f6",
            fg="#ffffff",
            font=("Segoe UI", 10, "bold"),
            pady=10,
            relief="groove"
        )
        self.muestra_color.pack(fill="x", pady=(5, 0))

        # =====================================================================
        # SECCIÓN 4: SIMPLEDIALOG (Entrada Rápida)
        # =====================================================================
        frame_input = tk.LabelFrame(
            cuerpo,
            text=" 4. Entradas Rápidas (simpledialog) ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#0284c7",
            padx=10,
            pady=8
        )
        frame_input.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        ttk.Button(frame_input, text="askstring() - Solicitar Texto", command=self._demo_askstring).pack(fill="x", pady=3)
        ttk.Button(frame_input, text="askinteger() - Solicitar Entero (1 a 100)", command=self._demo_askinteger).pack(fill="x", pady=3)
        ttk.Button(frame_input, text="askfloat() - Solicitar Decimal", command=self._demo_askfloat).pack(fill="x", pady=3)

        # =====================================================================
        # PANEL INFERIOR DE RETORNO Y REGISTRO
        # =====================================================================
        frame_salida = tk.LabelFrame(
            self.root,
            text=" Historial de Respuestas y Valores Retornados ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#334155",
            padx=10,
            pady=6
        )
        frame_salida.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.txt_salida = tk.Text(frame_salida, height=7, bg="#0f172a", fg="#38bdf8", font=("Consolas", 9), bd=0)
        scroll = ttk.Scrollbar(frame_salida, orient="vertical", command=self.txt_salida.yview)
        self.txt_salida.configure(yscrollcommand=scroll.set)

        self.txt_salida.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def _imprimir_retorno(self, funcion: str, resultado) -> None:
        linea = f"➔ [{funcion}] retornó: {repr(resultado)} (Tipo: {type(resultado).__name__})\n"
        self.txt_salida.insert("end", linea)
        self.txt_salida.see("end")

    # --- Métodos messagebox ---
    def _demo_showinfo(self):
        res = messagebox.showinfo("Información", "¡Operación completada con éxito!")
        self._imprimir_retorno("messagebox.showinfo()", res)

    def _demo_showwarning(self):
        res = messagebox.showwarning("Advertencia", "El espacio en disco es bajo.")
        self._imprimir_retorno("messagebox.showwarning()", res)

    def _demo_showerror(self):
        res = messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        self._imprimir_retorno("messagebox.showerror()", res)

    def _demo_askyesno(self):
        res = messagebox.askyesno("Confirmar", "¿Deseas guardar los cambios?")
        self._imprimir_retorno("messagebox.askyesno()", res)

    def _demo_askokcancel(self):
        res = messagebox.askokcancel("Confirmación", "¿Deseas continuar con la instalación?")
        self._imprimir_retorno("messagebox.askokcancel()", res)

    def _demo_askretrycancel(self):
        res = messagebox.askretrycancel("Fallo de Red", "¿Deseas reintentar la conexión?")
        self._imprimir_retorno("messagebox.askretrycancel()", res)

    # --- Métodos filedialog ---
    def _demo_open_file(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de código",
            filetypes=[("Archivos Python", "*.py"), ("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        self._imprimir_retorno("filedialog.askopenfilename()", ruta)

    def _demo_open_files(self):
        rutas = filedialog.askopenfilenames(
            title="Seleccionar múltiples archivos",
            filetypes=[("Archivos Python", "*.py"), ("Todos los archivos", "*.*")]
        )
        self._imprimir_retorno("filedialog.askopenfilenames()", rutas)

    def _demo_save_file(self):
        ruta = filedialog.asksaveasfilename(
            title="Guardar archivo como",
            defaultextension=".txt",
            filetypes=[("Documento de Texto", "*.txt"), ("Script Python", "*.py")]
        )
        self._imprimir_retorno("filedialog.asksaveasfilename()", ruta)

    def _demo_open_folder(self):
        carpeta = filedialog.askdirectory(title="Seleccionar Directorio")
        self._imprimir_retorno("filedialog.askdirectory()", carpeta)

    # --- Métodos colorchooser ---
    def _demo_choose_color(self):
        color = colorchooser.askcolor(title="Selecciona un color para la muestra", initialcolor="#3b82f6")
        self._imprimir_retorno("colorchooser.askcolor()", color)
        if color[1]:
            # color[1] contiene la cadena Hex (#RRGGBB)
            self.muestra_color.configure(bg=color[1], text=f"Color: {color[1]}")

    # --- Métodos simpledialog ---
    def _demo_askstring(self):
        texto = simpledialog.askstring("Nombre de Proyecto", "¿Cómo se llama tu proyecto?")
        self._imprimir_retorno("simpledialog.askstring()", texto)

    def _demo_askinteger(self):
        num = simpledialog.askinteger("Edad", "¿Cuál es tu edad?", minvalue=1, maxvalue=120)
        self._imprimir_retorno("simpledialog.askinteger()", num)

    def _demo_askfloat(self):
        flotante = simpledialog.askfloat("Calificación", "Ingresa una nota (0.0 a 10.0):", minvalue=0.0, maxvalue=10.0)
        self._imprimir_retorno("simpledialog.askfloat()", flotante)


def main():
    root = tk.Tk()
    app = DialogosDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
