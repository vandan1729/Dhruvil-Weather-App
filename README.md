# Dhruvil-Weather-App

A Python command-line weather application that provides weather information for cities in Gujarat state, India. The application stores weather data in a MySQL database for historical tracking.

## Features

- 🌤️ Real-time weather data for 25+ Gujarat cities
- 💾 MySQL database storage for weather history
- 📊 View historical weather data
- 🎯 Input validation for Gujarat cities only
- 🖥️ User-friendly command-line interface

## Prerequisites

- Python 3.7+
- MySQL Server
- OpenWeatherMap API key (free)

## Installation

1. Clone the repository and navigate to the project directory
2. Run the setup script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)

4. Set up MySQL database and update `.env` file with your credentials:
   ```
   WEATHER_API_KEY=your_api_key_here
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=weather_app
   ```

## Usage

1. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Follow the menu prompts to:
   - Get current weather for any Gujarat city
   - View weather history
   - See list of available cities

## Supported Cities

The app supports 25+ major cities in Gujarat including:
Ahmedabad, Surat, Vadodara, Rajkot, Bhavnagar, Jamnagar, Junagadh, Gandhinagar, and many more.

## Project Structure

```
Dhruvil-Weather-App/
├── main.py              # Main application file
├── weather_api.py       # Weather API handler
├── database.py          # Database operations
├── requirements.txt     # Python dependencies
├── .env                # Environment variables
├── setup.sh            # Setup script
└── README.md           # Project documentation
```

## Technologies Used

- Python 3
- MySQL
- OpenWeatherMap API
- Requests library
- MySQL Connector