from rdflib import Graph, URIRef, Literal, BNode
from rdflib.collection import Collection
from rdflib.namespace import RDF, RDFS, SKOS, OWL, XSD, DCTERMS
from pathlib import Path
from si_ref_point.settings import SIURL
from datetime import date
import os

ResBod_ns = SIURL + "bodies#"


class SiElements:
    def __init__(self, namespace: str = SIURL + "SI#", prefix: str = "si"):
        self.g = Graph()  # a triple store as the main data structure
        self.namespace = namespace
        self.namespace_units = SIURL + "SI/units/"
        self.namespace_prefixes = SIURL + "SI/prefixes/"
        self.namespace_operations = SIURL + "operations/"
        self.namespace_quantities = SIURL + "quantities/"
        self.namespace_constants = SIURL + "constants/"
        self.namespace_cgpm = SIURL + "bodies/CGPM#"

        self.g.bind(prefix, self.namespace)
        self.g.bind("units", self.namespace_units)
        self.g.bind("prefixes", self.namespace_prefixes)
        self.g.bind("ops", self.namespace_operations)
        self.g.bind("quantities", self.namespace_quantities)
        self.g.bind("constants", self.namespace_constants)
        self.g.bind("cgpm", self.namespace_cgpm)
        self.g.bind('rb', ResBod_ns)

        self.BASE_PATH = Path(__file__).resolve().parent.parent
        self.ResBod_ns = ResBod_ns

        # Classes

        # general
        self.g.add((URIRef(self.namespace), RDF.type, OWL.Ontology))
        self.g.add((URIRef(self.namespace), SKOS.prefLabel,
                    Literal("SI Reference Point - Base Ontology",
                            datatype=XSD.string)))
        self.g.add((URIRef(self.namespace), RDFS.comment,
                    Literal("Ontology, part of the SI reference point, "
                            "providing base concepts and their relations.",
                            datatype=XSD.string)))
        self.g.add((URIRef(self.namespace), DCTERMS.created,
                    Literal(str(date.today()), datatype=XSD.date)))

        # for Constants
        self.Constant = self.set_uri("Constant")
        self.g.add((self.Constant, RDF.type, SKOS.Concept))
        self.g.add((self.Constant, RDFS.label,
                    Literal("defining constant", lang="en")))
        self.g.add((self.Constant, RDFS.label,
                    Literal("définir la constante", lang="fr")))
        self.g.add((self.Constant, RDFS.comment,
                    Literal("Class for the seven defining constants "
                            "of the SI.", lang="en")))
        self.g.add((self.Constant, RDFS.comment,
                    Literal("La classe pour les sept constantes "
                            "définissant le SI.", lang="fr")))

        # for Units

        # MeasurementUnit
        self.MeasurementUnit = self.set_uri("MeasurementUnit")
        self.g.add((self.MeasurementUnit, RDF.type, SKOS.Concept))
        self.g.add((self.MeasurementUnit, RDFS.label,
                    Literal("measurement unit", lang="en")))
        self.g.add((self.MeasurementUnit, RDFS.label,
                    Literal("unité de mesure", lang="fr")))
        self.g.add((self.MeasurementUnit, RDFS.isDefinedBy,
                    Literal("VIM3 1.9")))
        self.g.add((self.MeasurementUnit, RDFS.comment,
                    Literal("Class for all measurement units.", lang="en")))
        self.g.add((self.MeasurementUnit, RDFS.comment,
                    Literal("La classe pour toutes les unités de mesure.",
                            lang="fr")))

        # SIBaseUnit
        self.SIBaseUnit = self.set_uri("SIBaseUnit")
        self.g.add((self.SIBaseUnit, RDFS.subClassOf, self.MeasurementUnit))
        self.g.add((self.SIBaseUnit, RDFS.label,
                    Literal("base unit", lang="en")))
        self.g.add((self.SIBaseUnit, RDFS.label,
                    Literal("unité de base", lang="fr")))
        self.g.add((self.SIBaseUnit, RDFS.isDefinedBy, Literal("VIM3 1.10")))
        self.g.add((self.SIBaseUnit, RDFS.comment,
                    Literal(
                        "Class of SI base units. Several definitions can "
                        "be attached to this class to represent definitions "
                        "of the BaseUnit throughout time.", lang="en")))
        self.g.add((self.SIBaseUnit, RDFS.comment,
                    Literal("La classe des unités de base SI. Plusieurs "
                            "définitions peuvent être attachées à cette "
                            "classe pour représenter les définitions de "
                            "l'unité de base en question à travers les "
                            "temps.",
                            lang="fr")))

        # SISpecialNamedUnit
        self.SISpecialNamedUnit = self.set_uri("SISpecialNamedUnit")
        self.g.add((self.SISpecialNamedUnit, RDFS.subClassOf,
                    self.MeasurementUnit))
        self.g.add((self.SISpecialNamedUnit, RDFS.label,
                    Literal("SI unit with special name", lang="en")))
        self.g.add((self.SISpecialNamedUnit, RDFS.label,
                    Literal("unité SI avec nom spécial", lang="fr")))

        self.g.add((self.SISpecialNamedUnit, RDFS.comment,
                    Literal("Class for the units of the SI that are not base "
                            "units but have a special name.",
                            lang="en")))
        self.g.add((self.SISpecialNamedUnit, RDFS.comment,
                    Literal("La classe des unités du SI qui ne sont pas des "
                            "unités de base mais qui ont un nom "
                            "spécial.", lang="fr")))

        # inBaseSIUnits
        self.inBaseSIUnits = self.set_uri("inBaseSIUnits")
        self.g.add((self.inBaseSIUnits, RDF.type, OWL.ObjectProperty))
        self.g.add((self.inBaseSIUnits, RDFS.label,
                    Literal("can be expressed in base SI units as",
                            lang="en")))
        self.g.add((self.inBaseSIUnits, RDFS.label,
                    Literal("peut être exprimé en unités SI de base sous "
                            "la forme", lang="fr")))
        self.g.add((self.inBaseSIUnits, RDFS.range, self.MeasurementUnit))

        # inOtherSIUnits
        self.inOtherSIUnits = self.set_uri("inOtherSIUnits")
        self.g.add((self.inOtherSIUnits, RDF.type, OWL.ObjectProperty))
        self.g.add((self.inOtherSIUnits, RDFS.label,
                    Literal("can be expressed in other SI units as",
                            lang="en")))
        self.g.add((self.inOtherSIUnits, RDFS.label,
                    Literal("peut être exprimé dans d’autres unités SI sous "
                            "la forme", lang="fr")))
        self.g.add((self.inOtherSIUnits, RDFS.range, self.MeasurementUnit))

        # NonSIUnit
        self.nonSIUnit = self.set_uri("nonSIUnit")
        self.g.add((self.nonSIUnit, RDFS.subClassOf, self.MeasurementUnit))
        self.g.add((self.nonSIUnit, RDFS.label,
                    Literal("non SI unit", lang="en")))
        self.g.add((self.nonSIUnit, RDFS.label,
                    Literal("unité en dehors du SI", lang="fr")))
        self.g.add((self.nonSIUnit, RDFS.comment,
                    Literal("Non-SI units that are accepted for use with the "
                            "SI", lang="en")))
        self.g.add((self.nonSIUnit, RDFS.comment,
                    Literal("Unités en dehors du SI dont l’usage est accepté "
                            "avec le SI", lang="fr")))

        # Definition
        self.Definition = self.set_uri("Definition")
        self.g.add((self.Definition, RDF.type, SKOS.Concept))
        self.g.add((self.Definition, RDFS.label,
                    Literal("definition of a base unit", lang="en")))
        self.g.add((self.Definition, RDFS.label,
                    Literal("définition d'une unité de base", lang="fr")))
        self.g.add((self.Definition, RDFS.comment,
                    Literal("The class for definitions of an SI base unit.",
                            lang="en")))
        self.g.add((self.Definition, RDFS.comment,
                    Literal("La classe pour les notes sur les définitions "
                            "des unités SI.", lang="fr")))

        # Definition Note
        self.DefinitionNote = self.set_uri("DefinitionNote")
        self.g.add((self.DefinitionNote, RDF.type, SKOS.Concept))
        self.g.add((self.DefinitionNote, RDFS.label,
                    Literal("unit definition note", lang="en")))
        self.g.add((self.DefinitionNote, RDFS.label,
                    Literal("note de définition d'unité", lang="fr")))
        self.g.add((self.DefinitionNote, RDFS.comment,
                    Literal("The class for notes related SI unit definitions.",
                            lang="en")))
        self.g.add((self.DefinitionNote, RDFS.comment,
                    Literal("La classe pour les définitions d'unités SI liées "
                            "aux notes.", lang="fr")))

        # SIPrefix
        self.SIPrefix = self.set_uri("SIPrefix")
        self.g.add((self.SIPrefix, RDF.type, SKOS.Concept))
        self.g.add((self.SIPrefix, RDFS.label,
                    Literal("SI prefix", lang="en")))
        self.g.add((self.SIPrefix, RDFS.label,
                    Literal("préfixe SI", lang="fr")))
        self.g.add((self.SIPrefix, RDFS.comment,
                    Literal("The class for SI Prefixes.", lang="en")))
        self.g.add((self.SIPrefix, RDFS.comment,
                    Literal("La classe pour les préfixes SI.", lang="fr")))

        # Classes for Quantities
        self.QuantityKind = self.set_uri("QuantityKind")
        self.g.add((self.QuantityKind, RDF.type, SKOS.Concept))
        self.g.add((self.QuantityKind, RDFS.label,
                    Literal("kind of quantity", lang="en")))
        self.g.add((self.QuantityKind, RDFS.label,
                    Literal("nature de grandeur", lang="fr")))
        self.g.add((self.QuantityKind, RDFS.isDefinedBy,
                    Literal("VIM3 1.2", datatype=XSD.string)))
        self.g.add((self.QuantityKind, RDFS.comment,
                    Literal("Class for the quantity kinds.", lang="en")))
        self.g.add((self.QuantityKind, RDFS.comment,
                    Literal("La classe pour les types de quantité.",
                            lang="fr")))

        # Disjoint statement among classes
        self.g.add((self.MeasurementUnit, OWL.disjointWith, self.SIPrefix))
        self.g.add((self.MeasurementUnit, OWL.disjointWith, self.Constant))
        self.g.add((self.MeasurementUnit, OWL.disjointWith, self.QuantityKind))
        self.g.add((self.Constant, OWL.disjointWith, self.QuantityKind))
        self.g.add((self.SIBaseUnit, OWL.disjointWith,
                    self.SISpecialNamedUnit))
        self.g.add((self.SIBaseUnit, OWL.disjointWith, self.nonSIUnit))
        self.g.add((self.SISpecialNamedUnit, OWL.disjointWith, self.nonSIUnit))

        # Predicates

        # general

        # hasSymbol
        self.hasSymbol = self.set_uri("hasSymbol")
        self.g.add((self.hasSymbol, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasSymbol, RDFS.label,
                    Literal("has symbol", lang="en")))
        self.g.add((self.hasSymbol, RDFS.label,
                    Literal("a un symbole", lang="fr")))
        self.g.add((self.hasSymbol, RDFS.range, XSD.string))
        self.g.add((self.hasSymbol, RDFS.comment,
                    Literal("Linking a measurement unit or prefix to a "
                            "symbol.", lang="en")))
        self.g.add((self.hasSymbol, RDFS.comment,
                    Literal("Associer une unité de mesure ou un préfixe à un "
                            "symbole.", lang="fr")))

        # for Measurement Units

        # hasUnit
        self.hasUnit = self.set_uri("hasUnit")  # maybe this is includesUnit ?
        self.g.add((self.hasUnit, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasUnit, RDFS.label, Literal("has unit", lang="en")))
        self.g.add((self.hasUnit, RDFS.label, Literal("a l'unité", lang="fr")))
        self.g.add((self.hasUnit, RDFS.range, self.MeasurementUnit))
        self.g.add((self.hasUnit, RDFS.comment,
                    Literal("Linking a measurement unit to an object.", lang="en")))
        self.g.add((self.hasUnit, RDFS.comment,
                    Literal("Associer une unité de mesure à un objet.", lang="fr")))

        # hasUnitTypeAsString
        self.hasUnitTypeAsString_oneOf_node = BNode()
        self.hasUnitTypeAsString_oneOf_subnode = BNode()
        self.hasUnitTypeAsString_oneOf_list = [
            self.SIBaseUnit,
            self.SISpecialNamedUnit,
            self.nonSIUnit,
            self.MeasurementUnit,
            self.Definition,
        ]
        self.hasUnitTypeAsString_oneOf_col = Collection(
            self.g, self.hasUnitTypeAsString_oneOf_subnode,
            self.hasUnitTypeAsString_oneOf_list)
        self.hasUnitTypeAsString = self.set_uri("hasUnitTypeAsString")

        self.g.add((self.hasUnitTypeAsString, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasUnitTypeAsString, RDFS.label,
                    Literal("unit type as a string", lang="en")))
        self.g.add((self.hasUnitTypeAsString, RDFS.label,
                    Literal("type d'unité sous forme de chaîne", lang="fr")))
        self.g.add((self.hasUnitTypeAsString, RDFS.domain,
                    self.hasUnitTypeAsString_oneOf_node))
        self.g.add((self.hasUnitTypeAsString_oneOf_node, OWL.oneOf,
                    self.hasUnitTypeAsString_oneOf_subnode))
        self.g.add((self.hasUnitTypeAsString, RDFS.range, RDFS.Literal))

        # for Constants

        # hasValue
        self.hasValue = self.set_uri("hasValue")
        self.g.add((self.hasValue, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasValue, RDFS.label,
                    Literal("has value", lang="en")))
        self.g.add((self.hasValue, RDFS.label,
                    Literal("a de la valeur", lang="fr")))
        self.g.add((self.hasValue, RDFS.domain, self.Constant))
        self.g.add((self.hasValue, RDFS.range, RDFS.Literal))

        # hasDatatype
        self.hasDatatype_oneOf_node = BNode()
        self.hasDatatype_oneOf_subnode = BNode()
        self.hasDatatype_oneOf_list = [self.Constant, self.SIPrefix]
        self.hasDatatype_oneOf_col = Collection(
            self.g, self.hasDatatype_oneOf_subnode,
            self.hasDatatype_oneOf_list)
        self.hasDatatype = self.set_uri("hasDatatype")

        self.g.add((self.hasDatatype, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasDatatype, RDFS.label,
                    Literal("has datatype", lang="en")))
        self.g.add((self.hasDatatype, RDFS.label,
                    Literal("a un type de données", lang="fr")))
        self.g.add((self.hasDatatype, RDFS.domain,
                    self.hasDatatype_oneOf_node))
        self.g.add((self.hasDatatype_oneOf_node, OWL.oneOf,
                    self.hasDatatype_oneOf_subnode))

        # hasValueAsString
        self.hasValueAsString = self.set_uri("hasValueAsString")
        self.g.add((self.hasValueAsString, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasValueAsString, RDFS.label,
                    Literal("has value as a string", lang="en")))
        self.g.add((self.hasValueAsString, RDFS.label,
                    Literal("a une valeur sous forme de chaîne", lang="fr")))
        self.g.add((self.hasValueAsString, RDFS.domain, self.Constant))
        self.g.add((self.hasValueAsString, RDFS.range, XSD.string))

        # hasUpdatedDate
        self.hasUpdatedDate = self.set_uri("hasUpdatedDate")
        self.g.add((self.hasUpdatedDate, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasUpdatedDate, RDFS.label,
                    Literal("has updated date", lang="en")))
        self.g.add((self.hasUpdatedDate, RDFS.label,
                    Literal("a mis à jour la date", lang="fr")))
        self.g.add((self.hasUpdatedDate, RDFS.domain, self.Constant))
        self.g.add((self.hasUpdatedDate, RDFS.range, XSD.date))

        # hasValueAsString
        self.hasUnitAsString = self.set_uri("hasUnitAsString")
        self.g.add((self.hasUnitAsString, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasUnitAsString, RDFS.label,
                    Literal("has unit as a string", lang="en")))
        self.g.add((self.hasUnitAsString, RDFS.label,
                    Literal("a l'unité comme chaîne", lang="fr")))
        self.g.add((self.hasUnitAsString, RDFS.domain, self.Constant))
        self.g.add((self.hasUnitAsString, RDFS.range, XSD.string))


        # for Units

        # hasDefinition
        self.hasDefinition = self.set_uri("hasDefinition")
        self.g.add((self.hasDefinition, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasDefinition, RDFS.label,
                    Literal("has definition", lang="en")))
        self.g.add((self.hasDefinition, RDFS.label,
                    Literal("a une définition", lang="fr")))
        self.g.add((self.hasDefinition, RDFS.domain, self.SIBaseUnit))
        self.g.add((self.hasDefinition, RDFS.range, self.Definition))
        self.g.add((self.hasDefinition, RDFS.comment,
                    Literal("Linking an SI base unit to its definition.",
                            lang="en")))
        self.g.add((self.hasDefinition, RDFS.comment,
                    Literal("Associer une unité de base SI à sa définition.",
                            lang="fr")))

        # hasDefiningText
        self.hasDefiningText = self.set_uri("hasDefiningText")
        self.g.add((self.hasDefiningText, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasDefiningText, RDFS.label,
                    Literal("has defining text", lang="en")))
        self.g.add((self.hasDefiningText, RDFS.label,
                    Literal("a un texte de définition", lang="fr")))
        self.g.add((self.hasDefiningText, RDFS.domain, self.Definition))
        self.g.add((self.hasDefiningText, RDFS.range, RDFS.Literal))
        self.g.add((self.hasDefiningText, RDFS.comment,
                    Literal("Linking an SI definition to the defining text.",
                            lang="en")))
        self.g.add((self.hasDefiningText, RDFS.comment,
                    Literal("Associer une définition SI au texte de "
                            "définition.", lang="fr")))

        # hasDefinitionNote
        self.hasDefinitionNote = self.set_uri("hasDefinitionNote")
        self.g.add((self.hasDefinitionNote, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasDefinitionNote, RDFS.label,
                    Literal("has definition note", lang="en")))
        self.g.add((self.hasDefinitionNote, RDFS.label,
                    Literal("a une note de définition", lang="fr")))
        self.g.add((self.hasDefinitionNote, RDFS.domain, self.Definition))
        self.g.add((self.hasDefinitionNote, RDFS.range, self.DefinitionNote))
        self.g.add((self.hasDefinitionNote, RDFS.comment,
                    Literal("Linking an SI definition to a definition note.",
                            lang="en")))
        self.g.add((self.hasDefinitionNote, RDFS.comment,
                    Literal("Associer une définition SI à une note de "
                            "définition.", lang="fr")))

        # hasNoteIndex
        self.hasNoteIndex = self.set_uri("hasNoteIndex")
        self.g.add((self.hasNoteIndex, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasNoteIndex, RDFS.label,
                    Literal("has note index", lang="en")))
        self.g.add((self.hasNoteIndex, RDFS.label,
                    Literal("a un texte de note", lang="fr")))
        self.g.add((self.hasNoteIndex, RDFS.domain, self.DefinitionNote))
        self.g.add((self.hasNoteIndex, RDFS.range, RDFS.Literal))
        self.g.add((self.hasNoteIndex, RDFS.comment,
                    Literal("The text of a definition note.", lang="en")))
        self.g.add((self.hasNoteIndex, RDFS.comment,
                    Literal("Le texte d'une note de définition.", lang="fr")))

        # hasNoteText
        self.hasNoteText = self.set_uri("hasNoteText")
        self.g.add((self.hasNoteText, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasNoteText, RDFS.label,
                    Literal("has note text", lang="en")))
        self.g.add((self.hasNoteText, RDFS.label,
                    Literal("a un index de notes", lang="fr")))
        self.g.add((self.hasNoteText, RDFS.domain, self.DefinitionNote))
        self.g.add((self.hasNoteText, RDFS.range, RDFS.Literal))
        self.g.add((self.hasNoteText, RDFS.comment,
                    Literal("The order index of a definition note.",
                            lang="en")))
        self.g.add((self.hasNoteText, RDFS.comment,
                    Literal("Index d'ordre d'une note de définition.",
                            lang="fr")))

        # hasConversionFactor
        self.hasConversionFactor = self.set_uri("hasConversionFactor")
        self.g.add((self.hasConversionFactor, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasConversionFactor, RDFS.label,
                    Literal("has a conversion factor", lang="en")))
        self.g.add((self.hasConversionFactor, RDFS.label,
                    Literal("a un facteur de conversion", lang="fr")))
        self.g.add((self.hasConversionFactor, RDFS.domain, self.nonSIUnit))
        self.g.add((self.hasConversionFactor, RDFS.range, RDFS.Literal))
        self.g.add((self.hasConversionFactor, RDFS.comment, Literal(
            "The conversion factor between non-SI unit and an SI Unit "
            "(number SI unit contained in 1 non SI unit)",
            lang='en')))
        self.g.add((self.hasConversionFactor, RDFS.comment, Literal(
            "Le facteur de conversion entre l'unité non SI et l'unité dans "
            "le SI (nombre d'unité de contenu dans "
            "l'unité non-SI)",
            lang='fr')))

        # hasConversionUnit
        self.hasConversionUnit = self.set_uri("hasConversionUnit")
        self.g.add((self.hasConversionUnit, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasConversionUnit, RDFS.label,
                    Literal("has conversion unit", lang='en')))
        self.g.add((self.hasConversionUnit, RDFS.label,
                    Literal("a une unité de conversion", lang='fr')))
        self.g.add((self.hasConversionUnit, RDFS.domain, self.nonSIUnit))
        self.g.add((self.hasConversionUnit, RDFS.range, self.MeasurementUnit))
        self.g.add((self.hasConversionUnit, RDFS.comment,
                    Literal("SI unit to which the non SI unit can be "
                            "converted", lang='en')))
        self.g.add((self.hasConversionUnit, RDFS.comment,
                    Literal("Unité SI dans laquelle l'unité non SI peut "
                            "être convertie", lang='fr')))

        # hasDefiningConstant
        # need to add isDefiningConstantOf
        self.hasDefiningConstant = self.set_uri("hasDefiningConstant")
        self.g.add((self.hasDefiningConstant, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasDefiningConstant, RDFS.label,
                    Literal("has defining constant", lang="en")))
        self.g.add((self.hasDefiningConstant, RDFS.label,
                    Literal("a une constante de définition", lang="fr")))
        self.g.add((self.hasDefiningConstant, RDFS.domain, self.Definition))
        self.g.add((self.hasDefiningConstant, RDFS.range, self.Constant))
        self.g.add((self.hasDefiningConstant, RDFS.comment,
                    Literal("Linking a definition to its defining constant.",
                            lang="en")))
        self.g.add((self.hasDefiningConstant, RDFS.comment,
                    Literal("Associer une définition à sa constante de "
                            "définition.", lang="fr")))

        # hasNextDefinition
        self.hasNextDefinition = self.set_uri("hasNextDefinition")
        self.g.add((self.hasNextDefinition, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasNextDefinition, RDFS.label,
                    Literal("has next definition", lang="en")))
        self.g.add((self.hasNextDefinition, RDFS.label,
                    Literal("a la prochaine définition", lang="fr")))
        self.g.add((self.hasNextDefinition, RDFS.domain, self.Definition))
        self.g.add((self.hasNextDefinition, RDFS.range, self.Definition))
        self.g.add((self.hasNextDefinition, RDFS.comment,
                    Literal("Linking an SI definition version to the next "
                            "version.", lang="en")))
        self.g.add((self.hasNextDefinition, RDFS.comment,
                    Literal("Associer une version de définition SI à la "
                            "version suivante.", lang="fr")))

        # hasPreviousDefinition
        self.hasPreviousDefinition = self.set_uri("hasPreviousDefinition")
        self.g.add((self.hasPreviousDefinition, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasPreviousDefinition, RDFS.label,
                    Literal("has previous definition", lang="en")))
        self.g.add((self.hasPreviousDefinition, RDFS.label,
                    Literal("a la définition précédente", lang="fr")))
        self.g.add((self.hasPreviousDefinition, RDFS.domain, self.Definition))
        self.g.add((self.hasPreviousDefinition, RDFS.range, self.Definition))
        self.g.add((self.hasPreviousDefinition, OWL.inverseOf,
                    self.hasNextDefinition))
        self.g.add((self.hasNextDefinition, OWL.inverseOf,
                    self.hasPreviousDefinition))
        self.g.add((self.hasPreviousDefinition, RDFS.comment,
                    Literal("Linking an SI definition version to the "
                            "previous version.", lang="en")))
        self.g.add((self.hasPreviousDefinition, RDFS.comment,
                    Literal("Associer une version de définition SI à la "
                            "version précédente.", lang="fr")))

        # hasStartValidity
        self.hasStartValidity = self.set_uri("hasStartValidity")
        self.g.add((self.hasStartValidity, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasStartValidity, RDFS.label,
                    Literal("has start validity", lang="en")))
        self.g.add((self.hasStartValidity, RDFS.label,
                    Literal("a une validité de départ", lang="fr")))
        self.g.add((self.hasStartValidity, RDFS.domain, self.Definition))
        self.g.add((self.hasStartValidity, RDFS.range, XSD.date))
        self.g.add((self.hasStartValidity, RDFS.comment,
                    Literal("Linking an SI definition to its starting "
                            "validity date.", lang="en")))
        self.g.add((self.hasStartValidity, RDFS.comment,
                    Literal("Associer une définition SI à sa date de début "
                            "de validité.", lang="fr")))

        # restriction on "hasStartValidity": minCardinality = 1 (exact cardinality not good in open world assumption)
        restr_hasStartValidity = BNode()
        self.g.add((restr_hasStartValidity, RDF.type, OWL.Restriction))
        self.g.add((restr_hasStartValidity, OWL.onProperty,
                    self.hasStartValidity))
        self.g.add((restr_hasStartValidity, OWL.minCardinality,
                    Literal(1, datatype=XSD.int)))
        self.g.add((self.Definition, RDFS.subClassOf, restr_hasStartValidity))

        # hasEndValidity
        self.hasEndValidity = self.set_uri("hasEndValidity")
        self.g.add((self.hasEndValidity, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasEndValidity, RDFS.label,
                    Literal("has end validity", lang="en")))
        self.g.add((self.hasEndValidity, RDFS.label,
                    Literal("a fin de validité", lang="fr")))
        self.g.add((self.hasEndValidity, RDFS.domain, self.Definition))
        self.g.add((self.hasEndValidity, RDFS.range, XSD.date))
        self.g.add((self.hasEndValidity, RDFS.comment,
                    Literal("Linking an SI definition to its ending "
                            "validity date.", lang="en")))
        self.g.add((self.hasEndValidity, RDFS.comment,
                    Literal("Associer une définition SI à sa date de fin "
                            "de validité.", lang="fr")))

        # hasDefiningEquation
        self.hasDefiningEquation_oneOf_node = BNode()
        self.hasDefiningEquation_oneOf_subnode = BNode()
        self.hasDefiningEquation_oneOf_list = [self.Definition,
                                                 self.Constant]
        self.hasDefiningEquation_oneOf_col = Collection(
            self.g, self.hasDefiningEquation_oneOf_subnode,
            self.hasDefiningEquation_oneOf_list)
        
        self.hasDefiningEquation = self.set_uri("hasDefiningEquation")
        self.g.add((self.hasDefiningEquation, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasDefiningEquation, RDFS.label,
                    Literal("has defining equation", lang="en")))
        self.g.add((self.hasDefiningEquation, RDFS.label,
                    Literal("a une équation de définition", lang="fr")))
        self.g.add((self.hasDefiningEquation, RDFS.domain,
                    self.hasDefiningEquation_oneOf_node))
        self.g.add((self.hasDefiningEquation_oneOf_node, OWL.oneOf,
                    self.hasDefiningEquation_oneOf_subnode))
        self.g.add((self.hasDefiningEquation, RDFS.range, RDFS.Literal))
        self.g.add((self.hasDefiningEquation, RDFS.comment,
                    Literal("Linking a SI definition to its defining "
                            "equation.", lang="en")))
        self.g.add((self.hasDefiningEquation, RDFS.comment,
                    Literal("Associer une définition SI à son équation de "
                            "définition.", lang="fr")))

        # hasStatus
        self.hasStatus = self.set_uri("hasStatus")
        self.g.add((self.hasStatus, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasStatus, RDFS.label,
                    Literal('has status', lang='en')))
        self.g.add((self.hasStatus, RDFS.label,
                    Literal("a l'état", lang='fr')))
        self.g.add((self.hasStatus, RDFS.domain, self.Definition))
        self.g.add((self.hasStatus, RDFS.range, RDFS.Literal))
        self.g.add((self.hasStatus, RDFS.comment,
                    Literal("Linking a SI definition to its status.",
                            lang='en')))
        self.g.add((self.hasStatus, RDFS.comment,
                    Literal("Associer une définition SI à son état.",
                            lang='fr')))

        # hasScalingFactor
        self.hasScalingFactor = self.set_uri("hasScalingFactor")
        self.g.add((self.hasScalingFactor, RDF.type, OWL.DatatypeProperty))
        self.g.add((self.hasScalingFactor, RDFS.label,
                    Literal("has scaling factor", lang="en")))
        self.g.add((self.hasScalingFactor, RDFS.label,
                    Literal("a un facteur d'échelle", lang="fr")))
        self.g.add((self.hasScalingFactor, RDFS.domain, self.SIPrefix))
        self.g.add((self.hasScalingFactor, RDFS.range, RDFS.Literal))
        self.g.add((self.hasScalingFactor, RDFS.comment,
                    Literal("Linking an SI prefix to its scaling factor.",
                            lang="en")))
        self.g.add((self.hasScalingFactor, RDFS.comment,
                    Literal("Associer un préfixe SI à son facteur d'échelle.",
                            lang="fr")))

        # restriction on "hasScalingFactor": cardinality = 1
        restr_hasScalingFactor = BNode()
        self.g.add((restr_hasScalingFactor, RDF.type, OWL.Restriction))
        self.g.add((restr_hasScalingFactor, OWL.onProperty,
                    self.hasScalingFactor))
        self.g.add((restr_hasScalingFactor, OWL.minCardinality,
                    Literal(1, datatype=XSD.int)))
        self.g.add((self.SIPrefix, RDFS.subClassOf, restr_hasScalingFactor))

        # hasDefiningResolution
        self.hasDefiningResolution_oneOf_node = BNode()
        self.hasDefiningResolution_oneOf_subnode = BNode()
        self.hasDefiningResolution_oneOf_list = [self.Definition,
                                                 self.Constant]
        self.hasDefiningResolution_oneOf_col = Collection(
            self.g, self.hasDefiningResolution_oneOf_subnode,
            self.hasDefiningResolution_oneOf_list)
        self.hasDefiningResolution = self.set_uri("hasDefiningResolution")

        self.g.add((self.hasDefiningResolution, RDF.type, OWL.ObjectProperty))
        self.g.add((self.hasDefiningResolution, RDFS.label,
                    Literal("has defining resolution", lang="en")))
        self.g.add((self.hasDefiningResolution, RDFS.label,
                    Literal("a une résolution déterminante", lang="fr")))
        self.g.add((self.hasDefiningResolution, RDFS.domain,
                    self.hasDefiningResolution_oneOf_node))
        self.g.add((self.hasDefiningResolution_oneOf_node, OWL.oneOf,
                    self.hasDefiningResolution_oneOf_subnode))
        self.g.add((self.hasDefiningResolution, RDFS.range,
                    URIRef(self.ResBod_ns + "Resolution")))  # text needed?
        self.g.add((self.hasDefiningResolution, RDFS.comment,
                    Literal("Linking an SI definition to the resolution by "
                            "which it was adopted.", lang="en")))
        self.g.add((self.hasDefiningResolution, RDFS.comment,
                    Literal("Associer une définition SI à la résolution par "
                            "laquelle elle a été adoptée.", lang="fr")))

        # isDefiningResolutionOf
        self.isDefiningResolutionOf_oneOf_node = BNode()
        self.isDefiningResolutionOf_oneOf_subnode = BNode()
        self.isDefiningResolutionOf_oneOf_list = [self.Definition,
                                                  self.Constant]
        self.isDefiningResolutionOf_oneOf_col = Collection(
            self.g, self.isDefiningResolutionOf_oneOf_subnode,
            self.isDefiningResolutionOf_oneOf_list)
        self.isDefiningResolutionOf = self.set_uri("isDefiningResolutionOf")

        self.g.add((self.isDefiningResolutionOf, RDF.type, OWL.ObjectProperty))
        self.g.add((self.isDefiningResolutionOf, RDFS.label,
                    Literal("is defining resolution of", lang="en")))
        self.g.add((self.isDefiningResolutionOf, RDFS.label,
                    Literal("définit la résolution de", lang="fr")))
        self.g.add((self.isDefiningResolutionOf, RDFS.domain,
                    URIRef(self.ResBod_ns + "Resolution")))  # text needed?
        self.g.add((self.isDefiningResolutionOf, RDFS.range,
                    self.isDefiningResolutionOf_oneOf_node))
        self.g.add((self.isDefiningResolutionOf_oneOf_node, OWL.oneOf,
                    self.isDefiningResolutionOf_oneOf_subnode))
        self.g.add((self.isDefiningResolutionOf, OWL.inverseOf,
                    self.hasDefiningResolution))
        self.g.add((self.isDefiningResolutionOf, RDFS.comment,
                    Literal("Linking a resolution to the SI definition it "
                            "defined.", lang="en")))
        self.g.add((self.isDefiningResolutionOf, RDFS.comment,
                    Literal("Associer une résolution à la définition SI "
                            "qu'elle a définie.", lang="fr")))

        # isUnitOfQtyKind
        self.isUnitOfQtyKind = self.set_uri("isUnitOfQtyKind")
        self.g.add((self.isUnitOfQtyKind, RDF.type, OWL.ObjectProperty))
        self.g.add((self.isUnitOfQtyKind, RDFS.label,
                    Literal("is unit of quantity kind", lang="en")))
        self.g.add((self.isUnitOfQtyKind, RDFS.label,
                    Literal("est une unité de quantité", lang="fr")))
        self.g.add((self.isUnitOfQtyKind, RDFS.domain, self.MeasurementUnit))
        self.g.add((self.isUnitOfQtyKind, RDFS.range, self.QuantityKind))
        self.g.add((self.isUnitOfQtyKind, RDFS.comment,
                    Literal("Linking a measurement unit to its quantity "
                            "kind.", lang="en")))
        self.g.add((self.isUnitOfQtyKind, RDFS.comment,
                    Literal("Associer une unité de mesure à son type de "
                            "quantité.", lang="fr")))

    # for Quantities
    # none

    def set_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace + name)

    def set_unit_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_units + name)

    def set_operation_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_operations + name)

    def set_prefix_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_prefixes + name)

    def set_quantity_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_quantities + name)

    def set_constant_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_constants + name)

    def set_cgpm_uri(self, name: str) -> URIRef:
        """ Utility method """
        return URIRef(self.namespace_cgpm + name)


def main():
    si_base_onto = SiElements()
    return si_base_onto.g
