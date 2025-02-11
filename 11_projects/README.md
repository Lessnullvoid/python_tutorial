# Python Projects (Section 11)

Esta sección contiene proyectos prácticos de Python que demuestran aplicaciones del mundo real.

## Estructura del Directorio 

## Lista de Proyectos
1. **File Organizer**
   - **Descripción**: Un script que organiza archivos en un directorio especificado en subdirectorios según sus tipos de archivo.
   - **Ubicación**: `file_organizer.py`

2. **Todo App**
   - **Descripción**: Una aplicación de línea de comandos para gestionar tareas pendientes. Permite añadir, listar, completar y eliminar tareas.
   - **Ubicación**: `todo_app.py`

3. **Weather App**
   - **Descripción**: Una aplicación de línea de comandos que utiliza la API de OpenWeatherMap para obtener y mostrar el clima actual de una ciudad.
   - **Ubicación**: `weather_app.py`

## Contenido de Esta Sección
Esta sección incluye varios proyectos de Python que muestran diferentes conceptos y técnicas de programación. Cada proyecto está diseñado para resolver un problema específico o automatizar una tarea, proporcionando experiencia práctica con Python.

## Objetivos de Aprendizaje
- Comprender cómo estructurar proyectos de Python.
- Aprender técnicas de manejo y organización de archivos.
- Obtener experiencia en la escritura de scripts para automatización.
- Desarrollar habilidades de resolución de problemas a través de ejercicios prácticos de codificación.

## Descripción Detallada del Código

### file_organizer.py
**File Organizer** es una aplicación que organiza automáticamente los archivos de un directorio en subcarpetas según su tipo (imágenes, documentos, audio, video, etc.).

**Funcionalidades:**
- Detecta el tipo de archivo basado en su extensión.
- Crea subcarpetas según el tipo de archivo.
- Mueve archivos a las subcarpetas correspondientes.
- Genera un reporte del proceso de organización.

**Ejemplo de uso:**
```python
organizer = FileOrganizer("C:/Users/Example/Downloads")
organizer.organize_files()
```

### todo_app.py
**Todo App** es una aplicación de línea de comandos para gestionar tareas pendientes (to-dos). Guarda las tareas en un archivo JSON y permite añadir, listar, completar y eliminar tareas.

**Funcionalidades:**
- Añadir nuevas tareas con título y descripción opcional.
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
**Weather App** es una aplicación de línea de comandos que utiliza la API de OpenWeatherMap para mostrar el clima actual de una ciudad. Permite guardar el historial de consultas en un archivo JSON.

**Funcionalidades:**
- Obtener el clima actual de cualquier ciudad.
- Mostrar detalles como temperatura, sensación térmica, humedad y velocidad del viento.
- Guardar el historial de consultas.
- Consultar las últimas cinco consultas de clima.

**Ejemplo de uso:**
```python
app = WeatherApp()
data = app.get_weather("Mexico City")
print(app.format_weather_data(data))
```

## Cómo Ejecutar los Programas
1. Asegúrate de tener Python instalado en tu máquina.
2. Clona o descarga el repositorio que contiene los proyectos.
3. Navega al directorio del proyecto en tu terminal.
4. Ejecuta el script deseado utilizando el comando:
   ```bash
   python file_organizer.py
   ```
5. Sigue las instrucciones adicionales proporcionadas en los comentarios del script para su uso específico.

