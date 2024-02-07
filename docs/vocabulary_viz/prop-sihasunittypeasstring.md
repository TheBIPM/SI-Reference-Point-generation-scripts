_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUnitTypeAsString


#### Tree

* rdf:Property
    * si:hasUnitTypeAsString





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasUnitTypeAsString

#### Description



#### Inherits from:
owl:Thing



#### Usage


[na38f2c0b404d4008bcfb1c25887fbc6bb10](entity-na38f2c0b404d4008bcfb1c25887fbc6bb10.md)
=&gt;&nbsp;_si:hasUnitTypeAsString_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasUnitTypeAsString a owl:DatatypeProperty ;
    rdfs:label "unit type as a string"@en,
        "type d'unité sous forme de chaîne"@fr ;
    rdfs:domain [ a owl:Class ;
            owl:unionOf ( si:SIBaseUnit si:SISpecialNamedUnit si:nonSIUnit si:MeasurementUnit ) ] ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_