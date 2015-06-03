from bottle import route,run,request,template,static_file
#Página lolstraw
@route('/')
def principal():
    return template('index.tpl')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


