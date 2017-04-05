#!/usr/bin/env python3

import cherrypy, os, core.mako

class Tinderism(object):
    def index(self):
        return "Hello World!"

    index.exposed = True

if __name__ == '__main__':
    static_root = os.path.dirname(os.path.abspath(__file__))
    static_root = os.path.join( static_root, 'static')

    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': static_root
        }
    }
    print(static_root)

    cherrypy.quickstart(Tinderism(), '/', conf)
