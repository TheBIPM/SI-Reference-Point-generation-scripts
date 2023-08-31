Constants
==========
created: April 2023 / GD

Machine-readable reference to CGPM

Short description of the sub-directories

_docs
-----
contains general information for the CGPM ontology
It contains the yml sources (obtained from Ron Tse) 
Output from the Python code is stored here

Python
------
contains two Python codes for serealizing knowledge graphs of the Constants
- CGPM_ABox.py: fetches the information from a local yml file (fetching from GitHub does not yet work) at GitHub (Pascal's file). This file contains all CGPMs and their resolutions and produces a ttl file as serialization of the knowledge graph.
- CGPM_TBox.py: defines the classes and predicates that are used by CGPM_ABox.py