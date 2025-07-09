import os
os.system('cls')
import requests
import pprint
userInput=input("Enter a movie name:")
Url=f"http://www.omdbapi.com/?t={userInput}&apikey=96db55e0"
r=requests.get(Url).json()
pprint.pprint(r)