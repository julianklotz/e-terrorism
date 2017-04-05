from SPARQLWrapper import SPARQLWrapper, JSON

class SparqlConnector():
    STORE_URL = "http://localhost:8080/rdf4j-server/repositories/tinderism"
    remote = None


    def __init__(self):
        self.remote = SPARQLWrapper("http://dbpedia.org/sparql")

    def execute_query(self, query):
        self.remote.setQuery(query)
        self.remote.setReturnFormat(JSON)
        results = self.remote.query().convert()
        for result in results["results"]["bindings"]:
            print(result)
        return results


    def query_hotels(self):
        return self.execute_query("""
            PREFIX schema: <http://schema.org/>
            SELECT *
            WHERE {
                ?s a schema:Hotel
            }
        """)

