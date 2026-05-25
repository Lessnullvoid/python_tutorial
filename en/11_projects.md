# Python Projects (Section 11)

This section contains practical Python projects that demonstrate real-world applications.

## Project List

1. **File Organizer**
   - **Description**: A script that organizes files in a specified directory into subdirectories based on their file types.
   - **File**: [`file_organizer.py`](../11_projects/file_organizer.py)

2. **Todo App**
   - **Description**: A command-line application for managing to-do tasks. Allows adding, listing, completing, and deleting tasks.
   - **File**: [`todo_app.py`](../11_projects/todo_app.py)

3. **Weather App**
   - **Description**: A command-line application that uses the OpenWeatherMap API to fetch and display the current weather for a city.
   - **File**: [`weather_app.py`](../11_projects/weather_app.py)

## Learning Objectives
- Understand how to structure Python projects.
- Learn file handling and organization techniques.
- Gain experience writing scripts for automation.
- Develop problem-solving skills through practical coding exercises.

## Concepts

### Why Build Projects?

Projects are where everything comes together. After learning individual concepts (variables, loops, functions, classes, etc.), you need to practice combining them to solve real problems. Projects teach you:

- How to break a large problem into smaller steps.
- How to structure code across functions and classes.
- How to handle real-world messiness (user input errors, missing files, network failures).
- How to read documentation and use third-party libraries.

### What These Projects Combine

| Project | Key concepts used |
|---------|-------------------|
| **File Organizer** | File handling, dictionaries, loops, `os` module, string methods |
| **Todo App** | Classes (OOP), JSON file I/O, lists, user input, command-line interface |
| **Weather App** | HTTP requests (API calls), JSON parsing, exception handling, dictionaries |

### How to Approach a Project

1. **Understand the goal**: what should the finished program do?
2. **Plan the structure**: what classes/functions will you need?
3. **Start small**: get the simplest version working first.
4. **Add features**: expand step by step, testing each addition.
5. **Handle errors**: what can go wrong? Add `try/except` for robustness.

## Detailed Code Description

### file_organizer.py
**File Organizer** is an application that automatically organizes files in a directory into subfolders based on their type (images, documents, audio, video, etc.).

**Features:**
- Detects file type based on its extension.
- Creates subfolders based on file type.
- Moves files to the corresponding subfolders.
- Generates a report of the organization process.

**Usage example:**
```python
organizer = FileOrganizer("C:/Users/Example/Downloads")
organizer.organize_files()
```

### todo_app.py
**Todo App** is a command-line application for managing to-do tasks. It saves tasks in a JSON file and allows adding, listing, completing, and deleting tasks.

**Features:**
- Add new tasks with a title and optional description.
- List all tasks (optionally show completed ones).
- Mark tasks as completed.
- Delete tasks.

**Usage example:**
```python
app = TodoApp()
app.add_todo("Buy milk", "Buy milk at the supermarket")
app.list_todos()
```

### weather_app.py
**Weather App** is a command-line application that uses the OpenWeatherMap API to display the current weather for a city. It can save query history in a JSON file.

**Features:**
- Get the current weather for any city.
- Display details such as temperature, feels-like temperature, humidity, and wind speed.
- Save query history.
- View the last five weather queries.

**Usage example:**
```python
app = WeatherApp()
data = app.get_weather("Mexico City")
print(app.format_weather_data(data))
```

## How to Run the Programs
1. Make sure Python is installed on your machine.
2. Navigate to the project directory in your terminal.
3. Run the desired script using the command:
   ```bash
   python 11_projects/file_organizer.py
   ```
