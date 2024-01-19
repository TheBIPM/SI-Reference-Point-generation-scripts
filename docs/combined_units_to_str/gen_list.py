from rdflib import Graph, OWL, RDFS, URIRef, BNode

import os
import sys


path_to_api = '/home/fmeynadier/tests/si_ref_point/API'

g = Graph()
g.parse(os.path.join(path_to_api, 'quantities.ttl'))
g.parse(os.path.join(path_to_api, 'units.ttl'))

def unitgraph_to_str(ug):
    if isinstance(ug, URIRef):
        symbq = "SELECT ?symb WHERE {" + g.qname(ug) + " si:hasSymbol ?symb .}"
        symres = g.query(symbq)
        for row in symres:
            return(row[0])
    elif isinstance(ug, BNode):
        import ipdb;ipdb.set_trace()  # noqa



is_qty = """
SELECT DISTINCT ?qty ?unit
WHERE {?qty si:hasUnit ?unit .
}"""

qres = g.query(is_qty)

qty_list = []
for row in qres:
    import ipdb;ipdb.set_trace()  # noqa






