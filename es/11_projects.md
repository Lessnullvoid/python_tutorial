# Proyectos de Python (Seccion 11)

Esta seccion contiene proyectos practicos de Python que demuestran aplicaciones del mundo real.

## Lista de Proyectos

1. **File Organizer**
   - **Descripcion**: Un script que organiza archivos en un directorio especificado en subdirectorios segun sus tipos de archivo.
   - **Archivo**: [`file_organizer.py`](../11_projects/file_organizer.py)

2. **Todo App**
   - **Descripcion**: Una aplicacion de linea de comandos para gestionar tareas pendientes. Permite anadir, listar, completar y eliminar tareas.
   - **Archivo**: [`todo_app.py`](../11_projects/todo_app.py)

3. **Weather App**
   - **Descripcion**: Una aplicacion de linea de comandos que utiliza la API de OpenWeatherMap para obtener y mostrar el clima actual de una ciudad.
   - **Archivo**: [`weather_app.py`](../11_projects/weather_app.py)

## Objetivos de Aprendizaje
- Comprender como estructurar proyectos de Python.
- Aprender tecnicas de manejo y organizacion de archivos.
- Obtener experiencia en la escritura de scripts para automatizacion.
- Desarrollar habilidades de resolucion de problemas a traves de ejercicios practicos de codificacion.

## Conceptos

### Por que construir proyectos?

Los proyectos son donde todo se une. Despues de aprender conceptos individuales (variables, bucles, funciones, clases, etc.), necesitas practicar combinandolos para resolver problemas reales. Los proyectos te ensenan:

- Como dividir un problema grande en pasos mas pequenos.
- Como estructurar codigo a traves de funciones y clases.
- Como manejar la complejidad del mundo real (errores de entrada del usuario, archivos faltantes, fallos de red).
- Como leer documentacion y usar bibliotecas de terceros.

### Que combinan estos proyectos

| Proyecto | Conceptos clave utilizados |
|----------|---------------------------|
| **File Organizer** | Manejo de archivos, diccionarios, bucles, modulo `os`, metodos de cadenas |
| **Todo App** | Clases (POO), lectura/escritura JSON, listas, entrada del usuario, interfaz de linea de comandos |
| **Weather App** | Solicitudes HTTP (llamadas a API), analisis JSON, manejo de excepciones, diccionarios |

### Como abordar un proyecto

1. **Entender el objetivo**: que deberia hacer el programa terminado?
2. **Planificar la estructura**: que clases/funciones necesitaras?
3. **Empezar pequeno**: haz que la version mas simple funcione primero.
4. **Agregar funcionalidades**: expande paso a paso, probando cada adicion.
5. **Manejar errores**: que puede salir mal? Agrega `try/except` para robustez.

## Descripcion Detallada del Codigo

### file_organizer.py
**File Organizer** es una aplicacion que organiza automaticamente los archivos de un directorio en subcarpetas segun su tipo (imagenes, documentos, audio, video, etc.).

**Funcionalidades:**
- Detecta el tipo de archivo basado en su extension.
- Crea subcarpetas segun el tipo de archivo.
- Mueve archivos a las subcarpetas correspondientes.
- Genera un reporte del proceso de organizacion.

**Ejemplo de uso:**
```python
organizer = FileOrganizer("C:/Users/Example/Downloads")
organizer.organize_files()
```

### todo_app.py
**Todo App** es una aplicacion de linea de comandos para gestionar tareas pendientes (to-dos). Guarda las tareas en un archivo JSON y permite anadir, listar, completar y eliminar tareas.

**Funcionalidades:**
- Anadir nuevas tareas con titulo y descripcion opcional.
- Listar todas las tareas (opcionalmente mostrar las completadas).
- Marcar tareas como completadas.
- Eliminar tareas.

**Ejemplo de uso:**
```python
app = TodoApp()
app.add_todo("Comprar leche", "Comprar leche en el supermercado")
app.list_todos()
```

### weather_app.py
**Weather App** es una aplicacion de linea de comandos que utiliza la API de OpenWeatherMap para mostrar el clima actual de una ciudad. Permite guardar el historial de consultas en un archivo JSON.

**Funcionalidades:**
- Obtener el clima actual de cualquier ciudad.
- Mostrar detalles como temperatura, sensacion termica, humedad y velocidad del viento.
- Guardar el historial de consultas.
- Consultar las ultimas cinco consultas de clima.

**Ejemplo de uso:**
```python
app = WeatherApp()
data = app.get_weather("Mexico City")
print(app.format_weather_data(data))
```

## Configuracion

### 1. Crear y activar un entorno virtual

Un entorno virtual mantiene las dependencias de tu proyecto aisladas del resto de tu sistema.

**MacOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

Deberias ver `(venv)` al inicio de tu terminal cuando el entorno este activo.

### 2. Instalar dependencias

Todas las bibliotecas necesarias estan listadas en `requirements.txt` en la raiz del proyecto. Instalalas con:

```bash
pip install -r requirements.txt
```

Esto instala paquetes como `requests`, `pandas`, `numpy`, etc. que los proyectos necesitan.

> **Tip:** Si obtienes errores de permisos, asegurate de que tu entorno virtual este activo (paso 1). Nunca deberas usar `sudo` con un entorno virtual.

### 3. Configurar claves API (Weather App)

La Weather App requiere una clave API gratuita de OpenWeatherMap.

1. Crea una cuenta gratuita en [openweathermap.org](https://openweathermap.org/).
2. Ve a [My API Keys](https://home.openweathermap.org/api_keys) y copia tu clave (la cadena larga de caracteres, no el nombre).
3. Crea un archivo `.env` dentro de la carpeta `11_projects/`:

```bash
echo "OPENWEATHER_API_KEY=tu_clave_api_aqui" > 11_projects/.env
```

Reemplaza `tu_clave_api_aqui` con la clave que copiaste.

> **Importante:** Las claves API nuevas pueden tardar hasta 2 horas en activarse. Si obtienes un error 401 Unauthorized, espera e intenta de nuevo mas tarde.

> **Importante:** Nunca subas tu archivo `.env` a git. El `.gitignore` en la raiz del proyecto ya lo excluye.

## Como Ejecutar los Programas

1. Asegurate de que tu entorno virtual este activo (deberias ver `(venv)` en tu terminal).
2. Navega a la raiz del proyecto en tu terminal.
3. Ejecuta el script deseado:

```bash
python 11_projects/file_organizer.py
python 11_projects/todo_app.py
python 11_projects/weather_app.py
```

### Desactivar el entorno virtual

Cuando termines, desactiva el entorno virtual con:

```bash
deactivate
```
