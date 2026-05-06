# Semantic SI
created: Jan 2023 / GD
last modified: 2026-03-27

This package implements the SI Reference point, a part of the SI digital framework. The package provides a 
machine-readable version (knowledge graph) of the units, prefixes, constants defined in the SI Brochure. 
The general workflow for the generation of the knowledge graph is:

```mermaid
flowchart TD
    A["Graph structure\n(py script)"] --> C{"Graph producer\n(py script)"}
    B["Information\n(YAML files)"] --> C
    C --> F["Serialised Knowledge Graph (ttl file)"]
```

See also SIDataModel.pdf (depicting the underlying data model used for this part of the SI digital framework 
\[may be obsolete on some aspects\]).
 
The package contains also a test Website (based on FastAPI), allowing to interrogate the produced knowledge graphs. 
Note that this is only provided for demo purposes. 

## Installation
Install as a python package

- Clone repository or download zip file and unzip it
- `pip install path/to/repo` (or `pip install -e path/to/repo` if you plan to edit the code and see the changes 
  immediately, "editable mode")

Python >= 3.11 required, for other requirements see pyproject.toml.

[Specific instructions for PyCharm](docs/pycharm.md)

## Command line usage
After installation, the `generate_sirp_files` is made available.

This command will create all `.ttl` and `.jsonld` files in a subfolder. The `-z` option generates a zip file of the ensemble.

For debugging purposes, you can choose to generate only one ttl by providing its label with the `--only` option.

`--gen_ontology_viz` updates the Markdown files in `docs/vocabulary_viz` using Ontospy. Make sure to add and commit 
changes if you want the up-to-date version to be displayed on GitHub.

`-o / --output_dir` indicates where to write the output files, and defaults to `./output`. Additionaly `--ttl_output_subdir` and `--jsonld_output_subdir` indicate the subdirectories for TTL and JSON-LD outputs. They default to `TTL` and `JSONLD`. 

`-h / --help` provides a list of available options.

### `launch_si_test_api`
This command will launch a local web-service for testing purposes.


## Short description of the `src/si_ref_point/` subdirectories

### tboxes

Contains the python scripts that will generate the "terminology" part of the SI Reference Point (`si_tbox.py`) and the additional concepts necessary to bond to responsible bodies (`rb_tbox.py`).

### aboxes

Contains the python scripts that will populate the "assertions" part of the SI Reference Point (constants, decisions, prefixes, quantities, units) and responsible bodies (CCTF, CGPM, CIPM). `symbols_format.py` is a common utility that handles the conversion between html, LaTeX, json and ascii formatting.


### inputs

Contains 2 subdirectories, `si` and `rb`, gathering all necessary input information. In general these are yaml files, but in the case for the SI concepts (that will feed the corresponding TBox) these are already ttl files.

Content of the `rb` directory originally come from a digitalization effort by Ron Tse (Ribose) in the frame of Metanorma (https://github.com/metanorma/cgpm-resolutions, https://github.com/metanorma/bipm-data-outcomes/tree/main)

### Test API
A fastapi instance allowing to test the TTL output used to be included in this package. It has now been transfered into a separate repo (sirp-tools).


## Current class diagram

```mermaid
classDiagram
	`si:QuantityKind`<|--`si:CompoundQuantityKind`
	`si:MeasurementUnit`<|--`si:CompoundUnit`
	`si:CompoundUnit`<|--`si:PrefixedUnit`
	`si:CompoundQuantityKind`<|--`si:QuantityKindPower`
	`si:CompoundQuantityKind`<|--`si:QuantityKindProduct`
	`si:MeasurementUnit`<|--`si:SIBaseUnit`
	`si:MeasurementUnit`<|--`si:SISpecialNamedUnit`
	`si:CompoundUnit`<|--`si:UnitMultiple`
	`si:CompoundUnit`<|--`si:UnitPower`
	`si:CompoundUnit`<|--`si:UnitProduct`
	`si:MeasurementUnit`<|--`si:nonSIUnit`
	class `si:CompoundQuantityKind`{
	}
	class `si:CompoundUnit`{
	}
	class `si:Constant`{
		+si:hasDatatype
		+si:hasDefiningResolution
		+si:hasUnit
		+si:hasUpdatedDate
		+si:hasValue
		+si:hasValueAsString
		+si:hasDefiningEquation
	}
	class `si:Definition`{
		+si:hasDefiningResolution
		+si:hasDefiningConstant
		+si:hasDefiningEquation
		+si:hasDefiningText
		+si:hasDefinitionNote
		+si:hasEndValidity
		+si:hasNextDefinition
		+si:hasPreviousDefinition
		+si:hasStartValidity
		+si:hasStatus
	}
	class `si:DefinitionNote`{
		+si:hasNoteIndex
		+si:hasNoteText
	}
	class `si:MeasurementUnit`{
		+si:prefixRestriction
		+si:isUnitOfQtyKind
		+si:hasUnitTypeAsString
		+si:hasNumericFactor
	}
	class `si:PrefixedUnit`{
		+si:hasNonPrefixedUnit
		+si:hasPrefix
	}
	class `si:QuantityKind`{
		+si:hasUnit
	}
	class `si:QuantityKindPower`{
	}
	class `si:QuantityKindProduct`{
	}
	class `si:SIBaseUnit`{
		+si:prefixRestriction
		+si:hasDefinition
		+si:hasUnitTypeAsString
	}
	class `si:SIDecision`{
	}
	class `si:SIDecisionTarget`{
	}
	class `si:SIPrefix`{
		+si:hasDatatype
		+si:hasScalingFactor
	}
	class `si:SISpecialNamedUnit`{
		+si:prefixRestriction
		+si:hasUnitTypeAsString
	}
	class `si:UnitMultiple`{
	}
	class `si:UnitPower`{
		+si:hasNumericExponent
		+si:hasUnitBase
	}
	class `si:UnitProduct`{
		+si:hasLeftUnitTerm
		+si:hasRightUnitTerm
	}
	class `si:nonSIUnit`{
		+si:prefixRestriction
		+si:hasUnitTypeAsString
	}
	`si:Constant` --o `rb:Resolution`
	`si:Constant` --o `si:MeasurementUnit`
	`si:Constant` --o `xsd:date`
	`si:Constant` --o `rdfs:Literal`
	`si:Constant` --o `xsd:string`
	`si:Definition` --o `rb:Resolution`
	`si:Definition` --o `si:Constant`
	`si:Definition` --o `rdfs:Literal`
	`si:Definition` --o `si:DefinitionNote`
	`si:Definition` --o `xsd:date`
	`si:Definition` --o `si:Definition`
	`si:DefinitionNote` --o `rdfs:Literal`
	`si:MeasurementUnit` --o `xsd:Boolean`
	`si:MeasurementUnit` --o `si:QuantityKind`
	`si:MeasurementUnit` --o `rdfs:Literal`
	`si:PrefixedUnit` --o `si:MeasurementUnit`
	`si:PrefixedUnit` --o `si:SIPrefix`
	`si:QuantityKind` --o `si:MeasurementUnit`
	`si:SIBaseUnit` --o `xsd:Boolean`
	`si:SIBaseUnit` --o `si:Definition`
	`si:SIBaseUnit` --o `rdfs:Literal`
	`si:SIPrefix` --o `rdfs:Literal`
	`si:SISpecialNamedUnit` --o `xsd:Boolean`
	`si:SISpecialNamedUnit` --o `rdfs:Literal`
	`si:UnitPower` --o `xsd:int`
	`si:UnitPower` --o `si:MeasurementUnit`
	`si:UnitProduct` --o `si:MeasurementUnit`
	`si:nonSIUnit` --o `xsd:Boolean`
	`si:nonSIUnit` --o `rdfs:Literal`
```
