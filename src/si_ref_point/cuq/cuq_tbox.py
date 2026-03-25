"""
CUQ TBox
"""

from datetime import datetime, timezone
import git
import os
import yaml
from rdflib import Graph, OWL,RDF,RDFS,URIRef, Literal, BNode, SKOS, PROV
from rdflib.collection import Collection
from rdflib.namespace import XSD, DCTERMS
from si_ref_point.settings import CC_LICENCE, CC_LICENCE_TEXT_EN, CC_LICENCE_TEXT_FR, CUQ_FILES_FOLDER, GITHUB_BASE_PATH, SIDFWBASE

RES_BOD_NS = SIDFWBASE + "/bodies#"
bodies_list = ['cgpm', 'cipm', 'cctf']


class SiElements:
    """ main class containing the SI graph"""
    def __init__(self, namespace: str = SIDFWBASE + "/SI#", ns_prefix: str = "si"):
        self.g = Graph()  # a triple store as the main data structure

    # 1) Define namespaces, sub-namespace and shortcuts used by A boxes
    
        # ~/SI
        self.namespace = namespace
        self.g.bind(ns_prefix, self.namespace)
        # ~/SI/units
        self.namespace_units = SIDFWBASE + "/SI/units/"
        # ~/SI/prefixes
        self.namespace_prefixes = SIDFWBASE + "/SI/prefixes/"
        # ~/SI/decisions
        self.namespace_decisions = SIDFWBASE + "/SI/decisions/"
        # ~/quantities
        self.namespace_quantities = SIDFWBASE + "/quantities/"
        # ~/constants
        self.namespace_constants = SIDFWBASE + "/constants/"
        # Explicitly binding a constants namespace to the URI
        self.g.bind("constants", self.namespace_constants)

       # Define the namespaces within (base)/bodies
        # ~/bodies
        self.namespace_bodies_base = SIDFWBASE + "/bodies/"
        self.namespace_bodies = {}
        for body in bodies_list:
            self.namespace_bodies[body] = self.namespace_bodies_base + body.upper() + "#"
            self.g.bind(body, self.namespace_bodies[body])
        #   ... and the shortcut
        self.g.bind('rb', RES_BOD_NS)

        #~/entities (in the sens of PROVENANCE)
        self.namespace_entities = SIDFWBASE + "/SI/entities#"
        self.g.bind("entities",self.namespace_entities)

        #~/activities (in the sens of PROVENANCE)
        self.namespace_activities = SIDFWBASE + "/SI/activities#"
        self.g.bind("activities",self.namespace_activities)
        
        #~/agents (in the sens of PROVENANCE)
        self.namespace_agents = SIDFWBASE + "/SI/agents#"
        self.g.bind("agents",self.namespace_agents)

        # Load graph from ttl files
        for ttl_file in ['CUQ_core_concepts.ttl',
                         'CUQ_extended_concepts.ttl']:
            self.g.parse(os.path.join(CUQ_FILES_FOLDER, ttl_file),
                         format="ttl")
            
    # 2) Add annotations to the ontology

    #   2.1 General annotations (type, comments etc)
        self.g.add(
            (URIRef(self.namespace),
             RDF.type,
             OWL.Ontology)
        )
        self.g.add(
            (URIRef(self.namespace),
             SKOS.prefLabel,
             Literal("SI Reference Point", datatype=XSD.string),
            )
        )

        self.g.add(
            (URIRef(self.namespace),
             RDFS.comment,
             Literal((
                    "Ontology, part of the SI Reference Point, covering "
                    "measurement units (SI base units and SI units with "
                    "special names) and prefixes."),datatype=XSD.string))
        )

    #   2.2 Versioning
        timestamp = datetime.now(timezone.utc)                              # get the system time (in UTC)
        uri_timestamp = timestamp.strftime("%Y%m%d%H%M%SZ")                 # used to identify uniquely the produced TTL file (entity)
        startedAt_timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")      # used with the predicate 'startedAtTime' of the corresponding activity
        
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha

    #     2.2.1 Agent
    #     declare this code as an 'agent' (in the sense of PROVENANCE) 
    #     and define the URI to a specific version by using its commit on github
        agent_sw = GITHUB_BASE_PATH +"blob/"+ sha + "/src/si_ref_point/cuq/cuq_tbox.py"
        self.g.add(
            (URIRef(agent_sw),
             RDF.type,
             PROV.Agent)
        )
        
    #     2.2.2 Entity
    #     there is no source file for the TBox, so there is no source entity
    
    #     declare the ttl output as an 'entity' (in the sense of PROVENANCE)
        si_out_entity = "si_"+uri_timestamp+".ttl"
        self.g.add(
            (self.set_entity_uri(si_out_entity),
             RDF.type,
             PROV.Entity)
             )
    
    #     2.2.3 Activity
    #     declare the si_ttl_generation as 'activity' (in the sense of PROVENANCE)
    #     make the activity unique by adding the timestamp to the identifier of the activity
        activity = 'si_ttl_generation'+uri_timestamp + '.ttl_generation'
        self.g.add(
            (self.set_activity_uri(activity),
            RDF.type,
            PROV.Activity)
            )
    #     2.2.4 Link activity, agent, entities
    #     activity - agent
        self.g.add(
            (self.set_activity_uri(activity),
            PROV.wasAssociatedWith,
            URIRef(agent_sw))
            )
        self.g.add(
            (self.set_activity_uri(activity),
                PROV.startedAtTime,
                Literal(str(startedAt_timestamp), datatype=XSD.dateTime))
        )
    #     output entity - source entity
    #      (no source entity for the TBox)
    #     output entity - agent
        self.g.add(
            (self.set_entity_uri(si_out_entity),
             PROV.wasAttributedTo,
             URIRef(agent_sw))
             )
    #     output entity - activity
        self.g.add(
            (self.set_entity_uri(si_out_entity),
             PROV.wasGeneratedBy,
             self.set_activity_uri(activity))
            )

    #   2.3 License
        self.g.add(
         (URIRef(self.namespace),
          DCTERMS.license,
          URIRef(CC_LICENCE))
        )
        self.g.add(
            (URIRef(self.namespace),
             RDFS.comment,
             Literal(CC_LICENCE_TEXT_EN,lang="en"))
        )
        self.g.add(
            (URIRef(self.namespace),        
             RDFS.comment,
             Literal(CC_LICENCE_TEXT_FR,lang="fr"))
        )
    # 3) Define classes and predicates used by different A boxes
        self.constant = self.set_uri("Constant")
        self.measurement_unit = self.set_uri("MeasurementUnit")
        self.si_base_unit = self.set_uri("SIBaseUnit")
        self.si_special_named_unit = self.set_uri("SISpecialNamedUnit")
        self.in_base_si_units = self.set_uri("inBaseSIUnits")
        self.in_other_si_units = self.set_uri("inOtherSIUnits")
        self.non_si_unit = self.set_uri("nonSIUnit")
        self.definition = self.set_uri("Definition")
        self.definition_note = self.set_uri("DefinitionNote")
        self.si_prefix = self.set_uri("SIPrefix")
        self.si_decision = self.set_uri("SIDecision")
        self.si_decision_scope = self.set_uri("SIDecisionScope")
        self.si_decision_target = self.set_uri("SIDecisionTarget")
        self.quantity_kind = self.set_uri("QuantityKind")
        self.has_symbol = self.set_uri("hasSymbol")
        self.has_alt_symbol = self.set_uri("hasAltSymbol")
        self.has_unit = self.set_uri("hasUnit")
        self.prefix_restriction = self.set_uri("prefixRestriction")
        self.has_unit_type_as_string_one_of_node = BNode()
        self.has_unit_type_as_string_one_of_subnode = BNode()
        self.has_unit_type_as_string_one_of_list = [
            self.si_base_unit,
            self.si_special_named_unit,
            self.non_si_unit,
            self.measurement_unit,
        ]
        self.has_unit_type_as_string_one_of_col = Collection(
            self.g,
            self.has_unit_type_as_string_one_of_subnode,
            self.has_unit_type_as_string_one_of_list)
        self.has_unit_type_as_string = self.set_uri("hasUnitTypeAsString")
        self.has_target = self.set_uri("hasTarget")
        self.is_target_of = self.set_uri("isTargetOf")
        self.has_decision = self.set_uri("hasDecision")
        self.is_decision_of = self.set_uri("isDecisionOf")
        self.corresponding_resolution = self.set_uri("correspondingResolution")
        self.has_value = self.set_uri("hasValue")
        self.has_datatype_one_of_node = BNode()
        self.has_datatype_one_of_subnode = BNode()
        self.has_datatype_one_of_list = [self.constant, self.si_prefix]
        self.has_datatype_one_of_col = Collection(
            self.g, self.has_datatype_one_of_subnode,
            self.has_datatype_one_of_list)
        self.has_datatype = self.set_uri("hasDatatype")
        self.has_updated_date = self.set_uri("hasUpdatedDate")
        self.has_unit_as_tring = self.set_uri("hasUnitAsString")
        self.is_unit_of_qty_kind = self.set_uri("isUnitOfQtyKind")
        self.has_definition = self.set_uri("hasDefinition")
        self.has_next_definition = self.set_uri("hasNextDefinition")
        self.has_previous_definition = self.set_uri("hasPreviousDefinition")
        self.has_start_validity = self.set_uri("hasStartValidity")
        self.has_end_validity = self.set_uri("hasEndValidity")
        self.has_defining_text = self.set_uri("hasDefiningText")
        self.has_defining_resolution = self.set_uri("hasDefiningResolution")
        self.has_status = self.set_uri("hasStatus")
        self.has_definition_note = self.set_uri("hasDefinitionNote")
        self.has_note_index = self.set_uri("hasNoteIndex")
        self.has_note_text = self.set_uri("hasNoteText")
        self.has_defining_equation = self.set_uri("hasDefiningEquation")
        self.has_defining_constant = self.set_uri("hasDefiningConstant")
        self.has_value_as_string = self.set_uri("hasValueAsString")
        self.has_scaling_factor = self.set_uri("hasScalingFactor")
        self.has_exponent = self.set_uri("hasNumericExponent")

    # 4) Utility methods

    def uri(self, name: str) -> URIRef:
        """Utility method """
        return URIRef(self.namespace + name)

    def set_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace + name)

    def set_activity_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_activities + name)

    def set_entity_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_entities + name)
    
    def set_unit_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_units + name)

    def set_prefix_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_prefixes + name)

    def set_decision_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_decisions + name)

    def set_quantity_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_quantities + name)

    def set_constant_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_constants + name)

    def set_cgpm_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_bodies['cgpm'] + name)

    def set_resolution_uri(self, name: str) -> URIRef:
        """ Utility method, generalizes set_cgpm_uri """
        try:
            bd, res_id = name.split(':')
        except IndexError:
            print(f"Error parsing a resolution URI : {name}")
            return URIRef('/')  # is this the correct default?
        for body in bodies_list:
            if body == bd:
                return URIRef(self.namespace_bodies[body] + res_id)


def main():
    """ Main of CUQ T-box"""
    si_base_onto = SiElements()
    return si_base_onto.g


if __name__ == "__main__":
    main()

