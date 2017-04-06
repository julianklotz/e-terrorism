from core.config import *
from core import sparql_connector

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
    events = []
    lodgings = []
    eat_and_drink = []
    shopping = []
    pois = []
    activities = []

    def get_lodgings(self):
        return self.lodgigns


class ResultFactory():
    def __init__(self):
        result_set = ResultSet()
        self.endpoint = sparql_connector.SparqlConnector()

    def get_results_for( self, categories ):
        for cat in categories:
            group = self.resolve_group( cat )

            if( group == GROUP_LODGINGS):
                recommendations = self.endpoint.recommended_lodgings( cat )
                print(recommendations)
            else:
                print("Passing group: " + str(group))



    def resolve_group(self, type_label):
        tm = TYPE_MAP

        for key, val in tm.items():
            if( type_label in tm[key] ):
                print('Type: ' + type_label + ', Super type: ' + key)
                return key
