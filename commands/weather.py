import requests
from core.speech_hander import speak
from config import API_KEY_WEATHER

def get_weather(command):
    city = command.split("weather in ")[-1]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_WEATHER}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            speak(f"The weather in {city} is {description} with a temperature of {temperature} degrees Celsius.")
        else:
            speak(f"Could not find weather information for {city}.")
    except Exception as e:
        print(f"Error getting weather: {e}")
        speak("There was an error retrieving weather information.")