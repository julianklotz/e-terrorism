#!/usr/bin/env python3

import cherrypy, os
from core import sparql_connector
from cherrypy import tools
from mako.template import Template
from pandas import DataFrame

import core.training_data as TD
import core.config as CFG
from core.decision_tree import DecisionTreeClassifier

ROOT = os.path.dirname(os.path.abspath(__file__))

class Tinderism(object):

    def __init__(self):
        self.classifier = DecisionTreeClassifier( TD.attr_data, TD.type_data )

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

        # get input as an array with 0|1 for each attribute
        # self.classifier.classify( DataFrame( data, CFG.ATTRIBUTES))

        con = sparql_connector.SparqlConnector()
        print( con.query_all_lodgings() )

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
