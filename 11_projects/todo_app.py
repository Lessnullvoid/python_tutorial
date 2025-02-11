# Simple Command-line Todo Application
import json
from datetime import datetime
from pathlib import Path

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        if Path(self.filename).exists():
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, title, description=""):
        """Add a new todo item"""
        todo = {
            'id': len(self.todos) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"Added todo: {title}")
    
    def list_todos(self, show_completed=False):
        """List all todos"""
        if not self.todos:
            print("No todos found!")
            return
        
        print("\nTodo List:")
        for todo in self.todos:
            if show_completed or not todo['completed']:
                status = "✓" if todo['completed'] else " "
                print(f"[{status}] {todo['id']}. {todo['title']}")
                if todo['description']:
                    print(f"   {todo['description']}")
    
    def complete_todo(self, todo_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                todo['completed_at'] = datetime.now().isoformat()
                self.save_todos()
                print(f"Marked todo {todo_id} as completed")
                return
        print(f"Todo {todo_id} not found")
    
    def delete_todo(self, todo_id):
        """Delete a todo"""
        self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
        self.save_todos()
        print(f"Deleted todo {todo_id}")

def main():
    app = TodoApp()
    
    while True:
        print("\n=== Todo App ===")
        print("1. Add Todo")
        print("2. List Todos")
        print("3. Complete Todo")
        print("4. Delete Todo")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter todo title: ")
            description = input("Enter description (optional): ")
            app.add_todo(title, description)
        
        elif choice == '2':
            show_completed = input("Show completed todos? (y/n): ").lower() == 'y'
            app.list_todos(show_completed)
        
        elif choice == '3':
            todo_id = int(input("Enter todo ID to complete: "))
            app.complete_todo(todo_id)
        
        elif choice == '4':
            todo_id = int(input("Enter todo ID to delete: "))
            app.delete_todo(todo_id)
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 