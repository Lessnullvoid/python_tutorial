# Python Tutorial / Tutorial de Python

## English

A hands-on Python tutorial designed for starting from scratch.
Covers fundamentals through advanced topics with runnable code examples organized in 11 progressive chapters.

-> [Start the tutorial in English](en/README.md)

---

## Espanol

Un tutorial practico de Python disenado para empezar desde cero.
Cubre desde fundamentos hasta temas avanzados con ejemplos ejecutables organizados en 11 capitulos progresivos.

-> [Comenzar el tutorial en Espanol](es/README.md)

---

## Setup / Configuracion

### Prerequisites / Prerrequisitos

Python 3.8+ ([download / descargar](https://www.python.org/))

### Virtual Environment / Entorno Virtual

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**MacOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies / Instalar Dependencias

```bash
pip install -r requirements.txt
```

### API Keys / Claves API

Some projects (e.g. `11_projects/weather_app.py`) require API keys. Follow these steps:

Algunos proyectos (e.g. `11_projects/weather_app.py`) requieren claves API. Sigue estos pasos:

#### 1. Get an OpenWeatherMap API Key / Obtener una clave API de OpenWeatherMap

1. Go to / Ir a [openweathermap.org](https://openweathermap.org/) and create a free account / y crear una cuenta gratuita.
2. Go to / Ir a **My API Keys** in your account dashboard / en el panel de tu cuenta: [openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)
3. Copy your API key / Copiar tu clave API.

#### 2. Create a `.env` file / Crear un archivo `.env`

Create a file named `.env` inside the project folder (e.g. `11_projects/`):

Crear un archivo llamado `.env` dentro de la carpeta del proyecto (e.g. `11_projects/`):

```bash
echo "OPENWEATHER_API_KEY=your_api_key_here" > 11_projects/.env
```

Replace `your_api_key_here` with the key you copied from OpenWeatherMap.

Reemplazar `your_api_key_here` con la clave que copiaste de OpenWeatherMap.

> **Note / Nota:** Never commit `.env` files to git. Add `.env` to your `.gitignore`.
>
> Nunca subas archivos `.env` a git. Agrega `.env` a tu `.gitignore`.

### Deactivate / Desactivar

```bash
deactivate
```

---

### Terminal Cheat Sheets

- MacOS/Linux: https://github.com/0nn0/terminal-mac-cheatsheet
- Windows: https://www.stationx.net/windows-command-line-cheat-sheet/
