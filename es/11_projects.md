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

## Como Ejecutar los Programas
1. Asegurate de tener Python instalado en tu maquina.
2. Navega al directorio del proyecto en tu terminal.
3. Ejecuta el script deseado utilizando el comando:
   ```bash
   python 11_projects/file_organizer.py
   ```
