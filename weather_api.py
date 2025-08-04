import requests
import os
from dotenv import load_dotenv

load_dotenv()

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Validate API key
        if not self.api_key or self.api_key == 'your_openweathermap_api_key_here':
            print("⚠️  Warning: Please set your WEATHER_API_KEY in .env file")
        
        # Gujarat cities list
        self.gujarat_cities = [
            'Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar',
            'Jamnagar', 'Junagadh', 'Gandhinagar', 'Anand', 'Navsari',
            'Morbi', 'Mahesana', 'Bharuch', 'Vapi', 'Veraval',
            'Godhra', 'Patan', 'Porbandar', 'Palanpur', 'Valsad',
            'Nadiad', 'Surendranagar', 'Bhuj', 'Gandhidham', 'Ankleshwar'
        ]

    def is_gujarat_city(self, city_name):
        """Check if the city is in Gujarat"""
        return city_name.title() in [city.title() for city in self.gujarat_cities]

    def get_weather_data(self, city_name):
        """Fetch weather data for a city"""
        if not self.api_key or self.api_key == 'your_openweathermap_api_key_here':
            return None, "❌ Weather API key not configured. Please update .env file."
            
        if not self.is_gujarat_city(city_name):
            return None, f"Sorry, {city_name} is not a recognized city in Gujarat state."

        try:
            # Make API request
            params = {
                'q': f"{city_name},Gujarat,IN",
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant weather information
            weather_info = {
                'city': data['name'],
                'temperature': round(data['main']['temp'], 2),
                'feels_like': round(data['main']['feels_like'], 2),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'wind_speed': round(data['wind'].get('speed', 0), 2)
            }
            
            return weather_info, None
            
        except requests.exceptions.Timeout:
            return None, "❌ Request timeout. Please check your internet connection."
        except requests.exceptions.RequestException as e:
            return None, f"❌ Error fetching weather data: {e}"
        except KeyError as e:
            return None, f"❌ Error parsing weather data. Missing field: {e}"
        except Exception as e:
            return None, f"❌ Unexpected error: {e}"

    def get_available_cities(self):
        """Return list of available Gujarat cities"""
        return sorted(self.gujarat_cities)