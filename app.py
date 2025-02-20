from flask import Flask, jsonify, render_template
import pandas as pd
from weatherprocessing import load_weather_data  # Import function

app = Flask(__name__)

# Load weather data from 'weatherfiles' folder
df = load_weather_data("weatherfiles")

# Route: Home Page
@app.route('/')
def home():
    return "Weather Reporting App is Running!"

# Route: Yearly Extreme Temperature Report
@app.route('/yearly/<int:year>')
def yearly_report(year):
    df['Year'] = df['Date'].dt.year  # Extract year
    yearly_data = df[df['Year'] == year]

    max_temp = yearly_data['Max TemperatureC'].max()
    min_temp = yearly_data['Min TemperatureC'].min()
    max_humidity = yearly_data['Max Humidity'].max()

    report = {
        "Year": year,
        "Max Temperature": max_temp,
        "Min Temperature": min_temp,
        "Max Humidity": max_humidity
    }
    return jsonify(report)

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)
