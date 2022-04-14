import requests

API_KEY = "fcc03213821a228c0d04640be25b50e0"
API_CALL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    # coletando a tempo
    weather = data['weather'][0]['description']
    # coventer para celsius e arredondar o valor
    temperature = round(data['main']['temp'] - 273.15, 0)

    print("Weather: ", weather)
    print("Temperature: ", temperature, "Celsius")
else:
    print('error accurred')
