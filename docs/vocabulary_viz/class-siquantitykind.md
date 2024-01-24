_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:QuantityKind


#### Tree

* owl:Thing
    * si:QuantityKind


        * [si:CompoundQuantityKind](class-sicompoundquantitykind.md) 
        






#### URI
http://si-digital-framework.org/SI#QuantityKind

#### Description
<p>Class for the quantity kinds.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:QuantityKind a owl:Class ;
    rdfs:label "kind of quantity"@en,
        "nature de grandeur"@fr ;
    rdfs:comment "Class for the quantity kinds."@en,
        "La classe pour les types de quantité."@fr ;
    rdfs:isDefinedBy "VIM3 1.2"^^xsd:string .


```




#### Instances of si:QuantityKind can have the following properties:

##### From [si:QuantityKind](class-siquantitykind.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|


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