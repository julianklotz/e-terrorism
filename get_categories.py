#!/usr/bin/env python3

import glob
from rdflib import Graph, plugin
from rdflib.serializer import Serializer

PATHS = [
    './data/accommodation/*.json'
]

for current_path in PATHS:
    file_list = glob.glob( current_path )

    master_graph = Graph() # .parse(data=testrdf, format='n3')

    for idx, json_file in enumerate( file_list ):
        if idx >= 100:
            continue

        with open ( json_file , "r") as myfile:
            print('----')
            print("Current file: "+ json_file)
            print("Graph size: " + len(master_graph) )
            data = myfile.read()
            master_graph.parse(data=data, format='json-ld')
            myfile.close()


    import pdb; pdb.set_trace()



