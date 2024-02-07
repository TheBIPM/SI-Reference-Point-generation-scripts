_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUnit


#### Tree

* rdf:Property
    * si:hasUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasUnit

#### Description
<p>Linking a measurement unit to an object.</p>


#### Inherits from:
owl:Thing



#### Usage


[na38f2c0b404d4008bcfb1c25887fbc6bb7](entity-na38f2c0b404d4008bcfb1c25887fbc6bb7.md)
=&gt;&nbsp;_si:hasUnit_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasUnit a owl:ObjectProperty ;
    rdfs:label "has unit"@en,
        "a l'unité"@fr ;
    rdfs:comment "Linking a measurement unit to an object."@en,
        "Associer une unité de mesure à un objet."@fr ;
    rdfs:domain [ a owl:Class ;
            owl:unionOf ( si:Constant si:QuantityKind ) ] ;
    rdfs:range si:MeasurementUnit .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_