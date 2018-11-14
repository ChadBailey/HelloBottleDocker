#!/usr/bin/python

from bottle import Bottle, request, template
import bjoern

app = Bottle()

@app.route('/ip')
def echoip():
    #NOTE: HTTP_X_FORWARDED_FOR is used if host is behind a reverse proxy such as nginx
    ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
    return ip

@app.route('/')
def hellohtml():
    html = \
"""
<!DOCTYPE html>
<html>
  <body>
    <p>Hello {{ip}}</p>
  </body>
</html>
"""
    return template(html,ip=request.environ.get('REMOTE_ADDR'))

@app.route('/rest')
def hellorest():
    return { 'hello' : 'rest' }

if __name__ == '__main__':
    bjoern.run(app, host='0.0.0.0', port=80)
# This is how you run the WSGI-REF server (sometimes useful for debugging)
#    app.run(host='0.0.0.0', port=80, debug=True)

