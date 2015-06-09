#mybottleapp.py de lolstraw

from bottle import route, default_app,Bottle,request,template,static_file
import json
import requests


#FUNCIONES:

#lista de personajes
def listadepersonajes():
	mi_api='fcf7e44d-5a7c-4699-9f58-88423c69fb9d'

	dicc={"champData":"stats","api_key":mi_api}
	lol = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion",params=dicc)

# https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion?locale=es_ES&champData=stats&api_key=fcf7e44d-5a7c-4699-9f58-88423c69fb9d EN ESPAnOL
	personajes=[]

	if lol.status_code == 200:
		champions = json.loads(lol.text)
		for i in champions['data'].keys():
			personajes.append(i)
	return personajes


#Datos de un personaje
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

#lista de los objetos
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


#RUTAS:

@route('/')
def index():
	personajes = listadepersonajes()
	return template("index.tpl", personajes=personajes)
	

@route('/campeon/<name>')
def personaje(name):
	return template ('campeon.tpl' , nombre=name)
	
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.environ['OPENSHIFT_REPO_DIR']+"wsgi/static")

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
