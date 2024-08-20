import requests
from collections import Counter
from tkinter import *
from PIL import Image, ImageTk

def fetch_weather_data(api_key, city, hours=12):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&hours={hours}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data['forecast']['forecastday'][0]['hour']
    else:
        return []


def calculate_averages(weather_data):
    averages = {}
    num_groups = len(weather_data) // 3

    for i in range(num_groups):
        group = weather_data[i * 3:(i + 1) * 3]

        avg_temp = sum(hour['temp_c'] for hour in group) / len(group)
        avg_humidity = sum(hour['humidity'] for hour in group) / len(group)
        avg_wind_kph = sum(hour['wind_kph'] for hour in group) / len(group)

        # Hava durumu koşullarını sayma
        conditions = [hour['condition']['text'] for hour in group]
        most_common_condition = Counter(conditions).most_common(1)[0][0]

        time_range = f"{group[0]['time'].split(' ')[1]} - {group[-1]['time'].split(' ')[1]}"
        averages[time_range] = {
            "temperature": round(avg_temp,2),
            "humidity": round(avg_humidity,2),
            "wind": round(avg_wind_kph,2),
            "con": most_common_condition
        }

    return averages

def update_weather(api,city):
    weather_data = fetch_weather_data(api,city)
    if weather_data:
        avg = calculate_averages(weather_data)
    return avg

def resize_image(image_path):
    """Resmi belirli bir boyuta küçült."""
    with Image.open(image_path) as img:
        width, height = img.size  # Genişlik ve yüksekliği al
        img = img.resize((width*0.25,height*0.25),Image.Resampling.BILINEAR)  # Resmi yeniden boyutlandır
        img.save(image_path)  # Aynı dosya adıyla kaydet