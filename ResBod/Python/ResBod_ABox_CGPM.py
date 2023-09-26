#
# ResBod ABox
#
#
# the module imports the Python script 'settings.py' located in a directory above this directory
# Should this lead to an error when executing the present script (... not found ...) you might need
# to add the location to the PYTHONPATH by typing (in the TERMINAL where you execute the Python script)
# export PYTHONPATH=(path where the package is located) (e.g. /Users/gregordudle/Development/Semantic-SI)
#

import glob
from datetime import date

import yaml
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS, XSD
from ResBod_ABox_CIPM import RB, get_outcome_values, sort_key

from settings import *

# further needed namespaces
CGPM = Namespace(SIURL + "bodies/CGPM#")


def main():
    # init graph
    g = Graph()
    g.bind("rb", RB)
    g.bind("cgpm", CGPM)

    # relative paths from this file
    BASE_PATH_FR = CGPM_FILES_FOLDER + "meetings-fr/"
    BASE_PATH_EN = CGPM_FILES_FOLDER + "meetings-en/"

    # Annotations to the ontology (name, Version number)
    g.add((URIRef(CGPM), RDF.type, OWL.Ontology))
    g.add((URIRef(CGPM), SKOS.prefLabel, Literal("SI Reference Point - CGPM meetings and outcomes", datatype=XSD.string)))
    g.add((URIRef(CGPM), RDFS.comment,
            Literal("Ontology, part of the SI Reference Point, covering the resolutions, "
                    "decisions, etc of the CGPM", datatype=XSD.string)))
    g.add((URIRef(CGPM), DCTERMS.created, Literal(str(date.today()), datatype=XSD.date)))

    # create the responsible body "CGPM"
    g.add((URIRef(CGPM.CGPM), RDF.type, RB.ResBod))

    # iterate over the resolutions files (in 'natural' sorted order)
    yaml_filenames_en = sorted(glob.glob(BASE_PATH_EN + "meeting-*.yml"), key = sort_key)
    yaml_filenames_fr = sorted(glob.glob(BASE_PATH_FR + "meeting-*.yml"), key = sort_key)

    for yaml_filename_en, yaml_filename_fr in zip(yaml_filenames_en, yaml_filenames_fr):

        with open(yaml_filename_fr, '+r', encoding='utf-8') as fr_file:
            meeting_fr = yaml.safe_load(fr_file)
        with open(yaml_filename_en, '+r', encoding='utf-8') as en_file:
            meeting_en = yaml.safe_load(en_file)

        # if both (en and fr) readings were successful, proceed to extract the information on the conference
        # and create the assertions
        conf_URI = CGPM.term(f"CGPM{meeting_fr['metadata']['identifier']}")
        conf_date = meeting_fr['metadata']['date']
        conf_Nr = meeting_fr['metadata']['identifier']
        conf_title_fr = meeting_fr['metadata']['title']
        conf_title_en = meeting_en['metadata']['title']

        # attach the Conference to the responsible body
        g.add((URIRef(CGPM.CGPM), RB.hasEvent, conf_URI))

        # add the information about the event
        g.add((conf_URI, RDF.type, RB.Event))
        g.add((conf_URI, RB.hasEventDate, Literal(conf_date, datatype=XSD.date)))
        g.add((conf_URI, RB.hasEventNr, Literal(conf_Nr))) #, datatype=XSD.int)))
        g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_fr, lang="fr")))
        g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_en, lang="en")))
        g.add((conf_URI, SKOS.hiddenLabel, Literal("CGPM" + str(conf_Nr), datatype=XSD.string)))


        # insert the assertion about the resolutions (attached to the responsible body)
        # in French
        for outcome in meeting_fr['resolutions']:

            outcome_URI, out_id, hidden_label, outcome_type = get_outcome_values(outcome, conf_Nr, CGPM, "CGPM")

            outcome_fr_DOI = outcome['url']
            outcome_title_fr = outcome['title']

            g.add((URIRef(CGPM.CGPM), RB.hasAdopted, outcome_URI))
            g.add((outcome_URI, RB.wasAdoptedBy, URIRef(CGPM.CGPM)))
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
            
            outcome_URI, out_id, hidden_label, outcome_type = get_outcome_values(outcome, conf_Nr, CGPM, "CGPM")

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


    # serialize the knowledge graph when all CGPMs are covered,         
    g.serialize(format='turtle', destination=APIPATH + 'cgpm.ttl')


if __name__ == "__main__":
    main()