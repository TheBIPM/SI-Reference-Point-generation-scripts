"""
demonstration of SHACL shapes to detect possible issues with the RDF that is being generated
- EndValidityDate after StartValidityDate
-
"""
from pyshacl import validate
from pathlib import Path


def test_siunits(TTLpath):
    df = TTLpath / 'units.ttl'
    dff = 'turtle'
    assert df.exists()

    sf = Path(__file__).parent / 'unit_shacl.ttl'
    sff = 'turtle'
    assert sf.exists()

    conforms, v_graph, v_text = validate(df, shacl_graph=sf,
                                         data_graph_format=dff,
                                         shacl_graph_format=sff,
                                         inference='rdfs', debug=True,
                                         serialize_report_graph=True)
    print(v_text)
