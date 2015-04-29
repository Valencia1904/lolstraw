from bottle import request
import json
import requests
mi_api='fcf7e44d-5a7c-4699-9f58-88423c69fb9d'

dicc={"champData":"stats","api_key":mi_api}
lol = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion",params=dicc)

# https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion?locale=es_ES&champData=stats&api_key=fcf7e44d-5a7c-4699-9f58-88423c69fb9d EN ESPAnOL

if lol.status_code == 200:
	champions = json.loads(lol.text)
	for i in champions['data'].keys():
		print i
		
