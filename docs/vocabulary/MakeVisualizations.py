""" Add documentation """

import argparse
from rdflib import Graph
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
    g.parse(os.path.join(APIPATH, 'bodies.ttl'))
    g.parse(os.path.join(APIPATH, 'cgpm.ttl'))

    # ------------------------------------------------------------------------
    # get classes
    unit_taxonomy_query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX si: <https://si-digital-framework.org/SI#>

            SELECT DISTINCT ?class ?superclass
            WHERE
            {
                ?class rdfs:subClassOf+ si:MeasurementUnit .
                OPTIONAL {?class rdfs:subClassOf ?superclass}
            }
            ORDER BY ?class
            """

    qty_taxonomy_query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX si: <https://si-digital-framework.org/SI#>

            SELECT DISTINCT ?class ?superclass
            WHERE
            {
                ?class rdfs:subClassOf+ si:QuantityKind .
                OPTIONAL {?class rdfs:subClassOf ?superclass}
            }
            ORDER BY ?class
            """

    comp_unit_query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX si: <https://si-digital-framework.org/SI#>

            SELECT DISTINCT ?class ?prop ?range
            WHERE
            {
                ?class rdfs:subClassOf si:CompoundUnit .
                ?prop rdfs:domain ?class . 
                OPTIONAL {?prop rdfs:range ?range}
            }
            ORDER BY ?class
            """

    definition_query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX si: <https://si-digital-framework.org/SI#>

            SELECT DISTINCT ?prop ?domain ?range
            WHERE
            {
                ?prop (rdfs:range|rdfs:domain)/owl:oneOf?/(rdf:first|rdf:rest)* ?class .
                OPTIONAL {?prop rdfs:domain/owl:oneOf?/(rdf:first|rdf:rest)* ?domain} .
                OPTIONAL {?prop rdfs:range/owl:oneOf?/(rdf:first|rdf:rest)* ?range} .
                FILTER (?class = si:Definition || ?class = si:Constant) .
                FILTER (?range != rdf:nil && ?domain != rdf:nil) . # filter last element of list
                FILTER (!isBlank(?domain)) . # filter blank nodes
                FILTER (!isBlank(?range)) . 
            }
            ORDER BY ?class
            """

    # Write diagram (mermaid code)
    with open('class_diagram_details.md', 'w') as out:
        out.write("# Diagrams\n")

        # Unit-related concepts
        out.write("## Unit-related Concepts\n")
        out.write("```mermaid\n")
        out.write("%%{init: { 'class': {'hideEmptyMembersBox':true} } }%%\n")
        out.write("classDiagram\ndirection RL\n")
        res = g.query(unit_taxonomy_query)
        for item in res:
            c, superc = item
            class_display = c.n3(g.namespace_manager)
            superclass_display = superc.n3(g.namespace_manager)
            print(class_display, superclass_display)

            out.write(f"`{class_display}` --|> `{superclass_display}` : rdfs#colon;subClassOf\n")
        out.write("```\n")

        # QuantityKind-related concepts
        out.write("## QuantityKind-related Concepts\n")
        out.write("```mermaid\n")
        out.write("%%{init: { 'class': {'hideEmptyMembersBox':true} } }%%\n")
        out.write("classDiagram\ndirection RL\n")
        res = g.query(qty_taxonomy_query)
        for item in res:
            c, superc = item
            class_display = c.n3(g.namespace_manager)
            superclass_display = superc.n3(g.namespace_manager)
            print(class_display, superclass_display)

            out.write(f"`{class_display}` --|> `{superclass_display}` : rdfs#colon;subClassOf\n")
        out.write("```\n")

        # CompoundUnit-related concepts
        out.write("## CompoundUnit-related properties\n")
        out.write("```mermaid\n")
        out.write("%%{init: { 'class': {'hideEmptyMembersBox':true} } }%%\n")
        out.write("classDiagram\ndirection LR\n")
        res = g.query(comp_unit_query)
        for item in res:
            c, prop, rng = item
            class_display = c.n3(g.namespace_manager)
            range_display = "owl:Thing" if rng is None else rng.n3(g.namespace_manager)
            prop_display = "owl:Thing" if prop is None else prop.n3(g.namespace_manager)
            print(class_display, superclass_display)

            out.write(f"`{class_display}` --|> `{range_display}` : {prop_display.replace(':', '#colon;')}\n")
        out.write("```\n")

        # definition-related concepts
        out.write("## Definition-related properties\n")
        out.write("```mermaid\n")
        out.write("%%{init: { 'class': {'hideEmptyMembersBox':true} } }%%\n")
        out.write("classDiagram\ndirection LR\n")
        res = g.query(definition_query)
        for item in res:
            prop, domain, rng = item
            range_display = "owl:Thing" if rng is None else rng.n3(g.namespace_manager)
            domain_display = "owl:Thing" if domain is None else domain.n3(g.namespace_manager)
            prop_display = "owl:Thing" if prop is None else prop.n3(g.namespace_manager)
            print(domain_display, prop_display, range_display)

            out.write(f"`{domain_display}` --|> `{range_display}` : {prop_display.replace(':', '#colon;')}\n")
        out.write("```\n")


    # convert to pdfs using mermaid-cli:
    # npx mmdc -i .\class_diagram_details.md -f -e pdf -o class_diagrams_details_converted.md

    # best result with mermaid 10.9.1 (current version 11.4.2 not showing multiple self-references):
    # npm install -g @mermaid-js/mermaid-cli@10.9.1
        

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Generate SI ref point vocabulary")
    parser.add_argument(
        "--path_to_ttl",
        default=os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "TTL")),
        help="Directory where TTLs are stored")
    args = parser.parse_args()
    main(args.path_to_ttl)
