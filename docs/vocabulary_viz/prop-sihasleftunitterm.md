_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasLeftUnitTerm


#### Tree


* [si:hasUnitTerm](prop-sihasunitterm.md)

    * si:hasLeftUnitTerm





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasLeftUnitTerm

#### Description
<p>preserve order of multiplication</p>


#### Inherits from (2)

- [si:hasUnitTerm](prop-sihasunitterm.md)

- [si:hasTerm](prop-sihasterm.md)




#### Usage


[si:UnitProduct](class-siunitproduct.md)
=&gt;&nbsp;_si:hasLeftUnitTerm_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasLeftUnitTerm a owl:ObjectProperty ;
    rdfs:label "has left unit term"@en,
        "a pour terme de gauche cette unité"@fr ;
    rdfs:comment "preserve order of multiplication" ;
    rdfs:domain si:UnitProduct ;
    rdfs:range si:MeasurementUnit ;
    rdfs:subPropertyOf si:hasUnitTerm .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_