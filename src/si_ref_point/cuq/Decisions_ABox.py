"""
Decisions ABox
"""



from datetime import date
import os
from rdflib import Graph, RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD
import yaml
from si_ref_point.cuq.cuq_tbox import SiElements
from si_ref_point.settings import CUQ_FILES_FOLDER

def cap1(instr):
    """Utility method"""
    return instr[0].upper() + instr[1:]

def main():
    """main of Decision A-box"""
    si_graph = SiElements()
    g = Graph()

    # copy over all namespaces from si_graph.g to g
    for key, val in si_graph.g.namespaces():
        g.bind(key, val)

    # Annotations to the ontology (name, Version number)
    g.add((URIRef(si_graph.namespace_decisions), RDF.type, OWL.Ontology))
    g.add((URIRef(si_graph.namespace_decisions), SKOS.prefLabel,
           Literal("SI Reference Point - Decisions", datatype=XSD.string)))
    g.add((URIRef(si_graph.namespace_decisions), RDFS.comment,
           Literal("Ontology, part of the SI reference point, "
                   "covering decisions",
                   datatype=XSD.string)))
    g.add((URIRef(si_graph.namespace_decisions), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # crawl through the items of the YAML file
    with open(os.path.join(CUQ_FILES_FOLDER, 'decisions.yaml'),
              encoding="utf8") as fp:
        dec_list = yaml.safe_load(fp)
    for dec in dec_list:
        # create an instance of scope if necessary, using the scope code as
        # local name [TODO] : is it really only doing it if necessary ?
        scope = si_graph.set_decision_uri(dec['scopeCode'])
        g.add((scope, RDF.type, si_graph.si_decision_scope))
        # add labels to scope (capitalize the first character)
        g.add((scope, RDFS.label,
               Literal(cap1(dec['scopeEN']), lang="en")))
        g.add((scope, RDFS.label,
               Literal(cap1(dec['scopeFR']), lang="fr")))
        # create instance of target if necessary using target code as local
        # name
        target = si_graph.set_decision_uri(dec['targetCode'])
        g.add((target, RDF.type, si_graph.si_decision_target))
        # add labels to target
        g.add((target, RDFS.label,
               Literal(cap1(dec['targetEN']), lang="en")))
        g.add((target, RDFS.label,
               Literal(cap1(dec['targetFR']), lang="fr")))
        # add links between target and scope
        g.add((scope, si_graph.has_target, target))
        g.add((target, si_graph.is_target_of, scope))
        # create instance of decision if necessary using decision code as local
        # name
        decision = si_graph.set_decision_uri(dec['decisionCode'])
        g.add((decision, RDF.type, si_graph.si_decision))
        # add labels to decision
        g.add((decision, RDFS.label,
               Literal(cap1(dec['decisionEN']), lang="en")))
        g.add((decision, RDFS.label,
               Literal(cap1(dec['decisionFR']), lang="fr")))
        # add links between decision and target
        g.add((target, si_graph.has_decision, decision))
        g.add((decision, si_graph.is_decision_of, target))
        # add link between decision and resolution (retrieved from one of
        # cgpm.ttl, cipm.ttl or cctf.ttl) using the ‘correspondingResolution’
        # object property
        g.add((decision, si_graph.corresponding_resolution,
               si_graph.set_resolution_uri(dec['ID-resolution'])))
        if 'crossReferences' in dec:
            for xref in dec['crossReferences']:
                # add link between decision and the cross-referenced decision
                g.add((decision, SKOS.related, si_graph.set_decision_uri(xref)))



    return g
