import requests
from datetime import datetime

user_id = "MayimaClark"
user_apiid = 'd1c1c58b79eac9e2736796a81eb7c78c'

r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=30079,us&units=imperial&appid=" + user_apiid)

time = datetime.fromtimestamp((r.json()["dt"])).strftime('%Y-%m-%d %H:%M:%S')

print('{0:25s} {1:10s}'.format("Name:", r.json()["name"]))
print('{0:25s} {1:3.2f} degrees Fahrenheit'.format("Current Temperature:", r.json()["main"]['temp']))
print('{0:25s} {1:4.2f} hPa'.format("Atmospheric Pressure:", r.json()["main"]['pressure']))
print('{0:25s} {1:3.2f} mph'.format("Wind Speed:", r.json()["wind"]['speed']))
print('{0:25s} {1:5.3f}'.format("Wind Direction:", r.json()["wind"]['deg']))
print('{0:25s} {1:20s}'.format("Time of Report:", time))
