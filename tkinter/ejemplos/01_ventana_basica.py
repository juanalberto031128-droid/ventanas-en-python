"""
==============================================================================
01_ventana_basica.py - Fundamentos del Ciclo de Vida de una Ventana en Tkinter
==============================================================================
Este script demuestra la inicialización, configuración de propiedades físicas,
centrado en la pantalla y el ciclo de eventos (mainloop) de una aplicación Tkinter.

Conceptos cubiertos:
- Inicialización con tk.Tk()
- Configuración de título, dimensiones y proporciones (geometry, resizable)
- Centrado dinámico en pantalla mediante cálculo de resolución
- Colores de fondo y propiedades avanzadas (alpha / transparencia)
- Intercepción del protocolo de cierre de ventana (WM_DELETE_WINDOW)
- Manipulación reactiva de propiedades en tiempo de ejecución
==============================================================================
"""

import tkinter as tk
from tkinter import messagebox


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Calcula las coordenadas X e Y para centrar la ventana en la pantalla del usuario."""
    # Obtenemos la resolución de la pantalla actual
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Cálculo matemático del punto superior izquierdo (x, y)
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2

    # Aplicamos la geometría con formato: "ANCHO x ALTO + X + Y"
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


def alternar_fondo(ventana: tk.Tk, label: tk.Label) -> None:
    """Alterna el color de fondo de la ventana principal."""
    color_actual = ventana.cget("bg")
    nuevo_color = "#1e293b" if color_actual != "#1e293b" else "#f8fafc"
    nuevo_texto_color = "#f8fafc" if nuevo_color == "#1e293b" else "#0f172a"

    ventana.configure(bg=nuevo_color)
    label.configure(
        bg=nuevo_color,
        fg=nuevo_texto_color,
        text=f"Color actual del fondo: {nuevo_color}"
    )


def confirmar_salida(ventana: tk.Tk) -> None:
    """Muestra un diálogo de confirmación antes de destruir la ventana."""
    respuesta = messagebox.askyesno(
        title="Confirmar Salida",
        message="¿Estás seguro de que deseas cerrar esta ventana?",
        icon="question"
    )
    if respuesta:
        print("[01_ventana_basica] Cerrando ventana y finalizando mainloop.")
        ventana.destroy()


def main():
    # 1. Instanciamos la ventana raíz principal
    root = tk.Tk()

    # 2. Asignamos un título visible en la barra superior
    root.title("01 - Ventana Básica y Propiedades | Tkinter")

    # 3. Dimensiones deseadas y centrado en el monitor
    ancho_deseado = 650
    alto_deseado = 450
    centrar_ventana(root, ancho_deseado, alto_deseado)

    # 4. Establecer dimensiones mínimas y permitir/restringir redimensión
    root.minsize(450, 300)
    root.maxsize(1000, 800)
    # root.resizable(True, True) -> Permite cambiar ancho y alto (por defecto True, True)

    # 5. Configuración de color de fondo inicial
    root.configure(bg="#f8fafc")

    # 6. Opcional: Nivel de transparencia (0.0 transparente a 1.0 completamente opaco)
    try:
        root.attributes("-alpha", 0.98)
    except tk.TclError:
        pass  # Algunos entornos virtuales o plataformas no soportan alpha

    # 7. Contenido visual explicativo
    contenedor = tk.Frame(root, bg="#ffffff", bd=1, relief="groove", padx=25, pady=25)
    contenedor.pack(expand=True, padx=20, pady=20, fill="both")

    titulo = tk.Label(
        contenedor,
        text="¡Hola Mundo con Tkinter!",
        font=("Helvetica", 18, "bold"),
        bg="#ffffff",
        fg="#2563eb"
    )
    titulo.pack(pady=(0, 10))

    descripcion = tk.Label(
        contenedor,
        text=(
            "Esta ventana demuestra cómo configurar las propiedades básicas de una GUI en Python:\n"
            "• Cálculo y centrado dinámico en pantalla\n"
            "• Dimensiones mínimas y máximas (minsize / maxsize)\n"
            "• Intercepción del protocolo de cierre de ventana (WM_DELETE_WINDOW)\n"
            "• Manipulación dinámica de colores y atributos en vivo"
        ),
        font=("Helvetica", 11),
        bg="#ffffff",
        fg="#475569",
        justify="left"
    )
    descripcion.pack(pady=10)

    lbl_estado = tk.Label(
        contenedor,
        text="Color actual del fondo: #f8fafc",
        font=("Consolas", 10, "italic"),
        bg="#ffffff",
        fg="#0f172a"
    )
    lbl_estado.pack(pady=15)

    # Panel de botones de acción
    panel_botones = tk.Frame(contenedor, bg="#ffffff")
    panel_botones.pack(pady=10)

    btn_color = tk.Button(
        panel_botones,
        text="Alternar Tema Claro / Oscuro",
        font=("Helvetica", 10, "bold"),
        bg="#0284c7",
        fg="#ffffff",
        activebackground="#0369a1",
        activeforeground="#ffffff",
        cursor="hand2",
        padx=12,
        pady=6,
        command=lambda: alternar_fondo(root, lbl_estado)
    )
    btn_color.pack(side="left", padx=5)

    btn_salir = tk.Button(
        panel_botones,
        text="Cerrar Ventana",
        font=("Helvetica", 10),
        bg="#ef4444",
        fg="#ffffff",
        activebackground="#dc2626",
        activeforeground="#ffffff",
        cursor="hand2",
        padx=12,
        pady=6,
        command=lambda: confirmar_salida(root)
    )
    btn_salir.pack(side="left", padx=5)

    # 8. Intercepción del botón [X] de la barra de título del sistema operativo
    root.protocol("WM_DELETE_WINDOW", lambda: confirmar_salida(root))

    # 9. Iniciar el bucle de eventos principal (escucha eventos de teclado, ratón, render)
    root.mainloop()


if __name__ == "__main__":
    main()
