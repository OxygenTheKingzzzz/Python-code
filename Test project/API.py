import requests
import pprint
import os
os.system('cls')
user_input=input("Enter the name of a city or country:")
Url=f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid=33e08b39312fb6449eed1cb7097f5f8c"
r=requests.get(Url).json()
print(r)
pprint.pprint(r)