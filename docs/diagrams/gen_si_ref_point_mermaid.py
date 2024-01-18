from rdflib import Graph, OWL, RDFS

import os
import sys

g = Graph()
for ttl in ['CUQ_core_concepts.ttl', 'CUQ_extended_concepts.ttl']:
    g.parse(os.path.join('..', '..', 'src', 'si_ref_point', 'cuq_data', ttl))


classes = []
for s, p, o in g.triples((None, None, OWL.Class)):
    classes.append(g.qname(s))

properties = []
for s, p, o in g.triples((None, None, OWL.ObjectProperty)):
    properties.append(g.qname(s))

classes_attributes = []
for s, p, o in g.triples((None, RDFS.domain, None)):
    try:
        classes_attributes.append({'class': g.qname(o),
                                   'attr': g.qname(s)})
    except ValueError:
        print("can't parse range for {} or {}".format(s, o))

inheritances = []
for s, p, o in g.triples((None, RDFS.subClassOf, None)):
    try:
        inheritances.append({'superclass': g.qname(o),
                             'subclass': g.qname(s)})
    except ValueError:
        print("can't parse range for {} or {}".format(s, o))


# output mermaid graph
out = sys.stdout

out.write("classDiagram\n")
for inh in inheritances:
    out.write("\t`{}`<|--`{}`\n".format(inh['superclass'],
                                        inh['subclass']))

for cl in classes:
    out.write("\tclass `{}`{{\n".format(cl))
    for at in classes_attributes:
        if at['class'] == cl:
            out.write("\t\t+{}\n".format(at['attr']))
    out.write("\t}\n")




