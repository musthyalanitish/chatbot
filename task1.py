import requests
import socket

def get_ip(host):
    try:
        result = socket.getaddrinfo(host, None)
        ip_address = result[0][4][0] if result else "No IP found"
    except Exception as e:
        ip_address = f"Error: {e}"
    return ip_address

def temp_room(room):
    return "Temp = 20°C, Humidity = 70%"

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"
    querystring = {"location": city, "format": "json", "u": "c"}
    headers = {
        "x-rapidapi-key": "501087d429msh2cac0beffdd4b58p1bf464jsn02d7b49ff5e1",
        "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        d1 = response.json()["current_observation"]
        hum = d1["atmosphere"]["humidity"]
        temp = d1["condition"]["temperature"]
        return f"Humidity: {hum}%, Temp: {temp}°C"
    except Exception as e:
        return f"Error: {e}"
