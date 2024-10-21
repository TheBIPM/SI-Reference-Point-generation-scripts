"""
CUQ TBox
"""

from datetime import date
import os
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.collection import Collection
from rdflib.namespace import XSD, DCTERMS
from si_ref_point.settings import CUQ_FILES_FOLDER, SIDFWBASE

RES_BOD_NS = SIDFWBASE + "/bodies#"
bodies_list = ['cgpm', 'cipm', 'cctf']


class SiElements:
    """ main class containing the SI graph"""
    def __init__(self, namespace: str = SIDFWBASE + "/SI#", ns_prefix: str = "si"):
        self.g = Graph()  # a triple store as the main data structure

        # Define the namespaces within (base)/SI
        self.namespace = namespace
        #   ... and the shortcut
        self.g.bind(ns_prefix, self.namespace)

        self.namespace_units = SIDFWBASE + "/SI/units/"
        self.namespace_prefixes = SIDFWBASE + "/SI/prefixes/"
        self.namespace_decisions = SIDFWBASE + "/SI/decisions/"

        # Define the namespace within (base)/quantities
        self.namespace_quantities = SIDFWBASE + "/quantities/"
        # Define the namespace within (base)/constants
        self.namespace_constants = SIDFWBASE + "/constants/"

       # Define the namespaces within (base)/bodies
        self.namespace_bodies_base = SIDFWBASE + "/bodies/"
        self.namespace_bodies = {}
        for body in bodies_list:
            self.namespace_bodies[body] = self.namespace_bodies_base + body.upper() + "#"
            self.g.bind(body, self.namespace_bodies[body])
        #   ... and the shortcut
        self.g.bind('rb', RES_BOD_NS)


        # self.g.bind("units", self.namespace_units)
        # self.g.bind("prefixes", self.namespace_prefixes)
        # self.g.bind("quantities", self.namespace_quantities)
        # self.g.bind("constants", self.namespace_constants)
        # self.g.bind("decisions", self.namespace_decisions)

        #self.res_bod_ns = RES_BOD_NS                        # wo wird das gebraucht?

        # Load graph from ttl files
        for ttl_file in ['CUQ_core_concepts.ttl',
                         'CUQ_extended_concepts.ttl']:
            self.g.parse(os.path.join(CUQ_FILES_FOLDER, ttl_file),
                         format="ttl")
        # Update creation date
        self.g.add((URIRef(self.namespace), DCTERMS.created,
                    Literal(str(date.today()), datatype=XSD.date)))

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

    def uri(self, name: str) -> URIRef:
        """Utility method """
        return URIRef(self.namespace + name)

    def set_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace + name)

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
