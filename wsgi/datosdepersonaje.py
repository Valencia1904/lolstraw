from bottle import request
import json
import requests
mi_api='fcf7e44d-5a7c-4699-9f58-88423c69fb9d'

dicc={"champData":"stats","api_key":mi_api}
lol = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion",params=dicc)
#nombre=raw_input("Nombre del personaje: ")
nombre="Fizz"
if lol.status_code == 200:
	champions = json.loads(lol.text)
	for dato in champions['data'][nombre]['stats'].keys():
		print dato,"=",champions['data'][nombre]['stats'][dato]
