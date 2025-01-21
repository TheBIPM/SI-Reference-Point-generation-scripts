"""
constants A-Box
"""

from datetime import date
import os
from rdflib import Graph, URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Literal
import yaml
from si_ref_point.cuq.cuq_tbox import SiElements
import si_ref_point.cuq.symbols_format as sf
from si_ref_point.settings import CUQ_FILES_FOLDER
from si_ref_point.cuq.units_abox import transform_to_graph


def main():
    """ main of constants A-Box"""
    si_graph = SiElements()     # get the predicates and classes that are common to all cuq files
    constants_graph = Graph()   # produce a separate graphe for the units

    # Define the namespaces within (base)/SI
    constants_graph.bind("constants",si_graph.namespace_constants)
    constants_graph.bind("units",si_graph.namespace_units)
    constants_graph.bind("si",si_graph.namespace)


    # 1) Add annotations to the ontology (name, creation date, comment)

    constants_graph.add(
        (URIRef(si_graph.namespace_constants),
         RDF.type,
         OWL.Ontology)
    )
    constants_graph.add(
        (URIRef(si_graph.namespace_constants),
         SKOS.prefLabel,
         Literal("SI Reference Point - Constants", datatype=XSD.string))
    )
    constants_graph.add(
        (URIRef(si_graph.namespace_constants),
         DCTERMS.created,
         Literal(str(date.today()), datatype=XSD.date))
    )
    constants_graph.add(
        (URIRef(si_graph.namespace_constants),
         RDFS.comment,
         Literal(("Ontology, part of the SI reference point, covering the "
                    "seven underpinning constants of the SI"),
                   datatype=XSD.string))
    )
    constants_graph.add(
        (URIRef(si_graph.namespace_constants),
         OWL.versionIRI,
         URIRef("https://si-digital-framework.org/SI/releases/2024-12-17/constants.ttl"))
    )

    # 3) open yaml with information
    with open(os.path.join(CUQ_FILES_FOLDER,  'si_constants.yaml'),
              encoding="utf8") as fp:
        cst_list = yaml.safe_load(fp)

    for cst in cst_list:
        element = si_graph.set_constant_uri(cst['id'])
        constants_graph.add((element, RDF.type, si_graph.constant))
        constants_graph.add((element, si_graph.has_value_as_string,
               Literal(cst['value_str'], datatype=XSD.string)))
        # Deprecated in favor of "combined units" style
        # si_graph.g.add((element, si_graph.hasUnitAsString,
        #       Literal(cst['unit_str'], datatype=XSD.string)))
        if 'unit' in cst and cst['unit'] is not None:
            if isinstance(cst['unit'], list):
                # Transform into dict
                cmpnd_unit = {"mult": []}
                for item in cst['unit']:
                    cmpnd_unit['mult'].append({"exp": [item[0], item[1]]})
                constants_graph, cmpnd_node = transform_to_graph(cmpnd_unit, si_graph, constants_graph)
                constants_graph.add((element, si_graph.has_unit, cmpnd_node))
            else:
                constants_graph.add((element, si_graph.has_unit, si_graph.set_unit_uri(cst['unit'])))
        constants_graph.add((element, si_graph.has_value,
               Literal(cst['value'], datatype=XSD[cst['xsd_type']], normalize=False)))
        constants_graph.add((element, si_graph.has_datatype, XSD[cst['xsd_type']]))
        # note on xsd:double :
        # RDFLib has a known bug that loses precision in value for xsd:double
        # https://github.com/RDFLib/rdflib/issues/1852
        # xsd:float should be preferred

        latex_symbol = sf.formattxt(cst['symbol'], 'latex')
        constants_graph.add((element, si_graph.has_symbol,
               Literal(latex_symbol, datatype=XSD.string)))
        constants_graph.add((element, si_graph.has_updated_date,
               Literal(cst['updateddate'], datatype=XSD.date)))
        constants_graph.add((element, SKOS.prefLabel,
               Literal(cst['name_en'], lang="en")))
        constants_graph.add((element, SKOS.prefLabel,
               Literal(cst['name_fr'], lang="fr")))
        constants_graph.add((element, SKOS.hiddenLabel,
               Literal(cst['hidden_label'], datatype=XSD.string)))
        constants_graph.add((element, si_graph.has_defining_resolution,
               si_graph.set_cgpm_uri(cst['hasDefiningResolution'])))

    return constants_graph


if __name__ == "__main__":
    main()
