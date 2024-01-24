_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasConversionUnit


#### Tree

* rdf:Property
    * si:hasConversionUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasConversionUnit

#### Description
<p>SI unit to which the non SI unit can be converted</p>


#### Inherits from:
owl:Thing



#### Usage


[si:nonSIUnit](class-sinonsiunit.md)
=&gt;&nbsp;_si:hasConversionUnit_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasConversionUnit a owl:ObjectProperty ;
    rdfs:label "has conversion unit"@en,
        "a une unité de conversion"@fr ;
    rdfs:comment "SI unit to which the non SI unit can be converted"@en,
        "Unité SI dans laquelle l'unité non SI peut être convertie"@fr ;
    rdfs:domain si:nonSIUnit ;
    rdfs:range si:MeasurementUnit .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_