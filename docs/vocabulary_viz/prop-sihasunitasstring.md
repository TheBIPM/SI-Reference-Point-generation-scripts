_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUnitAsString


#### Tree

* rdf:Property
    * si:hasUnitAsString





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasUnitAsString

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:Constant](class-siconstant.md)
=&gt;&nbsp;_si:hasUnitAsString_&nbsp;=&gt;&nbsp;[xsd:string](class-xsdstring.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:hasUnitAsString a owl:DatatypeProperty ;
    rdfs:label "has unit as a string"@en,
        "a l'unité comme chaîne"@fr ;
    rdfs:domain si:Constant ;
    rdfs:range xsd:string .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_