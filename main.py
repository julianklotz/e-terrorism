#!/usr/bin/env python3

import cherrypy, os
from core import sparql_connector
from cherrypy import tools
from mako.template import Template

ROOT = os.path.dirname(os.path.abspath(__file__))

class Tinderism(object):
    def index(self):
        template = Template(filename='templates/index.html', output_encoding='utf-8', encoding_errors='replace', input_encoding='utf-8')
        return template.render()

    index.exposed = True


    # @cherrypy.tools.json_out()
    def generate(self):
        # sports_adventure_active
        # hiking_biking
        # family
        # culture
        # fine_living

        con = sparql_connector.SparqlConnector()
        con.query_hotels()

        template = Template(filename='templates/sample_output.json', output_encoding='utf-8', encoding_errors='replace', input_encoding='utf-8')
        return template.render()

    generate.exposed = True


if __name__ == '__main__':
    static_root = os.path.join( ROOT, 'static')

    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': static_root
        }
    }
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.quickstart(Tinderism(), '/', conf)
