# API for Semantic SI
Gregor Dudle, 02.05.2023

## Quick intro
The following endpoints are implemented at http://localhost:8000 .

### "http://localhost:8000/CGPM"
Displays the titles of all CGPM meetings
- an optional parameter 'Year' allows to search for a CGPM of a given year. If no CGPM took place the return is empty

**Example**:
- "http://localhost:8000/CGPM?Year=2014" returns the 25th CGPM (which took place in 2014)

### "http://localhost:8000/CGPM{Id}
Displays the Resolutions of the {Id}th CGPM meeting.

**Example**:
- "http://localhost:8000/CGPM26" returns all Resolutions of the 26th CGPM

### "http://localhost:8000/CGPM{Id}/Res{R_Id}
Displays Resolution nr. {R_id} of the {Id}th CGPM meeting.

**Example**:
- "http://localhost:8000/CGPM26/Res1" returns the 1st Resolution of the 26th CGPM

### "http://localhost:8000/page/{keyword}"
DBpedia-like page. Displays all predicates and objectifs of the {keyword}

**Examples**:
- "http://localhost:8000/page/ampere" returns all information regarding the unit ampere
- "http://localhost:8000/page/nano" returns all information regarding the prefix nano

### "http://localhost:8000/Quantities"
Displays the kind of quantities (4-letter-code, corresponding unit and the unit's symbol)
- an optional parameter 'Code' allows to search for a specific kind of quantity
- an optional parameter 'Language' allows to define the language of the response (en or fr)

**Examples**:
- "http://localhost:8000/Quantities" returns the full list of defined kind of quantities
- "http://localhost:8000/Quantities/?Code=ELRE" returns the kind of quantity having the code "ELRE"

### "http://localhost:8000/SI/BaseUnits/"
Displays the current definition of the SI Base Unit(s) .
- an optional parameter 'Symbol' allows to search a specific Definition. If the parameter 'Symbol' is not used, 
  all definitions are returned
- an optional parameter 'language' allows to select between 'en' and 'fr'. If no language is indicated in the request, 
  'en' is returned by default. If the parameter language is used with another value, an exception is raised.
- an optional parameter 'date' allows to select the definition on a given date (format YYYY-MM-DD), If no date is 
  indicated, the current date is used

**Examples**: 
- "http://localhost:8000/SI/BaseUnits/?Symbol=s" returns the definition of the second in English
- "http://localhost:8000/SI/BaseUnits/?=fr" returns all definitions of the Base Units
- "http://localhost:8000/SI/BaseUnits/?Symbol=A&language=fr" returns the definiton of the Ampere in French
- "http://localhost:8000/SI/BaseUnits/?Symbol=A&date=2000-01-01" returns the definiton of the Ampere on 2000-01-01

### "http://localhost:8000/SI/Prefixes/"
Displays the prefix(es) with their multiplication factor
- an optional parameter 'Symbol' allows to search a specific Prefix
- an optional parameter 'ScalingFactor' allows to search a specific Prefix
- if neither 'Symbol' nor 'ScalingFactor' are defined, all prefixes are returned
- if both 'Symbol' and 'ScalingFactor' are provided, an exception is raised (system overdetermined)

**Examples**:
- "http://localhost:8000/SI/Prefixes/" returns all prefixes with their scaling factor
- "http://localhost:8000/SI/Prefixes/?Symbol=p" returns the info about the 'pico' prefix
- "http://localhost:8000/SI/Prefixes/?ScalingFactor=1000" return the info about the 'kilo' prefix
(some strange behaviour; positive exponents are written without the + sign [e.g. 1e12];
 0.1, 0.01, 0.001 do not give a correct response)

### "http://localhost:8000/SI/Units"
displays the unit (BaseUnit and SpecialNameUnits) and the Label (specifying the Quantity)
- an optional parameter 'Symbol' allows to search for a specific Unit
- an optional parameter 'Language' allows to define the language of the response ('en' or 'fr')

**Examples**:
- "http://localhost:8000/SI/Units" returns all units and their description
- "http://localhost:8000/SI/Units/?Symbol=F&Language=fr returns the unit farad and its description in French

## Input files
main.py reads several knowledge graphs,
- 'CGPM.ttl'
- 'Constants.ttl'
- 'Quantities.ttl'
- 'UnitsPrefixes.ttl'
All must be stored in the same directory as 'main.py'

## Output formats
If the header of the API call contains "accept application/json" it returns an array of JSON dictionary,
otherwise it returns HTML together with an instruction to use a given template.

## API Requirements

### Data:
The data is imported from four ttl files in the same directory as main.py 
Filename                Python code to be run to produce the ttl file
........                ...................................
CGPM.ttl                CGPM/CGPM_ABox.py
Constants.ttl           Constants/Constants_ABox_xlsReader.py
Quantities.ttl          Quantities/Quantities_ABox.py
UnitsPrefixes.ttl       Units/Units_ABox.py


### HTML-Templates:
'main.py' uses templates (Jinja2). They must be stored in a folder ./templates/
template-name           used by (web address)
BaseUnitsLayout.html    http://localhost:8000/SI/BaseUnits
CstLayout.html          http://localhost:8000/Constants
DbpediaLayout.html      http://localhost:8000/page/{keyword}
ParentLayout.html        (skeleton for all other layouts)
PrefixesLayout.html     http://localhost:8000/SI/Prefixes
QtyLayout.html          http://localhost:8000/Quantities
UnitLayout.html         http://localhost:8000/SI/Units

## Server:
To launch the API service, use 'uvicorn main:app' in the terminal 
1. To run this command, you must be in the directory of the 'main.py' app
2. to allow other devices on the same LAN  to access the Uvicorn server, the command must be complemented with 
   --host=0.0.0.0 (otherwise the ports are not open for devices other than "localhost")
