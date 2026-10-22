"""
==============================================================================
10_app_poo_to_do.py - Arquitectura Profesional con Programación Orientada a Objetos
==============================================================================
Este script implementa una aplicación completa de escritorio (Gestor de Tareas /
To-Do List) siguiendo las mejores prácticas de la industria en Python:
1. Herencia de tk.Tk o composición modular orientada a objetos (POO).
2. Separación de responsabilidades: Modelo de Datos, Persistencia y Capa de Presentación.
3. Persistencia de datos en disco mediante archivo JSON local.
4. Filtrado en tiempo real, búsqueda, prioridades y estadísticas automáticas.
==============================================================================
"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict, Any


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    """Centra la ventana en el monitor del usuario."""
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho) // 2
    posicion_y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")


# =============================================================================
# MODELO DE DATOS Y PERSISTENCIA (Data Layer)
# =============================================================================
class GestorTareasDatos:
    """Maneja el almacenamiento y persistencia de las tareas en formato JSON."""

    def __init__(self, ruta_archivo: str = "tareas.json"):
        self.ruta_archivo = ruta_archivo
        self.tareas: List[Dict[str, Any]] = self._cargar_desde_disco()

    def _cargar_desde_disco(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.ruta_archivo):
            try:
                with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[Error] No se pudo leer {self.ruta_archivo}: {e}")
        # Tareas de bienvenida iniciales
        return [
            {"id": 1, "titulo": "Aprender los widgets básicos de Tkinter", "prioridad": "Alta", "completada": True},
            {"id": 2, "titulo": "Dominar los gestores pack, grid y place", "prioridad": "Alta", "completada": True},
            {"id": 3, "titulo": "Construir una aplicación orientada a objetos", "prioridad": "Media", "completada": False},
            {"id": 4, "titulo": "Subir el repositorio a GitHub con buen README", "prioridad": "Alta", "completada": False},
        ]

    def guardar_en_disco(self) -> None:
        """Guarda la lista actual de tareas en el archivo JSON."""
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(self.tareas, f, indent=4, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error de Guardado", f"No se pudo guardar en disco: {e}")

    def agregar_tarea(self, titulo: str, prioridad: str) -> None:
        nuevo_id = max([t["id"] for t in self.tareas], default=0) + 1
        self.tareas.append({
            "id": nuevo_id,
            "titulo": titulo,
            "prioridad": prioridad,
            "completada": False
        })
        self.guardar_en_disco()

    def alternar_estado(self, tarea_id: int) -> None:
        for t in self.tareas:
            if t["id"] == tarea_id:
                t["completada"] = not t["completada"]
                break
        self.guardar_en_disco()

    def eliminar_tarea(self, tarea_id: int) -> None:
        self.tareas = [t for t in self.tareas if t["id"] != tarea_id]
        self.guardar_en_disco()


# =============================================================================
# APLICACIÓN PRINCIPAL (Capa de Presentación / GUI)
# =============================================================================
class ToDoApp(tk.Tk):
    """Ventana principal que gestiona la interfaz gráfica y los eventos."""

    def __init__(self):
        super().__init__()

        # Configuración de ventana
        self.title("10 - Gestor de Tareas POO con Persistencia | Tkinter")
        centrar_ventana(self, 860, 650)
        self.minsize(780, 560)
        self.configure(bg="#f8fafc")

        # Capa de datos
        self.gestor_datos = GestorTareasDatos()

        # Variables de control
        self.var_nueva_tarea = tk.StringVar()
        self.var_prioridad = tk.StringVar(value="Media")
        self.var_filtro = tk.StringVar(value="Todas")
        self.var_busqueda = tk.StringVar()
        self.var_busqueda.trace_add("write", lambda *args: self._refrescar_tabla())

        # Configurar estilos ttk
        self._configurar_estilos()

        # Construcción de la interfaz
        self._crear_encabezado()
        self._crear_formulario_entrada()
        self._crear_panel_filtros()
        self._crear_tabla_tareas()
        self._crear_barra_estadisticas()

        # Cargar datos iniciales
        self._refrescar_tabla()

    def _configurar_estilos(self) -> None:
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))
        self.style.configure("Treeview", font=("Segoe UI", 10), rowheight=28)
        self.style.map("Treeview", background=[("selected", "#0284c7")])

    def _crear_encabezado(self) -> None:
        header = tk.Frame(self, bg="#0284c7", padx=25, pady=16)
        header.pack(fill="x")

        tk.Label(
            header,
            text="Mi Gestor de Tareas (Task Manager)",
            font=("Segoe UI", 16, "bold"),
            bg="#0284c7",
            fg="#ffffff"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Arquitectura Orientada a Objetos en Tkinter con persistencia JSON automática",
            font=("Segoe UI", 9),
            bg="#0284c7",
            fg="#e0f2fe"
        ).pack(anchor="w")

    def _crear_formulario_entrada(self) -> None:
        frame_input = tk.Frame(self, bg="#ffffff", padx=20, pady=12, bd=1, relief="groove")
        frame_input.pack(fill="x", padx=15, pady=(12, 6))

        tk.Label(frame_input, text="Nueva Tarea:", font=("Segoe UI", 9, "bold"), bg="#ffffff").pack(side="left", padx=(0, 6))

        entry_tarea = ttk.Entry(frame_input, textvariable=self.var_nueva_tarea, font=("Segoe UI", 10))
        entry_tarea.pack(side="left", fill="x", expand=True, padx=6)
        entry_tarea.bind("<Return>", lambda e: self._agregar_tarea())
        entry_tarea.focus()

        tk.Label(frame_input, text="Prioridad:", font=("Segoe UI", 9), bg="#ffffff").pack(side="left", padx=(10, 4))
        cbo_prioridad = ttk.Combobox(frame_input, textvariable=self.var_prioridad, values=["Alta", "Media", "Baja"], state="readonly", width=8)
        cbo_prioridad.pack(side="left", padx=4)

        btn_agregar = tk.Button(
            frame_input,
            text="➕ Agregar",
            bg="#0284c7",
            fg="#ffffff",
            activebackground="#0369a1",
            activeforeground="#ffffff",
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=4,
            cursor="hand2",
            bd=0,
            command=self._agregar_tarea
        )
        btn_agregar.pack(side="left", padx=(10, 0))

    def _crear_panel_filtros(self) -> None:
        frame_filtros = tk.Frame(self, bg="#f8fafc", padx=15, pady=4)
        frame_filtros.pack(fill="x")

        # Filtro de estado
        tk.Label(frame_filtros, text="Filtrar por estado:", font=("Segoe UI", 9), bg="#f8fafc").pack(side="left", padx=(0, 6))
        for opc in ["Todas", "Pendientes", "Completadas"]:
            rb = tk.Radiobutton(
                frame_filtros,
                text=opc,
                variable=self.var_filtro,
                value=opc,
                bg="#f8fafc",
                command=self._refrescar_tabla,
                font=("Segoe UI", 9)
            )
            rb.pack(side="left", padx=5)

        # Búsqueda rápida
        tk.Label(frame_filtros, text="Buscar:", font=("Segoe UI", 9), bg="#f8fafc").pack(side="left", padx=(20, 4))
        entry_buscar = ttk.Entry(frame_filtros, textvariable=self.var_busqueda, width=18)
        entry_buscar.pack(side="left")

    def _crear_tabla_tareas(self) -> None:
        frame_tabla = tk.Frame(self, bg="#ffffff", bd=1, relief="groove")
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=8)

        cols = ("id", "estado", "titulo", "prioridad")
        self.tree = ttk.Treeview(frame_tabla, columns=cols, show="headings", selectmode="browse")

        self.tree.heading("id", text="# ID")
        self.tree.heading("estado", text="Estado")
        self.tree.heading("titulo", text="Descripción de la Tarea")
        self.tree.heading("prioridad", text="Prioridad")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("estado", width=120, anchor="center")
        self.tree.column("titulo", width=420, anchor="w")
        self.tree.column("prioridad", width=90, anchor="center")

        scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll_y.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        # Doble clic para alternar estado
        self.tree.bind("<Double-Button-1>", lambda e: self._alternar_estado_seleccionado())

        # Panel de acciones sobre la tabla
        frame_acciones = tk.Frame(self, bg="#f8fafc", padx=15)
        frame_acciones.pack(fill="x", pady=(0, 6))

        btn_toggle = tk.Button(
            frame_acciones,
            text="✔ Marcar / Desmarcar Completada",
            bg="#10b981",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            padx=10,
            pady=4,
            cursor="hand2",
            bd=0,
            command=self._alternar_estado_seleccionado
        )
        btn_toggle.pack(side="left", padx=2)

        btn_borrar = tk.Button(
            frame_acciones,
            text="🗑 Eliminar Tarea",
            bg="#ef4444",
            fg="white",
            font=("Segoe UI", 9),
            padx=10,
            pady=4,
            cursor="hand2",
            bd=0,
            command=self._eliminar_seleccionada
        )
        btn_borrar.pack(side="left", padx=5)

    def _crear_barra_estadisticas(self) -> None:
        self.statusbar = tk.Frame(self, bg="#e2e8f0", bd=1, relief="sunken", padx=15, pady=4)
        self.statusbar.pack(fill="x", side="bottom")

        self.lbl_stats = tk.Label(
            self.statusbar,
            text="Total: 0 | Pendientes: 0 | Completadas: 0",
            font=("Segoe UI", 9),
            bg="#e2e8f0",
            fg="#334155"
        )
        self.lbl_stats.pack(side="left")

        tk.Label(
            self.statusbar,
            text="Doble clic en una fila para cambiar su estado",
            font=("Segoe UI", 9, "italic"),
            bg="#e2e8f0",
            fg="#64748b"
        ).pack(side="right")

    # =========================================================================
    # LÓGICA DE CONTROLADORES
    # =========================================================================
    def _agregar_tarea(self) -> None:
        titulo = self.var_nueva_tarea.get().strip()
        if not titulo:
            messagebox.showwarning("Aviso", "Ingresa una descripción para la tarea.")
            return

        prioridad = self.var_prioridad.get()
        self.gestor_datos.agregar_tarea(titulo, prioridad)
        self.var_nueva_tarea.set("")
        self._refrescar_tabla()

    def _obtener_id_seleccionado(self) -> int | None:
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Selección", "Por favor selecciona una tarea de la lista.")
            return None
        valores = self.tree.item(seleccion[0])["values"]
        return int(valores[0])

    def _alternar_estado_seleccionado(self) -> None:
        tarea_id = self._obtener_id_seleccionado()
        if tarea_id is not None:
            self.gestor_datos.alternar_estado(tarea_id)
            self._refrescar_tabla()

    def _eliminar_seleccionada(self) -> None:
        tarea_id = self._obtener_id_seleccionado()
        if tarea_id is not None:
            confirm = messagebox.askyesno("Eliminar", "¿Deseas eliminar la tarea seleccionada?")
            if confirm:
                self.gestor_datos.eliminar_tarea(tarea_id)
                self._refrescar_tabla()

    def _refrescar_tabla(self) -> None:
        """Filtra y repuebla el Treeview con los datos actuales."""
        # Limpiar filas existentes
        for item in self.tree.get_children():
            self.tree.delete(item)

        filtro = self.var_filtro.get()
        termino = self.var_busqueda.get().strip().lower()

        total = len(self.gestor_datos.tareas)
        completadas = 0
        pendientes = 0

        for t in self.gestor_datos.tareas:
            if t["completada"]:
                completadas += 1
            else:
                pendientes += 1

            # Filtrar por estado
            if filtro == "Pendientes" and t["completada"]:
                continue
            if filtro == "Completadas" and not t["completada"]:
                continue

            # Filtrar por búsqueda
            if termino and termino not in t["titulo"].lower():
                continue

            estado_str = "✔ Completada" if t["completada"] else "⏳ Pendiente"
            self.tree.insert("", "end", values=(t["id"], estado_str, t["titulo"], t["prioridad"]))

        self.lbl_stats.configure(
            text=f"Total: {total} | Pendientes: {pendientes} | Completadas: {completadas}"
        )


def main():
    app = ToDoApp()
    app.mainloop()


if __name__ == "__main__":
    main()
