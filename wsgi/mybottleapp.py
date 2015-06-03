from bottle import route, default_app,request,template,static_file
#mybottleapp.py de lolstraw
@route('/')
def principal():
    return template('index.tpl')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
