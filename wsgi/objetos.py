from bottle import request
import json
import requests
mi_api='fcf7e44d-5a7c-4699-9f58-88423c69fb9d'

# https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item?api_key=fcf7e44d-5a7c-4699-9f58-88423c69fb9d
# https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item?locale=es_ES&itemListData=stats&api_key=fcf7e44d-5a7c-4699-9f58-88423c69fb9d EN ESPAÑOL

dicc={"champData":"stats","api_key":mi_api}
lol = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion",params=dicc)
