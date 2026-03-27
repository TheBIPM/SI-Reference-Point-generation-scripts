""" Decisions ABox """

import os
import yaml
from datetime import date
from rdflib import RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD
from si_ref_point.tboxes.si_tbox import SiElements
from si_ref_point.settings import SI_FILES_FOLDER

def cap1(instr):
    """Utility method"""
    return instr[0].upper() + instr[1:]

def main():
    """main of Decision A-box"""
    si_graph = SiElements()

    # Annotations to the ontology (name, Version number)
    si_graph.g.add((URIRef(si_graph.namespace_decisions), RDF.type, OWL.Ontology))
    si_graph.g.add((URIRef(si_graph.namespace_decisions), SKOS.prefLabel,
           Literal("SI Reference Point - Decisions", datatype=XSD.string)))
    si_graph.g.add((URIRef(si_graph.namespace_decisions), RDFS.comment,
           Literal("Ontology, part of the SI reference point, "
                   "covering decisions",
                   datatype=XSD.string)))
    si_graph.g.add((URIRef(si_graph.namespace_decisions), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # crawl through the items of the YAML file
    with open(os.path.join(SI_FILES_FOLDER, 'decisions.yaml'),
              encoding="utf8") as fp:
        dec_list = yaml.safe_load(fp)
    for dec in dec_list:
        # create an instance of scope if necessary, using the scope code as
        # local name [TODO] : is it really only doing it if necessary ?
        scope = si_graph.set_decision_uri(dec['scopeCode'])
        si_graph.g.add((scope, RDF.type, si_graph.si_decision_scope))
        # add labels to scope (capitalize the first character)
        si_graph.g.add((scope, RDFS.label,
               Literal(cap1(dec['scopeEN']), lang="en")))
        si_graph.g.add((scope, RDFS.label,
               Literal(cap1(dec['scopeFR']), lang="fr")))
        # create instance of target if necessary using target code as local
        # name
        target = si_graph.set_decision_uri(dec['targetCode'])
        si_graph.g.add((target, RDF.type, si_graph.si_decision_target))
        # add labels to target
        si_graph.g.add((target, RDFS.label,
               Literal(cap1(dec['targetEN']), lang="en")))
        si_graph.g.add((target, RDFS.label,
               Literal(cap1(dec['targetFR']), lang="fr")))
        # add links between target and scope
        si_graph.g.add((scope, si_graph.has_target, target))
        si_graph.g.add((target, si_graph.is_target_of, scope))
        # create instance of decision if necessary using decision code as local
        # name
        decision = si_graph.set_decision_uri(dec['decisionCode'])
        si_graph.g.add((decision, RDF.type, si_graph.si_decision))
        # add labels to decision
        si_graph.g.add((decision, RDFS.label,
               Literal(cap1(dec['decisionEN']), lang="en")))
        si_graph.g.add((decision, RDFS.label,
               Literal(cap1(dec['decisionFR']), lang="fr")))
        # add links between decision and target
        si_graph.g.add((target, si_graph.has_decision, decision))
        si_graph.g.add((decision, si_graph.is_decision_of, target))
        # add link between decision and resolution (retrieved from one of
        # cgpm.ttl, cipm.ttl or cctf.ttl) using the ‘correspondingResolution’
        # object property
        si_graph.g.add((decision, si_graph.corresponding_resolution,
               si_graph.set_resolution_uri(dec['ID-resolution'])))
        if 'crossReferences' in dec:
            for xref in dec['crossReferences']:
                # add link between decision and the cross-referenced decision
                si_graph.g.add((decision, SKOS.related, si_graph.set_decision_uri(xref)))

    return si_graph.g
