#!/usr/bin/python

from bottle import route, run, request, template

@route('/ip')
def echoip():
    #NOTE: HTTP_X_FORWARDED_FOR is used if host is behind a reverse proxy such as nginx
    ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
    return ip

@route('/')
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

@route('/rest')
def hellorest():
    return { 'hello' : 'rest' }

run(host='0.0.0.0', port=80, debug=True)
