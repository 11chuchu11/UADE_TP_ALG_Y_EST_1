# Uniturnos Sys GSJ

Trabajo práctico desarrollado para la materia **Algoritmos y Estructuras de Datos I** en la **Universidad Argentina de la Empresa (UADE)**.

## Tabla de Contenidos
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Instrucciones de Uso](#instrucciones-de-uso)
  - [Prerrequisitos](#prerrequisitos)
  - [Pasos de Uso](#pasos-de-uso)
- [Generación de Informes](#generación-de-informes)
- [Estructura del Código](#estructura-del-código)
  - [Módulos y Funciones](#módulos-y-funciones)
- [Archivos Generados](#archivos-generados)

---

## Descripción del Proyecto

**Uniturnos Sys GSJ** es un sistema de gestión de turnos que permite:
- Registrar y gestionar tipos de consultas con códigos únicos.
- Asignar turnos a los usuarios.
- Recopilar valoraciones de conformidad y estados de consulta.
- Generar informes y estadísticas diarias.

Los datos son almacenados en formatos CSV y JSON, y el programa permite la gestión desde la línea de comandos.

---

## Instrucciones de Uso

### Prerrequisitos

- Acceso a una terminal de comandos.
- Python 3.0 o superior instalado.
- Conocimientos básicos de terminal de comandos.

### Pasos de Uso

1. **Inicialización del Programa**
   - Cree un entorno virtual si no existe:
     ```bash
     python -m venv venv
     ```
   - Active el entorno virtual:
     ```bash
     ./venv/scripts/Activate  # Windows
     source ./venv/bin/activate  # macOS/Linux
     ```
   - Ejecute el programa:
     ```bash
     python main.py  # Windows
     python3 main.py  # macOS/Linux
     ```

2. **Carga de Operaciones**
   - En el primer inicio, cargue 5 tipos de consulta con un código único (100-999) y su nombre.
   - Las operaciones se guardarán en `files/operaciones.json` y estarán disponibles para futuros inicios.

3. **Carga de Turnos**
   - Ingrese los datos personales del alumno (legajo, nombre, apellido, email).
   - Seleccione un tipo de consulta y reciba el puesto asignado.
   - Proporcione la valoración de conformidad (1 a 3) y el estado de la consulta (1 a 3).

4. **Generación de Informes**
   - Al finalizar, el sistema genera informes detallados y archivos CSV para análisis.

---

## Generación de Informes

Al cierre del día, el sistema genera:
- Tabla de información detallada sobre cada consulta.
- Estadísticas de conformidad y estados de las consultas.

Archivos generados:
- `alumnos.csv`: Lista de alumnos con sus datos personales.
- `turnos.csv`: Detalle de cada turno registrado.
- `operaciones.csv`: Lista de operaciones disponibles.
- `operaciones.json`: Archivo con operaciones cargadas al inicio.

---

## Estructura del Código

El sistema está organizado en módulos para facilitar su mantenimiento:


```text
.
├── main.py
├── app/
│   ├── carga_operaciones.py
│   ├── carga_turnos.py
│   ├── generar_informes.py
│   ├── utils/
│   │   ├── archivos.py
│   │   ├── validaciones_regex.py
│   │   ├── mostrar_tabla_operaciones.py
│   │   └── ...
│   └── informes/
│       ├── informe_general.py
│       └── ...
├── files/
│   ├── alumnos.csv
│   ├── turnos.csv
│   ├── operaciones.csv
│   └── operaciones.json

  

### Módulos y Funciones

- **Carga de Operaciones**
  - `cargaOperaciones`: Carga operaciones desde un archivo JSON.
  - `cargaOperacionesManual`: Permite la carga manual de operaciones.
- **Gestión de Turnos**
  - `cargaTurnos`: Administra los turnos de los alumnos.
  - `ingresoUsuario`: Maneja el ingreso de datos personales.
  - `ingresoOperacion`: Selección de operaciones disponibles.
- **Generación de Informes**
  - `generarInformes`: Crea tablas y archivos con estadísticas y datos registrados.
- **Funciones Útiles**
  - Validación de entradas: `validarEmail`, `validarEntero`, `validarRango`.
  - Gestión de archivos: `cargaCSV`, `generarCSV`, `cargaJSON`, `generarJSON`.

---

## Archivos Generados

1. **`alumnos.csv`**
   - Formato: `id_alumno, nombre, apellido, legajo, email`.

2. **`turnos.csv`**
   - Formato: `id_turno, id_alumno, puesto, conformidad, estado, id_operación, fecha, hora`.

3. **`operaciones.csv`**
   - Formato: `id_operación, código, nombre`.

4. **`operaciones.json`**
   - Estructura: `[{ "id": int, "código": int, "nombre": string }]`.

---

## Notas

- Para recargar las operaciones, elimine el archivo `operaciones.json` de la carpeta `files`.
- Todos los datos ingresados son validados automáticamente.
