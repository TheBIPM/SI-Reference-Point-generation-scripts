_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:SIBaseUnit


#### Tree


* [si:MeasurementUnit](class-simeasurementunit.md)

    * si:SIBaseUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#SIBaseUnit

#### Description
<p>Class of SI base units. Several definitions can be attached to this class to represent definitions of the BaseUnit throughout time.</p>



#### Inherits from (1)

- [si:MeasurementUnit](class-simeasurementunit.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:SIBaseUnit a owl:Class ;
    rdfs:label "base unit"@en,
        "unité de base"@fr ;
    rdfs:comment "Class of SI base units. Several definitions can be attached to this class to represent definitions of the BaseUnit throughout time."@en,
        "La classe des unités de base SI. Plusieurs définitions peuvent être attachées à cette classe pour représenter les définitions de l'unité de base en question à travers les temps."@fr ;
    rdfs:isDefinedBy "VIM3 1.10" ;
    rdfs:subClassOf si:MeasurementUnit ;
    owl:disjointWith si:SISpecialNamedUnit,
        si:nonSIUnit .


```




#### Instances of si:SIBaseUnit can have the following properties:

##### From [si:SIBaseUnit](class-sisibaseunit.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasDefinition](prop-sihasdefinition.md) | Linking an SI base unit to its definition. |[si:Definition](class-sidefinition.md)|


##### From [si:MeasurementUnit](class-simeasurementunit.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasNumericFactor](prop-sihasnumericfactor.md) |  |*owl:Thing*|
| [si:isUnitOfQtyKind](prop-siisunitofqtykind.md) | Linking a measurement unit to its quantity kind. |[si:QuantityKind](class-siquantitykind.md)|


##### From [owl:Thing](class-owlthing.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasBase](prop-sihasbase.md) | Base ^ NumericExponent |*owl:Thing*|
| [si:hasQuantityTerm](prop-sihasquantityterm.md) |  |*owl:Thing*|
| [si:hasSymbol](prop-sihassymbol.md) | Linking a measurement unit or prefix to a symbol. |[xsd:string](class-xsdstring.md)|
| [si:hasTerm](prop-sihasterm.md) |  |*owl:Thing*|
| [si:hasUnit](prop-sihasunit.md) | Linking a measurement unit to an object. |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:hasUnitTerm](prop-sihasunitterm.md) |  |*owl:Thing*|
| [si:inBaseSIUnits](prop-siinbasesiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:inOtherSIUnits](prop-siinothersiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|











---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_