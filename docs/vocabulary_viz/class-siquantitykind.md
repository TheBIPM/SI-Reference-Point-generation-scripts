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
| [si:hasQuantityTerm](prop-sihasquantityterm.md) |  |*owl:Thing*|
| [si:hasSymbol](prop-sihassymbol.md) | Linking a measurement unit or prefix to a symbol. |[xsd:string](class-xsdstring.md)|
| [si:hasTerm](prop-sihasterm.md) |  |*owl:Thing*|
| [si:hasUnitTerm](prop-sihasunitterm.md) |  |*owl:Thing*|
| [si:inBaseSIUnits](prop-siinbasesiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:inOtherSIUnits](prop-siinothersiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|











---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_