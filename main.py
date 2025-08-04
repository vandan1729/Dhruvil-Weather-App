#!/usr/bin/env python3
"""
Gujarat Weather App
A simple web application to display weather data for Gujarat cities from a MySQL database.
"""

from flask import Flask, render_template, request
from database import WeatherDatabase

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def weather_report():
    """Render weather report page"""
    weather_data = []
    city = ""
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            db = WeatherDatabase()
            if db.connect():
                weather_data = db.get_weather_by_city(city)
                db.close()

    return render_template("weather_report.html", weather_data=weather_data, city=city)


def main():
    """Entry point of the application"""
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
