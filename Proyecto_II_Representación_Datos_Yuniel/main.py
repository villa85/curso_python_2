import json
import requests
from funtions import funciones as f

f.crear_user("Yuniel", "Villalón", "villa85", "villalon2511@gmail.com")


response = requests.get('https://itunes.apple.com/search?term=System+of+a+Down')
json_data = json.loads(response.content)
