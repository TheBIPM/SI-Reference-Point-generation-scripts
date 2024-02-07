_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:UnitMultiple


#### Tree


* [si:CompoundUnit](class-sicompoundunit.md)

    * si:UnitMultiple





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#UnitMultiple

#### Description




#### Inherits from (2)

- [si:CompoundUnit](class-sicompoundunit.md)

- [si:MeasurementUnit](class-simeasurementunit.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:UnitMultiple a owl:Class ;
    rdfs:label "unit multiple"@en,
        "multiple d'unité"@fr ;
    rdfs:subClassOf si:CompoundUnit .


```




#### Instances of si:UnitMultiple can have the following properties:

##### From [si:UnitMultiple](class-siunitmultiple.md):

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
| [si:hasUnitTerm](prop-sihasunitterm.md) |  |*owl:Thing*|
| [si:inBaseSIUnits](prop-siinbasesiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:inOtherSIUnits](prop-siinothersiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|











---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_