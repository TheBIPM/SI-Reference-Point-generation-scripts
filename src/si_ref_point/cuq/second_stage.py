import owlrl
from rdflib import Graph, URIRef, BNode
from rdflib.container import Seq


# function to get the power of the unit element
def get_pwr(qty_str: str) -> int:
    try:
        int(qty_str[-1:])
    except ValueError:
        return 1
    else:
        return int(qty_str[-2:])


# function to get the URI of a unit knowing its symbol
def get_uri_for_symbol(sym: str, units_g) -> URIRef:
    query = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX SI: <http://si-digital-framework.org/SI#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?Unit
        WHERE
        {
            ?Unit a SI:MeasurementUnit .
            OPTIONAL{?Unit SI:hasEndValidity ?EndValidity}
            FILTER(!BOUND(?EndValidity))

            ?Unit SI:hasSymbol ?Symbol .
            FILTER (?Symbol='""" + sym + """')
        }"""

    qres = units_g.query(query)
    ausgabe = None
    for elment in qres:
        ausgabe = elment['Unit']
    return ausgabe  # error indicates wrong type...


def add_unitpwr(g_dict: dict) -> Graph:
    units_g = Graph()
    units_g += g_dict['si']
    units_g += g_dict['units']
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(units_g)

    """ Copy-pasted from Constants_ABox.py - needs rewriting anyway
    piece_list = []
    pieces = cst['unit'].split(".")
    for piece in pieces:
        pwr = get_pwr(piece)
        if pwr != 1:
            piece = piece[:-2]
        blankNodeID = BNode()
        URI_unit = get_uri_for_symbol(piece, units_g)
        g.add((blankNodeID, PDF.hasUnit, URI_unit))
        g.add((blankNodeID, PDF.hasUnitPwr, Literal(pwr)))
        piece_list.append(blankNodeID)

    seq_uri = Seq(g, BNode(), piece_list).uri
    g.add((element, PDF.hasUnitElement, seq_uri))
    """
    return g_dict['constants']
