#
# Quantities ABox
#

from rdflib import Graph, RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD
from si_ref_point.cuq.CUQ_TBox import SiElements
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER
import yaml
import os


def main():
    PDF = SiElements()
    g = Graph()

    # copy over all namespaces from PDF.g to g
    for key, val in PDF.g.namespaces():
        g.bind(key, val)

    # Annotations to the ontology (name, Version number)
    g.add((URIRef(PDF.namespace_decisions), RDF.type, OWL.Ontology))
    g.add((URIRef(PDF.namespace_decisions), SKOS.prefLabel,
           Literal("SI Reference Point - Decisions", datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_decisions), RDFS.comment,
           Literal("Ontology, part of the SI reference point, "
                   "covering decisions",
                   datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_decisions), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # crawl through the items of the YAML file
    with open(os.path.join(CUQ_FILES_FOLDER, 'decisions.yaml'),
              encoding="utf8") as fp:
        dec_list = yaml.safe_load(fp)
    for dec in dec_list:
        # create an instance of scope if necessary, using the scope code as
        # local name [TODO] : is it really only doing it if necessary ?
        scope = PDF.set_decision_uri(dec['scopeCode'])
        g.add((scope, RDF.type, PDF.SIDecisionScope))
        # add labels to scope (capitalize the first character)
        g.add((scope, RDFS.label,
               Literal(dec['scopeEN'].capitalize(), lang="en")))
        g.add((scope, RDFS.label,
               Literal(dec['scopeFR'].capitalize(), lang="fr")))
        # create instance of target if necessary using target code as local
        # name
        target = PDF.set_decision_uri(dec['targetCode'])
        g.add((target, RDF.type, PDF.SIDecisionTarget))
        # add labels to target
        g.add((target, RDFS.label,
               Literal(dec['targetEN'].capitalize(), lang="en")))
        g.add((target, RDFS.label,
               Literal(dec['targetFR'].capitalize(), lang="fr")))
        # add links between target and scope
        g.add((scope, PDF.hasTarget, target))
        g.add((target, PDF.isTargetOf, scope))
        # create instance of decision if necessary using decision code as local
        # name
        decision = PDF.set_decision_uri(dec['decisionCode'])
        g.add((decision, RDF.type, PDF.SIDecision))
        # add labels to decision
        g.add((decision, RDFS.label,
               Literal(dec['decisionEN'].capitalize(), lang="en")))
        g.add((decision, RDFS.label,
               Literal(dec['decisionFR'].capitalize(), lang="fr")))
        # add links between decision and target
        g.add((target, PDF.hasDecision, decision))
        g.add((decision, PDF.isDecisionOf, target))
        # add link between decision and resolution (retrieved from one of
        # cgpm.ttl, cipm.ttl or cctf.ttl) using the ‘correspondingResolution’
        # object property
        # [TODO]
        if 'crossReferences' in dec:
            for xref in dec['crossReferences']:
                # add link between decision and the cross-referenced decision
                g.add((decision, SKOS.related, PDF.set_decision_uri(xref)))



    return g
