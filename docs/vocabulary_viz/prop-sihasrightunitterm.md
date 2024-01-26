_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasRightUnitTerm


#### Tree


* [si:hasUnitTerm](prop-sihasunitterm.md)

    * si:hasRightUnitTerm





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasRightUnitTerm

#### Description
<p>preserve order of multiplication</p>


#### Inherits from (2)

- [si:hasUnitTerm](prop-sihasunitterm.md)

- [si:hasTerm](prop-sihasterm.md)




#### Usage


[si:UnitProduct](class-siunitproduct.md)
=&gt;&nbsp;_si:hasRightUnitTerm_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasRightUnitTerm a owl:ObjectProperty ;
    rdfs:label "has right unit term"@en,
        "a pour terme de droite cette unité"@fr ;
    rdfs:comment "preserve order of multiplication" ;
    rdfs:domain si:UnitProduct ;
    rdfs:range si:MeasurementUnit ;
    rdfs:subPropertyOf si:hasUnitTerm .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_