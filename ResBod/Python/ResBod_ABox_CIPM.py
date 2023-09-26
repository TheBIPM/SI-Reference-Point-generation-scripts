import glob
import os
import re
from datetime import date

import yaml
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS, XSD
from ResBod_TBox import ResBod_ns

from settings import *

# useful function
def get_outcome_values(outcome, conf_Nr, ResBod, ResBod_label="CIPM"):
    out_id = outcome['identifier']
    outcome_type = RB.Outcome
    type_abbreviation = ""
    if outcome['type'] == 'resolution':
        type_abbreviation = f"-Res{out_id}"
        outcome_type = RB.Resolution
    elif outcome['type'] == 'declaration':
        type_abbreviation = f"-Decl{'' if out_id == 0 else out_id}"
        outcome_type = RB.Declaration
    elif outcome['type'] == 'recommendation':
        type_abbreviation = "-Rec" + str(out_id)
        outcome_type = RB.Recommendation
    elif outcome['type'] == 'decision':
        type_abbreviation = "-Dec" + str(out_id)
        outcome_type = RB.Decision
    elif outcome['type'] == 'publication':
        type_abbreviation = "-Pub" + str(out_id)
        outcome_type = RB.Publication
    
    local_id = str(conf_Nr) + type_abbreviation
    outcome_URI = ResBod.term(local_id)
    hidden_label = ResBod_label + local_id

    return outcome_URI, out_id, hidden_label, outcome_type

sort_key = lambda item : float(re.findall("[0-9]+[\-0-9]*", os.path.basename(item))[0].replace("-", "."))

# further needed namespaces
RB = Namespace(ResBod_ns)
CIPM = Namespace(SIURL + "bodies/CIPM#")

def main():
    # init graph
    g = Graph()
    g.bind("rb", RB)
    g.bind("cipm", CIPM)

    # relative paths from this file
    BASE_PATH_FR = CIPM_FILES_FOLDER + "meetings-fr/"
    BASE_PATH_EN = CIPM_FILES_FOLDER + "meetings-en/"

    # Annotations to the ontology (name, Version number)
    g.add((URIRef(CIPM), RDF.type, OWL.Ontology))
    g.add((URIRef(CIPM), SKOS.prefLabel, Literal("SI Reference Point - CIPM meetings and outcomes", datatype=XSD.string)))
    g.add((URIRef(CIPM), RDFS.comment,
            Literal("Ontology, part of the SI Reference Point, covering the resolutions, "
                    "decisions, etc of the CIPM", datatype=XSD.string)))
    g.add((URIRef(CIPM), DCTERMS.created, Literal(str(date.today()), datatype=XSD.date)))

    # create the responsible body "CIPM"
    g.add((URIRef(CIPM.CIPM), RDF.type, RB.ResBod))

    # iterate over the resolutions files (in 'natural' sorted order)
    yaml_filenames_en = sorted(glob.glob(BASE_PATH_EN + "meeting-*.yml"), key = sort_key)
    yaml_filenames_fr = sorted(glob.glob(BASE_PATH_FR + "meeting-*.yml"), key = sort_key)

    for yaml_filename_en, yaml_filename_fr in zip(yaml_filenames_en, yaml_filenames_fr):

        with open(yaml_filename_fr, '+r', encoding="utf8") as fr_file:
            meeting_fr = yaml.safe_load(fr_file)
        with open(yaml_filename_en, '+r', encoding="utf8") as en_file:
            meeting_en = yaml.safe_load(en_file)

        # if both (en and fr) readings were successful, proceed to extract the information on the conference
        # and create the assertions
        conf_URI = CIPM.term(f"CIPM{meeting_fr['metadata']['identifier']}")
        conf_date = meeting_fr['metadata']['date']
        conf_Nr = meeting_fr['metadata']['identifier']
        conf_title_fr = meeting_fr['metadata']['title']
        conf_title_en = meeting_en['metadata']['title']

        # attach the Conference to the responsible body
        g.add((URIRef(CIPM.CIPM), RB.hasEvent, conf_URI))

        # add the information about the event
        g.add((conf_URI, RDF.type, RB.Event))
        g.add((conf_URI, RB.hasEventDate, Literal(conf_date, datatype=XSD.date)))
        g.add((conf_URI, RB.hasEventNr, Literal(conf_Nr))) #, datatype=XSD.int)))
        g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_fr, lang="fr")))
        g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_en, lang="en")))
        g.add((conf_URI, SKOS.hiddenLabel, Literal("CIPM" + str(conf_Nr), datatype=XSD.string)))

        # insert the assertion about the resolutions (attached to the responsible body)
        # in French
        for outcome in meeting_fr['resolutions']:

            outcome_URI, out_id, hidden_label, outcome_type = get_outcome_values(outcome, conf_Nr, CIPM, "CIPM")

            outcome_fr_DOI = outcome['url']
            outcome_title_fr = outcome['title']

            g.add((URIRef(CIPM.CIPM), RB.hasAdopted, outcome_URI))
            g.add((outcome_URI, RB.wasAdoptedBy, URIRef(CIPM.CIPM)))
            g.add((outcome_URI, RDF.type, outcome_type))
            g.add((conf_URI, RB.hasOutcome, outcome_URI))
            g.add((outcome_URI, RB.isOutcomeOf, conf_URI))
            g.add((outcome_URI, RB.hasOutcomeTitle, Literal(outcome_title_fr, lang='fr')))
            g.add((outcome_URI, RB.hasOutcomeNr, Literal(out_id)))
            g.add((outcome_URI, SKOS.hiddenLabel, Literal(hidden_label, datatype=XSD.string)))
            g.add((outcome_URI, RB.hasDOI, Literal(outcome_fr_DOI, lang='fr')))
            if outcome['considerations']:  # only include this if there are considerations
                considering_blankNodeID = URIRef(outcome_URI + "Considering")  # Blank node holding the considerings
                g.add((outcome_URI, RB.hasConsidering, considering_blankNodeID))
                for consideration in outcome['considerations']:
                    g.add(
                        (considering_blankNodeID, RB.hasConsideringText, Literal(consideration['message'], lang='fr')))

            if outcome['actions']:  # only include this if there are actions
                actions_blankNodeID = URIRef(outcome_URI + "Action")  # Blank node holding the actions
                g.add((outcome_URI, RB.hasAction, actions_blankNodeID))
                for action in outcome['actions']:
                    g.add((actions_blankNodeID, RB.hasActionText, Literal(action['message'], lang='fr')))

        # in English
        for outcome in meeting_en['resolutions']:
            
            outcome_URI, out_id, hidden_label, outcome_type = get_outcome_values(outcome, conf_Nr, CIPM, "CIPM")

            resol_en_DOI = outcome['url']
            resol_title_en = outcome['title']
            considering_blankNodeID = URIRef(outcome_URI + "Considering")
            actions_blankNodeID = URIRef(outcome_URI + "Action")
            g.add((outcome_URI, RB.hasOutcomeTitle, Literal(resol_title_en, lang='en')))
            g.add((outcome_URI, RB.hasDOI, Literal(resol_en_DOI, lang='en')))
            if outcome['considerations']:  # only include this if there are considerations
                considering_blankNodeID = URIRef(outcome_URI + "Considering")  # Blank node holding the considerings
                g.add((outcome_URI, RB.hasConsidering, considering_blankNodeID))
                for consideration in outcome['considerations']:
                    g.add(
                        (considering_blankNodeID, RB.hasConsideringText, Literal(consideration['message'], lang='en')))

            if outcome['actions']:  # only include this if there are actions
                actions_blankNodeID = URIRef(outcome_URI + "Action")  # Blank node holding the actions
                g.add((outcome_URI, RB.hasAction, actions_blankNodeID))
                for action in outcome['actions']:
                    g.add((actions_blankNodeID, RB.hasActionText, Literal(action['message'], lang='en')))


    # serialize the knowledge graph when all CIPMs are covered,         
    g.serialize(format='turtle', destination=APIPATH + 'cipm.ttl')


if __name__ == "__main__":
    main()