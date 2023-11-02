import yaml
import os
from rdflib import Graph, URIRef, Namespace

from settings import APIPATH

# load existing decisions.ttl
g = Graph()
g.parse(os.path.join("CUQ",
                     "_docs",
                     "decisions_without_cipm.ttl"), format="ttl")

# add required namespaces
CIPM = Namespace("http://si-digital-framework.org/bodies/CIPM#")
CCTF = Namespace("http://si-digital-framework.org/bodies/CCTF#")
DEC = Namespace("http://si-digital-framework.org/Decisions#")
g.bind("cipm", CIPM)
g.bind("cctf", CCTF)
g.bind("dec", DEC)


# load missing entries from yaml file
with open(os.path.join("CUQ", "_docs", "missing_definitions_cipm.yaml")) as fp:
    missing_list = yaml.safe_load(fp)

ns_dict = dict(g.namespaces())
for missing in missing_list:
    obj_ns, obj_ref = missing['ID-resolution'].split(":")
    OBJ_NAMESPACE = Namespace(ns_dict[obj_ns])
    g.add((URIRef(DEC.term(missing['ID'])),
           URIRef(DEC.correspondingResolution),
           URIRef(OBJ_NAMESPACE.term(obj_ref)),
           ))
# output
g.serialize(format="turtle", destination=APIPATH + "decisions.ttl")
