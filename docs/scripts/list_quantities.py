""" Generate a list of quantities used in the SI Reference Point """

import logging
import argparse
from pathlib import Path
from rdflib import Graph, RDF, URIRef, BNode

def unitnode_to_str(g, nodeID) -> str|None:
    """ Recursively  generate unit representation strings
    Units may be compound units, i.e. nested binary trees with left and
    right terms, unit powers, multiples, etc...
    """
    fullURI = g.namespace_manager.expand_curie
    if isinstance(nodeID, URIRef):
        """ No further processing, this is the end : fetch corresponding symbol
        and return it
        """
        symbq = ("SELECT ?symb WHERE {" +
                 g.qname(nodeID) + " si:hasSymbol ?symb .}")
        symres = g.query(symbq)
        for srow in symres:
            return srow[0]
    elif isinstance(nodeID, BNode):
        """ This is a blank node, we first have to determine its type
        """
        nodeType = None
        for s, p, o in g.triples((nodeID, RDF.type, None)):
            nodeType = g.qname(str(o))
            break
        if nodeType == "si:UnitProduct":
            """ UnitProduct should have a left and a right term
            """
            leftTerm = ""
            rightTerm = ""
            for s, p, o in g.triples((nodeID, fullURI("si:hasLeftUnitTerm"), None)):
                leftTerm = unitnode_to_str(g, o)
                break
            for s, p, o in g.triples((nodeID, fullURI("si:hasRightUnitTerm"), None)):
                rightTerm = unitnode_to_str(g, o)
                break
            return "{} x {}".format(leftTerm, rightTerm)
        elif nodeType == "si:UnitPower":
            """ Unit power has a numeric exponent and a base unit
            """
            numericExponent = ""
            unitBase = ""
            for s, p, o in g.triples((nodeID, fullURI("si:hasNumericExponent"), None)):
                numericExponent = int(str(o))
                break
            for s, p, o in g.triples((nodeID, fullURI("si:hasUnitBase"), None)):
                unitBase = unitnode_to_str(g, o)
                break
            if numericExponent == 1:
                return "{}".format(unitBase)
            else:
                return "{}^{}".format(unitBase, numericExponent)
        elif nodeType == "si:UnitMultiple":
            """ Unit multiple has a Unit term and a numeric factor
            """
            numericFactor = 1
            unitTerm = ""
            for s, p, o in g.triples((nodeID, fullURI("si:hasNumericFactor"), None)):
                numericFactor = str(o)
                break
            for s, p, o in g.triples((nodeID, fullURI("si:hasunitTerm"), None)):
                unitTerm = unitnode_to_str(g, o)
                break
            return "{} x {}".format(numericFactor, unitTerm)
        elif nodeType == "si:PrefixedUnit":
            """ Prefixed unit has a prefix and a non prefixed unit
            """
            prefix = ""
            nonPrefixedUnit = ""
            for s, p, o in g.triples((nodeID, fullURI("si:hasPrefix"), None)):
                prefix = str(o)
                break
            for s, p, o in g.triples((nodeID, fullURI("si:hasNonPrefixedUnit"), None)):
                nonPrefixedUnit = unitnode_to_str(g, o)
                break
            return "{}{}".format(prefix, nonPrefixedUnit)
        else:
            logging.error("Unable to parse node {}".format(nodeID))
    return None


def main():
    parser = argparse.ArgumentParser(description="Generate list of quantities")
    parser.add_argument(
        "TTLPATH", type=Path,
        help="Directory containing the TTL files")
    args = parser.parse_args()
    # instantiate graph
    g = Graph()
    for ttl_file in ['quantities.ttl', 'units.ttl']:
        file_path = args.TTLPATH / ttl_file
        if not file_path:
            logging.error("{} does not exist, did you run generate_sirp_files ?".format(file_path))
            raise SystemExit
        g.parse(file_path)


    is_qty = """
    SELECT DISTINCT ?qty ?unit ?prefLabelEn
    WHERE {?qty si:hasUnit ?unit .
           ?qty skos:prefLabel ?prefLabelEn .
           FILTER(langmatches(lang(?prefLabelEn),'en'))
    }"""

    qres = g.query(is_qty)

    qty_list = []
    for row in qres:
        qty, unit, label = row
        print("{0:4s} | {1:20s} | {2:}".format(
            g.qname(qty).split(":")[1], unitnode_to_str(g, unit), label))

if __name__ == "__main__":
    main()
