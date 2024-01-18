# The SI Reference Point

## Scope

The [SI Reference Point](http://62.161.69.201:8080/SI) is a set of tools making the information of the SI Brochures available in machine-readable form, designed to provide an authoritative digital reference for the [International System of Units (SI)](https://www.bipm.org/measurement-units/). The present document provides a general overview for users, with a more detailed description of the Application Programming Interface (API) given in Annex 1, and some examples of SPARQL queries provided in Annex 2 for illustrative purposes.

The present document is structured as follows:
*	Section 2 shows the information covered by the SI Reference Point.
*	Section 3 shows the data model used to encode the information.
*	Section 4 briefly indicates how the information can be browsed.
*	Annex 1 lists the pre-programmed (API) calls
*	Annex 2 gives further details about the SPARQL endpoint.

For a broader overview of the SI Digital Framework please see document BIPM-DIG-G01.

## Information contained in the SI Reference Point

The SI Reference Point comprises three main pillars (TTL files):
1. SI/units:
    * SI base units (Table 2 of [2])
    * SI derived units with special names (Table 4 of [2])
    * Non-SI units allowed for use with the SI (Table 8 of [2])
    * Compound units (the examples given in Tables 5 and 6 of [2] plus additional examples from the BIPM key comparison database (KCDB))
1. SI/prefixes:
    * SI prefixes (Table 7 of [2])
1. SI/decisions:
    * Decisions relating to the SI, taken by the CGPM and CIPM  (Appendix 1 of [2])
  
A tool is provided to allow for machine-encoding and interpretation of prefixed and other combined units (µm, m<sup>2</sup>, <nobr>m s<sup>-1</sup>, etc.).

The SI Reference Point relies on the following closely related components of the SI Digital Framework:

4. Constants
    * Initially the 7 defining constants of the SI (Table 1 of [2])
5.	Quantities
    * SI base quantities (Table 3 of [2])
    * Other example quantities (Tables 5 and 6 of [2])
    * Some other quantities in the BIPM key comparison database (KCDB))
6. Responsible bodies
    * CGPM, CIPM, etc.

  
Table. List of tables in the SI Brochure [2] and corresponding information in the SI Reference Point

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


## Data model

The information contained in the nine editions of the SI Brochure has been encoded semantically and made publicly available on the internet at:

<p class="text-center">
[si-digital-framework.org/SI](http://62.161.69.201:8080/SI) 
</p>


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






 

## Next steps

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

