API for Semantic SI 
===================
Gregor Dudle, 02.05.2023

Quick intro
-----------
The following addresses are implemented (~ stands for the root address, including the port (8000) [localhost:8000/ or digital.extranet.bipm.org] )

"~/CGPM"
displays the titles of all CGPMs
- an optional parameter 'Year' aloows to search for a CGPM of a given year. If no CGPM took place the return is empty

Example:
"~/CGPM?Year=2014"                      returns the 25th CGPM (which took place in 2014)

"~/CGPM{Id}
displays the Resolutions of the {Id}th CGPM.

Example:
"~/CGPM26"                              returns all Resolutions of the 26th CGPM

"~/CGPM{Id}/Res{R_Id}
displays Resolution nr. {R_id} of the {Id}th CGPM

Example:
"~/CGPM26/Res1"                         returns the 1st Resolution of the 26th CGPM

"~/page/{keyword}"
dbpedia-like page
displays all predicates and objectifs of the {keyword}

Example
"~/page/ampere"                         returns all information regarding ampere
"~/page/nano"                           returns all informaiton regarding nano


"~/Quantities"
displays the kind of quantities (4-lettre-code, corresponding unit and the unit's symbol)
- an optional parameter 'Code' allows to search for a specific kind of quantity
- an optional parameter 'Language' allows to define the language of the response (en or fr)

Examples:
"~/Quantities"                           returns the full list of defined kind of quantities
"~/Quantities/?Code=ELRE"                returns the kind of quantity having the code "ELRE"


"~/SI/BaseUnits/"
displays the current definition of the Base Unit(s) 
- an optional parameter 'Symbol' allows to search a specific Definition. If the parameter
  'Symbol' is not used, all definitions are returned
- an optional parameter 'language' allows to select between 'en' and 'fr'
  If no language is indicated in the request, en is returned by default
  If the parameter language is used with another value, an exception is raised 
- an optional parameter 'date' allows to select the definition on a given date (format YYYY-MM-DD)
  If no date is indicated, the current date is used

Examples: 
"~/SI/BaseUnits/?Symbol=s"                 returns the definition of the second in english
"~/SI/BaseUnits/?=fr"                      returns all definitions of the Base Units
"~/SI/BaseUnits/?Symbol=A&language=fr"     returns the definiton of the Ampere in french
"~/SI/BaseUnits/?Symbol=A&date=2000-01-01" returns the definiton of the Ampere on 2000-01-01


"~/SI/Prefixes/"
displays the prefix(es) with their multiplication factor
- an optional parameter 'Symbol' allows to search a specific Prefix
- an optional parameter 'ScalingFactor' allows to search a specific Prefix
- if neither 'Symbol' nor 'ScalingFactor' are defined, all prefixes are returned
- if both 'Symbol' and 'ScalingFactor' are provided, an exception is raised (system overdetermined)

Examples:
"~/SI/Prefixes/"                           returns all prefixes with their scaling factor
"~/SI/Prefixes/?Symbol=p"                  returns the info about pico
"~/SI/Prefixes/?ScalingFactor=1000"        return the info about kilo
(some strange behaviour; positive exponents are written without the + sign [e.g. 1e12];
 0.1, 0.01, 0.001 do not give a correct response)


"~/SI/Units"
displays the unit (BaseUnit and SpecialNameUnits) and the Label (specifying the Quantity)
- an optional parameter 'Symbol' allows to search for a specific Unit
- an optional parameter 'Language' allows to define the language of the response (en or fr)

Examples:
"~/SI/Units"                             returns all units and their description
"~/SI/Units/?Symbol=F&Language=fr        returns the unit farad and its description in French

Remark on the input files
-------------------------
main.py reads several knowledge graphs,
- 'CGPM.ttl'
- 'Constants.ttl'
- 'Quantitis.ttl'
- 'UntisPrefixes.ttl' 
All must be stored in the same directory as 'main.py'

Remark on the output format
---------------------------
Previously, I had two APIs, one that return JSON and one that returns HTML(using Jinja2)
The two versions have now been merged to a single one. Before the return statement, the functions check the 
header of the call. If the header contains "accept application/json" it returns an array of JSON dictonnary,
otherwise it returns html together with an instruction to use a given template

Requirements
------------
Data:
The data is imported from two tt files in the same directory as main.py 
Filename                Python code to be run to produce the ttl file
........                ...................................
CGPM.ttl                CGPM/CGPM_ABox.py
Constants.ttl           Constants/Constants_ABox_xlsReader.py
Quantities.ttl          Quantities/Quantities_ABox.py
UnitsPrefixes.ttl       Units/Units_ABox.py


HTML-Templates:
'main.py' uses templates (Jinja2). They must be stored in a folder ./templates/
template-name           used by (web address)
BaseUnitsLayout.html    ~/SI/BaseUnits
CstLayout.html          ~/Constants
DbpediaLayout.html      ~/page/{keyword}
ParentLaout.html        (skeleton for all other layouts)
PrefixesLayout.html     ~/SI/Prefixes
QtyLayout.html          ~/Quantities
UnitLayout.html         ~/SI/Units

Server:
to launch the API service, use 'uvicorn main:app' in the terminal

Note1: to run this command, you must be in the directory of the 'main.py' app
Note2: to allow other devices on the same LAN  to access the Uvicorn server, the command must be complemented with --host=0.0.0.0 (otherwise the ports are not open for devices other than "localhost")


