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
import os
import re

import ResBod_TBox
import yaml
from rdflib import Literal, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS, XSD

from settings import *

PDF = ResBod_TBox.ResBod()

ResBod_ns = SIURL + "ResBod#"

# relative paths from this file
BASE_PATH_FR = CIPM_FILES_FOLDER + "meetings-fr/"
BASE_PATH_EN = CIPM_FILES_FOLDER + "meetings-en/"

# Annotations to the ontology (name, Version number)
PDF.g.add((URIRef(ResBod_ns), RDF.type, OWL.Ontology))
PDF.g.add((URIRef(ResBod_ns), SKOS.prefLabel, Literal("SI Reference Point - Responsible Bodies", datatype=XSD.string)))
PDF.g.add((URIRef(ResBod_ns), RDFS.comment,
           Literal("Ontology, part of the SI Reference Point, covering the Responsible Bodies and their resolutions, "
                   "decisions, etc (for the moment CGPM and CIPM)", datatype=XSD.string)))
PDF.g.add((URIRef(ResBod_ns), DCTERMS.created, Literal(str(date.today()), datatype=XSD.date)))

# 2) CIPM

# create the responsible body "CIPM"
cipm_URI = URIRef(ResBod_ns + "CIPM")
PDF.g.add((URIRef(cipm_URI), RDF.type, PDF.ResBod))

# iterate over the resolutions files (in 'natural' sorted order)
sort_key = lambda item : float(re.findall("[0-9]+[\-0-9]*", os.path.basename(item))[0].replace("-", "."))
yaml_filenames_en = sorted(glob.glob(BASE_PATH_EN + "meeting-*.yml"), key = sort_key)
yaml_filenames_fr = sorted(glob.glob(BASE_PATH_FR + "meeting-*.yml"), key = sort_key)

for yaml_filename_en, yaml_filename_fr in zip(yaml_filenames_en, yaml_filenames_fr):

    with open(yaml_filename_fr, '+r', encoding="utf8") as fr_file:
        meeting_fr = yaml.safe_load(fr_file)
    with open(yaml_filename_en, '+r', encoding="utf8") as en_file:
        meeting_en = yaml.safe_load(en_file)

    # if both (en and fr) readings were successful, proceed to extract the information on the conference
    # and create the assertions
    conf_URI = URIRef(ResBod_ns + "CIPM" + str(meeting_fr['metadata']['identifier']))
    conf_date = meeting_fr['metadata']['date']
    conf_Nr = meeting_fr['metadata']['identifier']
    conf_title_fr = meeting_fr['metadata']['title']
    conf_title_en = meeting_en['metadata']['title']

    # attach the Conference to the responsible body
    PDF.g.add((cipm_URI, PDF.hasEvent, conf_URI))

    # add the information about the event
    PDF.g.add((conf_URI, RDF.type, PDF.Event))
    PDF.g.add((conf_URI, PDF.hasEventDate, Literal(conf_date, datatype=XSD.date)))
    PDF.g.add((conf_URI, PDF.hasEventNr, Literal(conf_Nr))) #, datatype=XSD.int)))
    PDF.g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_fr, lang="fr")))
    PDF.g.add((conf_URI, SKOS.prefLabel, Literal(conf_title_en, lang="en")))
    PDF.g.add((conf_URI, SKOS.hiddenLabel, Literal("CIPM" + str(conf_Nr), datatype=XSD.string)))

    # insert the assertion about the resolutions (attached to the responsible body)
    # in French
    for resolution in meeting_fr['resolutions']:
        resol_URI = None
        resol_hidden_label = None
        if resolution['type'] == 'resolution':
            resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Res" + str(resolution['identifier']))
            resol_hidden_label = "CIPM" + str(conf_Nr) + "-Res" + str(resolution['identifier'])
        elif resolution['type'] == 'declaration':
            if resolution['identifier'] == 0:
                resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Decl")
                resol_hidden_label = "CIPM" + str(conf_Nr) + "-Decl"
            else:
                resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Decl" + str(resolution['identifier']))
                resol_hidden_label = "CIPM" + str(conf_Nr) + "-Decl" + str(resolution['identifier'])
        elif resolution['type'] == 'recommendation':
            resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Rec" + str(resolution['identifier']))
            resol_hidden_label = "CIPM" + str(conf_Nr) + "-Recom" + str(resolution['identifier'])
        elif resolution['type'] == 'decision':
            resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Dec" + str(resolution['identifier']))
            resol_hidden_label = "CIPM" + str(conf_Nr) + "-Dec" + str(resolution['identifier'])
        
        resol_fr_DOI = resolution['url']
        resol_title_fr = resolution['title']
        resol_nr = resolution['identifier']

        PDF.g.add((cipm_URI, PDF.hasAdopted, resol_URI))
        PDF.g.add((resol_URI, PDF.wasAdoptedBy, cipm_URI))
        PDF.g.add((resol_URI, RDF.type, PDF.Outcome))
        PDF.g.add((conf_URI, PDF.hasOutcome, resol_URI))
        PDF.g.add((resol_URI, PDF.isOutcomeOf, conf_URI))
        PDF.g.add((resol_URI, PDF.hasOutcomeTitle, Literal(resol_title_fr, lang='fr')))
        PDF.g.add((resol_URI, PDF.hasOutcomeNr, Literal(resol_nr)))
        PDF.g.add((resol_URI, SKOS.hiddenLabel, Literal(resol_hidden_label, datatype=XSD.string)))
        PDF.g.add((resol_URI, PDF.hasDOI, Literal(resol_fr_DOI, lang='fr')))
        if resolution['considerations']:  # only include this if there are considerations
            considering_blankNodeID = URIRef(resol_URI + "Considering")  # Blank node holding the considerings
            PDF.g.add((resol_URI, PDF.hasConsidering, considering_blankNodeID))
            for consideration in resolution['considerations']:
                PDF.g.add(
                    (considering_blankNodeID, PDF.hasConsideringText, Literal(consideration['message'], lang='fr')))

        if resolution['actions']:  # only include this if there are actions
            actions_blankNodeID = URIRef(resol_URI + "Action")  # Blank node holding the actions
            PDF.g.add((resol_URI, PDF.hasAction, actions_blankNodeID))
            for action in resolution['actions']:
                PDF.g.add((actions_blankNodeID, PDF.hasActionText, Literal(action['message'], lang='fr')))

    # in English
    for resolution in meeting_en['resolutions']:
        resol_URI = None
        resol_hidden_label = None
        if resolution['type'] == 'resolution':
            resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Res" + str(resolution['identifier']))
            resol_hidden_label = "CIPM" + str(conf_Nr) + "-Res" + str(resolution['identifier'])
        elif resolution['type'] == 'declaration':
            if resolution['identifier'] == 0:
                resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Decl")
                resol_hidden_label = "CIPM" + str(conf_Nr) + "-Decl"
            else:
                resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Decl" + str(resolution['identifier']))
                resol_hidden_label = "CIPM" + str(conf_Nr) + "-Decl" + str(resolution['identifier'])
        elif resolution['type'] == 'recommendation':
            resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Rec" + str(resolution['identifier']))
            resol_hidden_label = "CIPM" + str(conf_Nr) + "-Recom" + str(resolution['identifier'])
        elif resolution['type'] == 'decision':
            resol_URI = URIRef(ResBod_ns + "CIPM" + str(conf_Nr) + "-Dec" + str(resolution['identifier']))
            resol_hidden_label = "CIPM" + str(conf_Nr) + "-Dec" + str(resolution['identifier'])

        resol_en_DOI = resolution['url']
        resol_title_en = resolution['title']
        considering_blankNodeID = URIRef(resol_URI + "Considering")
        actions_blankNodeID = URIRef(resol_URI + "Action")
        PDF.g.add((resol_URI, PDF.hasOutcomeTitle, Literal(resol_title_en, lang='en')))
        PDF.g.add((resol_URI, PDF.hasDOI, Literal(resol_en_DOI, lang='en')))
        if resolution['considerations']:  # only include this if there are considerations
            considering_blankNodeID = URIRef(resol_URI + "Considering")  # Blank node holding the considerings
            PDF.g.add((resol_URI, PDF.hasConsidering, considering_blankNodeID))
            for consideration in resolution['considerations']:
                PDF.g.add(
                    (considering_blankNodeID, PDF.hasConsideringText, Literal(consideration['message'], lang='en')))

        if resolution['actions']:  # only include this if there are actions
            actions_blankNodeID = URIRef(resol_URI + "Action")  # Blank node holding the actions
            PDF.g.add((resol_URI, PDF.hasAction, actions_blankNodeID))
            for action in resolution['actions']:
                PDF.g.add((actions_blankNodeID, PDF.hasActionText, Literal(action['message'], lang='en')))



# serialize the knowledge graph when all CIPMs are covered,         
PDF.g.serialize(format='turtle', destination=APIPATH + 'cipm.ttl')
