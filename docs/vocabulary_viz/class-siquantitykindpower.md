_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:QuantityKindPower


#### Tree


* [si:CompoundQuantityKind](class-sicompoundquantitykind.md)

    * si:QuantityKindPower





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#QuantityKindPower

#### Description




#### Inherits from (2)

- [si:CompoundQuantityKind](class-sicompoundquantitykind.md)

- [si:QuantityKind](class-siquantitykind.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:QuantityKindPower a owl:Class ;
    rdfs:label "quantitykind power"@en,
        "quantité élevée à la puissance"@fr ;
    rdfs:subClassOf si:CompoundQuantityKind .


```




#### Instances of si:QuantityKindPower can have the following properties:

##### From [si:QuantityKindPower](class-siquantitykindpower.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|


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