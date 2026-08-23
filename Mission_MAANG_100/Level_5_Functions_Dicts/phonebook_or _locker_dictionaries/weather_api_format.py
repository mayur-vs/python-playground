# function (Juice Machine) and Dictionary (Data Locker) ka milan karke use karna hain

def get_weather_update(weather_data) :
    city_name = weather_data["city"]
    temperatue = weather_data["temp"]
    return f"It is {temperatue} degrees in {city_name}"

weather_api_response = {"city": "Mumbai", "temp": 32, "humidity": 80}
weather_info = get_weather_update(weather_api_response)

print(weather_info)