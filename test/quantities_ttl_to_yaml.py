""" Convert TTL files for quantities back to YAML input format

Apart from allogin some testing this also helps backporting additional
quantities introduced by the backoffice
"""

from rdflib import URIRef, Graph, Namespace

import argparse

rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
si = Namespace("https://si-digital-framework.org/SI#")
qty = Namespace("https://si-digital-framework.org/quantities/")

def get_unit(g, obj):
    if not obj.isidentifier():
        # This a leaf of the binary tree, return the code of the unit, power 1
        return [str(obj).split('/')[-1] , 1]
    else:
        for s, p, o in list(g.triples((obj, URIRef(rdf + 'type'), None))):
            rdftype = o
        if rdftype == URIRef(si + 'UnitProduct'):
            for s, p, o in list(g.triples((obj,
                                           URIRef(si + 'hasLeftUnitTerm'),
                                           None))):
                left_term = get_unit(g, o)
            for s, p, o in list(g.triples((obj,
                                           URIRef(si + 'hasRightUnitTerm'),
                                           None))):
                right_term = get_unit(g, o)
            return [left_term, right_term]
        elif rdftype == URIRef(si + 'UnitPower'):
            for s, p, o in list(g.triples((obj,
                                           URIRef(si + 'hasNumericExponent'),
                                           None))):
                num_ex = o.value
            for s, p, o in list(g.triples((obj,
                                           URIRef(si + 'hasUnitBase'),
                                           None))):
                unit = get_unit(g, o)
                unit[1] = num_ex
            return unit

def flatten_units(units):
    """ flatten the binary tree
    """
    if isinstance(units[0], str) and isinstance(units[1], int):
        return [units]
    elif isinstance(units[0], list) and isinstance(units[1], list):
        return flatten_units(units[0]) + flatten_units(units[1])

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
    for s, p, o in list(g.triples((None,
                                   URIRef(rdf + 'type'),
                                   URIRef(si + "QuantityKind")
                                  ))):

        q_id = str(s).split('/')[-1]
        if q_id not in qty_list:
            qty_list.append(q_id)

    # Gather data for all of these quantities
    output = []
    for q_id in qty_list:
        buf = {'identifier': q_id}
        quantity = URIRef(qty + q_id)
        for s, p, o in list(g.triples((quantity,
                                       URIRef(skos + "prefLabel"),
                                       None))):
            buf['quantity-' + o.language] = str(o)
        for s, p, o in list(g.triples((quantity,
                                       URIRef(si + "hasUnit"),
                                       None))):
            buf['Unit'] = get_unit(g, o)
        output.append(buf)


    print('Number of quantity kinds : {}'.format(len(qty_list)))

    with open('output.yaml', 'w') as fp:
        for qu in output:
            fp.write('- identifier: {}\n'.format(qu['identifier']))
            fp.write('  quantity-en: {}\n'.format(qu['quantity-en']))
            fp.write('  quantity-fr: {}\n'.format(qu['quantity-fr']))
            if 'Unit' not in qu or len(qu['Unit']) == 0:
                fp.write('  Unit: null\n')
            else:
                fp.write('  Unit:\n')
                for el in flatten_units(qu['Unit']):
                    fp.write('    - {}\n'.format(el))


if __name__ == "__main__":
    main()
