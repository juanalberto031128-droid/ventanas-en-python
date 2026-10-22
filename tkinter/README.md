# 🎨 Tkinter Masterclass: Guía Completa y Repositorio de Ejemplos en Python

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GUI Framework](https://img.shields.io/badge/GUI-Tkinter%20%2F%20ttk-38bdf8.svg)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#)

Un repositorio pedagógico, moderno y estructurado que reúne **10 módulos prácticos de código en Python** para aprender a desarrollar interfaces gráficas de usuario (GUI) con **Tkinter** y **ttk**, desde los fundamentos de ventanas hasta una arquitectura orientada a objetos (POO) con persistencia de datos.

Incluye además un **Lanzador Interactivo (`main.py`)** con interfaz gráfica que permite explorar, filtrar y ejecutar todas las demostraciones con un solo clic.

---

## 📋 Tabla de Contenidos

1. [Características del Repositorio](#-características-del-repositorio)
2. [Estructura del Proyecto](#-estructura-del-proyecto)
3. [Requisitos e Instalación](#-requisitos-e-instalación)
4. [Lanzador Visual Interactivo (`main.py`)](#-lanzador-visual-interactivo-mainpy)
5. [Guía Detallada de Archivos y Demostraciones](#-guía-detallada-de-archivos-y-demostraciones)
   - [01. Ventana Básica y Propiedades](#01_ventana_basicapy)
   - [02. Widgets Fundamentales y Reactividad](#02_widgets_fundamentalespy)
   - [03. Gestores de Geometría (`pack`, `grid`, `place`)](#03_layout_managerspy)
   - [04. Widgets Temáticos Avanzados (`ttk`)](#04_ttk_widgets_modernospy)
   - [05. Sistema de Eventos y Atajos de Teclado](#05_eventos_y_bindingspy)
   - [06. Cuadros de Diálogo Nativos](#06_cuadros_de_dialogopy)
   - [07. Gráficos 2D, Animación y Drag & Drop (`Canvas`)](#07_canvas_y_dibujopy)
   - [08. Menús, Barra de Herramientas y Estado](#08_menus_y_navegacionpy)
   - [09. Editor de Texto con Tags y Formato](#09_editor_texto_avanzadopy)
   - [10. Aplicación To-Do con POO y Persistencia JSON](#10_app_poo_to_dopy)
6. [Cómo Subir este Repositorio a GitHub](#-cómo-subir-este-repositorio-a-github)
7. [Buenas Prácticas con Tkinter](#-buenas-prácticas-con-tkinter)
8. [Licencia](#-licencia)

---

## ✨ Características del Repositorio

- **100% Python Estándar**: No requiere instalar paquetes externos (`pip install ...`); Tkinter viene integrado en la biblioteca estándar de Python.
- **Enfoque Progresivo**: Desde conceptos iniciales (título, geometría, centrado) hasta técnicas avanzadas (animaciones a 60 FPS, Canvas vectorial, bindings y POO).
- **Código Didáctico y Comentado**: Cada archivo cuenta con explicaciones detalladas en español, buenas prácticas de tipado y manejo de errores.
- **Diseño Limpio y Moderno**: Uso exhaustivo del subsistema temático `tkinter.ttk` para interfaces estilizadas y consistentes.
- **Lanzador Centralizado**: Ejecuta cualquier demo de forma aislada sin congelar la aplicación principal.

---

## 📂 Estructura del Proyecto

```text
tkinter/
│
├── .gitignore                      # Reglas de exclusión para entornos Python e IDEs
├── LICENSE                         # Licencia de código abierto MIT
├── README.md                       # Documentación exhaustiva del repositorio
├── main.py                         # Lanzador gráfico interactivo de ejemplos
│
└── ejemplos/                       # Módulos demostrativos individuales
    ├── 01_ventana_basica.py        # Inicialización, centrado dinámico y propiedades
    ├── 02_widgets_fundamentales.py # Label, Entry, Button, Checkbutton, Radiobutton
    ├── 03_layout_managers.py       # Comparativa interactiva de pack, grid y place
    ├── 04_ttk_widgets_modernos.py  # Treeview, Combobox, Progressbar, Scale y estilos
    ├── 05_eventos_y_bindings.py    # Ratón, teclado, atajos Ctrl+S y Event Inspector
    ├── 06_cuadros_de_dialogo.py    # MessageBox, FileDialog, ColorChooser, SimpleDialog
    ├── 07_canvas_y_dibujo.py       # Lienzo 2D, animación de rebote y Drag & Drop
    ├── 08_menus_y_navegacion.py    # Barra de menús, clic derecho, toolbar y statusbar
    ├── 09_editor_texto_avanzado.py # Widget Text con etiquetas, búsqueda y undo/redo
    └── 10_app_poo_to_do.py         # Arquitectura POO completa con persistencia JSON
```

---

## 🚀 Requisitos e Instalación

### Requisitos

- **Python 3.8 o superior** instalado en el sistema.

### Verificación de Tkinter

En la mayoría de instalaciones de Windows y macOS, Tkinter ya está disponible por defecto. Puedes comprobarlo ejecutando en tu terminal:

```bash
python -c "import tkinter; print('Tkinter listo. Versión:', tkinter.TkVersion)"
```

> **Nota para usuarios de Linux (Debian / Ubuntu / Raspbian):**  
> Si recibes `ModuleNotFoundError: No module named 'tkinter'`, instálalo con:
> ```bash
> sudo apt-get update && sudo apt-get install python3-tk
> ```

---

## 🖥️ Lanzador Visual Interactivo (`main.py`)

Para explorar todos los ejemplos de forma cómoda e intuitiva, ejecuta el panel interactivo:

```bash
python main.py
```

### Funcionalidades del Lanzador:
- **Filtrado en tiempo real**: Busca por palabra clave (ej. `canvas`, `tabla`, `formulario`, `evento`).
- **Etiquetas de dificultad**: Clasificación por niveles (*Básico*, *Intermedio*, *Avanzado*).
- **Ejecución no bloqueante**: Cada ejemplo se ejecuta en un subproceso aislado, permitiendo abrir múltiples ventanas simultáneamente para compararlas.

---

## 📖 Guía Detallada de Archivos y Demostraciones

---

### `01_ventana_basica.py`
> **Nivel:** Básico  
> **Comando de ejecución:** `python ejemplos/01_ventana_basica.py`

#### ¿Qué hace este archivo?
Explica el ciclo de vida elemental de una ventana de escritorio (`tk.Tk`), cómo centrarla de forma matemática en el monitor del usuario y cómo responder al evento de cierre.

#### Conceptos y Técnicas:
- **Centrado dinámico**: Obtención de dimensiones de pantalla mediante `winfo_screenwidth()` y `winfo_screenheight()`.
- **Dimensiones de ventana**: `geometry("ANCHO x ALTO + X + Y")`.
- **Límites de redimensión**: Uso de `minsize()` y `maxsize()`.
- **Interceptación de eventos del sistema**: Manejo del protocolo `WM_DELETE_WINDOW` con confirmación previa (`messagebox.askyesno`).
- **Manipulación dinámica en vivo**: Botón para alternar el fondo entre tema claro y oscuro en tiempo de ejecución.

---

### `02_widgets_fundamentales.py`
> **Nivel:** Básico  
> **Comando de ejecución:** `python ejemplos/02_widgets_fundamentales.py`

#### ¿Qué hace este archivo?
Presenta los bloques de construcción visuales clásicos de Tkinter y cómo vincularlos a **Variables de Control** reactivas (`StringVar`, `BooleanVar`, `IntVar`).

#### Widgets y Técnicas:
- **`tk.Label`**: Texto estático, fuentes con tuplas `("Segoe UI", 12, "bold")` y colores.
- **`tk.Entry`**: Cajas de texto, uso del cursor inicial con `.focus()`, modo contraseña con `show="•"`, y un checkbox para alternar la visibilidad de la clave.
- **`tk.Checkbutton` y `tk.Radiobutton`**: Selección múltiple e interruptores booleanos vs selecciones exclusivas.
- **`tk.LabelFrame`**: Organización perimetral de controles con borde temático.
- **Observadores reactivos (`trace_add`)**: Actualiza una tarjeta de resumen en tiempo real a medida que el usuario escribe, sin necesidad de pulsar botones.

---

### `03_layout_managers.py`
> **Nivel:** Intermedio  
> **Comando de ejecución:** `python ejemplos/03_layout_managers.py`

#### ¿Qué hace este archivo?
Ofrece una demostración visual interactiva dividida en pestañas (`ttk.Notebook`) de los tres sistemas de posicionamiento que ofrece Tkinter: `pack()`, `grid()` y `place()`.

#### Contenido de cada pestaña:
1. **Gestor `pack()`**: Alineación lineal contra bordes (`side=TOP, BOTTOM, LEFT, RIGHT`), expansión proporcional (`expand=True`) y relleno (`fill=X, Y, BOTH`).
2. **Gestor `grid()`**: Cuadrículas bidimensionales responsivas. Demuestra el uso de `rowspan`, `columnspan`, anclaje `sticky='nsew'` y adaptabilidad con `columnconfigure(weight=...)`.
3. **Gestor `place()`**: Posicionamiento absoluto en píxeles (`x`, `y`) y posicionamiento porcentual relativo (`relx`, `rely`, `relwidth`, `relheight`).
4. **Guía Comparativa**: Resumen teórico de cuándo elegir cada gestor y la regla de oro: *nunca mezclar `pack()` y `grid()` en el mismo contenedor padre*.

---

### `04_ttk_widgets_modernos.py`
> **Nivel:** Intermedio  
> **Comando de ejecución:** `python ejemplos/04_ttk_widgets_modernos.py`

#### ¿Qué hace este archivo?
Explora el módulo `tkinter.ttk` (Themed Tkinter), el cual desacopla la funcionalidad de la apariencia visual y provee componentes ricos ausentes en la librería clásica.

#### Widgets demostrados:
- **`ttk.Style`**: Inspección y cambio en caliente del tema del sistema (`clam`, `alt`, `default`, `vista`).
- **`ttk.Combobox`**: Menú desplegable con evento `<<ComboboxSelected>>` para cambiar el estilo visual.
- **`ttk.Progressbar`**: Barra de progreso con modo *determinado* (+/-10%) y modo *indeterminado* animado continuamente.
- **`ttk.Treeview`**: Tabla estructurada con encabezados, anchos de columna personalizables, alineación de texto y detección de fila seleccionada con `<<TreeviewSelect>>`.
- **`ttk.Scale` y `ttk.Spinbox`**: Deslizador numérico continuo y selector de pasos discretos.

---

### `05_eventos_y_bindings.py`
> **Nivel:** Intermedio  
> **Comando de ejecución:** `python ejemplos/05_eventos_y_bindings.py`

#### ¿Qué hace este archivo?
Implementa un laboratorio interactivo que captura eventos de ratón y teclado, los proyecta visualmente en un lienzo y los registra detalladamente en una consola en vivo.

#### Eventos cubiertos:
- **Ratón**: `<Button-1>` (clic izquierdo), `<Button-2>` (clic central), `<Button-3>` (clic derecho), `<Double-Button-1>` (doble clic), `<Motion>` (coordenadas continuas), `<B1-Motion>` (arrastre), `<Enter>` y `<Leave>` (detección de hover).
- **Teclado**: Captura de teclas físicas mediante `<Key>`, lectura de `event.char`, `event.keysym` y `event.keycode`.
- **Atajos combinados con modificadores**: Atajos globales como `Ctrl+S`, `Ctrl+L` (limpiar consola) y `Esc`.
- **Propagación**: Uso de `return 'break'` para prevenir la propagación de eventos predeterminados.

---

### `06_cuadros_de_dialogo.py`
> **Nivel:** Básico  
> **Comando de ejecución:** `python ejemplos/06_cuadros_de_dialogo.py`

#### ¿Qué hace este archivo?
Un panel interactivo con botones dedicados para invocar todos los tipos de cuadros de diálogo estándar del sistema operativo y registrar su valor de retorno en una consola.

#### Módulos incluidos:
1. **`messagebox`**:
   - Mensajes simples: `showinfo()`, `showwarning()`, `showerror()`.
   - Diálogos de confirmación: `askyesno()`, `askokcancel()`, `askretrycancel()`.
2. **`filedialog`**:
   - `askopenfilename()`: Selección de un archivo individual con filtros por extensión (`.py`, `.txt`, etc.).
   - `askopenfilenames()`: Selección múltiple de archivos.
   - `asksaveasfilename()`: Guardado de documentos con extensión predeterminada.
   - `askdirectory()`: Selección de carpetas.
3. **`colorchooser`**:
   - `askcolor()`: Selector de color nativo que actualiza una tarjeta de muestra con el valor Hexadecimal elegido.
4. **`simpledialog`**:
   - Solicitudes rápidas de texto (`askstring`), enteros con rango (`askinteger`) y decimales (`askfloat`).

---

### `07_canvas_y_dibujo.py`
> **Nivel:** Avanzado  
> **Comando de ejecución:** `python ejemplos/07_canvas_y_dibujo.py`

#### ¿Qué hace este archivo?
Demuestra la potencia gráfica del lienzo vectorial 2D (`tk.Canvas`), incluyendo primitivas geométricas, un bucle de animación fluida y soporte para arrastrar y soltar objetos (Drag & Drop).

#### Técnicas demostradas:
- **Primitivas vectoriales**: `create_line`, `create_rectangle`, `create_oval`, `create_polygon`, `create_arc`, `create_text`.
- **Gestión por identificadores y Tags**: Selección y manipulación en masa con `canvas.coords()` y `canvas.move()`.
- **Física de rebote animada**: Una pelota que detecta colisiones con los bordes de la ventana y se actualiza a 60 FPS mediante `root.after(16, ...)`.
- **Arrastrar y soltar (Drag and Drop)**: Arrastre libre de figuras geométricas calculando deltas de desplazamiento (`dx`, `dy`).
- **Pizarra a mano alzada**: Modo pincel con grosor y selector de color dinámico.

---

### `08_menus_y_navegacion.py`
> **Nivel:** Intermedio  
> **Comando de ejecución:** `python ejemplos/08_menus_y_navegacion.py`

#### ¿Qué hace este archivo?
Construye la arquitectura de navegación completa que se espera en aplicaciones de escritorio comerciales.

#### Componentes:
- **Barra de Menús (`tk.Menu`)**: Menús en cascada (*Archivo*, *Edición*, *Ver*, *Ayuda*).
- **Elementos avanzados de menú**: Comandos con texto acelerador (`Ctrl+N`, `Ctrl+S`), líneas separadoras (`add_separator`), casillas de verificación (`add_checkbutton`) y opciones de selección de zoom con botones de radio (`add_radiobutton`).
- **Menú Contextual (Popup)**: Menú flotante disparado con clic derecho en cualquier parte del área de trabajo mediante `tk_popup()`.
- **Barra de herramientas (Toolbar)**: Acceso directo con botones e iconos descriptivos.
- **Barra de estado (Statusbar)**: Indicadores contextuales en la zona inferior sincronizados con las acciones del usuario.

---

### `09_editor_texto_avanzado.py`
> **Nivel:** Avanzado  
> **Comando de ejecución:** `python ejemplos/09_editor_texto_avanzado.py`

#### ¿Qué hace este archivo?
Construye un editor de texto multilínea enriquecido utilizando el componente `tk.Text`, integrando formateo tipográfico por etiquetas, sincronización de scrollbars y motor de búsqueda.

#### Funcionalidades clave:
- **Sistema de Etiquetas (Tags)**: Creación de estilos como negrita, cursiva, subrayado, resaltado amarillo y bloques de código monoespaciados con `tag_configure()`.
- **Aplicación a selecciones**: Uso de los índices especiales `"sel.first"` y `"sel.last"`.
- **Búsqueda e indexación**: Algoritmo recursivo con `text.search()` para localizar y resaltar coincidencias de texto.
- **Historial de Deshacer/Rehacer**: Pila nativa integrada (`undo=True`, `edit_undo()`, `edit_redo()`).
- **Contador en vivo**: Actualización en tiempo real de líneas, palabras y caracteres calculadas sobre el texto plano.

---

### `10_app_poo_to_do.py`
> **Nivel:** Avanzado  
> **Comando de ejecución:** `python ejemplos/10_app_poo_to_do.py`

#### ¿Qué hace este archivo?
Presenta una solución completa que ilustra la arquitectura recomendada para aplicaciones profesionales en Tkinter: **Programación Orientada a Objetos**, separación de responsabilidades y persistencia de datos.

#### Arquitectura del script:
- **Capa de Modelo y Persistencia (`GestorTareasDatos`)**:
  - Lee y almacena tareas automáticamente en un archivo `tareas.json` en disco.
  - Administra operaciones CRUD (Crear, Leer, Alternar estado y Eliminar).
- **Capa de Vista y Controlador (`ToDoApp`)**:
  - Hereda limpiamente de `tk.Tk`.
  - Formulario de captura rápida con selección de prioridad (Alta, Media, Baja) y envío al presionar `Enter`.
  - Filtro interactivo por pestañas de estado (*Todas*, *Pendientes*, *Completadas*) y buscador en vivo.
  - Tabla `Treeview` que permite cambiar el estado de cualquier tarea con doble clic.
  - Barra de estadísticas que totaliza las tareas pendientes y completadas.

---

## 🌐 Cómo Subir este Repositorio a GitHub

Sigue estos sencillos pasos para publicar tu propio repositorio en GitHub:

### Paso 1: Asegurarte de tener Git instalado
Abre una terminal (PowerShell o CMD) y escribe:
```bash
git --version
```

> **¿No tienes Git instalado?**  
> Puedes instalarlo en Windows en un comando usando winget:
> ```powershell
> winget install --id Git.Git -e --source winget
> ```
> O descárgalo directamente desde el instalador oficial en [git-scm.com](https://git-scm.com/).  
> *(Una vez instalado, reinicia tu terminal)*.

### Paso 2: Configurar tu identidad en Git (si es la primera vez)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@ejemplo.com"
```

### Paso 3: Inicializar el repositorio local
Dentro de la carpeta de este proyecto (`c:\Users\ASUS\Desktop\tkinter`), ejecuta:

```bash
# 1. Inicializar git
git init

# 2. Agregar todos los archivos al área de preparación
git add .

# 3. Crear el primer commit
git commit -m "feat: inicializar repositorio completo con 10 ejemplos de Tkinter y launcher interactivo"

# 4. Asegurar que la rama principal se llame main
git branch -M main
```

### Paso 4: Crear el repositorio en GitHub y enlazarlo
1. Entra a [github.com/new](https://github.com/new) e inicia sesión.
2. Nombra tu repositorio (por ejemplo: `tkinter-python-masterclass` o `aprendiendo-tkinter`).
3. Déjalo como **Público** (o Privado) y **NO marques** las opciones de "Add a README" ni ".gitignore" (ya los tenemos creados aquí).
4. Haz clic en **Create repository**.
5. Copia la URL de tu repositorio (ejemplo: `https://github.com/tu-usuario/tkinter-python-masterclass.git`) y ejecuta:

```bash
git remote add origin https://github.com/tu-usuario/tkinter-python-masterclass.git
git push -u origin main
```

¡Listo! Tu repositorio estará completamente publicado con un README detallado y con formato profesional en GitHub.

---

## 💡 Buenas Prácticas con Tkinter

1. **Evita la importación global `from tkinter import *`**:
   - Prefiere `import tkinter as tk` y `from tkinter import ttk`. Esto evita colisiones de nombres de variables y mejora la legibilidad.
2. **Nunca mezcles `pack()` y `grid()` en el mismo contenedor padre**:
   - Cada contenedor (`tk.Frame` o `tk.Tk`) debe usar exclusivamente uno de los dos. Puedes anidar un marco que use `grid()` dentro de un marco que use `pack()`, pero nunca aplicarlos sobre el mismo contenedor.
3. **Utiliza `ttk` para controles estándar**:
   - Los controles `ttk.Button`, `ttk.Entry` y `ttk.Combobox` se adaptan a las fuentes y estilos modernos del sistema operativo.
4. **No bloquees el hilo principal (`mainloop`)**:
   - Para tareas lentas (como peticiones HTTP o procesamiento pesado de archivos), utiliza el módulo `threading` para evitar que la interfaz gráfica se congele (quede en estado "No responde").
5. **Estructura tu código con Clases (POO)**:
   - Evita variables globales para manejar estados de widgets; encapsular tu GUI en clases facilita el mantenimiento y la escalabilidad.

---

## 📄 Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE). Puedes usarlo, modificarlo, compartirlo y adaptarlo libremente para tus proyectos académicos, personales o comerciales.
