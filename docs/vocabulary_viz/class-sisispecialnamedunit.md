_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:SISpecialNamedUnit


#### Tree


* [si:MeasurementUnit](class-simeasurementunit.md)

    * si:SISpecialNamedUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#SISpecialNamedUnit

#### Description
<p>Class for the units of the SI that are not base units but have a special name.</p>



#### Inherits from (1)

- [si:MeasurementUnit](class-simeasurementunit.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:SISpecialNamedUnit a owl:Class ;
    rdfs:label "SI unit with special name"@en,
        "unité SI avec nom spécial"@fr ;
    rdfs:comment "Class for the units of the SI that are not base units but have a special name."@en,
        "La classe des unités du SI qui ne sont pas des unités de base mais qui ont un nom spécial."@fr ;
    rdfs:subClassOf si:MeasurementUnit ;
    owl:disjointWith si:nonSIUnit .


```




#### Instances of si:SISpecialNamedUnit can have the following properties:

##### From [si:SISpecialNamedUnit](class-sisispecialnamedunit.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|


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