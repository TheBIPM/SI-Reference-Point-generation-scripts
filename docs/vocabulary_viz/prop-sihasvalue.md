_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasValue


#### Tree

* rdf:Property
    * si:hasValue





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasValue

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:Constant](class-siconstant.md)
=&gt;&nbsp;_si:hasValue_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasValue a owl:DatatypeProperty ;
    rdfs:label "has value"@en,
        "a de la valeur"@fr ;
    rdfs:domain si:Constant ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_