from SPARQLWrapper import SPARQLWrapper, JSON

class ResultObject():
    node_id: None
    clazz: None
    name: None
    description: None
    image: None
    caption: None



class SparqlConnector():
    remote = None

    def __init__(self):
        STORE_URL = "http://localhost:8080/rdf4j-server/repositories/inference"
        self.remote = SPARQLWrapper( STORE_URL )

    def prefix_query(self, query):
        return """
        PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
        PREFIX schema: <http://schema.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        """ + query

    def execute_query(self, query):
        query = self.prefix_query(query)
        self.remote.setQuery(query)
        self.remote.setReturnFormat(JSON)
        results = self.remote.query().convert()
        for result in results["results"]["bindings"]:
            print(result)
        return results

    def recommended_lodgings(self, categories):


        pass

    def recommended_events(self):
        pass

    def recommended_eat_drink(self):
        pass

    def query_all_lodgings(self):
        return [ ResultObject(),^gt ]

        return self.execute_query("""
        SELECT DISTINCT ?type ?accomodation ?name ?description
        WHERE {
            ?accomodation a ?type .
            ?type rdfs:subClassOf schema:LodgingBusiness .
            ?accomodation schema:name ?name .
            ?accomodation schema:description ?description .
        }
        """)


