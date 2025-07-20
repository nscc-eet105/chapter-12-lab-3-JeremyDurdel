import requests

zip_code = input("Enter ZIP code: ")
url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid=c7883cbf72af53da44312ce470b39135&units=imperial"
response = requests.get(url)
data = response.json()

city = data['name']
conditions = data['weather'][0]['description'].title()
temperature = data['main']['temp']
feels_like = data['main']['feels_like']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
wind_direction = data['wind']['deg']

print(f"Current Weather for {city}:")
print(f"Conditions: {conditions}")
print(f"Temperature: {int(temperature)} Degrees")
print(f"Feels Like: {int(feels_like)} Degrees")
print(f"Humidity: {humidity}%")
print(f"Wind: {int(wind_speed)} knots @ {wind_direction} degrees")