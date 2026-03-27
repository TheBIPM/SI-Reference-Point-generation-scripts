

import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from pyvis.network import Network
from config import PROJECT_ROOT

g = rdflib.Graph()
si_path = PROJECT_ROOT / 'src' / 'si_ref_point' / 'TTL' / 'si.ttl'
si_graph = g.parse(si_path)


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
WHERE { GRAPH <https://si-digital-framework.org/SI> { ?s ?p ?o } . }
"""

# qres = g.query(q)

G = rdflib_to_networkx_multidigraph(g)


nt = Network('500px', '500px')
nt.from_nx(G)
nt.write_html('nx.html', notebook=False)
