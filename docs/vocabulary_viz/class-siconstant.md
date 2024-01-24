_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:Constant


#### Tree

* owl:Thing
    * si:Constant





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#Constant

#### Description
<p>Class for the seven defining constants of the SI.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:Constant a owl:Class ;
    rdfs:label "defining constant"@en,
        "définir la constante"@fr ;
    rdfs:comment "Class for the seven defining constants of the SI."@en,
        "La classe pour les sept constantes définissant le SI."@fr ;
    owl:disjointWith si:QuantityKind .


```




#### Instances of si:Constant can have the following properties:

##### From [si:Constant](class-siconstant.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasUnitAsString](prop-sihasunitasstring.md) |  |[xsd:string](class-xsdstring.md)|
| [si:hasUpdatedDate](prop-sihasupdateddate.md) |  |[xsd:date](class-xsddate.md)|
| [si:hasValue](prop-sihasvalue.md) |  |[rdfs:Literal](class-rdfsliteral.md)|
| [si:hasValueAsString](prop-sihasvalueasstring.md) |  |[xsd:string](class-xsdstring.md)|


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