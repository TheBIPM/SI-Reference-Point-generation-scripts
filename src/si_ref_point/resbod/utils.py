import glob
import os
import re
from datetime import date

import yaml
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS, XSD
from si_ref_point.resbod.ResBod_TBox import resbod_ns

from si_ref_point.settings import SIDFWBASE

RB = Namespace(resbod_ns)


class MeetingsFileExtractor:
    def __init__(
        self,
        base_url=SIDFWBASE + "/bodies/",
        resbod_acronym="CIPM",
        meeting_files_directory="",
    ):
        self.own_acronym = resbod_acronym
        meeting_files_directory = meeting_files_directory

        # relative paths from this file
        self.base_path_fr = os.path.join(meeting_files_directory, "meetings-fr/")
        self.base_path_en = os.path.join(meeting_files_directory, "meetings-en/")

        # needed namespaces
        self.RB = Namespace(resbod_ns)
        self.OWN_NS = Namespace(base_url + self.own_acronym + "#")
        self.OWN_node = URIRef(
            self.OWN_NS.term(self.own_acronym)
        )  # e.g. cipm:CIPM

    # main call from outside
    def create_and_return_graph(self):
        self.init_graph()
        self.add_general_description()
        self.add_meeting_information()
        return self.g

    def init_graph(self):
        self.g = Graph()
        self.g.bind("rb", self.RB)
        self.g.bind(self.own_acronym.lower(), self.OWN_NS)

    def add_general_description(self):

    # Annotations to the ontology (name, creation date, comment)
        self.g.add((URIRef(self.OWN_NS), RDF.type, OWL.Ontology))
        self.g.add(
            (
                URIRef(self.OWN_NS),
                SKOS.prefLabel,
                Literal(
                    f"SI Reference Point - {self.own_acronym} meetings and outcomes",
                    datatype=XSD.string,
                ),
            )
        )
        
        self.g.add(
            (
                URIRef(self.OWN_NS),
                DCTERMS.created,
                Literal(str(date.today()), datatype=XSD.date),
            )
        )
        
        self.g.add(
            (
                URIRef(self.OWN_NS),
                RDFS.comment,
                Literal(
                    f"Ontology, part of the SI Reference Point, covering the resolutions, "
                    f"decisions, etc of the {self.own_acronym}.",
                    datatype=XSD.string,
                ),
            )
        )

        # create the responsible body "self.own_acronym"
        self.g.add((self.OWN_node, RDF.type, RB.ResBod))

    def add_meeting_information(self):
        # iterate over the resolutions files (in 'natural' sorted order)
        filenames_en = sorted(
            glob.glob(self.base_path_en + "meeting-*.yml"), key=self.meetings_sort_key
        )
        filenames_fr = sorted(
            glob.glob(self.base_path_fr + "meeting-*.yml"), key=self.meetings_sort_key
        )

        for filename_en, filename_fr in zip(filenames_en, filenames_fr):
            with open(filename_fr, "+r", encoding="utf8") as fr_file:
                meeting_fr = yaml.safe_load(fr_file)
            with open(filename_en, "+r", encoding="utf8") as en_file:
                meeting_en = yaml.safe_load(en_file)

            # if both (en and fr) readings were successful, proceed to extract the information on the conference
            # and create the assertions
            conf_URI = self.OWN_NS.term(
                f"{self.own_acronym}{meeting_fr['metadata']['identifier']}"
            )
            conf_date = meeting_fr["metadata"]["date"]
            conf_Nr = meeting_fr["metadata"]["identifier"]
            conf_title_fr = meeting_fr["metadata"]["title"]
            conf_title_en = meeting_en["metadata"]["title"]

            # attach the Conference to the responsible body
            self.g.add((self.OWN_node, RB.hasEvent, conf_URI))

            # add the information about the event
            self.g.add((conf_URI, RDF.type, RB.Event))
            self.g.add(
                (conf_URI, RB.hasEventDate, Literal(conf_date, datatype=XSD.date))
            )
            self.g.add(
                (conf_URI, RB.hasEventNr, Literal(conf_Nr))
            )  # , datatype=XSD.int)))
            self.g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_fr, lang="fr")))
            self.g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_en, lang="en")))
            self.g.add(
                (
                    conf_URI,
                    SKOS.hiddenLabel,
                    Literal(self.own_acronym + str(conf_Nr), datatype=XSD.string),
                )
            )

            # insert the assertion about the resolutions (attached to the responsible body)
            # in French
            for outcome in meeting_fr["resolutions"]:
                (
                    outcome_URI,
                    out_id,
                    hidden_label,
                    outcome_type,
                ) = self.get_outcome_values(outcome, conf_Nr)

                outcome_fr_DOI = outcome["url"]
                outcome_title_fr = outcome["title"]

                self.g.add((self.OWN_node, RB.hasAdopted, outcome_URI))
                self.g.add((outcome_URI, RB.wasAdoptedBy, self.OWN_node))
                self.g.add((outcome_URI, RDF.type, outcome_type))
                self.g.add((conf_URI, RB.hasOutcome, outcome_URI))
                self.g.add((outcome_URI, RB.isOutcomeOf, conf_URI))
                self.g.add(
                    (
                        outcome_URI,
                        RB.hasOutcomeTitle,
                        Literal(outcome_title_fr, lang="fr"),
                    )
                )
                self.g.add((outcome_URI, RB.hasOutcomeNr, Literal(out_id)))
                self.g.add(
                    (
                        outcome_URI,
                        SKOS.hiddenLabel,
                        Literal(hidden_label, datatype=XSD.string),
                    )
                )
                self.g.add((outcome_URI, RB.hasDOI, Literal(outcome_fr_DOI, lang="fr")))
                if outcome[
                    "considerations"
                ]:  # only include this if there are considerations
                    considering_blankNodeID = URIRef(
                        outcome_URI + "Considering"
                    )  # Blank node holding the considerings
                    self.g.add(
                        (outcome_URI, RB.hasConsidering, considering_blankNodeID)
                    )
                    for consideration in outcome["considerations"]:
                        self.g.add(
                            (
                                considering_blankNodeID,
                                RB.hasConsideringText,
                                Literal(consideration["message"], lang="fr"),
                            )
                        )

                if outcome["actions"]:  # only include this if there are actions
                    actions_blankNodeID = URIRef(
                        outcome_URI + "Action"
                    )  # Blank node holding the actions
                    self.g.add((outcome_URI, RB.hasAction, actions_blankNodeID))
                    for action in outcome["actions"]:
                        self.g.add(
                            (
                                actions_blankNodeID,
                                RB.hasActionText,
                                Literal(action["message"], lang="fr"),
                            )
                        )

            # in English
            for outcome in meeting_en["resolutions"]:
                (
                    outcome_URI,
                    out_id,
                    hidden_label,
                    outcome_type,
                ) = self.get_outcome_values(outcome, conf_Nr)

                resol_en_DOI = outcome["url"]
                resol_title_en = outcome["title"]
                considering_blankNodeID = URIRef(outcome_URI + "Considering")
                actions_blankNodeID = URIRef(outcome_URI + "Action")
                self.g.add(
                    (
                        outcome_URI,
                        RB.hasOutcomeTitle,
                        Literal(resol_title_en, lang="en"),
                    )
                )
                self.g.add((outcome_URI, RB.hasDOI, Literal(resol_en_DOI, lang="en")))
                if outcome[
                    "considerations"
                ]:  # only include this if there are considerations
                    considering_blankNodeID = URIRef(
                        outcome_URI + "Considering"
                    )  # Blank node holding the considerings
                    self.g.add(
                        (outcome_URI, RB.hasConsidering, considering_blankNodeID)
                    )
                    for consideration in outcome["considerations"]:
                        self.g.add(
                            (
                                considering_blankNodeID,
                                RB.hasConsideringText,
                                Literal(consideration["message"], lang="en"),
                            )
                        )

                if outcome["actions"]:  # only include this if there are actions
                    actions_blankNodeID = URIRef(
                        outcome_URI + "Action"
                    )  # Blank node holding the actions
                    self.g.add((outcome_URI, RB.hasAction, actions_blankNodeID))
                    for action in outcome["actions"]:
                        self.g.add(
                            (
                                actions_blankNodeID,
                                RB.hasActionText,
                                Literal(action["message"], lang="en"),
                            )
                        )

    def get_outcome_values(self, outcome, conf_Nr):
        out_id = outcome["identifier"]
        outcome_type = RB.Outcome
        type_abbreviation = ""
        if outcome["type"] == "resolution":
            type_abbreviation = f"-Res{out_id}"
            outcome_type = RB.Resolution
        elif outcome["type"] == "declaration":
            type_abbreviation = f"-Decl{'' if out_id == 0 else out_id}"
            outcome_type = RB.Declaration
        elif outcome["type"] == "recommendation":
            type_abbreviation = "-Rec" + str(out_id)
            outcome_type = RB.Recommendation
        elif outcome["type"] == "decision":
            type_abbreviation = "-Dec" + str(out_id)
            outcome_type = RB.Decision
        elif outcome["type"] == "publication":
            type_abbreviation = "-Pub" + str(out_id)
            outcome_type = RB.Publication

        local_id = self.own_acronym + str(conf_Nr) + type_abbreviation
        outcome_URI = self.OWN_NS.term(local_id)
        hidden_label = local_id

        return outcome_URI, out_id, hidden_label, outcome_type

    def meetings_sort_key(self, item):
        return float(
            re.findall("[0-9]+[\-0-9]*", os.path.basename(item))[0].replace("-", ".")
        )
