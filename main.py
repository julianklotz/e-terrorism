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
        self.classifier = DecisionTreeClassifier( TD.attr_data, TD.type_data )

    def generate(self, adventure=-1, active=-1, family=-1, outdoor=-1, wellness=-1, couple=-1, culture=-1, lowbudget=-1):
        # get input as an array with 0|1 for each attribute
        classification_results = self.classifier.classify( DataFrame( [[
            self.make_bool( adventure ),
            self.make_bool( active ),
            self.make_bool( family ),
            self.make_bool( outdoor ),
            self.make_bool( wellness ),
            self.make_bool( couple ),
            self.make_bool( culture ),
            self.make_bool( lowbudget ),
        ]], columns=CFG.ATTRIBUTES))

        results = result_factory.ResultFactory().get_results_for( classification_results )
        return results.toJSON()

    generate.exposed = True

    def make_bool(self, val):
        if(val == 'true'):
            return True
        elif(val == 'false'):
            return False
        else:
            return val



if __name__ == '__main__':
    static_root = os.path.join( ROOT, 'static')

    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': static_root,
            'tools.staticdir.index': 'index.html'
        }
    }
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Tinderism(), '/', conf)
