#_*_coding:utf-8_*_

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return 'core.js'


