_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:DefinitionNote


#### Tree

* owl:Thing
    * si:DefinitionNote





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#DefinitionNote

#### Description
<p>The class for notes related SI unit definitions.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:DefinitionNote a owl:Class ;
    rdfs:label "unit definition note"@en,
        "note de définition d'unité"@fr ;
    rdfs:comment "The class for notes related SI unit definitions."@en,
        "La classe pour les définitions d'unités SI liées aux notes."@fr .


```




#### Instances of si:DefinitionNote can have the following properties:

##### From [si:DefinitionNote](class-sidefinitionnote.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasNoteIndex](prop-sihasnoteindex.md) | The text of a definition note. |[rdfs:Literal](class-rdfsliteral.md)|
| [si:hasNoteText](prop-sihasnotetext.md) | The order index of a definition note. |[rdfs:Literal](class-rdfsliteral.md)|


##### From [owl:Thing](class-owlthing.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasBase](prop-sihasbase.md) | Base ^ NumericExponent |*owl:Thing*|
| [si:hasFactor](prop-sihasfactor.md) |  |*owl:Thing*|
| [si:hasLeftUnitFactor](prop-sihasleftunitfactor.md) | preserve order of multiplication |*owl:Thing*|
| [si:hasNumericExponent](prop-sihasnumericexponent.md) | UnitBase ^ NumericExponent |*owl:Thing*|
| [si:hasNumericFactor](prop-sihasnumericfactor.md) |  |*owl:Thing*|
| [si:hasQuantityBase](prop-sihasquantitybase.md) | QuantityBase ^ NumericExponent |*owl:Thing*|
| [si:hasQuantityFactor](prop-sihasquantityfactor.md) |  |*owl:Thing*|
| [si:hasRightUnitFactor](prop-sihasrightunitfactor.md) | preserve order of multiplication |*owl:Thing*|
| [si:hasSymbol](prop-sihassymbol.md) | Linking a measurement unit or prefix to a symbol. |[xsd:string](class-xsdstring.md)|
| [si:hasUnit](prop-sihasunit.md) | Linking a measurement unit to an object. |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:hasUnitBase](prop-sihasunitbase.md) | UnitBase ^ NumericExponent |*owl:Thing*|
| [si:hasUnitFactor](prop-sihasunitfactor.md) |  |*owl:Thing*|
| [si:inBaseSIUnits](prop-siinbasesiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:inOtherSIUnits](prop-siinothersiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|











---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_