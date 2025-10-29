# ...existing code...
import requests
import json

def display_weather(city: str, api_key: str):
    """
    Fetch and display current weather for `city` from OpenWeatherMap as JSON output.
    No error handling included.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    # Example usage: enter city name and your OpenWeatherMap API key when prompted
    city = input("City: ")
    api_key = input("OpenWeatherMap API Key: ")
    display_weather(city, api_key)
# ...existing code...