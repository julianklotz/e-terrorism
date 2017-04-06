from SPARQLWrapper import SPARQLWrapper, JSON
from mako.template import Template
from core import result_factory

class SparqlConnector():
    remote = None

    def __init__(self):
        STORE_URL = "http://192.168.1.130:8080/rdf4j-server/repositories/inference"
        self.remote = SPARQLWrapper( STORE_URL )

    def prefix_query(self, query):
        return """
        PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
        PREFIX schema: <http://schema.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        """ + query

    def execute_query(self, query):
        print(query)
        query = self.prefix_query(query)
        self.remote.setQuery(query)
        self.remote.setReturnFormat(JSON)
        results = self.remote.query().convert()

        return results

    def recommended_lodgings(self, category):
        # Add min rating
        # Sort by rating
        # Filter by rating count

        template = Template(filename='templates/sparql/lodgings.sparql',
                input_encoding='utf-8')

        query_str = template.render(category=category)
        results = self.execute_query( query_str )
        return self.map_results_to_object( results, category )


    def map_results_to_object(self, results, category):
        objects = []

        for result in results['results']['bindings']:
            obj = result_factory.ResultObject()

            obj.node_id = result["nodeId"]["value"]
            obj.clazz = category
            obj.name = result['name']['value']
            obj.description = result['description']['value']
            obj.image = result['image']['value']
            obj.ratingValue = result['ratingValue']['value']
            obj.reviewCount = result['reviewCount']['value']

            objects.append(obj)
            print(obj)


        return objects


    def recommended_events(self):
        pass

    def recommended_eat_drink(self):
        pass


