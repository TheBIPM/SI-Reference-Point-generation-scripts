_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDatatype


#### Tree

* rdf:Property
    * si:hasDatatype





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDatatype

#### Description



#### Inherits from:
owl:Thing



#### Usage


[na38f2c0b404d4008bcfb1c25887fbc6bb1](entity-na38f2c0b404d4008bcfb1c25887fbc6bb1.md)
=&gt;&nbsp;_si:hasDatatype_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDatatype a owl:ObjectProperty ;
    rdfs:label "has datatype"@en,
        "a un type de données"@fr ;
    rdfs:domain [ owl:oneOf ( si:Constant si:SIPrefix ) ] .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_