"""
==============================================================================
09_editor_texto_avanzado.py - Widget Text, Formato con Tags y Scrollbars
==============================================================================
El widget tk.Text es un editor multilínea extraordinariamente potente. Permite
no solo escribir texto, sino formatear rangos con etiquetas (tags), buscar
cadenas, aplicar estilos tipográficos variados, incrustar imágenes o botones,
y gestionar un historial nativo de Deshacer/Rehacer (Undo/Redo).

Conceptos cubiertos:
- tk.Text con sincronización bidireccional de barras de desplazamiento (Scrollbars).
- Sistema de Etiquetas (Tags):
  • Creación y configuración: tag_config (fuente, colores, alineación, interlineado).
  • Aplicación dinámica a selecciones: tag_add("bold", "sel.first", "sel.last").
- Búsqueda y resaltado visual con text.search() y tag_add.
- Pila de Deshacer / Rehacer nativa (undo=True, autoseparators=True).
- Conteo de palabras, caracteres y líneas reactivo en tiempo real.
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


class EditorTextoAvanzado:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("09 - Editor de Texto con Tags y Formato (tk.Text) | Tkinter")
        centrar_ventana(self.root, 860, 680)
        self.root.minsize(760, 550)
        self.root.configure(bg="#f8fafc")

        self._crear_toolbar()
        self._crear_editor()
        self._crear_statusbar()
        self._configurar_tags()
        self._cargar_texto_inicial()

    def _crear_toolbar(self) -> None:
        """Crea la barra de botones de formato superior."""
        toolbar = ttk.Frame(self.root, padding=6)
        toolbar.pack(fill="x")

        # Botones de estilo
        btn_bold = ttk.Button(toolbar, text="Negrita (B)", width=10, command=lambda: self._aplicar_tag("negrita"))
        btn_bold.pack(side="left", padx=2)

        btn_italic = ttk.Button(toolbar, text="Cursiva (I)", width=10, command=lambda: self._aplicar_tag("cursiva"))
        btn_italic.pack(side="left", padx=2)

        btn_under = ttk.Button(toolbar, text="Subrayado (U)", width=12, command=lambda: self._aplicar_tag("subrayado"))
        btn_under.pack(side="left", padx=2)

        btn_highlight = ttk.Button(toolbar, text="Resaltar", width=9, command=lambda: self._aplicar_tag("resaltado"))
        btn_highlight.pack(side="left", padx=2)

        btn_clean = ttk.Button(toolbar, text="Quitar Formato", width=14, command=self._limpiar_formato_seleccion)
        btn_clean.pack(side="left", padx=2)

        ttk.Separator(toolbar, orient="vertical").pack(side="left", fill="y", padx=8)

        # Barra de búsqueda
        ttk.Label(toolbar, text="Buscar:").pack(side="left", padx=2)
        self.entry_buscar = ttk.Entry(toolbar, width=14)
        self.entry_buscar.pack(side="left", padx=2)
        self.entry_buscar.bind("<Return>", lambda e: self._buscar_texto())

        btn_buscar = ttk.Button(toolbar, text="🔍", width=4, command=self._buscar_texto)
        btn_buscar.pack(side="left", padx=2)

        ttk.Separator(toolbar, orient="vertical").pack(side="left", fill="y", padx=8)

        # Deshacer y Rehacer
        btn_undo = ttk.Button(toolbar, text="↶ Deshacer", width=10, command=self._deshacer)
        btn_undo.pack(side="left", padx=2)

        btn_redo = ttk.Button(toolbar, text="↷ Rehacer", width=10, command=self._rehacer)
        btn_redo.pack(side="left", padx=2)

    def _crear_editor(self) -> None:
        """Contenedor con el widget Text y scrollbars."""
        contenedor = tk.Frame(self.root, bg="#ffffff", bd=1, relief="sunken")
        contenedor.pack(fill="both", expand=True, padx=12, pady=6)

        # Scrollbars
        scroll_y = ttk.Scrollbar(contenedor, orient="vertical")
        scroll_x = ttk.Scrollbar(contenedor, orient="horizontal")

        # Widget Text con soporte undo habilitado
        self.txt_editor = tk.Text(
            contenedor,
            wrap="word",
            undo=True,
            maxundo=-1,
            autoseparators=True,
            font=("Georgia", 11),
            padx=15,
            pady=15,
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
            bg="#ffffff",
            fg="#1e293b",
            insertbackground="#0284c7"  # Color del cursor cursor
        )

        scroll_y.configure(command=self.txt_editor.yview)
        scroll_x.configure(command=self.txt_editor.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")
        self.txt_editor.pack(side="left", fill="both", expand=True)

        # Vincular actualización de estadísticas al escribir
        self.txt_editor.bind("<KeyRelease>", self._actualizar_estadisticas)

    def _crear_statusbar(self) -> None:
        """Barra de estado inferior."""
        self.statusbar = tk.Frame(self.root, bg="#e2e8f0", bd=1, relief="ridge")
        self.statusbar.pack(fill="x", side="bottom")

        self.lbl_stats = tk.Label(
            self.statusbar,
            text="Líneas: 1 | Palabras: 0 | Caracteres: 0",
            bg="#e2e8f0",
            fg="#475569",
            font=("Segoe UI", 9)
        )
        self.lbl_stats.pack(side="left", padx=10, pady=3)

        self.lbl_aviso = tk.Label(
            self.statusbar,
            text="Selecciona texto para aplicar estilos",
            bg="#e2e8f0",
            fg="#64748b",
            font=("Segoe UI", 9, "italic")
        )
        self.lbl_aviso.pack(side="right", padx=10, pady=3)

    def _configurar_tags(self) -> None:
        """Define la configuración visual de cada etiqueta (tag)."""
        self.txt_editor.tag_configure("negrita", font=("Georgia", 11, "bold"))
        self.txt_editor.tag_configure("cursiva", font=("Georgia", 11, "italic"))
        self.txt_editor.tag_configure("subrayado", underline=True)
        self.txt_editor.tag_configure("resaltado", background="#fef08a", foreground="#854d0e")
        self.txt_editor.tag_configure("coincidencia_busqueda", background="#f9a8d4", foreground="#831843")
        self.txt_editor.tag_configure("titulo_principal", font=("Georgia", 16, "bold"), foreground="#0284c7")
        self.txt_editor.tag_configure("codigo", font=("Consolas", 10), background="#f1f5f9", foreground="#0f172a")

    def _cargar_texto_inicial(self) -> None:
        """Inserta un texto demostrativo con formato variado."""
        texto_ejemplo = (
            "Bienvenido al Editor de Texto Avanzado con Tkinter\n\n"
            "El widget tk.Text permite asignar etiquetas ('tags') a cualquier porción de texto. "
            "Esto te da libertad completa para modificar fuentes, colores de fondo y estilo.\n\n"
            "Puedes seleccionar cualquier palabra o frase y pulsar los botones superiores para "
            "volverla negrita, cursiva, subrayada o resaltarla en amarillo.\n\n"
            "Código de ejemplo:\n"
            "    texto.tag_add('mi_estilo', '1.0', '1.10')\n\n"
            "¡Prueba escribir tus propias notas y usar la herramienta de búsqueda!"
        )
        self.txt_editor.insert("1.0", texto_ejemplo)

        # Aplicar tags iniciales programáticamente
        self.txt_editor.tag_add("titulo_principal", "1.0", "1.52")
        self.txt_editor.tag_add("negrita", "3.17", "3.24")
        self.txt_editor.tag_add("codigo", "9.0", "9.46")

        self._actualizar_estadisticas()

    def _aplicar_tag(self, nombre_tag: str) -> None:
        """Aplica el tag especificado a la selección actual de texto."""
        try:
            inicio = self.txt_editor.index("sel.first")
            fin = self.txt_editor.index("sel.last")
            self.txt_editor.tag_add(nombre_tag, inicio, fin)
            self.lbl_aviso.configure(text=f"Etiqueta '{nombre_tag}' aplicada.")
        except tk.TclError:
            messagebox.showinfo("Aviso", "Primero selecciona el texto al que deseas aplicar el estilo.")

    def _limpiar_formato_seleccion(self) -> None:
        """Elimina todos los tags en la selección."""
        try:
            inicio = self.txt_editor.index("sel.first")
            fin = self.txt_editor.index("sel.last")
            for t in ["negrita", "cursiva", "subrayado", "resaltado", "coincidencia_busqueda"]:
                self.txt_editor.tag_remove(t, inicio, fin)
            self.lbl_aviso.configure(text="Formato eliminado de la selección.")
        except tk.TclError:
            messagebox.showinfo("Aviso", "Selecciona el texto cuyo formato deseas remover.")

    def _buscar_texto(self) -> None:
        """Busca y resalta todas las ocurrencias de la palabra clave."""
        # Limpiar resaltados previos de búsqueda
        self.txt_editor.tag_remove("coincidencia_busqueda", "1.0", "end")

        termino = self.entry_buscar.get().strip()
        if not termino:
            return

        pos_actual = "1.0"
        total_coincidencias = 0

        while True:
            # Buscar ocurrencia insensible a mayúsculas
            pos_encontrada = self.txt_editor.search(termino, pos_actual, stopindex="end", nocase=True)
            if not pos_encontrada:
                break

            fin_coincidencia = f"{pos_encontrada}+{len(termino)}c"
            self.txt_editor.tag_add("coincidencia_busqueda", pos_encontrada, fin_coincidencia)
            pos_actual = fin_coincidencia
            total_coincidencias += 1

        self.lbl_aviso.configure(text=f"Búsqueda finalizada: {total_coincidencias} coincidencias encontradas.")
        if total_coincidencias == 0:
            messagebox.showinfo("Búsqueda", f"No se encontró '{termino}' en el documento.")

    def _deshacer(self) -> None:
        try:
            self.txt_editor.edit_undo()
            self._actualizar_estadisticas()
        except tk.TclError:
            pass

    def _rehacer(self) -> None:
        try:
            self.txt_editor.edit_redo()
            self._actualizar_estadisticas()
        except tk.TclError:
            pass

    def _actualizar_estadisticas(self, event=None) -> None:
        contenido = self.txt_editor.get("1.0", "end-1c")
        caracteres = len(contenido)
        palabras = len(contenido.split()) if contenido.strip() else 0
        lineas = int(self.txt_editor.index("end-1c").split(".")[0])

        self.lbl_stats.configure(
            text=f"Líneas: {lineas} | Palabras: {palabras} | Caracteres: {caracteres}"
        )


def main():
    root = tk.Tk()
    app = EditorTextoAvanzado(root)
    root.mainloop()


if __name__ == "__main__":
    main()
