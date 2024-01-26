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


[n0fe14176d0b84ad0ae63b0a583714332b1](entity-n0fe14176d0b84ad0ae63b0a583714332b1.md)
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

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_