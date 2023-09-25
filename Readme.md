Semantic SI
===========
created: Jan 2023 / GD
last modified: 2023-07-25

This package implements the SI Reference point, a part of the SI digital framework. The package allows to produce a machine readable version of the SI Brochures (knowledge graph). 
A good entry point to understand the philosophy of the package is the Generation_TTL.pdf (showing the general principle for the generation of the knowledge graphs) SIDataModel.pdf (depicting the underlying data model used for this part of the si digital framework).
 
The package contains also a test Website (based on FastAPI), allowing to interrogate the produced knowledge graphs. Note that this is only provided for demo purposes. 

Short description of the sub directories

CUQ
---
The subfolder Python contains several Python codes that allow to produce 4 serialized knowledge graphs (as ttl) containing information about:
- the 7 constants underpinning the SI, 
- the Prefixes,
- the Quantities, 
- the Units.
The TBox (classes and properties) is common to all parts, the ABoxes (allowing to fill the knowledge graphs with individuals) are separate for the different parts. 
Each ABox gets the relevant information from an XLS file. The location of the input and output files is defined in settings.py

ResBod
------
Contains a Python code that allows to produce a serialized knowledge graph (as ttl file) of Responsible Bodies, their Events and the Outcomes thereof. 
For the moment, only information about the CGPM conferences (1,3 and 7 to 26 are present. Conferences 2, 4, 5, 6 and 27 are missing)
The information is read from yaml files (provided by Ron Tse). The code is separated in TBox (definition of the classes and properties) and ABox (istances using TBox)
The location of the input and output files is defined in settings.py

A summary of the input- and output-files together with the name of the graph producing engine (xxx_ABox.py) is given in the documentation.

Testing
-------
Contains a Python code that can be run under uvicorn to offer an API


Remark on usage of the package
------------------------------
For most users and use cases it will be sufficient to use the TTL files that are provided. The following instructions are only of interest for those who need (want) to re-generate one or several TTL file. 

To re-generate the TTL file, download the whole package to your local machine.
At the top level (in the folder "Semantic-SI") create a file 'localsettings.py' (not present in the distribution). This file should contain one line:
LOCALBASE = "/Users/gregordudle/Developments/"
where the right hand side of the equal sign points to the place where the package is installed.

Once this is fixed, you can run the *_ABox.py files, 
~/CUQ/Python/Constants_ABox.py
~/CUQ/Python/Prefixes_ABox.py
~/CUQ/Python/Quantities_ABox.py
~/CUQ/Python/Units_ABox.py
~/ResBod/Python/ResBod_ABox_CGPM.py
~/ResBod/Python/ResBod_ABox_CIPM.py




