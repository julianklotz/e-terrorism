from core.config import *
from core import sparql_connector
import json

class ResultObject():
    node_id = None
    clazz = None
    name = None
    description = None
    image = None
    ratingValue = None
    reviewCount = None

    def __str__(self):
        return "{}, {}".format(self.name, self.clazz)

class ResultSet():
    lodgings = []
    eat_and_drink = []
    events = []


    def toJSON(self):
        #return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class ResultFactory():
    def __init__(self):
        self.endpoint = sparql_connector.SparqlConnector()

    def get_results_for( self, categories ):
        result_set = ResultSet()
        for cat in categories:
            group = self.resolve_group( cat )

            if( group == GROUP_LODGINGS):
                recommendations = self.endpoint.recommended_lodgings( cat )
                result_set.lodgings += recommendations

            elif( group == GROUP_EAT_AND_DRINK ):
                print("GROUP EAT AND DRINK")
                print("CAT: " + cat)
                recommendations = self.endpoint.recommended_eat_and_drink( cat )
                if(recommendations):
                    result_set.eat_and_drink += recommendations

            elif( group == GROUP_EVENTS ):
                recommendations = self.endpoint.recommended_events( cat )

                if(recommendations):
                    result_set.events += recommendations
            else:
                print("Passing group: " + str(group))

            recommendations = None

        return result_set



    def resolve_group(self, type_label):
        tm = TYPE_MAP

        for key, val in tm.items():
            if( type_label in tm[key] ):
                print('Type: ' + type_label + ', Super type: ' + key)
                return key
