_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:inBaseSIUnits


#### Tree

* rdf:Property
    * si:inBaseSIUnits





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#inBaseSIUnits

#### Description



#### Inherits from:
owl:Thing



#### Usage
owl:Thing=&gt;&nbsp;_si:inBaseSIUnits_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:inBaseSIUnits a owl:ObjectProperty ;
    rdfs:label "can be expressed in base SI units as"@en,
        "peut être exprimé en unités SI de base sous la forme"@fr ;
    rdfs:range si:MeasurementUnit .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_