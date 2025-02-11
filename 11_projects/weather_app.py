# Weather Application using OpenWeatherMap API
import requests
import json
from datetime import datetime
import os
from dotenv import load_load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

class WeatherApp:
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = API_KEY
    
    def get_weather(self, city):
        """Get weather data for a city"""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use Celsius
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def format_weather_data(self, data):
        """Format weather data for display"""
        if not data:
            return "Unable to get weather data"
        
        weather = data['weather'][0]
        main = data['main']
        
        return f"""
Weather in {data['name']}, {data.get('sys', {}).get('country', '')}
Temperature: {main['temp']}°C
Feels like: {main['feels_like']}°C
Humidity: {main['humidity']}%
Condition: {weather['main']} - {weather['description']}
Wind Speed: {data['wind']['speed']} m/s
"""
    
    def save_weather_history(self, data, filename="weather_history.json"):
        """Save weather data to history"""
        history = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                history = json.load(f)
        
        history.append({
            'timestamp': datetime.now().isoformat(),
            'data': data
        })
        
        with open(filename, 'w') as f:
            json.dump(history, f, indent=2)
    
    def view_history(self, filename="weather_history.json"):
        """View weather history"""
        if not os.path.exists(filename):
            return "No weather history found"
        
        with open(filename, 'r') as f:
            history = json.load(f)
        
        output = "\nWeather History:\n"
        for entry in history[-5:]:  # Show last 5 entries
            data = entry['data']
            output += f"\nTime: {entry['timestamp']}"
            output += f"\nLocation: {data['name']}"
            output += f"\nTemperature: {data['main']['temp']}°C\n"
        
        return output

def main():
    app = WeatherApp()
    
    while True:
        print("\n=== Weather App ===")
        print("1. Get Current Weather")
        print("2. View Weather History")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            city = input("Enter city name: ")
            weather_data = app.get_weather(city)
            if weather_data:
                print(app.format_weather_data(weather_data))
                app.save_weather_history(weather_data)
        
        elif choice == '2':
            print(app.view_history())
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if not API_KEY:
        print("Please set OPENWEATHER_API_KEY in .env file")
    else:
        main() 