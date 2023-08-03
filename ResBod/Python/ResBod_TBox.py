from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, SKOS, OWL, XSD
from settings import *

ResBod_ns = SIURL + "ResBod#"


class ResBod:
    def __init__(self, namespace: str = ResBod_ns, prefix: str = 'rb'):
        self.namespace = namespace
#        self.CGPM_namespace = Namespace(ResBod_ns)         #not used elsewhere
        self._g = Graph()  # a triple store as the main data structure
        self._g.bind(prefix, namespace)
        self._g.bind("skos", SKOSURL)

        self.ResBod = self.set_uri('ResBod')
        self._g.add((self.ResBod, RDF.type, SKOS.Concept))
        self._g.add((self.ResBod, RDFS.label, Literal('Responsible Body',lang='en')))
        self._g.add((self.ResBod, RDFS.label, Literal('Organisme responsable',lang='fr')))
        self._g.add((self.ResBod, RDFS.comment, Literal('Can be CGPM, CIPM, one of the CCs, JCRB, JCTLM',lang='en')))

        self.Event = self.set_uri('Event')  
        self._g.add((self.Event, RDF.type, SKOS.Concept))
        self._g.add((self.Event, RDFS.label, Literal('Event', lang='en')))
        self._g.add((self.Event, RDFS.label, Literal('Evènement', lang='fr')))
        self._g.add((self.Event, RDFS.comment, Literal("Class for the events of a Responsible Body",lang='en')))

        self.Outcome = self.set_uri('Outcome')  
        self._g.add((self.Outcome, RDF.type, SKOS.Concept))
        self._g.add((self.Outcome, RDFS.label, Literal('Outcome', lang='en')))
        self._g.add((self.Outcome, RDFS.label, Literal('Résultat', lang='fr')))
        self._g.add((self.Outcome, RDFS.comment, Literal("Class for the Outcome of an Event",lang='en')))

        self.OutcomeType = self.set_uri('OutcomeType')  
        self._g.add((self.OutcomeType, RDF.type, SKOS.Concept))
        self._g.add((self.OutcomeType, RDFS.label, Literal('OutcomeType', lang='en')))
        self._g.add((self.OutcomeType, RDFS.label, Literal('Résultat', lang='fr')))
        self._g.add((self.OutcomeType, RDFS.comment, Literal('Class for the Outcome Type. Depending on the Responsible Body this can be a Resolution, a Recommendation, a Decision', lang='en')))

        self.Considerings = self.set_uri('Considerings')
        self._g.add((self.Considerings, RDF.type, SKOS.Concept))

        self._g.add((self.ResBod, OWL.disjointWith, self.Event))
        self._g.add((self.ResBod, OWL.disjointWith, self.Outcome))
        self._g.add((self.ResBod, OWL.disjointWith, self.Considerings))        
        self._g.add((self.Event, OWL.disjointWith, self.Outcome))
        self._g.add((self.Event, OWL.disjointWith, self.Considerings))
        self._g.add((self.Outcome, OWL.disjointWith, self.Considerings))

        self.hasAdopted = self.set_uri("hasAdopted")
        self._g.add((self.hasAdopted, RDF.type, OWL.ObjectProperty))
        self._g.add((self.hasAdopted, RDFS.label, Literal('has adopted', lang="en")))
        self._g.add((self.hasAdopted, RDFS.label, Literal('a adopté',lang='fr')))
        self._g.add((self.hasAdopted, RDFS.domain, self.ResBod))
        self._g.add((self.hasAdopted, RDFS.range, self.Outcome))
        self._g.add((self.hasAdopted, RDFS.comment, Literal('Linking a Responsible Body and an Outcome',lang='en')))

        self.wasAdoptedBy = self.set_uri("wasAdoptedBy")
        self._g.add((self.wasAdoptedBy, RDF.type, OWL.ObjectProperty))
        self._g.add((self.wasAdoptedBy, RDFS.label, Literal('was adopted by', lang="en")))
        self._g.add((self.wasAdoptedBy, RDFS.domain, self.Outcome))
        self._g.add((self.wasAdoptedBy, RDFS.range, self.ResBod))
        self._g.add((self.wasAdoptedBy, OWL.inverseOf, self.hasAdopted))
        self._g.add((self.wasAdoptedBy, RDFS.comment, Literal('Linking an Outcome and a Responsible Body',lang='en')))

        self.hasActions = self.set_uri("hasActions")
        self._g.add((self.hasActions, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasActions, RDFS.label, Literal('has Actions', lang="en")))
        self._g.add((self.hasActions, RDFS.domain, self.Outcome))
        self._g.add((self.hasActions, RDFS.range, RDFS.Literal))
        self._g.add((self.hasActions, RDFS.comment, Literal('Linking an Outcome and Actions (BlankNode)',lang='en')))

        self.hasActionText = self.set_uri("hasActionText")
        self._g.add((self.hasActionText, RDF.type,
                     OWL.DatatypeProperty))  # I don't fully understand why this should be a Datatype property
        self._g.add((self.hasActionText, RDFS.label, Literal('has Action Text', lang="en")))
        self._g.add((self.hasActionText, RDFS.domain, self.Outcome))
        self._g.add((self.hasActionText, RDFS.range, RDFS.Literal))
        self._g.add((self.hasAdopted, RDFS.comment, Literal('Linking the BlankNode and an Action Text',lang='en')))        

        self.hasEvent = self.set_uri("hasEvent")
        self._g.add((self.hasEvent, RDF.type, OWL.ObjectProperty))
        self._g.add((self.hasEvent, RDFS.label, Literal('has Event', lang='en')))
        self._g.add((self.hasEvent, RDFS.label, Literal('a événement', lang='en')))
        self._g.add((self.hasEvent, RDFS.domain, self.ResBod))
        self._g.add((self.hasEvent, RDFS.range, self.Event))
        self._g.add((self.hasEvent, RDFS.comment, Literal('Linking a Responsible Body to an Event', lang='en')))

        self.hasEventDate = self.set_uri("hasEventDate")
        self._g.add((self.hasEventDate, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasEventDate, RDFS.label, Literal('has Date' , lang="en")))
        self._g.add((self.hasEventDate, RDFS.domain, self.Event))
        self._g.add((self.hasEventDate, RDFS.range, XSD.date))
        self._g.add((self.hasEventDate, RDFS.comment, Literal('Linking an Event and a Responsible Body',lang='en')))


        self.hasEventNr = self.set_uri("hasEventNr")
        self._g.add((self.hasEventNr, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasEventNr, RDFS.label, Literal('has Conference Number', lang='en')))
        self._g.add((self.hasEventNr, RDFS.domain, self.Event))
        self._g.add((self.hasEventNr, RDFS.range, XSD.int))
        self._g.add((self.hasEventNr, RDFS.comment, Literal('Linking an Event and its Number',lang='en')))

        self.hasConsiderings = self.set_uri("hasConsiderings")
        self._g.add((self.hasConsiderings, RDF.type,
                     OWL.DatatypeProperty))  # I don't fully understand why this should be a Datatype property
        self._g.add((self.hasConsiderings, RDFS.label, Literal('has Considerings', lang='en')))
        self._g.add((self.hasConsiderings, RDFS.domain, self.Outcome))
        self._g.add((self.hasConsiderings, RDFS.range, RDFS.Literal))
        self._g.add((self.hasConsiderings, RDFS.comment, Literal('Linking an Outcome and the Considerings (Blank Node)',lang='en')))

        self.hasConsideringText = self.set_uri("hasConsideringText")
        self._g.add((self.hasConsideringText, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasConsideringText, RDFS.label, Literal('has Considering Text', lang='en')))
        self._g.add((self.hasConsideringText, RDFS.domain, self.Outcome))
        self._g.add((self.hasConsideringText, RDFS.range, RDFS.Literal))
        self._g.add((self.hasConsideringText, RDFS.comment, Literal('Linking the Blank Node and the Considering Text',lang='en')))

        self.hasDOI = self.set_uri("hasDOI")
        self._g.add((self.hasDOI, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasDOI, RDFS.label, Literal('has DOI', lang='en')))
        self._g.add((self.hasDOI, RDFS.domain, self.Outcome))
        self._g.add((self.hasDOI, RDFS.range, RDFS.Literal))
        self._g.add((self.hasDOI, RDFS.comment, Literal('Linking an Outcome and a DOI', lang='en')))

        self.hasOutcome = self.set_uri("hasOutcome")
        self._g.add((self.hasOutcome, RDF.type, OWL.ObjectProperty))
        self._g.add((self.hasOutcome, RDFS.label, Literal('has outcome', lang='en')))
        self._g.add((self.hasOutcome, RDFS.label, Literal('a résultat', lang='fr')))
        self._g.add((self.hasOutcome, RDFS.domain, self.Event))
        self._g.add((self.hasOutcome, RDFS.range, self.Outcome))
        self._g.add((self.hasOutcome, RDFS.comment, Literal('Linking an Event to an Outcome',lang='en')))

        self.isOutcomeOf = self.set_uri("isOutcomeOf")
        self._g.add((self.isOutcomeOf, RDF.type, OWL.ObjectProperty))
        self._g.add((self.isOutcomeOf, RDFS.label, Literal('is outcome of', lang='en')))
        self._g.add((self.isOutcomeOf, RDFS.label, Literal('est le résultat de', lang='fr')))
        self._g.add((self.isOutcomeOf, RDFS.domain, self.Outcome))
        self._g.add((self.isOutcomeOf, RDFS.range, self.Event))
        self._g.add((self.isOutcomeOf, RDFS.comment, Literal('Linking an Outcome to an Event',lang='en')))

        self.hasOutcomeNr = self.set_uri("hasOutcomeNr")
        self._g.add((self.hasOutcomeNr, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasOutcomeNr, RDFS.label, Literal('has Outcome Number', lang='en')))
        self._g.add((self.hasOutcomeNr, RDFS.domain, self.Outcome))
        self._g.add((self.hasOutcomeNr, RDFS.range, XSD.int))
        self._g.add((self.hasOutcomeNr, RDFS.comment, Literal('Linking an Outcome and its Number', lang='en')))

        self.hasOutcomeTitle = self.set_uri("hasOutcomeTitle")
        self._g.add((self.hasOutcomeTitle, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasOutcomeTitle, RDFS.label, Literal('has Outcome Title', lang='en')))
        self._g.add((self.hasOutcomeTitle, RDFS.domain, self.Outcome))
        self._g.add((self.hasOutcomeTitle, RDFS.range, RDFS.Literal))
        self._g.add((self.hasOutcomeTitle, RDFS.comment, Literal('Linking an Outcome and its Title', lang='en')))

        self.hasOutcomeType = self.set_uri("hasOutcomeType")
        self._g.add((self.hasOutcomeType, RDF.type, OWL.DatatypeProperty))
        self._g.add((self.hasOutcomeType, RDFS.label, Literal('has Outcome Type', lang='en')))
        self._g.add((self.hasOutcomeType, RDFS.domain, self.Outcome))
        self._g.add((self.hasOutcomeType, RDFS.range, RDFS.Literal))
        self._g.add((self.hasOutcomeType, RDFS.comment, Literal('Linking an Outcome and its type (Resolution, Recommandation, ...)', lang='en')))

        self.g.serialize(format='ttl', destination=APIPATH + 'rb.ttl')

    def set_uri(self, name: str) -> URIRef:
        # Utility method
        return URIRef(self.namespace + name)

    @property
    def g(self):
        return self._g
