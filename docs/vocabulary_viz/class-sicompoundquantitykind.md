_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:CompoundQuantityKind


#### Tree


* [si:QuantityKind](class-siquantitykind.md)

    * si:CompoundQuantityKind


        * [si:QuantityKindPower](class-siquantitykindpower.md) 

        * [si:QuantityKindProduct](class-siquantitykindproduct.md) 
        






#### URI
http://si-digital-framework.org/SI#CompoundQuantityKind

#### Description




#### Inherits from (1)

- [si:QuantityKind](class-siquantitykind.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:CompoundQuantityKind a owl:Class ;
    rdfs:label "compound quantitykind"@en,
        "quantité composée"@fr ;
    rdfs:subClassOf si:QuantityKind .


```




#### Instances of si:CompoundQuantityKind can have the following properties:

##### From [si:CompoundQuantityKind](class-sicompoundquantitykind.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|


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