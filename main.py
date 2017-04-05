#!/usr/bin/env python3

import cherrypy, os, core.mako
from cherrypy import tools
from mako.template import Template

ROOT = os.path.dirname(os.path.abspath(__file__))

class Tinderism(object):
    def index(self):
        template = Template(filename='templates/index.html', output_encoding='utf-8', encoding_errors='replace', input_encoding='utf-8')
        return template.render_unicode()

    index.exposed = True


    def generate(self):
        pass

    generate.exposed = True


if __name__ == '__main__':
    static_root = os.path.join( ROOT, 'static')

    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': static_root
        }
    }

    cherrypy.quickstart(Tinderism(), '/', conf)
