#
# Prefixes ABox
#
#
# the module imports the Python script 'settings.py' located in a directory above this directory
# Should this lead to an error when executing the present script (... not found ...) you might need
# to add the location to the PYTHONPATH by typing (in the TERMINAL where you execute the Python script)
# export PYTHONPATH=(path where the package is located) (e.g. /Users/gregordudle/Development/Semantic-SI)
#

from rdflib import *
from CUQ_TBox import SiElements
from datetime import date
from settings import *
import openpyxl
import re

PDF = SiElements()
SIURL = SIURL + "SI"

# Annotations to the ontology (name, Version number)
PDF.g.add((URIRef(SIURL), RDF.type, OWL.Ontology))
PDF.g.add((URIRef(SIURL), SKOS.prefLabel, Literal("SI Reference Point - Units and Prefixes", datatype=XSD.string)))
PDF.g.add((URIRef(SIURL), RDFS.comment, Literal("Ontology, part of the SI Reference Point, covering measurement units "
                                                "(SI base units and SI units with special names) and prefixes.")))
PDF.g.add((URIRef(SIURL), DCTERMS.created, Literal(str(date.today()), datatype=XSD.date)))

# 1) open XLS files with information
units_wb_obj = openpyxl.load_workbook(XLS_FILES_FOLDER + 'units_prefixes.xlsx')
notes_wb_obj = openpyxl.load_workbook(XLS_FILES_FOLDER + 'notes.xlsx')

# 2) create dictionary with the note symbol codes (@xxx@) in text
notessym = notes_wb_obj["symbols"]
syms, symtypes, formats = {}, {}, {'html': 6, 'latex': 7, 'json': 8, 'text': 9}
for symrow in range(2, notessym.max_row + 1):
    symtypes.update({notessym.cell(symrow, column=5).value: notessym.cell(symrow, column=4).value})
    for ttype in ['latex']:
        if ttype not in syms.keys():
            syms.update({ttype: {}})
        code = notessym.cell(symrow, column=5).value
        text = notessym.cell(symrow, column=formats[ttype]).value
        syms[ttype].update({code: text})


# 3) Note function to change out symbol references in notes (@xxx@), uses syms and symtypes vars defined above
def formattxt(txt, fmt='html', lvl=0):
    """
    formats a text string with symbols replaced in any of the following formats
    html, latex, json, text
    """
    if fmt not in ['html', 'latex', 'json', 'text']:
        return txt

    matches = re.findall(f"@(.*?)@", txt)
    # order matches by length of substituting string (smallest first) so that replacement of substrings
    # at the top level does not result in multiple replacements at top level (resulting in $$)
    tmatches = {}
    for match in matches:
        strlen = len(syms[fmt][match])
        tmatches.update({match: strlen})
    omatches = dict(sorted(tmatches.items(), key=lambda item: item[1]))
    if omatches:
        for grp in omatches:
            if lvl == 0 and fmt == 'latex':
                # add latex delimiters at the top level
                if symtypes[grp] == 'symbol':
                    txt = txt.replace('@' + grp + '@', "$" + syms[fmt][grp] + "$")
                elif symtypes[grp] == 'equation':
                    txt = txt.replace('@' + grp + '@', "$$" + syms[fmt][grp] + "$$")
            else:
                txt = txt.replace('@' + grp + '@',  syms[fmt][grp])
        txt = txt.replace('\n', ' ')
        # check for text still containing symbols based on symbols being parts of other symbols
        if '@' in text:
            lvl = lvl+1
            txt = formattxt(txt, fmt, lvl)
    return txt


# 4) Create prefixes
sheet = units_wb_obj["Prefixes"]

for row in range(2, sheet.max_row + 1):
    uri_text = sheet.cell(row, column=1).value
    prefLabel_en = sheet.cell(row, column=2).value
    prefLabel_fr = sheet.cell(row, column=3).value
    scalingFactor = sheet.cell(row, column=4).value
    symbol = sheet.cell(row, column=5).value
    defres = sheet.cell(row, column=6).value

    if uri_text is not None:
        element = PDF.set_uri(uri_text)
        PDF.g.add((element, RDF.type, PDF.SIPrefix))
        PDF.g.add((element, SKOS.prefLabel, Literal(prefLabel_fr, lang='fr')))
        PDF.g.add((element, SKOS.prefLabel, Literal(prefLabel_en, lang='en')))
        PDF.g.add((element, PDF.hasScalingFactor, Literal(scalingFactor, datatype=XSD.integer)))
        PDF.g.add((element, PDF.hasDatatype, XSD.integer))
        PDF.g.add((element, PDF.hasSymbol, Literal(symbol, datatype=XSD.string)))
        PDF.g.add((element, PDF.hasDefiningResolution, URIRef(PDF.ResBod_ns + defres)))

# 5) Serialization prefixes
PDF.g.serialize(format='turtle', destination=APIPATH + 'prefixes.ttl')
