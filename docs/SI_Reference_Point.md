# The SI Reference Point

## 1. Scope

The [SI Reference Point](http://62.161.69.201:8080/SI) is a set of tools making the information of the SI Brochures available in machine-readable form, designed to provide an authoritative digital reference for the [International System of Units (SI)](https://www.bipm.org/measurement-units/). The present document provides a general overview for users, with a more detailed description of the Application Programming Interface (API) given in Annex 1, and some examples of SPARQL queries provided in Annex 2 for illustrative purposes.

The present document is structured as follows:
*	Section 2 shows the information covered by the SI Reference Point.
*	Section 3 shows the data model used to encode the information.
*	Section 4 briefly indicates how the information can be browsed.
*	Section 5 summarizes the next steps.
*	Annex 1 lists the Classes and Predicates in the data model

For a broader overview of the SI Digital Framework please see document BIPM-DIG-G01.

## 2. Information contained in the SI Reference Point

The SI Reference Point is based on five main pillars, or knowledge graphs:
1. **[SI/units](http://172.16.124.201:8080/SI/units)**
    * SI base units (Table 2 of [2])
    * SI derived units with special names (Table 4 of [2])
    * Non-SI units allowed for use with the SI (Table 8 of [2])
    * Compound units (the examples given in Tables 5 and 6 of [2] plus additional examples from the BIPM key comparison database (KCDB))
1. **[SI/prefixes](http://172.16.124.201:8080/SI/prefixes)**
    * SI prefixes (Table 7 of [2])
1. **[SI/decisions](http://172.16.124.201:8080/SI/decisions)**
    * Decisions relating to the SI, taken by the CGPM and CIPM  (Appendix 1 of [2])
1. **[Constants](http://172.16.124.201:8080/constants)**
    * Initially the 7 defining constants of the SI (Table 1 of [2])
1.	**[Quantities](http://172.16.124.201:8080/quantities)**
    * SI base quantities (Table 3 of [2])
    * Other example quantities (Tables 5 and 6 of [2])
    * Other quantities in the BIPM key comparison database (KCDB))
  
The SI/decisions information is presented in a stand-alone file, but interfaces with another component of the SI Digital Framework under development:

6. Responsible bodies
    * CGPM, CIPM, etc.

A tool is provided to allow for machine-encoding and interpretation of prefixed and other combined units (µm, m<sup>2</sup>, <nobr>m s<sup>-1</sup>, etc.).
  
**Table 1.** List of tables in the SI Brochure [2] and corresponding information in the SI Reference Point

| Table | Title | Encoded in|
| :----- | :----- | :---- |
| 1 |  The seven defining constants of the SI and the seven corresponding units they define  | constants |
| 2 | SI base units | SI/units |
| 3 |  Base quantities and dimensions  used in the SI | quantities |
| 4 |  The 22 SI units with special names and symbols | SI/units |
| 5 |  Examples of coherent derived units in the SI expressed in terms of base units | SI/units |
| 6 |  Examples of SI coherent derived units whose names and symbols include SI coherent derived units with special names and symbol | SI/units |
| 7 |  SI prefixes | SI/prefixes|
| 8 |  Non-SI units accepted for use with the SI units | SI/units |
| <nobr>Annex 1</nobr> |  Decisions of the CGPM and the CIPM | SI/decisions |


## 3. Data model

The information contained in the nine editions of the SI Brochure has been encoded semantically and made publicly available on the internet at:

[si-digital-framework.org/SI](http://62.161.69.201:8080/SI) 


Figure 1 and Figure 2 show the data models developed for this purpose. Figure 1 shows the part covering measurement units.

```mermaid
classDiagram
    MeasurementUnit <|-- SIBaseUnit
    MeasurementUnit <|-- SISpecialNamedUnit
    MeasurementUnit <|-- CompoundUnit
    CompoundUnit <|-- PrefixedUnit
    CompoundUnit <|-- UnitProduct
    CompoundUnit <|-- UnitPower
    class PrefixedUnit{
      +hasNonPrefixedUnit
      +hasPrefix
    }
```

The data model (classes and predicates) for prefixes:

![image](https://github.com/TheBIPM/SI-Reference-Point-2023/assets/105931640/0713ac62-74e2-4ccb-bf5f-dd0b8c4a2e43)



## 4. Browsing the knowledge graphs

### General

The set of knowledge graphs are presented in the form of TTL files, which can be browsed by different means as outlined below. As they are interlinked, the five TTL files should be available together for parsing by the chosen application. The information can then be displayed and exploited according to the services offered by the application.

Following standard practice, the TTL files are divided between “T-boxes” (specifying the data model at the “SI” level, for example) and “A-boxes” (specifying the data entries at the “units”, “prefixes” and “decisions” levels).


![image](https://github.com/TheBIPM/SI-Reference-Point-2023/assets/105931640/00292ef7-f8dc-4a9b-b20e-2c0f5fed141a)


### Application Programming Interface (API)

The web interface at https://si-digital-framework.org/SI is designed to simplify access to the knowledge graphs for a human reader. Underpinning the web pages are a set of pre-programmed calls to the TTL files, such as (expressed as words rather than data requests) “list all the SI units”, “list all the SI prefixes”, “what is the current definition of the metre”, etc. 

The same pre-programmed queries (API calls) are documented in the Swagger interface at
[https://si-digital-framework.org/api-docs/swagger-ui](https://si-digital-framework.org/api-docs/swagger-ui)

Select the service `SI REFERENCE POINT` from the drop-down menu at the top right of the screen.

![image](https://github.com/TheBIPM/SI-Reference-Point-2023/assets/105931640/c1d4a392-aaf0-4da7-8916-2c597ceb3d88)

The responses will be given according to the header information, which can be modified manually from a Command Line Interface if desired. For example: 
* `-H ‘accept:application/json’`	will return JSON code
* `-H ‘accept:application/xml’`	will return XML code
* `-H ‘accept:application/octet-stream’`	will return the response without change of format (i.e. in TTL)
 

### SPARQL endpoint

The TTL files can also be interrogated directly either using the [SPARQL interface](http://62.161.69.201:8080/SI/query?lang=en) provided or via a human-friendly tool such as GraphDB. 

![image](https://github.com/TheBIPM/SI-Reference-Point-2023/assets/105931640/db59e808-d34d-4fb6-9ee0-6bcdcc236bb4)

* Download the (free) GraphDB Desktop software [6] and install it on your computer.
* Create a new repository, e.g. MMDD-SI Ref
* Download the TTL files from the SI Reference Point and upload them into GraphDB. Ensure the “Autocomplete” function is selected and import the files to the following locations:
    * SI/units
    * SI/prefixes
    * SI/decisions
    * constants
    * quantities

GraphDB provides a visual graph interface.

The Classes and Predicates are listed in Annex 1.


## 5. Next steps

This beta version of the SI Reference Point is open for comment, but it is hoped that the PIDs given here for the units defined in the SI can now be inserted into existing systems for representing units (such as QUDT, UnitsML, etc.), and used in other services under development. 

The list of kinds of quantity will gradually be extended to cover all the quantities included in the BIPM key comparison database (KCDB). 

To increase interoperability, authoritative external digital references for the listed quantities should be built in (such as from the the [e-ILV](https://cie.co.at/e-ilv), the [IEV](https://electropedia.org/), and the [IUPAC Gold Book](https://goldbook.iupac.org/). Currently this has been done for just a few of the quantities, as examples. The ongoing task to identify appropriate external references for the quantities will be carried out in collaboration with the subject experts in the CIPM’s Consultative Committees.


### Acknowlegements

This project was undertaken as part of the BIPM's Work Programme in Digital Transformation, with contributions from seconding NMIs.

Janet Miles (Head of Digital Transformation, BIPM) thanks in particular the following people, listed alphabetically, who all made invaluable contributions:

* Amin Ben Abdallah
* Stuart Chalk (UNF)
* Gregor Dudle (METAS, now OST)
* Maximilian Gruber (PTB)
* Jean-Laurent Hippolyte (NPL)
* Frédéric Meynadier (BIPM)


## Annex 1:	List of Classes and Predicates

The Python script MakeVocabulary.py produces a full list of classes contained in the knowledge graphs
* SI/units.ttl
* SI/prefixes.ttl
* SI/decisions.ttl
* constants.ttl
* quantities.ttl
 
The list is TAB separated and sorted by Class.


