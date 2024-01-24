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
owl:Thing=&gt;&nbsp;_si:hasUnit_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasUnit a owl:ObjectProperty ;
    rdfs:label "has unit"@en,
        "a l'unité"@fr ;
    rdfs:comment "Linking a measurement unit to an object."@en,
        "Associer une unité de mesure à un objet."@fr ;
    rdfs:range si:MeasurementUnit .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_