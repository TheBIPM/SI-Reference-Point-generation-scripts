"""
demonstration of SHACL shapes to detect possible issues with the RDF that is being generated
- EndValidityDate after StartValidityDate
-
"""
from pyshacl import validate
from os import path
from config import TTLPATH

df = TTLPATH / 'cgpm.ttl'
df = path.abspath(df)
dff = 'turtle'

sf = 'resbod_shacl.ttl'
sf = path.abspath(sf)
sff = 'turtle'

conforms, v_graph, v_text = validate(df, shacl_graph=sf,
                                     data_graph_format=dff,
                                     shacl_graph_format=sff,
                                     inference='rdfs', debug=False,
                                     serialize_report_graph=True)
print(v_text)
