"""
demonstration of SHACL shapes to detect possible issues with the RDF that is being generated
- EndValidityDate after StartValidityDate
-
"""
from pyshacl import validate
from pathlib import Path


def test_rb(TTLpath):
    df = TTLpath / 'cgpm.ttl'
    dff = 'turtle'
    assert df.exists()

    sf = Path(__file__).parent / 'resbod_shacl.ttl'
    sff = 'turtle'
    assert sf.exists()

    conforms, v_graph, v_text = validate(df, shacl_graph=sf,
                                         data_graph_format=dff,
                                         shacl_graph_format=sff,
                                         inference='rdfs', debug=False,
                                         serialize_report_graph=True)
    print(v_text)
