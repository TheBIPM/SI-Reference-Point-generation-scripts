import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import os
import matplotlib.pyplot as plt
from pyvis.network import Network

g = rdflib.Graph()
si_graph = g.parse(os.path.join('API', 'si.ttl'))


# subclasses of MeasurementUnit
subMeas = []

q = """
SELECT ?a
WHERE {
    ?a rdfs:subClassOf si:MeasurementUnit .
  }
  """

qres = g.query(q)
for res in qres:
    print(res.a)
    subMeas.append(res.a)

q = """
SELECT ?a
WHERE {
?a schema:domainIncludes si:MeasurementUnit .
  }
  """
qres = g.query(q)
propMeas = []
for res in qres:
    print(res.a)
    propMeas.append(res.a)


q = """
CONSTRUCT { ?s ?p ?o }
WHERE { GRAPH <http://si-digital-framework.org/SI> { ?s ?p ?o } . }
"""

# qres = g.query(q)

G = rdflib_to_networkx_multidigraph(g)


nt = Network('500px', '500px')
nt.from_nx(G)
nt.write_html('nx.html', notebook=False)
