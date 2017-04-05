#!/usr/bin/env python3

import glob
from rdflib import Graph, plugin
from rdflib.serializer import Serializer

PATHS = {
        'accomodations': '../data/accommodation/*.json',
        'events': '../data/event/*.json',
        'infrastructure': '../data/infrastructure/*.json'
}

for ooi_type, current_path in PATHS.items():
    file_list = glob.glob( current_path )

    master_graph = Graph() # .parse(data=testrdf, format='n3')

    for idx, json_file in enumerate( file_list ):
        if(idx >= 1000):
            continue
        with open ( json_file , "r") as myfile:
            print('----')
            print("Current file: "+ json_file)
            print("Graph size: " + str(len(master_graph) ))
            data = myfile.read()
            master_graph.parse(data=data, format='json-ld')
            myfile.close()

    master_graph.serialize( destination="{}.turtle".format(ooi_type), format="turtle")
    master_graph = None

