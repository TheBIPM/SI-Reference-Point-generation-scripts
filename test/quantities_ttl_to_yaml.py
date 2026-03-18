""" Convert TTL files for quantities back to YAML input format

Apart from allogin some testing this also helps backporting additional
quantities introduced by the backoffice
"""

from rdflib import URIRef, Graph, Namespace

import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert quantitities TTL to YAML")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "input_TTL", type=str,
        help="The input quantities knowdledge graphe, serialized as TTL"
    )
    args = parser.parse_args()


    g = Graph()
    g.parse(args.input_TTL, format="n3")

    # Get list of quantities 4-char ids
    qty_list = []
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    skos = Namespace("http://www.w3.org/2004/02/skos/core#")
    si = Namespace("https://si-digital-framework.org/SI#")
    qty = Namespace("https://si-digital-framework.org/quantities/")
    for s, p, o in list(g.triples((None,
                                   URIRef(rdf + 'type'),
                                   URIRef(si + "QuantityKind")
                                  ))):

        q_id = str(s).split('/')[-1]
        if q_id not in qty_list:
            qty_list.append(q_id)

    output = []
    for q_id in qty_list:
        buf = {'identifier': q_id}
        qty = URIRef(qty + q_id)
        for s, p, o in list(g.triples((qty,
                                       URIRef(skos + "prefLabel"),
                                       None))):
            buf['quantity-' + o.language] = str(o)
        for s, p, o in list(g.triples((qty,
                                       URIRef(si + "hasUnit"),
                                       None))):
            buf['Unit'] = str(o)
        output.append(buf)
    import ipdb;ipdb.set_trace()  # noq

if __name__ == "__main__":
    main()
