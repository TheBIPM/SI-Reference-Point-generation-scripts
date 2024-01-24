_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:nonSIUnit


#### Tree


* [si:MeasurementUnit](class-simeasurementunit.md)

    * si:nonSIUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#nonSIUnit

#### Description
<p>Non-SI units that are accepted for use with the SI</p>



#### Inherits from (1)

- [si:MeasurementUnit](class-simeasurementunit.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:nonSIUnit a owl:Class ;
    rdfs:label "non SI unit"@en,
        "unité en dehors du SI"@fr ;
    rdfs:comment "Non-SI units that are accepted for use with the SI"@en,
        "Unités en dehors du SI dont l’usage est accepté avec le SI"@fr ;
    rdfs:subClassOf si:MeasurementUnit .


```




#### Instances of si:nonSIUnit can have the following properties:

##### From [si:nonSIUnit](class-sinonsiunit.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasConversionFactor](prop-sihasconversionfactor.md) | The conversion factor between non-SI unit and an SI Unit (number SI unit contained in 1 non SI unit) |[rdfs:Literal](class-rdfsliteral.md)|
| [si:hasConversionUnit](prop-sihasconversionunit.md) | SI unit to which the non SI unit can be converted |[si:MeasurementUnit](class-simeasurementunit.md)|


##### From [si:MeasurementUnit](class-simeasurementunit.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:isUnitOfQtyKind](prop-siisunitofqtykind.md) | Linking a measurement unit to its quantity kind. |[si:QuantityKind](class-siquantitykind.md)|


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