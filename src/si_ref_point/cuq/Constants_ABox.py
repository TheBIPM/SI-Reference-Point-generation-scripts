#
# Constants ABox
#
#
# the module imports the Python script 'settings.py' located in a directory
# above this directory
# Should this lead to an error when executing the present script
# (... not found ...) you might need
# to add the location to the PYTHONPATH by typing
# (in the TERMINAL where you execute the Python script)
# export PYTHONPATH=(path where the package is located)
# (e.g. /Users/gregordudle/Development/Semantic-SI)
#

from rdflib import (URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Graph, Literal,
                    BNode)
from si_ref_point.cuq.CUQ_TBox import SiElements
import si_ref_point.cuq.symbols_format as sf
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER, APIPATH
import owlrl
import yaml
import os
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


def main():
    g = Graph()
    PDF = SiElements()

    # copy over all namespaces from PDF.g to g
    for key, val in PDF.g.namespaces():
        g.bind(key, val)

    # Annotations to the ontology (name, creation date, comment)
    g.add((URIRef(PDF.namespace_constants), RDF.type, OWL.Ontology))
    g.add((URIRef(PDF.namespace_constants), SKOS.prefLabel,
           Literal("SI Reference Point - Constants", datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_constants), RDFS.comment,
           Literal(("Ontology, part of the SI reference point, covering the "
                    "seven underpinning constants of the SI"),
                   datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_constants), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # worksheet containing the basic information
    with open(os.path.join(CUQ_FILES_FOLDER,  'si_constants.yaml')) as fp:
        cst_list = yaml.safe_load(fp)

    # load Units graph (to allow identification of URI for a given unit symbol)
    units_g = Graph()
    units_g.parse(APIPATH + 'si.ttl')
    units_g.parse(APIPATH + 'units.ttl')
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(units_g)

    for cst in cst_list:
        element = PDF.set_constant_uri(cst['id'])
        g.add((element, RDF.type, PDF.Constant))
        g.add((element, PDF.hasValueAsString,
               Literal(cst['value_str'], datatype=XSD.string)))
        g.add((element, PDF.hasUnitAsString,
               Literal(cst['unit_str'], datatype=XSD.string)))
        if cst['value_type'] == "xsd:integer":
            g.add((element, PDF.hasDatatype,  XSD.integer))
            g.add((element, PDF.hasValue,
                   Literal(cst['value'], datatype=XSD.integer,
                           normalize=False)))
        elif cst['value_type'] == "xsd:double":
            # changing the output datatype to xsd:float as RDFLib has a
            # known bug that loses precision in value
            # https://github.com/RDFLib/rdflib/issues/1852
            g.add((element, PDF.hasDatatype, XSD.float))
            g.add((element, PDF.hasValue,
                   Literal(cst['value'], datatype=XSD.float, normalize=False)))
        latex_symbol = sf.formattxt(cst['symbol'], 'latex')
        g.add((element, PDF.hasSymbol,
               Literal(latex_symbol, datatype=XSD.string)))
        g.add((element, PDF.hasUpdatedDate,
               Literal(cst['updateddate'], datatype=XSD.date)))
        g.add((element, SKOS.prefLabel,
               Literal(cst['name_en'], lang="en")))
        g.add((element, SKOS.prefLabel,
               Literal(cst['name_fr'], lang="fr")))
        g.add((element, SKOS.hiddenLabel,
               Literal(cst['hidden_label'], datatype=XSD.string)))
        g.add((element, PDF.hasDefiningResolution,
               PDF.set_cgpm_uri(cst['hasDefiningResolution'])))

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

    g.serialize(format='turtle', destination=APIPATH + 'constants.ttl')


if __name__ == "__main__":
    main()
