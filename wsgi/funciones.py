import json
import requests

def listadepersonajes():
	dicc={"champData":"stats","api_key":mi_api}
	lol = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion",params=dicc)

	if lol.status_code == 200:
		champions = json.loads(lol.text)
	    return champions['data'].keys():

def datosdepersonaje(nombre):
	dicc={"champData":"stats","api_key":mi_api}
	lol = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion",params=dicc)
	nombre=raw_input("Nombre del personaje: ")

	if lol.status_code == 200:
		datos={}
		champions = json.loads(lol.text)
		
		for dato in champions['data'][nombre]['stats'].keys():
			datos[dato]=champions['data'][nombre]['stats'][dato]
#			print dato,"=",champions['data'][nombre]['stats'][dato]
			
	return datos

def objetos():
	dicc={"locale":"es_ES","itemListData":"stats","api_key":mi_api}
	lol = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item",params=dicc)
	if lol.status_code == 200:
		objetos = json.loads(lol.text)
		lista={}
		
		for i in objetos['data'].keys():
			lista[i]=[objetos['data'][i]['name'],objetos['data'][i]['description']]
#			print i,'=',objetos['data'][i]['name']
#			print '	',objetos['data'][i]['description']
			
	return lista



	
	
	
	
	
	
	
	
	
	
	
	
	
