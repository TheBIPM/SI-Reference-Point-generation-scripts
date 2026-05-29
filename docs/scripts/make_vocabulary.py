""" Create a vocabulary file and the class_diagram.md file (mermaid code) """

import argparse
from rdflib import Graph, BNode, RDF
from pathlib import Path
from si_ref_point.settings import PKG_ROOT


def main(APIPATH: Path, VOCPATH: Path=None):
    # ------------------------------------------------------------------------
    # load ttl files into knowledge graph
    g = Graph()
    g.parse(APIPATH / 'si.ttl')
    g.parse(APIPATH / 'units.ttl')
    g.parse(APIPATH / 'prefixes.ttl')
    g.parse(APIPATH / 'quantities.ttl')
    g.parse(APIPATH / 'constants.ttl')
    g.parse(APIPATH / 'bodies.ttl')
    g.parse(APIPATH / 'decisions.ttl')
    g.parse(APIPATH / 'cctf.ttl')
    g.parse(APIPATH / 'cgpm.ttl')
    g.parse(APIPATH / 'cipm.ttl')

    # ------------------------------------------------------------------------
    # get classes
    class_query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            SELECT DISTINCT ?Class ?Label ?Superclass
            WHERE
            {
                ?Class a owl:Class .
                OPTIONAL { ?Class rdfs:subClassOf ?Superclass } .
                OPTIONAL { ?Class rdfs:label ?Label } .
                FILTER(langmatches(lang(?Label),'en'))
            }
            ORDER BY ?Class
            """

    # run SPARQL query for units
    c_res = g.query(class_query)

    diagram = {}

    class_list = []
    for element in c_res:
        teil = {
            'class': element['Class'],
            'label': element['Label'],
        }
        # Markdown output
        class_list.append(teil)
        # Diagram output
        try:
            sc = g.qname(element['Superclass'])
        except (ValueError, TypeError):
            sc = "owl:Class"
        diagram[g.qname(element['Class'])] = {'superclass': sc, 'predicates': []}

    with open(VOCPATH / 'vocabulary.md', 'w') as output_file:
        for subject in class_list:
            topic = subject['class'].n3(g.namespace_manager)
            print(topic + ": ", end="")
            predicate_query = """
                PREFIX si: <https://si-digital-framework.org/SI#>
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX rb: <https://si-digital-framework.org/bodies#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                SELECT DISTINCT ?Predicate ?Domain ?Range ?Comment ?Comment_wo
                WHERE
                {
                    BIND (""" + topic + """ AS ?SearchClass)

                    ?class a ?SearchClass .
                    ?class ?Predicate ?o .
                    OPTIONAL {?Predicate rdfs:domain ?Domain}
                    OPTIONAL {?Predicate rdfs:range ?Range}
                    OPTIONAL {?Predicate rdfs:comment ?Comment
                          FILTER (langmatches(lang(?Comment),'en')) }
                }
                ORDER BY ?Predicate
                """
            p_res = g.query(predicate_query)
            print(len(p_res))

            output_file.write('## ' + g.qname(subject['class']) + "\n\n")
            output_file.write(subject['label'] + "\n\n")
            output_file.write(
                '|  Predicate | Domain | Range | Comment |\n'
                '|------------|--------|-------|---------|\n')
            for verb in p_res:
                output_file.write("| ")
                output_file.write(verb['Predicate'].n3(g.namespace_manager))
                output_file.write(" | ")
                pr = g.qname(verb['Predicate'])
                if verb['Range'] is not None:
                    rng = g.qname(verb['Range'])
                else:
                    rng = None
                if verb['Domain'] is not None:
                    if isinstance(verb['Domain'], BNode):
                        items = parse_multi(g, verb['Domain'])
                        output_file.write(", ".join(items))
                        # diagram output
                        for dm in items:
                            if pr not in diagram[dm]['predicates']:
                                diagram[dm]['predicates'].append({
                                    'label': pr,
                                    'range': rng})
                    else:
                        output_file.write(g.qname(verb['Domain']))
                        dm = g.qname(verb['Domain'])
                        if dm not in diagram:
                            diagram[dm] = {'superclass': "foo",
                                           'predicates': []}
                        if pr not in diagram[dm]['predicates']:
                            diagram[dm]['predicates'].append({
                                'label': pr,
                                'range': rng})
                else:
                    output_file.write(" ")
                output_file.write(" | ")
                if verb['Range'] is not None:
                    output_file.write(verb['Range'].n3(g.namespace_manager))
                output_file.write(" | ")
                if verb['Comment'] is not None:
                    output_file.write(verb['Comment'])
                output_file.write(" |\n")
            output_file.write("\n")

    # Write diagram (mermaid code)
    with open(VOCPATH / 'class_diagram.md', 'w') as out:
        out.write("```mermaid\n")
        out.write("classDiagram\n")
        for cl, vals in diagram.items():
            if vals['superclass'] != "owl:Class":
                out.write("\t`{}`<|--`{}`\n".format(vals['superclass'],
                                                    cl))
        for cl, vals in diagram.items():
            already_shown = []
            out.write("\tclass `{}`{{\n".format(cl))
            for pr in vals["predicates"]:
                if pr['label'] in already_shown:
                    continue
                out.write("\t\t+{}\n".format(pr['label']))
                already_shown.append(pr['label'])
            out.write("\t}\n")

        for cl, vals in diagram.items():
            already_drawn = []
            for pr in vals["predicates"]:
                if pr['range'] and pr['range'] not in already_drawn:
                    out.write("\t`{}` --o `{}`\n".format(cl, pr['range']))
                    already_drawn.append(pr['range'])
        out.write("```")


def parse_multi(g, nodeID):
    items = []
    for s, p, o in g.triples((nodeID, None, None)):
        if "owl#oneOf" in str(p) or "owl#unionOf" in str(p):
            next_node = o
            next_node_string = ""
            while next_node_string != "rdf:nil":
                for s2, p2, o2 in g.triples((next_node, RDF.first, None)):
                    items.append(g.qname(o2))
                for s2, p2, o2 in g.triples((next_node, RDF.rest, None)):
                    next_node = o2
                try:
                    # Does not work with a BNode
                    next_node_string = str(g.qname(next_node))
                except ValueError:
                    pass
    return items


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an SI Reference Point vocabulary")
    parser.add_argument("path_to_ttl",
                        type=Path,
                        help="Directory where TTLs are stored")
    parser.add_argument(
    "--VOCPATH", type=Path,
    default = PKG_ROOT.parent.parent / 'docs' / 'vocabulary',
    help="Directory for output mermaid code, default PKGROOT/docs/vocabulary")
    args = parser.parse_args()
    main(args.path_to_ttl, VOCPATH=args.VOCPATH)
