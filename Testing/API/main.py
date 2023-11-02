#############################################################################
#
# SI Reference Point 
# to launch the service, type the following line in a Terminal
# uvicorn main_html:app --reload
#
# This app returns html pages (using Jinja2Templates)
#
# Based on a tutorial found at: http://www.youtube.com/watch?v=SORiTsvnU28
# 
# to start the API server use: uvicorn main:app --host=0.0.0.0 
#  (the --host=0.0.0.0 ensures that the server can be reached from the same network)
#
# G. Dudle/ 16.02.2023
# ATTENTION: apparently this code requires at least Python 3.11 (Type issue)
# 
#
from typing import List
from pathlib import Path
from rdflib import Graph

from fastapi import FastAPI, APIRouter, HTTPException, Request  # , Header, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from datetime import date, datetime
from settings import *
import re

BASE_PATH = PROJECTBASE + "Testing/API/"

TEMPLATES = Jinja2Templates(directory=str(BASE_PATH + "templates"))

app = FastAPI(title="API Semantic SI", openapi_url="/openapi.json")

app.mount("/static", StaticFiles(directory=Path(BASE_PATH, 'static')), name="static")

templates = Jinja2Templates(directory="templates")

api_router = APIRouter()

# ----------------------------------------------------------------------------------------
# setup section
#
# load ttl files into knowledge graph
g = Graph()
g.parse(APIPATH + '/units.ttl')
g.parse(APIPATH + '/prefixes.ttl')
g.parse(APIPATH + '/quantities.ttl')
g.parse(APIPATH + '/constants.ttl')
g.parse(APIPATH + '/cgpm.ttl')

# reasoner (used e.g. to infer "?Conf CGPM:adopted ?Res" is equivalent to "?Res CGPM:wasAdoptedBy ?Conf")
# owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)

# list of the possible parameters of the API call
param_list_base_unit_grps = ["lang"]
param_list_base_units = ["lang", "datestr"]
param_list_named_units = ["lang"]
param_list_named_unit = ["lang"]
param_list_prefixes = ["sym", "factor"]
param_list_quantities = ["lang"]
param_list_constants = ["name", "lang"]
param_list_lang = ['en', 'fr']

# produce dictionaries of symbol:units / symobol:prefix_name / symbol:prefix_scaling
# unit_list_dict
units_query = """
            PREFIX si: <http://si-digital-framework.org/SI#>
            SELECT ?Unit ?Symbol 
            WHERE
            {
                {?Unit a si:SISpecialNamedUnit }
                UNION
                {?Unit a si:SIBaseUnit } 
                UNION
                {?Unit a si:nonSIUnit}
                ?Unit si:hasSymbol ?Symbol
            } 
            """

# run SPARQL query for units
units = g.query(units_query)
unit_list_dict = dict()

for unit in units:
    unit_list_dict[str(unit['Symbol'])] = unit['Unit']

# prefix_list_dict / scaling_list_dict
fixquery = """
            PREFIX si: <http://si-digital-framework.org/SI#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
            SELECT ?Prefix ?PrefixLabel ?Symbol ?ScalingFactor
            WHERE
            {
                ?Prefix a si:SIPrefix ;
                        skos:prefLabel ?PrefixLabel ;
                        si:hasScalingFactor ?ScalingFactor ;
                        si:hasSymbol ?Symbol
            } 
            """

# run SPARQL query for prefixes
fixes = g.query(fixquery)
prefix_list_dict = dict()
scaling_list_dict = dict()

for fix in fixes:
    prefix_list_dict[str(fix['Symbol'])] = fix['Prefix']
    scaling_list_dict[str(fix['Symbol'])] = fix['ScalingFactor']


# ----------------------------------------------------------------------------------------
# function definitions
#


# get the name of a unit based on the symbol
def get_unit_name(sym: str, lang: str | None = 'en'):
    unit_query = """
            PREFIX si: <http://si-digital-framework.org/SI#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
            SELECT ?Unit ?Label
            WHERE
            {
                {?Unit a si:SISpecialNamedUnit }
                UNION
                {?Unit a si:SIBaseUnit }
                UNION
                {?Unit a si:nonSIUnit}
                ?Unit skos:prefLabel ?Label .
                ?Unit si:hasSymbol ?Symbol . 
                FILTER (?Symbol='""" + sym + """') .
                FILTER (langmatches(lang(?Label),'""" + lang + """'))}"""

    # run SPARQL query for units
    ures = g.query(unit_query)
    for element in ures:
        return element['Label']


# get the name of a prefix base on a symbol
def get_prefix_name(sym: str):
    prefix_query = """
            PREFIX si: <http://si-digital-framework.org/SI#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
            SELECT ?Prefix ?Label
            WHERE
            {
                ?Prefix a si:SIPrefix .
                ?Prefix skos:prefLabel ?Label .
                ?Prefix si:hasSymbol ?Symbol . 
                FILTER (?Symbol='""" + sym + """')}"""

    # run SPARQL query for units
    pres = g.query(prefix_query)
    for element in pres:
        return element['Label']


# get the URI of a unit based on the symbol
def get_unit_uri(symbol: str):
    return unit_list_dict[symbol]


# get the URI of a prefix based on the symbol
def get_prefix_uri(symbol: str):
    return prefix_list_dict[symbol]


# get the scaling factor of a prefix with symbol
def get_scalingfactor(symbol: str) -> float:
    return scaling_list_dict[symbol]


# ----------------------------------------------------------------------------------------
# parser of prefixed unit 
def prefixedunit(unit_element: str):
    dictionary = {}

    if unit_element[-1:].isnumeric():
        unit_str = unit_element[:-2]
        unit_pwr = int(unit_element[-2:])
    else:
        unit_str = unit_element
        unit_pwr = 1

    expo = "" if unit_pwr == 1 else "^" + str(unit_pwr)

    if unit_str[-1:] == "g":
        if unit_str == "kg":
            dictionary['unit_URI'] = get_unit_uri("kg")
            dictionary['unit_symbol'] = "kg"
            dictionary['prefix_name'] = ""
            dictionary['unit_name'] = "kilogram"
            dictionary.update({'scaling': 1})

        else:
            if unit_str == "g":
                dictionary['unit_symbol'] = "kg"
                dictionary['unit_URI'] = get_unit_uri("kg")
                dictionary['unit_name'] = "kilogram"
                dictionary['scaling'] = 0.001 ** abs(unit_pwr)
                dictionary['relation'] = "1 g" + expo + " = " + str(dictionary['scaling']) + " kg" + expo

            # case "g" with a prefix ≠ k
            else:
                if unit_str[0] in prefix_list_dict.keys():
                    dictionary['prefix_symbol'] = unit_str[0]
                    dictionary['unit_URI'] = get_unit_uri("kg")
                    dictionary['unit_symbol'] = "g"
                    dictionary['unit_name'] = "gram"
                    dictionary['unit_url'] = BASE_URL + "si-unit/kg"
                    dictionary['prefix_URI'] = get_prefix_uri(unit_str[0])
                    dictionary['prefix_name'] = str(get_prefix_name(unit_str[0]))
                    dictionary['prefix_url'] = BASE_URL + "si-prefix/" + dictionary['prefix_name']
                    dictionary['scaling'] = str((float(get_scalingfactor(unit_str[0])) / 1000) ** abs(unit_pwr))
                    dictionary['relation'] = "1 " + unit_str + expo + " = " + dictionary['scaling'] + " kg" + expo

                else:
                    raise HTTPException(
                        status_code=404,
                        detail=f"No information available. Make sure the prefixes and units are correct")
    else:
        # last character not g
        if unit_str in unit_list_dict.keys():
            dictionary['unit_symbol'] = unit_str
            dictionary['unit_URI'] = get_unit_uri(unit_str)
            dictionary['unit_name'] = get_unit_name(unit_str)
            dictionary['unit_url'] = BASE_URL + "si-unit/" + dictionary['unit_name']
            dictionary['scaling'] = 1

        else:
            remains = unit_str[1:]

            if (unit_str[0] in prefix_list_dict.keys()) and (remains in unit_list_dict.keys()):
                dictionary['prefix_symbol'] = unit_str[0]
                dictionary['prefix_URI'] = get_prefix_uri(unit_str[0])
                dictionary['prefix_name'] = str(get_prefix_name(unit_str[0]))
                dictionary['prefix_url'] = BASE_URL + "si-prefix/" + dictionary['prefix_name']
                dictionary['unit_symbol'] = remains
                dictionary['unit_name'] = get_unit_name(remains)
                dictionary['unit_URI'] = get_unit_uri(remains)
                dictionary['unit_url'] = BASE_URL + "si-unit/" + dictionary['unit_name']
                dictionary['scaling'] = str(float(get_scalingfactor(unit_str[0])) ** abs(unit_pwr))
                dictionary['relation'] = "1 " + unit_str + expo + " = " + dictionary['scaling'] + " " + dictionary[
                    'unit_symbol'] + expo

            else:
                raise HTTPException(
                    status_code=404,
                    detail=f"No information available. Make sure the prefixes and units are correct")

    return dictionary


# ----------------------------------------------------------------------------------------
# API endpoints
#


# ----------------------------------------------------------------------------------------
@app.get("/")
def landing_page(request: Request):
    return TEMPLATES.TemplateResponse(
        "ParentLayout.html",
        {"request": request})


# ----------------------------------------------------------------------------------------
@app.get("/cgpm")
def displ_cgpms(request: Request, lang: str | None = 'en'):
    # 20230710_datamodel_event_ok
    knows_query = """
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX si: <http://si-digital-framework.org/SI#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX rb: <http://si-digital-framework.org/ResBod#>
    

    SELECT ?CGPM_title ?Identifier ?Conf_date 
    WHERE {
        ?Conf a rb:Event ;
              skos:prefLabel ?CGPM_title ;
              rb:hasEventNr ?Identifier ;
              rb:hasEventDate ?Conf_date .
        BIND(year(?Conf_date) as ?Jahr) .
        FILTER (langmatches(lang(?CGPM_title),'""" + lang + """')).
    }
    ORDER by ?Identifier
    """

    qres = g.query(knows_query)
    responses = []

    for element in qres:
        year = element['Conf_date'][:4]
        responses.append({
            'Title': element['CGPM_title'],
            'Year': year,
            'Link': BASE_URL + "cgpm/" + element['Identifier'],
            "Lang": lang
        }
        )

    if not responses:
        raise HTTPException(
            status_code=404, detail=f"No conference found.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'Conferences': responses}
    else:
        return TEMPLATES.TemplateResponse(
            "ConfsLayout.html",
            {"request": request, "Conferences": responses, "language": lang}
        )


# ----------------------------------------------------------------------------------------
@app.get("/cgpm/{confid}")
def displ_cgpm(request: Request, confid: int | None = None, lang: str | None = 'en'):
    # 20230710_datamodel_event_ok

    years = [1889, 1901, 1927, 1933, 1948, 1954, 1960, 1964, 1967, 1971, 1975,
             1979, 1983, 1987, 1991, 1995, 1999, 2003, 2007, 2011, 2014, 2018, 2022]
    nums = [1, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    if confid in years:
        fstr = "FILTER (YEAR(?Conf_date)=" + str(confid) + ")."
    elif confid in nums:
        fstr = "FILTER (?Identifier=" + str(confid) + ")."
    elif confid is not None:
        return RedirectResponse("/CGPM")
    else:
        raise HTTPException(
            status_code=404, detail=f"Should be list of conferences...")
        # fstr = ""

    knows_query = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rb: <http://si-digital-framework.org/ResBod#>

        SELECT ?Event_title ?Conf ?Identifier ?Event_date
        WHERE {
            ?Conf a rb:Event ;
                skos:prefLabel ?Event_title ;
                rb:hasEventNr ?Identifier ;
                rb:hasEventDate ?Event_date .
            FILTER (langmatches(lang(?Event_title),'""" + lang + """')).
            """ + fstr + """
        }
        ORDER by ?Identifier
        """
    qres = g.query(knows_query)
    responses = []

    for element in qres:
        res_query = """
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX si: <http://si-digital-framework.org/SI#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX rb: <http://si-digital-framework.org/ResBod#>

            SELECT ?Event_title ?Event_date ?Outcome_Nr ?Outcome_title ?Outcome_DOI
            WHERE {
                ?ResBod a rb:ResBod ;
                        rb:hasEvent ?Event .
                ?Event 	rb:hasOutcome ?Outcome ;
                        rb:hasEventNr ?Identifier ;
                        skos:prefLabel ?Event_title ;
                        rb:hasEventDate ?Event_date .
                ?Outcome rb:hasOutcomeNr ?Outcome_Nr ;
                        rb:hasOutcomeTitle ?Outcome_title ;
                        rb:hasDOI ?Outcome_DOI .
            FILTER(langmatches(lang(?Outcome_title),'""" + lang + """')) .
            FILTER(langmatches(lang(?Outcome_DOI),'""" + lang + """')) .
            FILTER(langmatches(lang(?Event_title),'""" + lang + """')) .
            """ + fstr + """
            }
            ORDER by ?Outcome_Nr
        """

        resolutions = g.query(res_query)
        res_list = []
        for resolution in resolutions:
            res_list.append({'Nr': resolution['Outcome_Nr'], 'Title': resolution['Outcome_title'],
                             'Res_Link': resolution['Outcome_DOI']})
        responses.append(
            {
                'Title': element['Event_title'],
                'Date': element['Event_date'],
                'Resolutions': res_list
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404, detail=f"No conference found.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'Conferences': responses}
    else:
        return TEMPLATES.TemplateResponse(
            "ConfLayout.html",
            {"request": request, "Conferences": responses, "language": lang}
        )


# ----------------------------------------------------------------------------------------
# noinspection DuplicatedCode
@app.get("/constants/")
def displ_constants(request: Request, lang: str | None = 'en'):
    """ endpoint to get the full list of defining constants """

    # check params
    for param in request.query_params:
        if param not in param_list_constants:
            error_msg = "Parameter " + param + " unknown. Allowed parameter: "
            for allowed_para in param_list_constants:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(
                status_code=404, detail=error_msg)

    # check language
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    # SPARQL query to get all the information about all defining constants
    constants_query = """
        SELECT ?unit ?constant ?res ?sym ?ustr ?date ?nval ?sval ?dtype ?label ?eDOI ?fDOI ?eText ?fText
        WHERE {
            ?constant	rdf:type si:Constant ;
                        si:hasDefiningResolution ?res ;
                        si:hasSymbol ?sym ;
                        si:hasUnitAsString ?ustr ;
                        si:hasUpdatedDate ?date ;
                        si:hasValue ?nval ;
                        si:hasValueAsString ?sval ;
                        si:hasDatatype ?dtype ;
                        skos:hiddenLabel ?label ;
                        skos:prefLabel ?eText ;
                        skos:prefLabel ?fText .
            ?unit		si:hasDefiningConstant ?constant ;
                        si:hasStatus ?status .
            ?res        rb:hasDOI ?eDOI ;
                        rb:hasDOI ?fDOI .
            FILTER (?status = "current")
            FILTER (lang(?eDOI) = "en")
            FILTER (lang(?fDOI) = "fr")
            FILTER (lang(?eText) = "en")
            FILTER (lang(?fText) = "fr")
        }
    """

    # run SPARQL query
    consset = g.query(constants_query)

    # check for data
    if not consset:
        raise HTTPException(
            status_code=404, detail=f"No constants data found.")

    # generate output
    baseurl = "http://si-digital-framework.org"
    consurl = baseurl + '/constants/'
    siurl = baseurl + '/SI#'
    xsdurl = 'http://www.w3.org/2001/XMLSchema#'

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'constants': consset.bindings}
    elif accept == 'application/ld+json':
        # create context
        ctx = ["https://stuchalk.github.io/scidata/contexts/si.jsonld",
               {"si": siurl,
                "constants": consurl,
                'xsd': xsdurl},
               {"@base": consurl}]
        jld = {"@context": ctx, "@id": consurl, "@type": "si:Constant"}
        cons = []
        for constant in consset:
            name = constant['constant'].replace(consurl, 'constants:')
            con = {"@id": name, "@type": "si:Constant"}
            con.update({"name_en": constant['eText']})
            con.update({"name_fr": constant['fText']})
            con.update({"symbol": constant['sym']})
            # needed to correctly display numeric value
            dtype = constant['dtype'].replace(xsdurl, 'xsd:')
            if dtype == 'xsd:integer':
                con.update({'value': int(constant['nval'])})
            elif dtype == 'xsd:float':
                con.update({'value': float(constant['nval'])})
            con.update({"value_str": constant['sval']})
            con.update({'datatype': dtype})
            con.update({"unit": constant['ustr']})
            con.update({'defining_resolution_en': constant['eDOI']})
            con.update({'defining_resolution_fr': constant['fDOI']})
            unit = constant['unit'].replace(siurl, 'si:')
            con.update({'defines': unit})
            cons.append(con)
        jld.update({"constants": cons})
        return jld
    else:
        return TEMPLATES.TemplateResponse(
            "ConstantsLayout.html",
            {"request": request, "cons": consset, "lang": lang}
        )


# ----------------------------------------------------------------------------------------
@app.get("/constant/{name}/")
def displ_constant(request: Request, name: str | None = None, lang: str | None = 'en'):
    for param in request.query_params:
        if param not in param_list_constants:
            error_msg = "Parameter " + param + " unknown. Allowed parameter: "
            for allowed_para in param_list_constants:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(
                status_code=404, detail=error_msg)
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    knows_query = """
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX si: <http://si-digital-framework.org/SI#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

            SELECT ?Label ?Value ?Unit ?Unitstr ?Updated ?Valuestr ?Symbol ?Hidden ?Type
            WHERE { 
                ?SIBaseUnit si:hasDefiningConstant ?Constant .
                ?Constant skos:prefLabel ?Label ;
                    skos:hiddenLabel ?Hidden ;
                    si:hasValueAsString ?Valuestr ;
                    si:hasUnitAsString ?Unitstr ;
                    si:hasUpdatedDate ?Updated ;
                    si:hasDatatype ?Type ;
                    si:hasValue ?Value ;
                    si:hasUnitElement ?list ;
                    si:hasSymbol ?Symbol .
                ?list rdf:_1 ?el1 .
                ?el1 si:hasUnit ?u1 ;
                     si:hasUnitPwr ?p1.
                     ?u1 si:hasSymbol ?sym1 .
                     BIND(IF(?p1=1, str(?sym1), CONCAT(str(?sym1),"<sup>",str(?p1),'</sup>')) AS ?u1Str)

                OPTIONAl {
                    ?list rdf:_2 ?el2 .
                    ?el2 si:hasUnit ?u2 ;
                        si:hasUnitPwr ?p2.
                        ?u2 si:hasSymbol ?sym2 .
                        BIND(IF(?p2=1, str(?sym2), CONCAT(str(?sym2),"<sup>",str(?p2),'</sup>')) AS ?u2Str)
                }
                
                FILTER (langmatches(lang(?Label),'""" + lang + """')) .
                FILTER (?Hidden='""" + name + """') .
                BIND(IF(EXISTS {?list rdf:_2 ?el }, CONCAT(?u1Str, " ", ?u2Str ), ?u1Str) AS ?Unit)
            }
        """
    qres = g.query(knows_query)
    response: dict = {}
    for element in qres:  # using iteration even though only unit returned...
        response.update(
            {
                'Cst_Label': element['Label'],
                'Cst_Symbol': element['Symbol'],
                'Cst_Value': element['Value'],
                'Cst_Valuestr': element['Valuestr'],
                'Cst_Date': element['Updated'],
                'Cst_Unit': element['Unit'],
                'Cst_Unitstr': element['Unitstr'],
                'Cst_Hidden': element['Hidden'],
                'Cst_Datatype': element['Type']
            }
        )

    if not response:
        raise HTTPException(
            status_code=404, detail=f"No Constant found.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'constant': response}
    elif accept == 'application/ld+json':
        resp = response
        # create url
        url = 'https://si-digital-framework.org/constant/' + resp['Cst_Hidden']
        # create context
        ctx = ["https://stuchalk.github.io/scidata/contexts/constants.jsonld",
               {"si": "http://si-digital-framework.org/SI/sio.owl"},
               {"@base": url}]
        # # populate graph
        gph = {"@id": url, "@type": "si:Constant"}
        gph.update({"name": resp['Cst_Label']})
        gph.update({"symbol": resp['Cst_Symbol']})
        gph.update({"value": resp['Cst_Value']})
        gph.update({"valuestr": resp['Cst_Valuestr']})
        gph.update({"datatype": resp['Cst_Datatype']})
        gph.update({"unit": resp['Cst_Unit']})
        gph.update({"unitstr": resp['Cst_Unitstr']})
        gph.update({"url": url})
        gph.update({"lastupdated": resp['Cst_Date']})

        # build JSON-LD
        jld = {
            "@context": ctx, "@id": url,
            "generatedAt": str(datetime.now()), "version": 1, "@graph": gph}
        return jld
    else:
        return TEMPLATES.TemplateResponse(
            "ConstantLayout.html",
            {"request": request, "constant": response}
        )


@app.get("/baseunit/{unitname}")
def displ_baseunitdefinition(request: Request, unitname: str | None = None, lang: str | None = 'en',
                             datestr: str | None = str(date.today())):
    # 20230710_datamodel_event_ok
    for param in request.query_params:
        if param not in param_list_base_unit_grps:
            error_msg = "Parameter " + param + " unknown. Allowed parameters: "
            for allowed_para in param_list_base_units:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(status_code=404, detail=error_msg)

    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language not available {lang}")

    # these are the names of the units in the ttl file, language specific not needed here
    allowed = ['ampere', 'metre', 'kilogram', 'second', 'mole', 'candela', 'kelvin', 'arcminute', 'arcsecond', 'dalton',
               'astronomicalunit', 'day', 'degree', 'electronvolt', 'hour', 'litre', 'minute', 'tonne', 'becquerel',
               'coulomb', 'degreeCelsius', 'farad', 'gray', 'henry', 'hertz', 'joule', 'katal', 'lumen', 'lux',
               'newton', 'ohm', 'pascal', 'radian', 'siemens', 'sievert', 'steradian', 'tesla', 'volt', 'watt', 'weber']

    if unitname not in allowed:
        raise HTTPException(
            status_code=404, detail=f"No acceptable SI unit with name '{unitname}'.")

    # SPARQL query to get the general information about a unit of measurement
    unit_query = """
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX units: <http://si-digital-framework.org/SI/units/>
        
        SELECT ?Unit ?sym ?quant ?defns ?eLabel ?fLabel ?unitType
        WHERE {
            ?Unit	rdf:type ?unitType ;
                    si:isUnitOfQtyKind ?quant ;
                    skos:prefLabel ?eLabel ;
                    skos:prefLabel ?fLabel ;
                    si:hasSymbol ?sym .
            FILTER (lang(?eLabel) = "en").
            FILTER (lang(?fLabel) = "fr") .
            FILTER (?unitType IN (si:SIBaseUnit, si:nonSIUnit, si:SISpecialNamedUnit)) .
            FILTER (?Unit=units:""" + unitname + """) .
        }
    """

    unitset = g.query(unit_query)

    # organize data
    response: dict = {}
    baseurl = "http://si-digital-framework.org/SI"
    uniturl = baseurl + '/units/' + unitname
    unitdata = {}
    for row in unitset:
        if str(row['eLabel']) == unitname:
            unitdata = row

    # SPARQL query to get definitions
    defns_query = """
            PREFIX si: <http://si-digital-framework.org/SI#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX units: <http://si-digital-framework.org/SI/units/>

            SELECT ?UnitDefn ?res ?status ?vfrom ?vtill ?next ?notes 
                    ?eLabel ?fLabel ?const ?eqn ?eDOI ?fDOI ?eText ?fText
            WHERE {
                units:""" + unitname + """ si:hasDefinition ?UnitDefn .
                ?UnitDefn	rdf:type si:Definition ;
                            si:hasStatus ?status ;
                            si:hasStartValidity ?vfrom ;
                            si:hasDefiningResolution ?res ;
                            si:hasDefiningText ?eText ;
                            si:hasDefiningText ?fText ;
                            skos:prefLabel ?eLabel ;
                            skos:prefLabel ?fLabel .
                ?res    rb:hasDOI ?eDOI ;
                        rb:hasDOI ?fDOI .
                OPTIONAL {?UnitDefn si:hasEndValidity ?vtill .}
                OPTIONAL {?UnitDefn si:hasNextDefinition ?next .}
                OPTIONAL {?UnitDefn si:hasDefiningConstant ?const .}
                OPTIONAL {?UnitDefn si:hasDefiningEquation ?eqn .}
                FILTER (lang(?eLabel) = "en")
                FILTER (lang(?eText) = "en")
                FILTER (lang(?eDOI) = "en")
                FILTER (lang(?fLabel) = "fr")
                FILTER (lang(?fText) = "fr")
                FILTER (lang(?fDOI) = "fr")
        }
        """

    #  output
    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'unit': unitdata}
    elif accept == 'application/ld+json':
        resp = unitdata
        # create context
        ctx = ["https://stuchalk.github.io/scidata/contexts/si.jsonld",
               {"si": baseurl + "#"},
               {"@base": uniturl}]
        # # populate graph
        utype = resp['unitType'].replace(baseurl + '#', 'si:'),
        gph = {"@context": ctx, "@id": uniturl, "@type": utype}
        gph.update({"name_en": resp['eLabel']})
        gph.update({"name_fr": resp['fLabel']})
        gph.update({"symbol": resp['sym']})
        gph.update({"quantity": resp['quant']})

        # add definitions
        defns = g.query(defns_query)
        defs = []
        for defn in defns:
            dfn = {}
            dfn.update({'@id': defn['UnitDefn'], '@type': 'si:Definition'})
            dfn.update({'status': defn['status']})
            dfn.update({'label_en': defn['eLabel']})
            dfn.update({'label_fr': defn['fLabel']})
            dfn.update({"definition_en": defn['eText']})
            dfn.update({"definition_fr": defn['fText']})
            dfn.update({'defining_resolution_en': defn['eDOI']})
            dfn.update({'defining_resolution_fr': defn['fDOI']})
            dfn.update({'valid_from': defn['vfrom']})
            if defn['vtill']:
                dfn.update({'valid_till': defn['vtill']})
            if defn['const']:
                dfn.update({'defining_constant': defn['const']})
            if defn['eqn']:
                dfn.update({'defining_equation': defn['eqn'].replace("\\\\", "\\")})
            if defn['next']:
                dfn.update({'next_definition': defn['next']})

            # search for and add notes
            defnname = defn['UnitDefn'].replace(baseurl + '#', '')
            notes_query = """
                PREFIX si: <http://si-digital-framework.org/SI#>
                SELECT ?note ?index ?eText ?fText
                WHERE {
                    si:""" + defnname + """	si:hasDefinitionNote ?note .
                    ?note 			        si:hasNoteIndex ?index ;
                                            si:hasNoteText ?eText ;
                                            si:hasNoteText ?fText ;
                    FILTER (lang(?eText) = "en")
                    FILTER (lang(?fText) = "fr")
                }
            """

            # add notes
            notes = g.query(notes_query)
            ntes = []
            for note in notes:
                nte = {}
                nte.update({'@id': note['note'], '@type': 'si:DefinitionNote'})
                nte.update({'noteindex': note['index']})
                nte.update({'notetext_en': note['eText']})
                nte.update({'notetext_fr': note['fText']})
                ntes.append(nte)
            dfn.update({'notes': ntes})

            defs.append(dfn)
        gph.update({'definitions': defs})

        # build JSON-LD
        # jld = {"@context": ctx, "@id": uniturl, "generatedAt": str(datetime.now()), "version": 1, "@graph": gph}
        return gph
    else:
        return TEMPLATES.TemplateResponse(
            "BaseUnitLayout.html",
            {"request": request, "units": response, "language": lang}
        )


# ----------------------------------------------------------------------------------------
@app.get("/si-baseunit/{baseunitid}")
def displ_baseunitdefinition(request: Request, baseunitid: str | None = None, lang: str | None = 'en',
                             datestr: str | None = str(date.today())):
    # 20230710_datamodel_event_ok
    for param in request.query_params:
        if param not in param_list_base_units:
            error_msg = "Parameter " + param + " unknown. Allowed parameters: "
            for allowed_para in param_list_base_units:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(status_code=404, detail=error_msg)

    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language not available {lang}")

    knows_query = """
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX si: <http://si-digital-framework.org/SI#>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    PREFIX rb: <http://si-digital-framework.org/ResBod#>

                    SELECT DISTINCT ?Symbol ?Label ?Q_Label ?Q_Code ?DefiningText ?DefiningResolution
                        ?StartValidity ?EndValidity ?Equation ?Constant ?Cst_Label ?Cst_Hidden ?ConfNr ?ResNr ?Res_DOI
                    WHERE 
                    { 
                        VALUES ?datum {'""" + datestr + """'^^xsd:date} .
                        ?SIBaseUnit a si:SIBaseUnit ;
                            si:hasSymbol ?Symbol ;
                            skos:prefLabel ?Label .
                        FILTER (langmatches(lang(?Label),'""" + lang + """')) .
                        
                        ?SIBaseUnit si:hasDefinition ?Definition .
                        ?Definition si:hasDefiningText ?DefiningText .
                        FILTER (langmatches(lang(?DefiningText),'""" + lang + """')) .
                        
                        
                        OPTIONAL {?SIBaseUnit si:isUnitOfQtyKind ?QtyKind .}
                        OPTIONAL {?QtyKind skos:prefLabel ?Q_Label ;
                                           skos:altLabel ?Q_Code .
                                FILTER (langmatches(lang(?Q_Label),'""" + lang + """'))}.
                        
                        OPTIONAL {?Definition si:hasDefiningConstant ?Constant .
                                  ?Constant skos:prefLabel ?Cst_Label ;
                                            skos:hiddenLabel ?Cst_Hidden .
                                  FILTER (langmatches(lang(?Cst_Label),'""" + lang + """'))} .

                        ?Definition si:hasStartValidity ?StartValidity .
                        OPTIONAL {?Definition si:hasEndValidity ?EndValidity} .
                        FILTER (((?StartValidity <= ?datum) && !BOUND(?EndValidity)) || 
                                ((?StartValidity <= ?datum) && (?EndValidity >= ?datum))). 
                        
                        ?Definition si:hasDefiningResolution ?DefiningResolution .
                        OPTIONAL {?Definition si:hasDefinitionNote ?Note .
                                   ?Note    si:hasNoteIndex ?NoteIndex;
                                            si:hasNoteText ?NoteText .
                                  FILTER (langmatches(lang(?NoteText),'""" + lang + """')) .
                        
                                }
                        ?Conf rb:hasOutcome ?DefiningResolution ;
                              rb:hasEventNr ?ConfNr .
                        ?DefiningResolution rb:hasOutcomeNr ?ResNr ;
                                            rb:hasDOI ?Res_DOI .
                        FILTER (langmatches(lang(?Res_DOI),'""" + lang + """')) 
                        
                        OPTIONAL {?Definition si:hasDefiningEquation ?Equation} .}"""
    if len(baseunitid) < 4:
        knows_query = knows_query[:-1] + """FILTER (?Symbol='""" + baseunitid + """') .}"""
    else:
        knows_query = knows_query[:-1] + """FILTER (?Label='""" + baseunitid + """'@""" + lang + """) .}"""

    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Label': element['Label'],
                'Symbol': element['Symbol'],
                'StartValidity': element['StartValidity'],
                'EndValidity': element['EndValidity'],
                'Definition': element['DefiningText'],
                'Q_Label': element['Q_Label'],
                'Q_Link': BASE_URL + "quantity/" + element['Q_Code'],
                'DefiningResolution': "CGPM" + str(element['ConfNr']) + "-Res" + str(element['ResNr']),
                'Res_Link': element['Res_DOI'],
                'Equation': element['Equation'],
                'Cst_Label': element['Cst_Label'],
                'Cst_Link': None if element['Cst_Hidden'] is None else BASE_URL + "constant/" + element['Cst_Hidden']
            }
        )

    notes_query = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rb: <http://si-digital-framework.org/ResBod#>

        SELECT DISTINCT ?NoteIndex ?NoteText           
            WHERE 
                { 
                    VALUES ?datum {'""" + datestr + """'^^xsd:date} .
                    ?SIBaseUnit a si:SIBaseUnit ;
                        si:hasSymbol ?Symbol ;
                        skos:prefLabel ?Label .
                    FILTER (langmatches(lang(?Label),'""" + lang + """')) .
                        
                    ?SIBaseUnit si:hasDefinition ?Definition .

                    ?Definition si:hasStartValidity ?StartValidity .
                    OPTIONAL {?Definition si:hasEndValidity ?EndValidity} .
                    FILTER (((?StartValidity <= ?datum) && !BOUND(?EndValidity)) || 
                            ((?StartValidity <= ?datum) && (?EndValidity >= ?datum))). 
                        
                    OPTIONAL {?Definition si:hasDefinitionNote ?Note .
                            ?Note    si:hasNoteIndex ?NoteIndex;
                                     si:hasNoteText ?NoteText .
                            FILTER (langmatches(lang(?NoteText),'""" + lang + """')) .
                }
                """

    if len(baseunitid) < 4:
        notes_query = notes_query[:-1] + """FILTER (?Symbol='""" + baseunitid + """') .}"""
    else:
        notes_query = notes_query[:-1] + """FILTER (?Label='""" + baseunitid + """'@""" + lang + """) .}"""

    nres = g.query(notes_query)
    nresponses: List[dict] = []

    for element in nres:
        nresponses.append(
            {
                'index': element['NoteIndex'],
                'text': element['NoteText']
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404, detail=f"No Base Unit with Symbol {baseunitid}.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}
    elif accept == 'application/ld+json':
        resp = responses[0]
        # create context
        ctx = ["https://stuchalk.github.io/scidata/contexts/si.jsonld",
               {"si": "http://si-digital-framework.org/SI/sio.owl"},
               {"@base": "http://si-digital-framework.org/SI/ampere"}]
        # add notes
        notes = []
        for nresponse in nresponses:
            note = {"@id": "note/" + str(nresponse['index']) + "/", "@type": "si:DefinitionNote"}
            note.update({"notetext": nresponse['text']})
            notes.append(note)
        # # populate graph
        gph = {"@id": "http://si-digital-framework.org/SI/" + resp['Label'], "@type": "si:SIBaseUnit"}
        gph.update({"name": resp['Label']})
        gph.update({"symbol": resp['Symbol']})
        gph.update({"startvaliditydate": resp['StartValidity']})
        gph.update({"endvaliditydate": resp['EndValidity']})
        gph.update({"definition": resp['Definition']})
        gph.update({"quantity": resp['Q_Label']})
        gph.update({"equation": resp['Equation']})
        gph.update({"resolution_defn": resp['DefiningResolution']})
        gph.update({"resolution_url": resp['Res_Link']})
        gph.update({"notes": notes})

        # build JSON-LD
        jld = {
            "@context": ctx, "@id": "http://si-digital-framework.org/SI/" + resp['Label'],
            "generatedAt": str(datetime.now()), "version": 1, "@graph": gph}
        return jld
    else:
        return TEMPLATES.TemplateResponse(
            "BaseUnitLayout.html",
            {"request": request, "units": responses, "notes": nresponses, "language": lang}
        )


# ----------------------------------------------------------------------------------------
@app.get("/si-baseunits/")
def displ_baseunitsdefinitions(request: Request, sym: str | None = None, lang: str | None = 'en',
                               datestr: str | None = str(date.today())):
    # 20230710_datamodel_event_ok
    for param in request.query_params:
        if param not in param_list_base_units:
            error_msg = "Parameter " + param + " unknown. Allowed parameters: "
            for allowed_para in param_list_base_units:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(status_code=404, detail=error_msg)

    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language not available {lang}")

    knows_query = """
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX si: <http://si-digital-framework.org/SI#>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    PREFIX rb: <http://si-digital-framework.org/ResBod#>

                    SELECT DISTINCT ?Symbol ?Label ?Q_Label ?Q_Code ?DefiningText ?DefiningResolution ?NoteText
                        ?StartValidity ?EndValidity ?Equation ?Constant ?Cst_Label ?Cst_Hidden ?ConfNr ?ResNr ?Res_DOI
                    WHERE 
                    { 
                        VALUES ?datum {'""" + datestr + """'^^xsd:date} .
                        ?SIBaseUnit a si:SIBaseUnit ;
                            si:hasSymbol ?Symbol ;
                            skos:prefLabel ?Label .
                        FILTER (langmatches(lang(?Label),'""" + lang + """')) .
                        
                        ?SIBaseUnit si:hasDefinition ?Definition .
                        ?Definition si:hasDefiningText ?DefiningText .
                        FILTER (langmatches(lang(?DefiningText),'""" + lang + """')) .
                        
                        OPTIONAL {
                            ?SIBaseUnit si:hasDefinitionNote ?Note .
                            ?Note si:hasNoteIndex ?NoteIndex .
                            ?Note si:hasNoteText ?NoteText .
                            FILTER (?NoteIndex = 1) .
                        }
                        
                        OPTIONAL {?SIBaseUnit si:isUnitOfQtyKind ?QtyKind .}
                        OPTIONAL {?QtyKind skos:prefLabel ?Q_Label ;
                                           skos:altLabel ?Q_Code .
                                FILTER (langmatches(lang(?Q_Label),'""" + lang + """'))}.
                        
                        OPTIONAL {?Definition si:hasDefiningConstant ?Constant .
                                  ?Constant skos:prefLabel ?Cst_Label ;
                                            skos:hiddenLabel ?Cst_Hidden .
                                  FILTER (langmatches(lang(?Cst_Label),'""" + lang + """'))} .

                        ?Definition si:hasStartValidity ?StartValidity .
                        OPTIONAL {?Definition si:hasEndValidity ?EndValidity} .
                        FILTER (((?StartValidity <= ?datum) && !BOUND(?EndValidity)) || 
                                ((?StartValidity <= ?datum) && (?EndValidity >= ?datum))). 
                        
                        ?Definition si:hasDefiningResolution ?DefiningResolution .
                        ?Conf rb:hasOutcome ?DefiningResolution ;
                              rb:hasEventNr ?ConfNr .
                        ?DefiningResolution rb:hasOutcomeNr ?ResNr ;
                                            rb:hasDOI ?Res_DOI .
                        FILTER (langmatches(lang(?Res_DOI),'""" + lang + """')) 
                        
                        OPTIONAL {?Definition si:hasDefiningEquation ?Equation} .}"""
    if sym is not None:
        knows_query = knows_query[:-1] + """FILTER (?Symbol='""" + sym + """') .}"""

    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Label': element['Label'],
                'Symbol': element['Symbol'],
                'StartValidity': element['StartValidity'],
                'EndValidit?y': element['EndValidity'],
                'Definition': element['DefiningText'],
                'Q_Label': element['Q_Label'],
                'Q_Link': BASE_URL + "quantity/" + element['Q_Code'],
                'DefiningResolution': "CGPM" + str(element['ConfNr']) + "-Res" + str(element['ResNr']),
                'Res_Link': element['Res_DOI'],
                'Equation': element['Equation'],
                'Note': element['NoteText'],
                'Cst_Label': element['Cst_Label'],
                'Cst_Link': None if element['Cst_Hidden'] is None else BASE_URL + "constant/" + element['Cst_Hidden']
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404, detail=f"No Base Unit with Symbol {sym}.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}

    else:
        return TEMPLATES.TemplateResponse(
            "BaseUnitsLayout.html",
            {"request": request, "units": responses, "language": lang}
        )


# ----------------------------------------------------------------------------------------
# displays ALL SI units, i.e. SI Units with special names AND SI Base Units
@app.get("/si-units/")
def displ_units(request: Request, sym: str | None = None, lang: str | None = 'en'):
    for param in request.query_params:
        if param not in param_list_named_units:
            error_msg = "Parameter " + param + " unknown. Allowed parameter(s): "
            for allowed_para in param_list_named_units:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(
                status_code=404, detail=error_msg)
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    knows_query = """
                    PREFIX si: <http://si-digital-framework.org/SI#>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    SELECT DISTINCT ?Symbol ?Label ?Description ?Q_Label ?Q_Code
                    WHERE { 
                        {?Unit a si:SIBaseUnit}   
                        UNION
                        {?Unit a si:SISpecialNamedUnit}
                        ?Unit si:hasSymbol ?Symbol ;
                                    skos:prefLabel ?Label ;
                                    si:isUnitOfQtyKind ?QtyKind .
                            ?QtyKind skos:prefLabel ?Q_Label ;
                                     skos:altLabel ?Q_Code .
                            FILTER (langmatches(lang(?Label),'""" + lang + """')) .
                            FILTER (langmatches(lang(?Q_Label),'""" + lang + """')) .
                    } ORDER BY ASC (?Label)
                    """

    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Name': element['Label'],
                'Symbol': element['Symbol'],
                'Label': element['Label'],
                'Q_Label': element['Q_Label'],
                'Q_Link': BASE_URL + "quantity/" + element['Q_Code'],
                'N_Link': BASE_URL + "page/" + element['Label'],
                'C_Link': BASE_URL + "si-unit/" + element['Symbol']
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404, detail=f"No Unit with Symbol {sym}.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}
    else:
        return TEMPLATES.TemplateResponse(
            "NamedUnitsLayout.html",
            {"request": request, "units": responses, "language": lang}
        )


# ----------------------------------------------------------------------------------------
# selects from ALL SI units, i.e. SI Units with special names AND SI Base Units
@app.get("/si-unit/{sym}")
def displ_unit(request: Request, sym: str | None = None, lang: str | None = 'en'):
    for param in request.query_params:
        if param not in param_list_named_unit:
            error_msg = "Parameter " + param + " unknown. Allowed parameter(s): "
            for allowed_para in param_list_named_unit:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(
                status_code=404, detail=error_msg)
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    knows_query = """
                    PREFIX si: <http://si-digital-framework.org/SI#>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    SELECT DISTINCT ?Symbol ?Label ?Description ?Q_Label ?Q_Code
                    WHERE { 
                            {?Unit a si:SIBaseUnit}   
                            UNION
                            {?Unit a si:SISpecialNamedUnit}
                            ?Unit si:hasSymbol ?Symbol ;
                                    skos:prefLabel ?Label ;
                                    si:isUnitOfQtyKind ?QtyKind .
                            ?QtyKind skos:prefLabel ?Q_Label ;
                                     skos:altLabel ?Q_Code .
                            FILTER (langmatches(lang(?Label),'""" + lang + """')) .
                            FILTER (langmatches(lang(?Q_Label),'""" + lang + """')) .}"""

    if len(sym) < 4:
        knows_query = knows_query[:-1] + """FILTER (?Symbol='""" + sym + """') .}"""
    else:
        knows_query = knows_query[:-1] + """FILTER (?Label='""" + sym.lower() + """'@""" + lang + """) .}"""

    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Name': element['Label'],
                'Symbol': element['Symbol'],
                'Label': element['Label'],
                'Q_Label': element['Q_Label'],
                'Q_Link': BASE_URL + "quantity/" + element['Q_Code'],
                'N_Link': BASE_URL + "page/" + element['Label']
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404, detail=f"No Unit with Symbol or Name {sym}.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}
    else:
        return TEMPLATES.TemplateResponse(
            "NamedUnitLayout.html",
            {"request": request, "units": responses, "language": lang}
        )


# ----------------------------------------------------------------------------------------
@app.get("/si-prefix/{sym}")
def displ_prefix(request: Request, sym: str | None = None):
    for param in request.query_params:
        if param not in param_list_prefixes:
            error_msg = "Parameter " + param + " unkonwn. Allowed parameter: "
            for allowed_para in param_list_prefixes:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(
                status_code=404, detail=error_msg)

    knows_query = """
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT ?Label ?PrefixSymbol ?ScalingFactor
        WHERE
        {
            ?SIPrefix a si:SIPrefix;
                      si:hasSymbol ?PrefixSymbol ;
                      skos:prefLabel ?Label ;
                      si:hasScalingFactor ?ScalingFactor .}"""

    if len(sym) > 1:
        knows_query = knows_query[:-1] + """FILTER (?Label='""" + sym.lower() + """')} """
    else:
        knows_query = knows_query[:-1] + """FILTER (?PrefixSymbol='""" + sym + """')} """
    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Label': element['Label'],
                'Symbol': element['PrefixSymbol'],
                'ScalingFactor': element['ScalingFactor']
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404, detail=f"No prefix for Symbol {sym}.")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'prefixes': responses}

    else:
        return TEMPLATES.TemplateResponse(
            "PrefixesLayout.html",
            {"request": request, "prefixes": responses}
        )


# ----------------------------------------------------------------------------------------
@app.get("/SI/prefixes/")
def displ_prefixes(request: Request):
    """ endpoint to get the full list of SI prefixes """

    # SPARQL query to get all the information about all defining constants
    fixes_query = """
        PREFIX rb: <http://si-digital-framework.org/bodies#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        SELECT ?fix ?factor ?type ?sym ?res ?eDOI ?fDOI ?eText ?fText
        WHERE {
            ?fix 	rdf:type si:SIPrefix ;
                    si:hasScalingFactor ?factor ;
                    si:hasDatatype ?type ;
                    si:hasSymbol ?sym ;
                    si:hasDefiningResolution ?res ;
                    skos:prefLabel ?eText ;
                    skos:prefLabel ?fText .
            ?res	rb:hasDOI ?eDOI ;
                    rb:hasDOI ?fDOI .
            FILTER (lang(?eDOI) = "en")
            FILTER (lang(?fDOI) = "fr")
            FILTER (lang(?eText) = "en")
            FILTER (lang(?fText) = "fr")
        }
        ORDER BY DESC(?factor)
    """

    # run SPARQL query
    fixset = g.query(fixes_query)

    # check for data
    if not fixset:
        raise HTTPException(
            status_code=404, detail=f"SPARQL query not working?.")

    # generate output
    baseurl = "http://si-digital-framework.org"
    fixesurl = baseurl + '/SI/prefixes/'
    siurl = baseurl + '/SI#'
    xsdurl = 'http://www.w3.org/2001/XMLSchema#'

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'prefixes': fixset.bindings}
    elif accept == 'application/ld+json':
        # create context
        ctx = ["https://stuchalk.github.io/scidata/contexts/si.jsonld",
               {"si": siurl,
                "prefixes": fixesurl,
                "xsd": xsdurl},
               {"@base": fixesurl}]
        jld = {"@context": ctx, "@id": fixesurl, "@type": "si:Prefix"}
        fixes = []
        for prefix in fixset:
            name = prefix['fix'].replace(fixesurl, 'prefixes:')
            fix = {"@id": name, "@type": "si:Prefix"}
            fix.update({"name_en": prefix['eText']})
            fix.update({"name_fr": prefix['fText']})
            fix.update({'symbol': prefix['sym']})
            # needed to correctly display factor as numeric value in JSON
            f = float(prefix['factor'])
            if 1 < f < 1E+18:
                fix.update({'factor': int(f)})
            else:
                fix.update({'factor': f})
            dtype = prefix['type'].replace(xsdurl, 'xsd:')
            fix.update({'datatype': dtype})
            fix.update({'resolution_en': prefix['eDOI']})
            fix.update({'resolution_fr': prefix['fDOI']})
            fixes.append(fix)
        jld.update({"prefixes": fixes})
        return jld
    else:
        return TEMPLATES.TemplateResponse(
            "PrefixesLayout.html",
            {"request": request, "prefixes": fixset}
        )


# ----------------------------------------------------------------------------------------
@app.get("/si/{combined}")
def displ_comb_unit(request: Request, combined: str):
    c_unit = combined.split(".")
    responses = []
    titel = ""
    for element in c_unit:
        answer = prefixedunit(element)
        prefunitdict = dict()
        for label in answer.keys():
            prefunitdict[label] = answer[label]
        responses.append(prefunitdict)
        if element[-1:].isnumeric():
            titel = titel + element[:-2]
            titel = titel + "$^{" + element[-2:] + "}$ "
        else:
            titel = titel + element + " "

    if not responses:
        raise HTTPException(
            status_code=404,
            detail=f"No information available. Make sure the prefixes and units are correct")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}

    else:
        return TEMPLATES.TemplateResponse(
            "siLayout.html",
            {"request": request, "units": responses, "title": titel}
        )


# ----------------------------------------------------------------------------------------
@app.get("/non-si-units/")
def displ_nonsiunits(request: Request, lang: str | None = 'en'):
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    knows_query = """
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT DISTINCT ?Symbol ?Label ?Q_Label ?Q_Code ?Factor ?SIUnitSymbol
        WHERE { 
                ?Unit a si:nonSIUnit .
                ?Unit si:hasSymbol ?Symbol ;
                        skos:prefLabel ?Label ;
                        si:isUnitOfQtyKind ?QtyKind;
                        si:hasConversionFactor ?Factor;
                        si:hasConversionUnit ?SIUnit.
                ?SIUnit si:hasSymbol ?SIUnitSymbol.
                ?QtyKind skos:prefLabel ?Q_Label ;
                            skos:altLabel ?Q_Code .
                FILTER(langmatches(lang(?Label),'""" + lang + """')) .
                FILTER (langmatches(lang(?Q_Label),'""" + lang + """')) .}"""

    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Name': element['Label'],
                'Symbol': element['Symbol'],
                'Label': element['Label'],
                'Factor': element['Factor'],
                'SIUnitSymbol': element['SIUnitSymbol'],
                'Q_Label': element['Q_Label'],
                'Q_Link': BASE_URL + "quantity/" + element['Q_Code'],
                'U_Link': BASE_URL + "non-si-unit/" + element['Label']
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404,
            detail=f"No non-SI unit found")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}

    else:
        return TEMPLATES.TemplateResponse(
            "NonSILayout.html",
            {"request": request, "units": responses}
        )


# ----------------------------------------------------------------------------------------
@app.get("/non-si-unit/{identifier}")
def displ_nonsiunit(request: Request, identifier: str, lang: str | None = 'en'):
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    knows_query = """
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT DISTINCT ?Symbol ?Label ?Q_Label ?Q_Code ?Factor ?SIUnitSymbol
        WHERE { 
                VALUES ?identifier {'""" + identifier + """'@""" + lang + """}
                ?Unit a si:nonSIUnit .
                ?Unit si:hasSymbol ?Symbol ;
                        skos:prefLabel ?Label ;
                        si:isUnitOfQtyKind ?QtyKind ;
                        si:hasConversionFactor ?Factor;
                        si:hasConversionUnit ?SIUnit.
                ?SIUnit si:hasSymbol ?SIUnitSymbol.
                ?QtyKind skos:prefLabel ?Q_Label ;
                            skos:altLabel ?Q_Code .
                FILTER(?Label =?identifier) .
                FILTER (langmatches(lang(?Q_Label),'""" + lang + """')) .}"""

    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Name': element['Label'],
                'Symbol': element['Symbol'],
                'Factor': element['Factor'],
                'SIUnitSymbol': element['SIUnitSymbol'],
                'Label': element['Label'],
                'Q_Label': element['Q_Label'],
                'Q_Link': BASE_URL + "quantity/" + element['Q_Code'],
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404,
            detail=f"No non-SI unit found")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}

    else:
        return TEMPLATES.TemplateResponse(
            "NonSILayout.html",
            {"request": request, "units": responses}
        )


# ----------------------------------------------------------------------------------------
@app.get("/quantities/")
def displ_quants(request: Request, lang: str | None = 'en'):
    """ generate a list of the quantities referenced in the SI brochure"""

    # check the language is allowed
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    # SPARQL query to get all the information about quantities and related SI allowed units
    quants_query = """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX si: <http://si-digital-framework.org/SI#>
        
        SELECT ?quant ?code ?unit ?usym ?eText ?fText
        WHERE {
            ?quant 	rdf:type si:QuantityKind ;
                    skos:altLabel ?code ;
                    skos:prefLabel ?eText ;
                    skos:prefLabel ?fText .
            ?unit	si:isUnitOfQtyKind ?quant ;
                    si:hasSymbol ?usym.
            FILTER (lang(?eText) = "en")
            FILTER (lang(?fText) = "fr")
        }
        ORDER BY ASC(?eText)
    """

    # run SPARQL query
    quantset = g.query(quants_query)

    # check for data
    if not quantset:
        raise HTTPException(
            status_code=404,
            detail=f"No Quantity corresponding to the request (Language = {lang}).")

    # generate output
    baseurl = "http://si-digital-framework.org"
    quantsurl = baseurl + '/quantities/'
    unitsurl = baseurl + '/SI/units/'

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'quantities': quantset.bindings}
    elif accept == 'application/ld+json':
        # preprocess units as some quantities have more than one
        units = {}
        for q in quantset:
            if q['code'] not in units.keys():
                units.update({q['code']: []})
            u = q['unit'].replace(unitsurl, "units:")
            units[q['code']].append(u)
        # create context
        ctx = ["https://stuchalk.github.io/scidata/contexts/quantities.jsonld",
               {"si": "http://si-digital-framework.org/SI/sio.owl"},
               {"@base": quantsurl}]
        jld = {"@context": ctx, "@id": quantsurl, "@type": "si:QuantityKind"}
        quants = []
        for quant in quantset:
            # check if this is the quantity with the first unit in units[quant.code], if not ignore
            u = quant['unit'].replace(unitsurl, "units:")
            if u == units[quant['code']][0]:
                name = quant['quant'].replace(quantsurl, "quantities:")
                qty = {"@id": name, "@type":"siQuantityKind"}
                qty.update({"name_en": quant['eText']})
                qty.update({"name_fr": quant['fText']})
                qty.update({'code': quant['code']})
                qty.update({'siunits': units[quant.code]})
                quants.append(qty)
        jld.update({"quantities": quants})
        return jld
    else:
        return TEMPLATES.TemplateResponse(
            "QtyLayout.html",
            {"request": request, "quants": quantset, "language": lang}
        )


# ----------------------------------------------------------------------------------------
@app.get("/quantity/{code}")
def displ_quant(request: Request, code: str | None = None, lang: str | None = 'en'):
    for param in request.query_params:
        if param not in param_list_quantities:
            error_msg = "Parameter " + param + " unkonwn. Allowed parameter: "
            for allowed_para in param_list_quantities:
                error_msg += allowed_para + ", "
            error_msg = error_msg[:-2]
            raise HTTPException(
                status_code=404, detail=error_msg)
    if lang not in param_list_lang:
        raise HTTPException(
            status_code=404, detail=f"Requested language unknown {lang}")

    # the SPARQL query below could be written without UNION and rely on inferences
    # (owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g))
    # 'SIBaseUnits' and 'SIUnitSpecialName' are both 'MeasurementUnits'.
    knows_query = """
                PREFIX si: <http://si-digital-framework.org/SI#>
                PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                SELECT DISTINCT ?Q_Label ?U_Label ?Symbol ?Code
                WHERE {
                        {?Unit a si:SIBaseUnit}   
                        UNION
                        {?Unit a si:SISpecialNamedUnit}
                        ?Quantity a si:QuantityKind ;
                                    skos:altLabel ?Code ;
                                    skos:prefLabel ?Q_Label ;
                                    si:hasUnit ?Unit.	
                        ?Unit si:hasSymbol ?Symbol ;
                                skos:prefLabel ?U_Label.
                        FILTER (langmatches(lang(?Q_Label),'""" + lang + """')) .
                        FILTER (langmatches(lang(?U_Label),'""" + lang + """')) . 
                    }"""
    if code is not None:
        knows_query = knows_query[:-1] + """FILTER (?Code='""" + code + """')}"""

    qres = g.query(knows_query)

    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                'Q_Label': element['Q_Label'],
                'Code': element['Code'],
                'U_Label': element['U_Label'],
                'Symbol': element['Symbol'],
                'Link': BASE_URL + "si-unit/" + element['Symbol']
            }
        )

    if not responses:
        raise HTTPException(
            status_code=404,
            detail=f"no Quantity  corresponding to the request (Code = {code} and Language = {lang}).")

    accept = request.headers.get("Accept")
    if not accept or accept == "application/json":
        return {'units': responses}

    else:
        return TEMPLATES.TemplateResponse(
            "QtyLayout.html",
            {"request": request, "units": responses, "language": lang}
        )


# ----------------------------------------------------------------------------------------
@app.get("/page/{word}")
def dbpedia_page(request: Request, word: str):
    # CHECKED DATAMODEL 20230512
    knows_query = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX si: <http://si-digital-framework.org/SI#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT DISTINCT ?p ?o
        WHERE {
            {?s (skos:prefLabel | skos:hiddenLabel | skos:altLabel) ?word .
                ?s ?p ?o .
                VALUES ?word {'""" + word + """'@en '""" + word + """'@fr '""" + word + """'^^xsd:string}
            }       
        }       
    """
    qres = g.query(knows_query)
    responses: List[dict] = []

    for element in qres:
        responses.append(
            {
                # the property .n3(g.namespace_manager) allows to display the identifiers using the PREFIXES
                'URI': element['p'].n3(g.namespace_manager),
                'object': element['o'].n3(g.namespace_manager)
            }
        )

    return TEMPLATES.TemplateResponse(
        "DbpediaLayout.html",
        {"request": request, "title": word, "teile": responses}
    )
