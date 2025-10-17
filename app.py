import requests

api_key = "3cc559478e9ea7fbea8bf3502c3db6a5"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")
complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

response = requests.get(complete_url)
data = response.json()

if data.get("cod") != 200:
    print("Error:", data.get("message", "City Not Found or Invalid API Key"))
else:
    main = data["main"]
    weather = data["weather"][0]
    print(f"City: {city}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Pressure: {main['pressure']} hPa")
    print(f"Weather Description: {weather['description']}")
