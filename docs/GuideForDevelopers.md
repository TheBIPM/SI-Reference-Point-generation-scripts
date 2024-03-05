# The SI Reference Point - Guide for Developers

## 1. Scope

The [SI Reference Point](https://si-digital-framework.org/SI/) is a digital reference in support of the [International System of Units (SI)](https://www.bipm.org/en/measurement-units/). It is aimed at anyone wishing to express their measurement data in a [FAIR](https://www.go-fair.org/fair-principles/) manner.

The SI Reference Point contains
* the values of (and PIDs for) the constants defining the SI
* the definitions of (and PIDs for) the named SI units and prefixes, along with the relevant official decisions
* the list of non-SI units allowed for use with the SI
* examples of physical and chemical quantities, along with their corresponding SI units

The information in the SI Reference Point is provided as a knowledge graph serialized in a set of six Turtle (TTL) or JSON-LD files:

* SI.ttl
* SI/units.ttl
* SI/prefixes.ttl
* SI/decisions.ttl
* constants.ttl
* quantities.ttl

The SI Reference Point provides:
* an Application Programming Interface (API) providing JSON, JSON-LD, XML or HTML outputs
* a SPARQL endpoint
* a tool to generate the PID of any compound unit

An introductory overview of the service for users is given [HERE](https://github.com/TheBIPM/SI_Digital_Framework/tree/main/SI_Reference_Point/docs). The present document provides more information about the Application Programming Interface.


## 2. Introduction to the SI

The SI is an internationally agreed, practical system of units of measurement, comprising a set of "SI units" and a set of "SI prefixes". In brief:

* an SI unit can be multiplied by an SI prefix to create multiples or submultiples of the unit: e.g. nanosecond (ns) = 10<sup>-9</sup> s. 
* compound units can be formed by multiplying (or dividing) combinations of the units (prefixed or not): e.g. metres per second squared (m⋅s<sup>-2</sup>) for acceleration.   
* each kind of quantity has one corresponding SI unit (though it might be possible to express that unit in different ways).
* a derived SI unit can correspond to more than one derived quantity.

All SI units can be expressed in terms of a set of seven so-called "base units": namely, the second (s), metre (m), kilogram (kg), kelvin (K), mole (mol) and candela (cd). There are another 22 named units corresponding to different kinds of quantity, such as the newton (N) for force, the joule (J) for energy, and the watt (W) for power. 

Full details are provided in the [SI Brochure](https://www.bipm.org/en/publications/si-brochure) published by the BIPM and currently in its 9th edition. Since its creation in 1960, the SI has evolved both through the inclusion of new units and new prefixes, and through the redefinition of existing units. When a unit is redefined, the new definition ensures that continuity is kept with the previous definition, but usually there will be some practical advantage such as an improved means to "realize" the unit in question. After a major revision of the SI adopted in 2018, the whole SI is now defined in terms of seven defining constants. In particular, new definitions of the kilogram, kelvin, mole and candela were agreed at that time.
The following table shows how the information from the SI Brochure is distributed amon the TTL (or JSON-LD) files.


**Table 1.** List of tables in the SI Brochure and corresponding information in the SI Reference Point

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
| <nobr>App. 1</nobr> |  Decisions of the CGPM and the CIPM | SI/decisions |


## 3. Getting started 

The Application Programming Interface provides a set of predefined SPARQL queries to retrieve the information in the knowledge graph. The available calls are described below and in the Swagger interface at https://si-digital-framework.org/api-docs/swagger-ui/?urls.primaryName=SI%20REFERENCE%20POINT. They can be used to retrieve information about the units, prefixes, defining constants, related official decisions, and kinds of quantity.

### 3.1 Authentication and Authorization

The API of the beta-version of the SI Reference Point is openly available at https://si-digital-framework.org/api-docs/swagger-ui/?urls.primaryName=SI%20REFERENCE%20POINT under the Creative Commons Attribution 3.0 Intergovernmental Organization license ([CC BY 3.0 IGO](https://creativecommons.org/licenses/by/3.0/igo/)). 

Currently no pre-registration is required, but please note that during the beta-testing phase the API calls provided may be subject to revision. During this phase (at least until the end of 2024), two weeks' notice will be given, via the website and the GitHub site, to announce upcoming changes. The changes will be logged on the GitHub site.

Once the official version is released, registration of users will be encouraged to facilitate the communication of any further changes to the API.

A rate limit of XXXX is in place.

### 3.2 API calls

The API queries can be triggered through the [Swagger interface](https://si-digital-framework.org/api-docs/swagger-ui/?urls.primaryName=SI%20REFERENCE%20POINT) or by a Command Line Interface (CLI). The same API calls underpin the web interface.

The header information can be adjusted as follows to return data in JSON, JSON-LD, XML, HTML or TTL formats, respectively:

* `curl -H "accept: application/json"`
* `curl  -H "accept: application/ld+json"`
* `curl -H "accept: application/xml"`
* `curl -H "accept: application/htm"l`
* `curl -H "accept: application/octet-stream"`

The names of the calls indicated below should be appended to the base URL `si-digital-framework.org/`. Thus the call `SI/units`, for example, listed below represents `https://si-digital-framework.org/SI/units`.

| Query | Essential parameter | Action | Optional parameter | Effect | 
| :----- | :----- | :---- | :---- | :---- |
| `GET SI/units` |returns list of units | | | default language is English |
| | | | `lang=en` | text in English |
| | | | `lang=fr` | text in French |
| `GET SI/units/{name}` | information about specified unit {name} | {name} of unit | | default language is English |
| | | | `lang=en` | text in English |
| | | | `lang=fr` | text in French |
| `GET SI/prefixes` | returns list of SI prefixes | | | default language is English |
| | | | `lang=en` | text in English |
| | | | `lang=fr` | text in French |

  **3.2.1 `SI/units`**

This query returns a list of all the units The units included are: the SI base units, SI derived units with special names, and non-SI units allowed for use with the SI units.

<i>Optional parameters:</i>
  * `lang=fr` (to return French information) or `lang=en` (the default setting: English)
  * `date=YYYY-MM-DD` (e.g. `date=2024-02-14` for 14 February 2024); the default setting is the query date


If no language is specified, the default language is returned: English

  For example:
  ```curl -X GET "https://www.si-digital-framework.org/SI/units?lang=en" -H "accept: application/json"``` (linux/MacOS)
  ```curl -X GET "https://www.si-digital-framework.org/SI/units?lang=en" -Headers "{accept='application/json'}``` (Windows)

  **3.2.2 `SI/units/{name}`**
  
  This query returns information about the particular unit specified by `{name}`, where `{name}` is the English name of the unit, after any spaces have been removed (e.g. degreeCelsius for degree Celsius). For confirmation of the name to use, please refer to the output of `SI/units`.

<i>Optional parameters:</i>
  * `lang=fr` (to return French information) or `lang=en` (the default setting: English)
  * `date=YYYY-MM-DD` (e.g. `date=2024-02-14` for 14 February 2024); the default setting is the query date

For example

```curl -X GET "https://www.si-digital-framework.org/SI/units/kilogram?lang=fr&date=2007-11-21"```

will return information in French relating to the SI unit "kilogram" as at (and up until) 21 November 2007.


  **3.2.3 `SI/prefixes`**
  
  This query returns a list of all the SI prefixes.
  
  <i>Optional parameters</i>
  * `lang=fr` (to return French information) or `lang=en` (for English: default setting)


  **3.2.4 `SI/prefixes/{name}`**
  
  This query returns information about the particular SI prefix spcified by `{name}`, where `{name}` is the English name of the prefix.
 
  <i>Optional parameters:</i> 
    * `lang=fr` (to return French information) or `lang=en` (for English: default setting)

  For example, 

  `curl -X GET "https://www.si-digital-framework.org/SI/prefixes/mega?lang=fr" -H "accept: application/json"`


  **3.2.5 `constants`**

   This query returns information about the defining constants. (Note: The knowledge base is currently restricted to the seven constants defining the SI.)

  <i>Optional parameters:</i>
    * `lang=fr` (to return French information) or `lang=en` (for English: default setting)

  For example,

  ```curl -X GET "https://si-digital-framework.org/constants?lang=en" -H "accept: application/json"```

  will return (in JSON format) information in English about all the defining constants


  **3.2.6 `constants/{parameter}`**

This query returns information about the particular constant specified by {parameter}, where {parameter} is the ID of the constant as listed by `constants`. 

The constants are named using the English name in CamelCase (camel caps), with an initial capital letter and no spaces. For confirmation of the name to use, please refer to the output of `constants`.

<i>Optional parameters:</i>
  * `lang=fr` (to return French information) or `lang=en` (for English: default setting)

For example,

```curl -X GET "https://si-digital-framework.org/constants/PlanckConstant?lang=en" -H "accept: application/json"```

will return (in JSON format) information in English about the Planck constant.





