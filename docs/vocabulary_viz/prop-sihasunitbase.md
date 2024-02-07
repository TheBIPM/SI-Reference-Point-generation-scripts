_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUnitBase


#### Tree


* [si:hasBase](prop-sihasbase.md)

    * si:hasUnitBase





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasUnitBase

#### Description
<p>UnitBase ^ NumericExponent</p>


#### Inherits from (1)

- [si:hasBase](prop-sihasbase.md)




#### Usage


[si:UnitPower](class-siunitpower.md)
=&gt;&nbsp;_si:hasUnitBase_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasUnitBase a owl:ObjectProperty ;
    rdfs:label "has unit base"@en,
        "a pour base cette unité"@fr ;
    rdfs:comment "UnitBase ^ NumericExponent" ;
    rdfs:domain si:UnitPower ;
    rdfs:range si:MeasurementUnit ;
    rdfs:subPropertyOf si:hasBase .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_