#!/usr/bin/env python3

import cherrypy, os
from core import sparql_connector, result_factory
from cherrypy import tools
from mako.template import Template
from pandas import DataFrame

import core.training_data as TD
import core.config as CFG
from core.decision_tree import DecisionTreeClassifier

ROOT = os.path.dirname(os.path.abspath(__file__))

class Tinderism(object):

    def __init__(self):
        pass
        #self.classifier = DecisionTreeClassifier( TD.attr_data, TD.type_data )

    def index(self):
        template = Template(filename='templates/index.html', output_encoding='utf-8', encoding_errors='replace', input_encoding='utf-8')
        return template.render()

    index.exposed = True


    # @cherrypy.tools.json_out()
    def generate(self):
        # get input as an array with 0|1 for each attribute
        #types = self.classifier.classify( DataFrame( [[1,0,0,1,0,1,0,0]], columns=CFG.ATTRIBUTES))

        classification_results = [ 'BedAndBreakfast', 'Campground', 'Hotel', 'Event' ]
        factory = result_factory.ResultFactory().get_results_for( classification_results )


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
