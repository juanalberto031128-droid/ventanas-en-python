"""
==============================================================================
02_widgets_fundamentales.py - Controles Básicos y Variables de Control
==============================================================================
Este script explora los componentes visuales esenciales de Tkinter (Widgets)
y la sincronización de datos en tiempo real mediante Variables de Control
(StringVar, IntVar, BooleanVar).

Widgets y conceptos cubiertos:
- tk.Label: Presentación de texto enriquecido, alineación, fuentes y bordes (relief).
- tk.Entry: Cajas de texto de una línea, lectura (.get()), escritura (.insert()),
            borrado (.delete()) y ocultación de caracteres (contraseñas).
- tk.Button: Botones interactivos, estados (normal, disabled), cursos de ratón.
- tk.Checkbutton: Casillas de selección múltiple e interruptores booleanos.
- tk.Radiobutton: Opciones de selección única agrupadas por variable compartida.
- tk.LabelFrame: Marcos de agrupación temática con título perimetral.
- Variables reactivas: StringVar, BooleanVar y observadores de cambios (.trace_add).
==============================================================================
"""

import tkinter as tk
from tkinter import messagebox


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en el monitor del usuario."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


class FormularioWidgetsBasicos:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("02 - Widgets Fundamentales | Tkinter")
        centrar_ventana(self.root, 720, 680)
        self.root.configure(bg="#f1f5f9")
        self.root.minsize(650, 600)

        # ---------------------------------------------------------------------
        # Variables de Control reactivas de Tkinter
        # Sincronizan el estado interno con la interfaz gráfica automáticamente
        # ---------------------------------------------------------------------
        self.var_nombre = tk.StringVar(value="")
        self.var_email = tk.StringVar(value="")
        self.var_password = tk.StringVar(value="")
        self.var_mostrar_pass = tk.BooleanVar(value=False)
        self.var_genero = tk.StringVar(value="Otro")
        self.var_notificaciones = tk.BooleanVar(value=True)
        self.var_terminos = tk.BooleanVar(value=False)

        # Trazadores (observadores) que disparan una función cuando cambia la variable
        self.var_nombre.trace_add("write", self.actualizar_resumen)
        self.var_genero.trace_add("write", self.actualizar_resumen)

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        # Encabezado principal
        lbl_titulo = tk.Label(
            self.root,
            text="Formulario de Demostración de Widgets",
            font=("Segoe UI", 16, "bold"),
            bg="#f1f5f9",
            fg="#1e293b"
        )
        lbl_titulo.pack(pady=(15, 5))

        lbl_subtitulo = tk.Label(
            self.root,
            text="Interactúa con los controles para observar la reactividad en directo",
            font=("Segoe UI", 10),
            bg="#f1f5f9",
            fg="#64748b"
        )
        lbl_subtitulo.pack(pady=(0, 15))

        # Contenedor con scroll o directo
        contenedor = tk.Frame(self.root, bg="#f1f5f9")
        contenedor.pack(fill="both", expand=True, padx=25)

        # =====================================================================
        # 1. LabelFrame: Entradas de Texto (Entry)
        # =====================================================================
        frame_entradas = tk.LabelFrame(
            contenedor,
            text=" 1. Entradas de Texto (tk.Entry) ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#0284c7",
            padx=15,
            pady=10
        )
        frame_entradas.pack(fill="x", pady=6)

        # Nombre
        tk.Label(frame_entradas, text="Nombre completo:", bg="#ffffff", font=("Segoe UI", 9)).grid(row=0, column=0, sticky="w", pady=4)
        entry_nombre = tk.Entry(frame_entradas, textvariable=self.var_nombre, font=("Segoe UI", 10), width=30)
        entry_nombre.grid(row=0, column=1, padx=10, pady=4, sticky="w")
        entry_nombre.focus()  # Pone el cursor en este campo al abrir

        # Correo Electrónico
        tk.Label(frame_entradas, text="Correo Electrónico:", bg="#ffffff", font=("Segoe UI", 9)).grid(row=1, column=0, sticky="w", pady=4)
        entry_email = tk.Entry(frame_entradas, textvariable=self.var_email, font=("Segoe UI", 10), width=30)
        entry_email.grid(row=1, column=1, padx=10, pady=4, sticky="w")

        # Contraseña con toggle de visibilidad
        tk.Label(frame_entradas, text="Contraseña:", bg="#ffffff", font=("Segoe UI", 9)).grid(row=2, column=0, sticky="w", pady=4)
        self.entry_pass = tk.Entry(frame_entradas, textvariable=self.var_password, show="•", font=("Segoe UI", 10), width=30)
        self.entry_pass.grid(row=2, column=1, padx=10, pady=4, sticky="w")

        chk_ver_pass = tk.Checkbutton(
            frame_entradas,
            text="Ver contraseña",
            variable=self.var_mostrar_pass,
            command=self._toggle_ver_password,
            bg="#ffffff",
            activebackground="#ffffff",
            font=("Segoe UI", 9)
        )
        chk_ver_pass.grid(row=2, column=2, padx=5, sticky="w")

        # =====================================================================
        # 2. LabelFrame: Selección Única (Radiobutton)
        # =====================================================================
        frame_radios = tk.LabelFrame(
            contenedor,
            text=" 2. Opciones Exclusivas (tk.Radiobutton) ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#0284c7",
            padx=15,
            pady=10
        )
        frame_radios.pack(fill="x", pady=6)

        tk.Label(frame_radios, text="Identidad / Género:", bg="#ffffff", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        opciones_genero = [("Femenino", "Femenino"), ("Masculino", "Masculino"), ("No binario", "No binario"), ("Prefiero no decir", "Otro")]

        frame_opciones_radio = tk.Frame(frame_radios, bg="#ffffff")
        frame_opciones_radio.pack(fill="x", pady=4)
        for texto, valor in opciones_genero:
            rb = tk.Radiobutton(
                frame_opciones_radio,
                text=texto,
                value=valor,
                variable=self.var_genero,
                bg="#ffffff",
                activebackground="#ffffff",
                font=("Segoe UI", 9)
            )
            rb.pack(side="left", padx=10)

        # =====================================================================
        # 3. LabelFrame: Casillas de Verificación (Checkbutton)
        # =====================================================================
        frame_checks = tk.LabelFrame(
            contenedor,
            text=" 3. Casillas de Verificación (tk.Checkbutton) ",
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            fg="#0284c7",
            padx=15,
            pady=10
        )
        frame_checks.pack(fill="x", pady=6)

        chk_notif = tk.Checkbutton(
            frame_checks,
            text="Deseo recibir notificaciones periódicas por correo",
            variable=self.var_notificaciones,
            bg="#ffffff",
            activebackground="#ffffff",
            font=("Segoe UI", 9)
        )
        chk_notif.pack(anchor="w", pady=2)

        chk_term = tk.Checkbutton(
            frame_checks,
            text="Acepto los Términos de Servicio y Condiciones (Requerido)",
            variable=self.var_terminos,
            command=self._validar_estado_boton_enviar,
            bg="#ffffff",
            activebackground="#ffffff",
            font=("Segoe UI", 9, "bold"),
            fg="#0f172a"
        )
        chk_term.pack(anchor="w", pady=2)

        # =====================================================================
        # 4. Tarjeta de Resumen en Vivo (Label reactivo)
        # =====================================================================
        self.frame_resumen = tk.Frame(contenedor, bg="#e2e8f0", padx=15, pady=8, bd=1, relief="ridge")
        self.frame_resumen.pack(fill="x", pady=8)

        self.lbl_resumen = tk.Label(
            self.frame_resumen,
            text="Resumen en vivo: Escribe un nombre arriba...",
            font=("Consolas", 9),
            bg="#e2e8f0",
            fg="#1e293b",
            anchor="w"
        )
        self.lbl_resumen.pack(fill="x")

        # =====================================================================
        # 5. Botones de Acción (tk.Button)
        # =====================================================================
        frame_acciones = tk.Frame(contenedor, bg="#f1f5f9")
        frame_acciones.pack(fill="x", pady=10)

        self.btn_enviar = tk.Button(
            frame_acciones,
            text="Registrar Datos",
            font=("Segoe UI", 10, "bold"),
            bg="#10b981",
            fg="#ffffff",
            activebackground="#059669",
            activeforeground="#ffffff",
            state=tk.DISABLED,  # Inicia deshabilitado hasta aceptar términos
            padx=15,
            pady=6,
            cursor="arrow",
            command=self._procesar_formulario
        )
        self.btn_enviar.pack(side="left", padx=5)

        btn_limpiar = tk.Button(
            frame_acciones,
            text="Limpiar Campos",
            font=("Segoe UI", 10),
            bg="#94a3b8",
            fg="#ffffff",
            activebackground="#64748b",
            activeforeground="#ffffff",
            padx=15,
            pady=6,
            cursor="hand2",
            command=self._limpiar_formulario
        )
        btn_limpiar.pack(side="left", padx=5)

    def _toggle_ver_password(self) -> None:
        """Muestra u oculta los caracteres del campo de contraseña."""
        if self.var_mostrar_pass.get():
            self.entry_pass.configure(show="")
        else:
            self.entry_pass.configure(show="•")

    def _validar_estado_boton_enviar(self) -> None:
        """Habilita o deshabilita el botón de envío según los términos."""
        if self.var_terminos.get():
            self.btn_enviar.configure(state=tk.NORMAL, cursor="hand2", bg="#10b981")
        else:
            self.btn_enviar.configure(state=tk.DISABLED, cursor="arrow", bg="#94a3b8")

    def actualizar_resumen(self, *args) -> None:
        """Actualiza la barra de resumen reactiva al detectar cambios."""
        nombre = self.var_nombre.get().strip() or "(Sin nombre)"
        genero = self.var_genero.get()
        self.lbl_resumen.configure(
            text=f"Resumen en vivo ➜ Nombre: {nombre} | Identidad: {genero}"
        )

    def _limpiar_formulario(self) -> None:
        """Restaura los valores predeterminados de todos los campos."""
        self.var_nombre.set("")
        self.var_email.set("")
        self.var_password.set("")
        self.var_mostrar_pass.set(False)
        self._toggle_ver_password()
        self.var_genero.set("Otro")
        self.var_notificaciones.set(True)
        self.var_terminos.set(False)
        self._validar_estado_boton_enviar()
        messagebox.showinfo("Formulario Limpio", "Todos los campos fueron restablecidos.")

    def _procesar_formulario(self) -> None:
        """Procesa y valida los datos recopilados."""
        nombre = self.var_nombre.get().strip()
        email = self.var_email.get().strip()

        if not nombre or not email:
            messagebox.showwarning("Campos Requeridos", "Por favor completa al menos Nombre y Correo.")
            return

        detalles = (
            f"Registro exitoso con los siguientes datos:\n\n"
            f"• Nombre: {nombre}\n"
            f"• Correo: {email}\n"
            f"• Género: {self.var_genero.get()}\n"
            f"• Notificaciones: {'Sí' if self.var_notificaciones.get() else 'No'}\n"
            f"• Longitud clave: {len(self.var_password.get())} caracteres"
        )
        messagebox.showinfo("Éxito", detalles)


def main():
    root = tk.Tk()
    app = FormularioWidgetsBasicos(root)
    root.mainloop()


if __name__ == "__main__":
    main()
