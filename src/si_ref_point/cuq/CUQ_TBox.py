import os
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.collection import Collection
from rdflib.namespace import XSD, DCTERMS
from pathlib import Path
from si_ref_point.settings import CUQ_FILES_FOLDER, SIURL
from datetime import date

ResBod_ns = SIURL + "bodies#"
bodies_list = ['cgpm', 'cipm', 'cctf']

class SiElements:
    def __init__(self, namespace: str = SIURL + "SI#", prefix: str = "si"):
        self.g = Graph()  # a triple store as the main data structure
        self.namespace = namespace
        self.namespace_units = SIURL + "SI/units/"
        self.namespace_prefixes = SIURL + "SI/prefixes/"
        self.namespace_decisions = SIURL + "SI/decisions/"
        self.namespace_quantities = SIURL + "quantities/"
        self.namespace_constants = SIURL + "constants/"
        self.namespace_bodies =  {}
        for body in bodies_list:
            self.namespace_bodies[body] = SIURL + "bodies/" + body.upper() + "#"

        self.g.bind(prefix, self.namespace)
        self.g.bind("units", self.namespace_units)
        self.g.bind("prefixes", self.namespace_prefixes)
        self.g.bind("quantities", self.namespace_quantities)
        self.g.bind("constants", self.namespace_constants)
        self.g.bind("decisions", self.namespace_decisions)
        for body in bodies_list:
            self.g.bind(body, self.namespace_bodies[body])
        self.g.bind('rb', ResBod_ns)

        self.BASE_PATH = Path(__file__).resolve().parent.parent
        self.ResBod_ns = ResBod_ns

        # Load graph from ttl files
        for ttl_file in ['CUQ_core_concepts.ttl',
                         'CUQ_extended_concepts.ttl']:
            self.g.parse(os.path.join(CUQ_FILES_FOLDER, ttl_file),
                         format="ttl")
        # Update creation date
        self.g.add((URIRef(self.namespace), DCTERMS.created,
                    Literal(str(date.today()), datatype=XSD.date)))
        # Are these shortcuts still useful ?
        # Could they be auto-generated ?
        self.Constant = self.set_uri("Constant")
        self.MeasurementUnit = self.set_uri("MeasurementUnit")
        self.SIBaseUnit = self.set_uri("SIBaseUnit")
        self.SISpecialNamedUnit = self.set_uri("SISpecialNamedUnit")
        self.inBaseSIUnits = self.set_uri("inBaseSIUnits")
        self.inOtherSIUnits = self.set_uri("inOtherSIUnits")
        self.nonSIUnit = self.set_uri("nonSIUnit")
        self.Definition = self.set_uri("Definition")
        self.DefinitionNote = self.set_uri("DefinitionNote")
        self.SIPrefix = self.set_uri("SIPrefix")
        self.SIDecision = self.set_uri("SIDecision")
        self.SIDecisionScope = self.set_uri("SIDecisionScope")
        self.SIDecisionTarget = self.set_uri("SIDecisionTarget")
        self.QuantityKind = self.set_uri("QuantityKind")
        self.hasSymbol = self.set_uri("hasSymbol")
        self.hasAltSymbol = self.set_uri("hasAltSymbol")
        self.hasUnit = self.set_uri("hasUnit")
        self.prefixRestriction = self.set_uri("prefixRestriction")
        self.hasAuthorizedPrefix = self.set_uri("hasAuthorizedPrefix")
        self.hasUnitTypeAsString_oneOf_node = BNode()
        self.hasUnitTypeAsString_oneOf_subnode = BNode()
        self.hasUnitTypeAsString_oneOf_list = [
            self.SIBaseUnit,
            self.SISpecialNamedUnit,
            self.nonSIUnit,
            self.MeasurementUnit,
        ]
        self.hasUnitTypeAsString_oneOf_col = Collection(
            self.g, self.hasUnitTypeAsString_oneOf_subnode,
            self.hasUnitTypeAsString_oneOf_list)
        self.hasUnitTypeAsString = self.set_uri("hasUnitTypeAsString")
        self.hasTarget = self.set_uri("hasTarget")
        self.isTargetOf = self.set_uri("isTargetOf")
        self.hasDecision = self.set_uri("hasDecision")
        self.isDecisionOf = self.set_uri("isDecisionOf")
        self.correspondingResolution = self.set_uri("correspondingResolution")
        self.hasValue = self.set_uri("hasValue")
        self.hasDatatype_oneOf_node = BNode()
        self.hasDatatype_oneOf_subnode = BNode()
        self.hasDatatype_oneOf_list = [self.Constant, self.SIPrefix]
        self.hasDatatype_oneOf_col = Collection(
            self.g, self.hasDatatype_oneOf_subnode,
            self.hasDatatype_oneOf_list)
        self.hasDatatype = self.set_uri("hasDatatype")
        self.hasUpdatedDate = self.set_uri("hasUpdatedDate")
        self.hasUnitAsString = self.set_uri("hasUnitAsString")
        self.isUnitOfQtyKind = self.set_uri("isUnitOfQtyKind")
        self.hasDefinition = self.set_uri("hasDefinition")
        self.hasNextDefinition = self.set_uri("hasNextDefinition")
        self.hasPreviousDefinition = self.set_uri("hasPreviousDefinition")
        self.hasStartValidity = self.set_uri("hasStartValidity")
        self.hasEndValidity = self.set_uri("hasEndValidity")
        self.hasDefiningText = self.set_uri("hasDefiningText")
        self.hasDefiningResolution = self.set_uri("hasDefiningResolution")
        self.hasStatus = self.set_uri("hasStatus")
        self.hasDefinitionNote = self.set_uri("hasDefinitionNote")
        self.hasNoteIndex = self.set_uri("hasNoteIndex")
        self.hasNoteText = self.set_uri("hasNoteText")
        self.hasDefiningEquation = self.set_uri("hasDefiningEquation")
        self.hasDefiningConstant = self.set_uri("hasDefiningConstant")
        self.hasValueAsString = self.set_uri("hasValueAsString")
        self.hasScalingFactor = self.set_uri("hasScalingFactor")

    def uri(self, name: str) -> URIRef:
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

    def set_resolution_uri(self, name:str) -> URIRef:
        """ Utility method, generalizes set_cgpm_uri """
        try:
            bd, resId = name.split(':')
        except IndexError:
            print("Error parsing a resolution URI : %s" % name)
            return None
        for body in bodies_list:
            if body == bd:
                return URIRef(self.namespace_bodies[body] + resId)

def main():
    si_base_onto = SiElements()
    return si_base_onto.g


if __name__ == "__main__":
    main()
