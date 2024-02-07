_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:MeasurementUnit


#### Tree

* owl:Thing
    * si:MeasurementUnit


        * [si:CompoundUnit](class-sicompoundunit.md) 

        * [si:SIBaseUnit](class-sisibaseunit.md) 

        * [si:SISpecialNamedUnit](class-sisispecialnamedunit.md) 

        * [si:nonSIUnit](class-sinonsiunit.md) 
        






#### URI
http://si-digital-framework.org/SI#MeasurementUnit

#### Description
<p>Class for all measurement units.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:MeasurementUnit a owl:Class ;
    rdfs:label "measurement unit"@en,
        "unité de mesure"@fr ;
    rdfs:comment "Class for all measurement units."@en,
        "La classe pour toutes les unités de mesure."@fr ;
    rdfs:isDefinedBy "VIM3 1.9" ;
    owl:disjointWith si:Constant,
        si:QuantityKind,
        si:SIPrefix .


```




#### Instances of si:MeasurementUnit can have the following properties:

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