import argparse
from rdflib import Graph, BNode, RDF
import os


def main(APIPATH):
    # ------------------------------------------------------------------------
    # load ttl files into knowledge graph
    g = Graph()
    g.parse(os.path.join(APIPATH, 'si.ttl'))
    g.parse(os.path.join(APIPATH, 'units.ttl'))
    g.parse(os.path.join(APIPATH, 'prefixes.ttl'))
    g.parse(os.path.join(APIPATH, 'quantities.ttl'))
    g.parse(os.path.join(APIPATH, 'constants.ttl'))
    g.parse(os.path.join(APIPATH, 'cgpm.ttl'))


    # ------------------------------------------------------------------------
    # get classes

    class_query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            SELECT DISTINCT ?Class ?Label
            WHERE
            {
                {?Class a skos:Concept }
                UNION
                {?Class rdfs:subClassOf ?empty}
                ?Class rdfs:label ?Label
                FILTER(langmatches(lang(?Label),'en'))
            }
            ORDER BY ?Class
            """

    # run SPARQL query for units
    c_res = g.query(class_query)

    class_list = []
    for element in c_res:
        teil = {
            'class': element['Class'],
            'label': element['Label']
        }
        class_list.append(teil)


    with open('vocabulary.md', 'w') as output_file:
        for subject in class_list:
            topic = subject['class'].n3(g.namespace_manager)
            print(topic+": ", end="")
            predicate_query = """
                PREFIX si: <http://si-digital-framework.org/SI#>
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX rb: <http://si-digital-framework.org/ResBod#>
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
                if verb['Domain'] is not None:
                    if isinstance(verb['Domain'], BNode):
                        items = parse_multi(g, verb['Domain'])
                        output_file.write(", ".join(items))
                    else:
                        output_file.write(g.qname(verb['Domain']))
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

def parse_multi(g, nodeID):
    for s, p, o in g.triples((nodeID, None, None)):
        if "owl#oneOf" in str(p):
            next_node = o
            items = []
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


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Generate SI ref point vocabulary")
    parser.add_argument("path_to_ttl", default=".",
                        help="Directory where TTLs are stored"
                       )
    args = parser.parse_args()
    main(args.path_to_ttl)
