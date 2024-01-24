from rdflib import Graph, RDF, URIRef, BNode

import os
import logging


default_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            "..", "..", "build"))

g = Graph()
for ttl_file in ['quantities.ttl', 'units.ttl']:
    file_path = os.path.join(default_path, ttl_file)
    if not os.path.exists(file_path):
        logging.error(
            "{} does not exist, did you run generate_turtle_file ?".format(
                file_path))
        raise SystemExit
    g.parse(file_path)

fullURI = g.namespace_manager.expand_curie


def unitnode_to_str(nodeID) -> str:
    """ Recursively  generate unit representation strings
    Units may be compound units, i.e. nested binary trees with left and
    right terms, unit powers, multiples, etc...
    """
    if isinstance(nodeID, URIRef):
        """ No further processing, this is the end : fetch corresponding symbol
        and return it
        """
        symbq = ("SELECT ?symb WHERE {" +
                 g.qname(nodeID) + " si:hasSymbol ?symb .}")
        symres = g.query(symbq)
        for row in symres:
            return row[0]
    elif isinstance(nodeID, BNode):
        """ This is a blank node, we first have to determine its type
        """
        for s, p, o in g.triples((nodeID, RDF.type, None)):
            nodeType = g.qname(o)
            break
        if nodeType == "si:UnitProduct":
            """ UnitProduct should have a left and a right term
            """
            leftTerm = ""
            rightTerm = ""
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasLeftUnitTerm"),
                                      None)):
                leftTerm = unitnode_to_str(o)
                break
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasRightUnitTerm"),
                                      None)):
                rightTerm = unitnode_to_str(o)
                break
            return "{} x {}".format(leftTerm, rightTerm)
        elif nodeType == "si:UnitPower":
            """ Unit power has a numeric exponent and a base unit
            """
            numericExponent = ""
            unitBase = ""
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasNumericExponent"),
                                      None)):
                numericExponent = int(o)
                break
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasUnitBase"),
                                      None)):
                unitBase = unitnode_to_str(o)
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
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasNumericFactor"),
                                      None)):
                numericFactor = str(o)
                break
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasunitTerm"),
                                      None)):
                unitTerm = unitnode_to_str(o)
                break
                return "{} x {}".format(numericFactor, unitTerm)
        elif nodeType == "si:PrefixedUnit":
            """ Prefixed unit has a prefix and a non prefixed unit
            """
            prefix = ""
            nonPrefixedUnit = ""
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasPrefix"),
                                      None)):
                prefix = str(o)
                break
            for s, p, o in g.triples((nodeID,
                                      fullURI("si:hasNonPrefixedUnit"),
                                      None)):
                nonPrefixedUnit = unitnode_to_str(o)
                break
                return "{}{}".format(prefix, nonPrefixedUnit)
        else:
            logging.error("Unable to parse node {}".format(nodeID))



is_qty = """
SELECT DISTINCT ?qty ?unit
WHERE {?qty si:hasUnit ?unit .
}"""

qres = g.query(is_qty)

qty_list = []
for row in qres:
    qty, unit = row
    print(g.qname(qty), unitnode_to_str(unit))






