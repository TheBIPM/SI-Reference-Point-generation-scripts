""" Quantities ABox """

import git
import os
import logging
import yaml
from datetime import datetime, timezone
from fractions import Fraction
from rdflib import BNode, Graph, RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD, PROV
from si_ref_point.tboxes.si_tbox import SiElements
from si_ref_point.aboxes.units_abox import transform_unit_expr_to_graph
from si_ref_point.settings import PKG_ROOT, CC_LICENCE, CC_LICENCE_TEXT_EN, CC_LICENCE_TEXT_FR, SI_FILES_FOLDER, \
    GITHUB_BASE_PATH, SIDFWBASE, SIRPVERSION

def transform_qty_expr_to_graph(expression, si_graph, graph):
    """ Transform any "quantity expression" 
                   
    Accepts dicts, strings, lists.

    Returns : rdflib.Graph, rdflib.Bnode

    For representing LENG/TIME, for example

    Dicts will be expected to be like
    {"mult": [{"exp": ["LENG", 1]}, {"exp": ["TIME", -2]}]}

    Lists will be expected to be like :
    [["LENG", 1], ["TIME", -2]
    (this allows more compact notation in source YAML files)

    Strings will be considered to represent a single quantity, and turned into a URI.

    This function calls itself in order to walk the tree of nested QuantityKindProduct
    and QuantityKindPower objects.
    """
    
    def nest_mult(expr):
        """Transform
        {'mult': [A, B, C, D...]'}
        into
        {'mult: [A, {'mult': [B, C, D...]}}
        (to be used recursively)
        """
        # Check number of terms
        if len(expr['mult']) == 1:
            return expr
        left_term = expr['mult'][0]
        right_term = expr['mult'][1:]
        if len(right_term) == 1:
            return {'mult': [left_term, right_term[0]]}
        else:
            return {'mult': [left_term,
                            nest_mult({'mult': right_term})]}
            
    if isinstance(expression, list):
        # turn into a dict
        tmp_expr = {"mult": []}
        for item in expression:
            tmp_expr['mult'].append({"exp": [item[0], item[1]]})
        expression = tmp_expr
    expr_node = BNode()

    if isinstance(expression, str):
        expr_node = si_graph.set_quantity_uri(expression)

    elif isinstance(expression, dict):
        if "mult" in expression.keys():
            if len(expression["mult"]) == 1:
                # This is not really a product...
                graph, expr_node = transform_qty_expr_to_graph(
                    expression["mult"][0], si_graph, graph)
                return graph, expr_node

            # Rearrange products into binary tree (i.e. nested "mult" with
            # only 2 terms, to keep track of order terms)
            expression = nest_mult(expression)

            # set type of expression node
            graph.add((expr_node, RDF.type, si_graph.quantity_kind_product))


            # insert factors
            graph, node = transform_qty_expr_to_graph(expression["mult"][0],
                                             si_graph, graph)
            graph.add((expr_node, si_graph.has_left_quantity_term, node))
            graph, node = transform_qty_expr_to_graph(expression["mult"][1],
                                             si_graph, graph)
            graph.add((expr_node, si_graph.has_right_quantity_term, node))

        elif "exp" in expression.keys():
            if expression["exp"][1] in [1, "1"]:
                # This is not really a unitPower
                graph, expr_node = transform_qty_expr_to_graph(
                    expression["exp"][0], si_graph, graph)
                return graph, expr_node
            else:
                # set type of expression node
                graph.add((expr_node, RDF.type, si_graph.quantity_kind_power))                

                expon_expression = expression["exp"][1]
                fraction_exponent = Fraction(expon_expression).limit_denominator()
                
                # insert base and exponent
                graph, node = transform_qty_expr_to_graph(expression["exp"][0],
                                                si_graph, graph)
                graph.add((expr_node, si_graph.has_numeric_exponent, Literal(fraction_exponent.numerator,datatype=XSD.short)))
                
                if fraction_exponent.denominator >= 2:
                    graph.add((expr_node, RDF.type, si_graph.quantity_kind_fraction_power))
                    graph.add((expr_node, si_graph.has_numeric_exponent_denominator, Literal(fraction_exponent.denominator,datatype=XSD.short)))

                graph.add((expr_node, si_graph.has_quantity_base, node))


        else:
            raise ValueError(
                f"Unrecognized keys in expression-object: {expression.keys()}."
            )

    else:
        raise ValueError(
            f"Expecting either a string, a list or dict. Got '{type(expression)}'."
        )

    return graph, expr_node

def main():
    """Main of Quantities A-box"""
     # get the predicates and classes that are common to all cuq files
    si_graph = SiElements()
    # produce a separate graphe for the units
    quantities_graph = Graph()

    # 1) Define the namespaces within (base)/SI
    quantities_graph.bind("quantities",si_graph.namespace_quantities)
    quantities_graph.bind("units",si_graph.namespace_units)
    quantities_graph.bind("si",si_graph.namespace)

    # 2) Add annotations to the quantity graph

    # 2.1 General annotations (type, labels, comments etc)

    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDF.type,
         OWL.Ontology)
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         SKOS.prefLabel,
         Literal("SI Reference Point - Quantities", datatype=XSD.string))
    )

    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDFS.comment,
         Literal("Ontology, part of the SI reference point, "
                   "covering quantities",
                   datatype=XSD.string))
    )

    # SemVer
    version_iri = URIRef(SIDFWBASE + "/" + SIRPVERSION + "/quantities/")
    quantities_graph.add((URIRef(si_graph.namespace_quantities), OWL.versionIRI, version_iri))
    quantities_graph.add((URIRef(si_graph.namespace_quantities), OWL.versionInfo, Literal(SIRPVERSION, datatype=XSD.string)))

    # 2.2 Versioning (using PROVENANCE vocabulary)
    timestamp = datetime.now(timezone.utc)                              # get the system time (in UTC)
    uri_timestamp = timestamp.strftime("%Y%m%d%H%M%SZ")                 # used to identify uniquely the produced TTL file (entity)
    startedAt_timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")      # used with the predicate 'startedAtTime' of the corresponding activity
    repo = git.Repo(PKG_ROOT, search_parent_directories=True)
    sha = repo.head.object.hexsha
    #   2.2.1 Agent
    #   declare this code as an 'agent' (in the sense of PROVENANCE)
    #   and define UàRI to a specific version by using its commit on GitHub
    agents = [GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq/si_tbox.py",
              GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq/quantities_abox.py"]

    for agent_sw in agents:
        quantities_graph.add(
            (URIRef(agent_sw),
                RDF.type,
                PROV.Agent)
        )

    #   2.2.2 Entity
    #   declare the sources (YAML files) as 'entity' (in the sense of PROVENANCE)
    #   The manually produced YAML files are stored on GitHub. Their hexsha together
    #   with the path is used to define a unique URI for each file.
    source_files = [GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/quantities_core.yaml",
                    GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/quantities_other.yaml"]
    for source in source_files:
        quantities_graph.add(
            (URIRef(source),
             RDF.type,
             PROV.Entity)
        )
    quantities_out_entity ="quantities_" + uri_timestamp + ".ttl"
    quantities_graph.add(
        (si_graph.set_entity_uri(quantities_out_entity),
         RDF.type,
         PROV.Entity)
    )

    #   2.2.3 Activity
    #     declare the constants_ttl_generation as 'activity' (in the sense of PROVENANCE)
    #     make the activity unique by adding the timestamp to the identifier of the activity
    activity = 'quantities_'+uri_timestamp + '.ttl_generation'

    quantities_graph.add(
        (si_graph.set_activity_uri(activity),
        RDF.type,
        PROV.Activity)
    )

    #   2.2.4 Relation activity, agent, entities
    #   activity - agent
    for agent_sw in agents:
        quantities_graph.add(
                (si_graph.set_activity_uri(activity),
                PROV.wasAssociatedWith,
                URIRef(agent_sw))
            )
    quantities_graph.add(
        (si_graph.set_activity_uri(activity),
            PROV.startedAtTime,
            Literal(str(startedAt_timestamp), datatype=XSD.dateTime))
    )
    #   output entity - source entities
    for source in source_files:
        quantities_graph.add(
            (si_graph.set_entity_uri(quantities_out_entity),
                PROV.wasDerivedFrom,
                URIRef(source))
    )
    #   output entity - agent
    for agent_sw in agents:
        quantities_graph.add(
            (si_graph.set_entity_uri(quantities_out_entity),
            PROV.wasAttributedTo,
            URIRef(agent_sw))
    )
    #   output entity - activity
    quantities_graph.add(
        (si_graph.set_entity_uri(quantities_out_entity),
         PROV.wasGeneratedBy,
         si_graph.set_activity_uri(activity))
    )

    # 2.3 License information
    quantities_graph.add(
         (URIRef(si_graph.namespace_quantities),
          DCTERMS.license,
          URIRef(CC_LICENCE))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_EN,lang="en"))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_FR,lang="fr"))
    )

    # 3) Build quantity graph
    #  crawl through the list of YAML files
    qty_files = ['quantities_core.yaml', 'quantities_other.yaml']
    qty_code_list = []

    # open YAML files with information
    for filename in qty_files:
        with open(os.path.join(SI_FILES_FOLDER, filename), encoding="utf8") as fp:
            qty_list = yaml.safe_load(fp)

            # add the individual quantities to the graph
            for qty in qty_list["data"]:
                if qty['identifier'] not in qty_code_list:
                    qty_code_list.append(qty['identifier'])
                else:
                    logging.error("quantity %s already defined !", qty['identifier'] )
                element = si_graph.set_quantity_uri(qty['identifier'])
                quantities_graph.add((element, RDF.type, si_graph.quantity_kind))
                quantities_graph.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-en'], lang="en")))
                quantities_graph.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-fr'], lang="fr")))
                quantities_graph.add((element, SKOS.altLabel, Literal(qty['identifier'],
                                                       datatype=XSD.string)))
                # append the units of the quantity
                if 'Unit' in qty and qty['Unit'] is not None:
                    quantities_graph, cmpnd_node = transform_unit_expr_to_graph(qty['Unit'], si_graph, quantities_graph)
                    quantities_graph.add((element, si_graph.has_unit, cmpnd_node))
                
                # append the base quantity kinde of the quantity
                if 'Base_quantity' in qty and qty['Base_quantity'] is not None:
                    quantities_graph, cmpnd_node = transform_qty_expr_to_graph(qty['Base_quantity'], si_graph, quantities_graph)
                    quantities_graph.add((element, si_graph.has_quantity_base, cmpnd_node))
                    

    return quantities_graph

if __name__ == "__main__":
    main()
