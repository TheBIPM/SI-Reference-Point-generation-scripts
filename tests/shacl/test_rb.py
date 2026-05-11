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

    conforms, v_graph, v_text = validate(str(df), shacl_graph=str(sf),
                                         data_graph_format=dff,
                                         shacl_graph_format=sff,
                                         inference='rdfs', debug=False)
    print(v_text)
    assert conforms

if __name__ == "__main__":
    test_rb(Path('../TTL'))
