from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']

    # Call the get_weather function
    temperature, humidity = get_weather(city)

    return render_template('weather.html', city=city, temperature=temperature, humidity=humidity)

def get_weather(city):
    # Replace 'YOUR_API_KEY' with your actual Weatherbit API key
    api_key = '25e263864cc84b50b22a16577803055e'
    base_url = f'https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}'

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        weather_data = response.json()

        # Extract temperature from weather data
        temperature = weather_data['data'][0]['temp']
        humidity = weather_data['data'][0]['hum']

        return temperature, humidity
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while retrieving weather data: {e}")
        return None

if __name__ == '__main__':
    app.run()
