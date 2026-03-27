""" Responsible Bodies TBox """

from datetime import date
from rdflib import URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Graph, Literal
from si_ref_point.settings import SIDFWBASE, SKOSURL

RES_BOD_NS = SIDFWBASE + "/bodies#"

class ResBod:
    def __init__(self, namespace: str = RES_BOD_NS, prefix: str = 'rb'):
        self.namespace = namespace
        self._g = Graph()  # a triple store as the main data structure
        self._g.bind(prefix, namespace)
        self._g.bind("skos", SKOSURL)

        self._g.add((URIRef(RES_BOD_NS), RDF.type, OWL.Ontology))
        self._g.add((URIRef(RES_BOD_NS), SKOS.prefLabel,
                     Literal("SI Reference Point - Responsible Bodies", datatype=XSD.string)))
        self._g.add((URIRef(RES_BOD_NS), RDFS.comment,
                     Literal("Ontology, part of the SI Reference Point, covering the Responsible Bodies and their "
                             "resolutions, decisions, etc", datatype=XSD.string)))
        self._g.add((URIRef(RES_BOD_NS), DCTERMS.created, Literal(str(date.today()), datatype=XSD.date)))

        self.ResBod = self.set_uri('ResBod')
        self._g.add((self.ResBod, RDF.type, SKOS.Concept))
        self._g.add((self.ResBod, RDFS.label, Literal('Responsible Body', lang='en')))
        self._g.add((self.ResBod, RDFS.label, Literal('Organisme responsable', lang='fr')))
        self._g.add((self.ResBod, RDFS.comment, Literal('Can be CGPM, CIPM, one of the CCs, JCRB, JCTLM', lang='en')))

        self.Event = self.set_uri('Event')
        self._g.add((self.Event, RDF.type, SKOS.Concept))
        self._g.add((self.Event, RDFS.label, Literal('Event', lang='en')))
        self._g.add((self.Event, RDFS.label, Literal('Evènement', lang='fr')))
        self._g.add((self.Event, RDFS.comment, Literal("Class for the events of a Responsible Body", lang='en')))

        self.Outcome = self.set_uri('Outcome')
        self._g.add((self.Outcome, RDF.type, SKOS.Concept))
        self._g.add((self.Outcome, RDFS.label, Literal('Outcome', lang='en')))
        self._g.add((self.Outcome, RDFS.label, Literal('Résultat', lang='fr')))
        self._g.add((self.Outcome, RDFS.comment, Literal("Class for the outcome of an Event", lang='en')))

        self.Considering = self.set_uri('Considering')
        self._g.add((self.Considering, RDF.type, SKOS.Concept))
        self._g.add((self.Considering, RDFS.label, Literal('Considering', lang='en')))
        self._g.add((self.Considering, RDFS.label, Literal('Considérant', lang='fr')))
        self._g.add((self.Considering, RDFS.comment, Literal("Class for considering outcomes", lang='en')))

        self.Resolution = self.set_uri('Resolution')
        self._g.add((self.Resolution, RDF.type, SKOS.Concept))
        self._g.add((self.Resolution, RDFS.label, Literal('Resolution', lang='en')))
        self._g.add((self.Resolution, RDFS.label, Literal('Résolution', lang='fr')))
        self._g.add((self.Resolution, RDFS.subClassOf, self.Outcome))
        self._g.add((self.Resolution, RDFS.comment, Literal("Class for resolution outcomes", lang='en')))

        self.Declaration = self.set_uri('Declaration')
        self._g.add((self.Declaration, RDF.type, SKOS.Concept))
        self._g.add((self.Declaration, RDFS.label, Literal('Declaration', lang='en')))
        self._g.add((self.Declaration, RDFS.label, Literal('Déclaration', lang='fr')))
        self._g.add((self.Declaration, RDFS.subClassOf, self.Outcome))
        self._g.add((self.Declaration, RDFS.comment, Literal("Class for declaration outcomes", lang='en')))

        self.Decision = self.set_uri('Decision')
        self._g.add((self.Decision, RDF.type, SKOS.Concept))
        self._g.add((self.Decision, RDFS.label, Literal('Decision', lang='en')))
        self._g.add((self.Decision, RDFS.label, Literal('Décision', lang='fr')))
        self._g.add((self.Decision, RDFS.subClassOf, self.Outcome))
        self._g.add((self.Decision, RDFS.comment, Literal("Class for decision outcomes", lang='en')))

        self.Recommendation = self.set_uri('Recommendation')
        self._g.add((self.Recommendation, RDF.type, SKOS.Concept))
        self._g.add((self.Recommendation, RDFS.label, Literal('Recommendation', lang='en')))
        self._g.add((self.Recommendation, RDFS.label, Literal('Recommandation', lang='fr')))
        self._g.add((self.Recommendation, RDFS.subClassOf, self.Outcome))
        self._g.add((self.Recommendation, RDFS.comment, Literal("Class for recommendation outcomes", lang='en')))

        self.Publication = self.set_uri('Publication')
        self._g.add((self.Publication, RDF.type, SKOS.Concept))
        self._g.add((self.Publication, RDFS.label, Literal('Publication', lang='en')))
        self._g.add((self.Publication, RDFS.label, Literal('Publication', lang='fr')))
        self._g.add((self.Publication, RDFS.subClassOf, self.Outcome))
        self._g.add((self.Publication, RDFS.comment, Literal("Class for publication outcomes", lang='en')))

        self.Action = self.set_uri('Action')
        self._g.add((self.Action, RDF.type, SKOS.Concept))
        self._g.add((self.Action, RDFS.label, Literal('Action', lang='en')))
        self._g.add((self.Action, RDFS.label, Literal('Action', lang='fr')))
        self._g.add((self.Action, RDFS.comment, Literal("Class for action outcomes", lang='en')))

        # disjoint statements
        self._g.add((self.ResBod, OWL.disjointWith, self.Event))
        self._g.add((self.ResBod, OWL.disjointWith, self.Outcome))
        self._g.add((self.ResBod, OWL.disjointWith, self.Considering))
        self._g.add((self.Event, OWL.disjointWith, self.Outcome))
        self._g.add((self.Event, OWL.disjointWith, self.Considering))
        self._g.add((self.Outcome, OWL.disjointWith, self.Considering))

        self.hasAdopted = self.set_uri("hasAdopted")
        self._g.add((self.hasAdopted, RDF.type, OWL.ObjectProperty))
        self._g.add((self.hasAdopted, RDFS.label, Literal('has adopted', lang="en")))
        self._g.add((self.hasAdopted, RDFS.label, Literal('a adopté', lang='fr')))
        self._g.add((self.hasAdopted, RDFS.domain, self.ResBod))
        self._g.add((self.hasAdopted, RDFS.range, self.Outcome))
        self._g.add((self.hasAdopted, RDFS.comment, Literal('Linking a Responsible Body and an Outcome', lang='en')))

        self.wasAdoptedBy = self.set_uri("wasAdoptedBy")
        self._g.add((self.wasAdoptedBy, RDF.type, OWL.ObjectProperty))
        self._g.add((self.wasAdoptedBy, RDFS.label, Literal('was adopted by', lang="en")))
        self._g.add((self.wasAdoptedBy, RDFS.domain, self.Outcome))
        self._g.add((self.wasAdoptedBy, RDFS.range, self.ResBod))
        self._g.add((self.wasAdoptedBy, OWL.inverseOf, self.hasAdopted))
        self._g.add((self.wasAdoptedBy, RDFS.comment, Literal('Linking an outcome and a Responsible Body', lang='en')))

        self.hasAction = self.set_uri("hasAction")
        self._g.add((self.hasAction, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasAction, RDFS.label, Literal('has Actions', lang="en")))
        self._g.add((self.hasAction, RDFS.domain, self.Outcome))
        self._g.add((self.hasAction, RDFS.range, RDFS.Literal))
        self._g.add((self.hasAction, RDFS.comment, Literal('Linking an outcome and Actions (BlankNode)', lang='en')))

        self.hasActionText = self.set_uri("hasActionText")
        self._g.add((self.hasActionText, RDF.type,
                     OWL.DatatypeProperty))  # I don't fully understand why this should be a Datatype property
        self._g.add((self.hasActionText, RDFS.label, Literal('has Action Text', lang="en")))
        self._g.add((self.hasActionText, RDFS.domain, self.Outcome))
        self._g.add((self.hasActionText, RDFS.range, RDFS.Literal))
        self._g.add((self.hasAdopted, RDFS.comment, Literal('Linking the BlankNode and an Action Text', lang='en')))

        self.hasEvent = self.set_uri("hasEvent")
        self._g.add((self.hasEvent, RDF.type, OWL.ObjectProperty))
        self._g.add((self.hasEvent, RDFS.label, Literal('has Event', lang='en')))
        self._g.add((self.hasEvent, RDFS.label, Literal('a événement', lang='en')))
        self._g.add((self.hasEvent, RDFS.domain, self.ResBod))
        self._g.add((self.hasEvent, RDFS.range, self.Event))
        self._g.add((self.hasEvent, RDFS.comment, Literal('Linking a responsible body to an event', lang='en')))

        self.hasEventDate = self.set_uri("hasEventDate")
        self._g.add((self.hasEventDate, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasEventDate, RDFS.label, Literal('has Date', lang="en")))
        self._g.add((self.hasEventDate, RDFS.domain, self.Event))
        self._g.add((self.hasEventDate, RDFS.range, XSD.date))
        self._g.add((self.hasEventDate, RDFS.comment, Literal('Linking an event and a responsible body', lang='en')))

        self.hasEventNr = self.set_uri("hasEventNr")
        self._g.add((self.hasEventNr, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasEventNr, RDFS.label, Literal('has conference number', lang='en')))
        self._g.add((self.hasEventNr, RDFS.domain, self.Event))
        self._g.add((self.hasEventNr, RDFS.range, XSD.int))
        self._g.add((self.hasEventNr, RDFS.comment, Literal('Linking an event and its number', lang='en')))

        self.hasConsidering = self.set_uri("hasConsidering")
        self._g.add((self.hasConsidering, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasConsidering, RDFS.label, Literal('has considering', lang='en')))
        self._g.add((self.hasConsidering, RDFS.domain, self.Outcome))
        self._g.add((self.hasConsidering, RDFS.range, RDFS.Literal))
        self._g.add((self.hasConsidering, RDFS.comment, Literal('Linking an outcome to a considering', lang='en')))

        self.hasResolution = self.set_uri("hasResolution")
        self._g.add((self.hasResolution, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasResolution, RDFS.label, Literal('has resolution', lang='en')))
        self._g.add((self.hasResolution, RDFS.domain, self.Outcome))
        self._g.add((self.hasResolution, RDFS.range, RDFS.Literal))
        self._g.add((self.hasResolution, RDFS.comment, Literal('Linking an outcome to a resolution', lang='en')))

        self.hasConsideringText = self.set_uri("hasConsideringText")
        self._g.add((self.hasConsideringText, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasConsideringText, RDFS.label, Literal('has considering text', lang='en')))
        self._g.add((self.hasConsideringText, RDFS.domain, self.Outcome))
        self._g.add((self.hasConsideringText, RDFS.range, RDFS.Literal))
        self._g.add((self.hasConsideringText, RDFS.comment, Literal('Linking an outcome to '
                                                                    'its considering text', lang='en')))

        self.hasDOI = self.set_uri("hasDOI")
        self._g.add((self.hasDOI, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasDOI, RDFS.label, Literal('has DOI', lang='en')))
        self._g.add((self.hasDOI, RDFS.domain, self.Outcome))
        self._g.add((self.hasDOI, RDFS.range, RDFS.Literal))
        self._g.add((self.hasDOI, RDFS.comment, Literal('Linking an outcome and its DOI', lang='en')))

        self.hasOutcome = self.set_uri("hasOutcome")
        self._g.add((self.hasOutcome, RDF.type, OWL.ObjectProperty))
        self._g.add((self.hasOutcome, RDFS.label, Literal('has outcome', lang='en')))
        self._g.add((self.hasOutcome, RDFS.label, Literal('a résultat', lang='fr')))
        self._g.add((self.hasOutcome, RDFS.domain, self.Event))
        self._g.add((self.hasOutcome, RDFS.range, self.Outcome))
        self._g.add((self.hasOutcome, RDFS.comment, Literal('Linking an event to an outcome', lang='en')))

        self.isOutcomeOf = self.set_uri("isOutcomeOf")
        self._g.add((self.isOutcomeOf, RDF.type, OWL.ObjectProperty))
        self._g.add((self.isOutcomeOf, RDFS.label, Literal('is outcome of', lang='en')))
        self._g.add((self.isOutcomeOf, RDFS.label, Literal('est le résultat de', lang='fr')))
        self._g.add((self.isOutcomeOf, RDFS.domain, self.Outcome))
        self._g.add((self.isOutcomeOf, RDFS.range, self.Event))
        self._g.add((self.isOutcomeOf, RDFS.comment, Literal('Linking an outcome to an Event', lang='en')))

        self.hasOutcomeNr = self.set_uri("hasOutcomeNr")
        self._g.add((self.hasOutcomeNr, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasOutcomeNr, RDFS.label, Literal('has outcome Number', lang='en')))
        self._g.add((self.hasOutcomeNr, RDFS.domain, self.Outcome))
        self._g.add((self.hasOutcomeNr, RDFS.range, XSD.int))
        self._g.add((self.hasOutcomeNr, RDFS.comment, Literal('Linking an outcome and its Number', lang='en')))

        self.hasOutcomeTitle = self.set_uri("hasOutcomeTitle")
        self._g.add((self.hasOutcomeTitle, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasOutcomeTitle, RDFS.label, Literal('has outcome Title', lang='en')))
        self._g.add((self.hasOutcomeTitle, RDFS.domain, self.Outcome))
        self._g.add((self.hasOutcomeTitle, RDFS.range, RDFS.Literal))
        self._g.add((self.hasOutcomeTitle, RDFS.comment, Literal('Linking an outcome and its Title', lang='en')))

    def set_uri(self, name: str) -> URIRef:
        """Utility method"""
        return URIRef(self.namespace + name)

    @property
    def g(self):
        return self._g


def main():
    """Main of ResBod T-Box"""
    resbod_TBox = ResBod()
    return resbod_TBox.g
