#!/usr/bin/env python3

import cherrypy

class Tinderism(object):
    def index(self):
        return "Hello World!"

    index.exposed = True

cherrypy.quickstart(Tinderism())
