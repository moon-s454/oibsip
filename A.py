import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        print(f"Weather in {location}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather conditions: {weather_description}")
    else:
        print("Error fetching weather data. Please check the location or try again later.")

def main():
    api_key = "0753d5f9f33cf4803e001b93ce1caa29" 
    location = input("Enter a city name or ZIP code: ")
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
