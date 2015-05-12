from bottle import Bottle,route,run,request,template,static_file
#indez
@route('/')
def principal():
    return template('html5up-alpha/index.html')


@route('html5up-alpha/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


run(host='0.0.0.0', port=8080)
