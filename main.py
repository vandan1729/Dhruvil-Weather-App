#!/usr/bin/env python3
"""
Gujarat Weather App
A simple command-line weather application for Gujarat cities with MySQL database storage.
"""

from datetime import datetime
from weather_api import WeatherAPI
from database import WeatherDatabase

class WeatherApp:
    def __init__(self):
        self.weather_api = WeatherAPI()
        self.database = WeatherDatabase()
        
    def setup_database(self):
        """Initialize database connection and create tables"""
        if self.database.connect():
            self.database.create_tables()
            return True
        return False

    def save_to_database(self, weather_data):
        """Save weather data to database"""
        data_tuple = (
            weather_data['city'],
            weather_data['temperature'],
            weather_data['feels_like'],
            weather_data['humidity'],
            weather_data['pressure'],
            weather_data['description'],
            weather_data['wind_speed']
        )
        
        record_id = self.database.insert_weather_data(data_tuple)
        if record_id:
            print(f"✅ Weather data saved to database (ID: {record_id})")
        else:
            print("❌ Failed to save weather data to database")

    def display_weather(self, weather_data):
        """Display weather information in a formatted way"""
        print("\n" + "="*50)
        print(f"🌤️  WEATHER REPORT FOR {weather_data['city'].upper()}")
        print("="*50)
        print(f"🌡️  Temperature: {weather_data['temperature']}°C")
        print(f"🤔  Feels like: {weather_data['feels_like']}°C")
        print(f"💧  Humidity: {weather_data['humidity']}%")
        print(f"📊  Pressure: {weather_data['pressure']} hPa")
        print(f"🌤️  Conditions: {weather_data['description'].title()}")
        print(f"💨  Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"⏰  Retrieved at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)

    def show_weather_history(self, city_name):
        """Display weather history for a city"""
        history = self.database.get_weather_history(city_name, 5)
        
        if not history:
            print(f"No weather history found for {city_name}")
            return
            
        print(f"\n📊 RECENT WEATHER HISTORY FOR {city_name.upper()}")
        print("-" * 80)
        print(f"{'Date & Time':<20} {'Temp':<8} {'Humidity':<10} {'Description':<20}")
        print("-" * 80)
        
        for record in history:
            # Handle both dict and tuple formats
            if isinstance(record, dict):
                timestamp = record['timestamp'].strftime('%Y-%m-%d %H:%M')
                temp = f"{record['temperature']}°C"
                humidity = f"{record['humidity']}%"
                desc = record['description'][:18] + ".." if len(record['description']) > 20 else record['description']
            else:
                timestamp = record[7].strftime('%Y-%m-%d %H:%M')
                temp = f"{record[1]}°C"
                humidity = f"{record[3]}%"
                desc = record[5][:18] + ".." if len(record[5]) > 20 else record[5]
            print(f"{timestamp:<20} {temp:<8} {humidity:<10} {desc:<20}")
        print("-" * 80)

    def show_available_cities(self):
        """Display available Gujarat cities"""
        cities = self.weather_api.get_available_cities()
        print("\n🏙️  AVAILABLE GUJARAT CITIES:")
        print("-" * 40)
        
        # Display cities in columns
        for i in range(0, len(cities), 3):
            row = cities[i:i+3]
            print(f"{row[0]:<15} {row[1] if len(row) > 1 else '':<15} {row[2] if len(row) > 2 else '':<15}")
        print("-" * 40)

    def run(self):
        """Main application loop"""
        print("🌤️  Welcome to Gujarat Weather App! 🌤️")
        
        # Setup database
        if not self.setup_database():
            print("❌ Failed to setup database. Exiting...")
            return

        while True:
            print("\n" + "="*50)
            print("MAIN MENU")
            print("="*50)
            print("1. Get weather for a city")
            print("2. View weather history")
            print("3. Show available cities")
            print("4. Exit")
            print("-" * 50)
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                city_name = input("\nEnter city name: ").strip()
                if not city_name:
                    print("❌ Please enter a valid city name")
                    continue
                    
                print(f"🔍 Fetching weather data for {city_name}...")
                weather_data, error = self.weather_api.get_weather_data(city_name)
                
                if error:
                    print(f"❌ {error}")
                else:
                    self.display_weather(weather_data)
                    self.save_to_database(weather_data)
                    
            elif choice == '2':
                city_name = input("\nEnter city name for history: ").strip()
                if not city_name:
                    print("❌ Please enter a valid city name")
                    continue
                self.show_weather_history(city_name)
                
            elif choice == '3':
                self.show_available_cities()
                
            elif choice == '4':
                print("👋 Thank you for using Gujarat Weather App!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1-4.")

        # Close database connection
        self.database.close()

def main():
    """Entry point of the application"""
    try:
        app = WeatherApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted by user. Goodbye!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()